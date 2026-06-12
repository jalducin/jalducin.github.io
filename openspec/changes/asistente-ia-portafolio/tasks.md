> Spec-driven: estas son las specs aprobadas; la implementación es posterior y por capability.
> CI/CD: SIEMPRE git → AWS (push al repo dispara el deploy). Cuenta 957266312835 · us-east-2.

## 0. Preparación (OBLIGATORIO — PRIMERO, por capability)

- [ ] 0.1 Leer `openspec/config.yaml`, `docs/base-standards.md`, `docs/frontend-standards.md` y este design.md
- [ ] 0.2 Crear feature branch de la capability (`feature/<capability>`)
- [ ] 0.3 Decidir proveedor del LLM: **Bedrock (recomendado)** vs API key de Anthropic (ver design Open Questions)

## 1. asistente-ia-backend (Lambda)

- [ ] 1.1 Código del backend en `backend/assistant/` (Python): recibe pregunta, arma prompt con `llms.txt`, llama al LLM, responde JSON
- [ ] 1.2 Bootstrap: crear función Lambda + rol de ejecución; habilitar Bedrock (Opción A) o setear key en env cifrada (Opción B, una sola vez, fuera de CI)
- [ ] 1.3 Function URL (HTTPS) + CORS acotado a los orígenes del sitio (CloudFront / github.io)
- [ ] 1.4 Controles: modelo Haiku, `max_tokens` bajo, reserved concurrency baja; grounding + manejo de fuera-de-alcance; degradación elegante
- [ ] 1.5 Grounding embebido (sin RAG): `llms.txt` completo en el prompt; resistencia a prompt-injection / on-topic
- [ ] 1.6 Caché de respuestas (preguntas normalizadas) para no llamar al LLM en repeticiones; invalidar si cambia `llms.txt`
- [ ] 1.7 Rate limiting por IP (~10/min, ~50/día) + tope global diario (~500/día) con DynamoDB on-demand + TTL; 429 sin llamar al LLM
- [ ] 1.8 (opcional) Logging anónimo de preguntas SIN PII para mejorar `llms.txt`

## 2. cicd-asistente-aws (GitHub → AWS)

- [ ] 2.1 `.github/workflows/deploy-assistant.yml`: push a main con cambios en `backend/assistant/**` → empaqueta y `lambda:update-function-code` vía OIDC
- [ ] 2.2 Extender el rol de deploy con permiso mínimo (`lambda:UpdateFunctionCode` sobre la función)
- [ ] 2.3 Verificar: el deploy ocurre solo tras el push (git → AWS) y sin llaves estáticas

## 3. asistente-ia-chat-widget (front)

- [ ] 3.1 Widget de chat vanilla en `index.html` (burbuja) que hace `fetch` al Function URL
- [ ] 3.2 Accesible (teclado, foco, Esc), responsive, respeta paleta y `prefers-reduced-motion`
- [ ] 3.3 Fallback con CTAs si el backend falla; sin secretos en el front
- [ ] 3.4 Preguntas sugeridas (chips) que disparan preguntas frecuentes (mejoran UX y aciertos de caché)
- [ ] 3.5 Tope de turnos por sesión (~8) que invita a contacto directo al alcanzarse

## 4. qr-apunta-al-sitio-aws

- [ ] 4.1 Definir URL destino (CloudFront actual o dominio canónico) — única fuente de verdad
- [ ] 4.2 Regenerar `assets/img/QR.png` apuntando a esa URL, conservando estilo (módulos negros + ícono JVAV centrado), con **corrección de errores H**, logo ≤ ~25% del área, zona de silencio ≥ 4 módulos y alto contraste
- [ ] 4.3 **Verificar legibilidad**: decodificar el QR con un lector real (celular y/o decodificador de software); no cerrar hasta confirmar que escanea y abre el sitio AWS
- [ ] 4.4 Regenerar el CV (`cv/cv.html` → PDF) con el QR actualizado

## 5. Verificación y reporte (OBLIGATORIO — EL AGENTE EJECUTA)

- [ ] 5.1 Backend: probar el endpoint (curl) con preguntas en-alcance y fuera-de-alcance; verificar CORS y que no hay key en front/repo
- [ ] 5.2 Widget: flujo en navegador + 3 breakpoints; fallback ante error
- [ ] 5.3 QR: escaneo abre el sitio AWS; estilo preservado
- [ ] 5.4 Reporte en `openspec/changes/asistente-ia-portafolio/reports/AAAA-MM-DD-<capability>.md`

## 6. Documentación y cierre (OBLIGATORIO)

- [ ] 6.1 Actualizar `README.md` / `CLAUDE.md` / `docs/` (endpoint, deploy del backend, costo/budgets)
- [ ] 6.2 Consolidar con la capability `asistente-ia-portafolio` de `mejoras-portafolio-ai-native` (evitar duplicación)
- [ ] 6.3 Archivar el cambio cuando backend + widget + QR estén implementados y verificados
