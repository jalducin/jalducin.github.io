## Context

Sitio estático en S3+CloudFront (tier-0), CI/CD por OIDC (rol `gh-actions-portfolio-deploy`). Cuenta
957266312835, us-east-2. El asistente necesita backend porque la credencial del LLM no puede ir en el front.
Ya existe `llms.txt` como base de conocimiento del perfil.

## Goals / Non-Goals

**Goals:** asistente que responde sobre el perfil, credencial fuera del front/repo, costo controlado
(cómputo en free tier), deploy CI/CD git→AWS, UI vanilla accesible.
**Non-Goals:** RAG con vector DB (el `llms.txt` cabe en contexto), histórico de conversaciones persistente,
autenticación de usuarios, multi-idioma avanzado.

## Decisions

- **Cómputo: AWS Lambda + Function URL** (no API Gateway). *Por qué:* Function URL da HTTPS gratis y es más
  simple/barato; suficiente para un solo endpoint. CORS configurado a los orígenes del sitio.
- **Proveedor del LLM — DECISIÓN ABIERTA (recomendado: Amazon Bedrock):**
  - **Opción A — Amazon Bedrock (recomendada):** el Lambda invoca Claude por **IAM** (sin API key en
    ninguna parte). Costo de tokens va a la **factura AWS** (cubierta por los budgets ya configurados).
    Alinea con la cert de Bedrock de Juan y mantiene todo "in-AWS". Requiere habilitar acceso al modelo.
  - **Opción B — API de Anthropic:** key en **variable de entorno del Lambda** (cifrada con KMS gestionada,
    gratis), nunca en el repo/front. Costo de tokens en factura Anthropic (aparte).
  - En ambas: modelo **Haiku** por defecto (barato/rápido), `max_tokens` bajo (~400), temperatura baja.
- **Grounding:** system prompt = contenido de `llms.txt` + instrucción de responder SOLO desde el perfil y
  declarar cuando algo está fuera de alcance (no inventar). El front solo manda la pregunta del visitante.
- **Costo/abuso:** `reserved concurrency` baja (p. ej. 2) para acotar gasto; `max_tokens` chico; caché de
  preguntas frecuentes (en memoria del contenedor / opcional); CORS estricto; los **budgets** existentes
  avisan al correo del CV. Sin auth (endpoint público acotado por CORS + límites).
- **Credencial fuera de CI:** si se usa Opción B, la key se setea **una sola vez** en el Lambda
  (`update-function-configuration` manual o secret de entorno), **no** viaja por el repo. CI solo actualiza
  **código**, nunca la credencial.
- **Lenguaje del Lambda:** Python (boto3 para Bedrock / `anthropic` SDK para Opción B). Empaquetado simple
  (zip) por GitHub Actions.

## CI/CD (git → AWS)

- Workflow `.github/workflows/deploy-assistant.yml`: en push a `main` que toque `backend/assistant/**`,
  empaqueta el zip y hace `aws lambda update-function-code` (bootstrap inicial: crear función una vez).
- Reusa **OIDC**; el rol de deploy se extiende con `lambda:UpdateFunctionCode` (y bootstrap con
  create-function/role) — sin llaves estáticas en GitHub.
- **Orden explícito:** el cambio entra **primero al repo (GitHub)** y de ahí GitHub Actions despliega a
  **AWS** — mismo principio que el sitio. Nada se sube a AWS sin pasar antes por el repo.

## Risks / Trade-offs

- **Costo de tokens (no free tier)** → mitigado: Haiku + max_tokens bajo + reserved concurrency + budgets.
  [Riesgo] abuso del endpoint → [Mitigación] CORS estricto, concurrencia reservada, respuestas cacheadas,
  posible captcha/turnstile si escala.
- **Function URL sin rate-limit nativo** → reserved concurrency limita el blast radius; evaluar AWS WAF si
  hay abuso (WAF tiene costo → solo si necesario).
- **Bedrock requiere habilitar acceso al modelo** en la consola (paso manual una vez).
- **CORS** debe incluir el dominio CloudFront actual y (si aplica) github.io.

## Migration / Rollout

1. (Spec aprobada) Implementar backend en `feature/asistente-ia-backend`.
2. Bootstrap del Lambda + permisos; setear credencial/Bedrock una vez.
3. CI/CD del backend (OIDC) y verificación del endpoint en staging.
4. Widget en el sitio detrás de un flag/sección; deploy del sitio por el pipeline existente.
5. Verificar end-to-end; monitorear costo con budgets.
Rollback: ocultar el widget (el sitio sigue), deshabilitar el Function URL.

## Open Questions

- **¿Bedrock (recomendado) o API key de Anthropic?** (Default: Bedrock — sin secretos, todo-AWS.)
- ¿Modelo exacto en Bedrock (Claude Haiku) y región con acceso habilitado? (Default: Haiku en us-east-2 si
  disponible; si no, us-east-1.)
- ¿Límite de uso aceptable (max_tokens, concurrencia) y umbral para añadir WAF/captcha?
- ¿El widget en todas las páginas o solo en una sección/CTA?
