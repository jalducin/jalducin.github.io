> Spec-driven: estas son las specs aprobadas; la implementación es posterior y por capability.
> CI/CD: SIEMPRE git → AWS (push al repo dispara el deploy). Cuenta 957266312835 · us-east-2.

## 0. Preparación (OBLIGATORIO — PRIMERO, por capability)

- [x] 0.1 Leer `openspec/config.yaml`, `docs/base-standards.md`, `docs/frontend-standards.md` y este design.md (verificación 2026-09-20)
- [x] 0.2 Crear feature branch de la capability (`feature/<capability>`) — implementación ya en `main`; esta auditoría corre en `feature/verificar-asistente-ia`
- [x] 0.3 Decidir proveedor del LLM: **Bedrock (recomendado)** vs API key de Anthropic (ver design Open Questions) — decidido: Bedrock + Claude Haiku por IAM (`backend/assistant/app.py:25`)

## 1. asistente-ia-backend (Lambda)

- [x] 1.1 Código del backend en `backend/assistant/` (Python): recibe pregunta, arma prompt con `llms.txt`, llama al LLM, responde JSON — `app.py` completo, verificado con curl en vivo (ver reporte 2026-09-20)
- [x] 1.2 Bootstrap: crear función Lambda + rol de ejecución; habilitar Bedrock — Lambda `jalducin-assistant` activo (python3.12), rol `jalducin-assistant-lambda-role`, Bedrock respondiendo en vivo
- [x] 1.3 Endpoint HTTPS + CORS acotado a los orígenes del sitio (CloudFront / github.io) — (nota: es API Gateway HTTP API, no Function URL como decía el design original; corregido en design.md) — CORS verificado con curl (`access-control-allow-origin` acotado)
- [ ] 1.4 Controles: modelo Haiku, `max_tokens` bajo, **reserved concurrency baja** (falta — ver reporte); grounding + manejo de fuera-de-alcance (verificado); degradación elegante (verificada)
- [x] 1.5 Grounding embebido (sin RAG): `llms.txt` completo en el prompt (vía `profile.txt`, copiado por el CI); resistencia a prompt-injection / on-topic (`app.py:38-39`)
- [x] 1.6 Caché de respuestas (preguntas normalizadas) — verificado en vivo: segunda llamada idéntica devuelve `"cached": true`
- [x] 1.7 Rate limiting por IP (~10/min, ~50/día) + tope global diario (~500/día) con DynamoDB on-demand + TTL — tabla `jalducin-assistant` confirmada (`PAY_PER_REQUEST`, TTL `ttl` ENABLED); no se probó con ráfagas (instrucción explícita de no cargar el endpoint)
- [ ] 1.8 (opcional) Logging anónimo de preguntas SIN PII para mejorar `llms.txt` (n/a: opcional, no implementado; no bloquea el cierre)

## 2. cicd-asistente-aws (GitHub → AWS)

- [x] 2.1 `.github/workflows/deploy-assistant.yml`: push a main con cambios en `backend/assistant/**` (y `llms.txt`) → empaqueta y `lambda:update-function-code` vía OIDC — 5+ runs exitosos (`gh run list`), el más reciente 2026-09-20
- [x] 2.2 Extender el rol de deploy con permiso mínimo (`lambda:UpdateFunctionCode` sobre la función) — workflow usa `role-to-assume: gh-actions-portfolio-deploy`; el JSON de la policy no se auditó (bloqueado por el sandbox del agente al tratar la exploración de políticas IAM como "credential exploration"); evidencia indirecta (el workflow solo invoca `update-function-code`) sugiere alcance acotado
- [x] 2.3 Verificar: el deploy ocurre solo tras el push (git → AWS) y sin llaves estáticas — confirmado (`permissions: id-token: write`, sin secrets estáticos en el workflow)

## 3. asistente-ia-chat-widget (front)

- [x] 3.1 Widget de chat vanilla en `index.html` (burbuja) que hace `fetch` al endpoint — `index.html:729-738,884-920`
- [x] 3.2 Accesible (teclado, foco, Esc), responsive, respeta paleta — verificado con probe headless en 1280/768/480 (aria-label, foco al abrir, Esc cierra, sin overflow horizontal); `prefers-reduced-motion` (n/a: el panel no usa animación que mitigar)
- [x] 3.3 Fallback con CTAs si el backend falla; sin secretos en el front — `index.html:911-913`; `ASSISTANT_URL` es la única referencia al backend
- [x] 3.4 Preguntas sugeridas (chips) que disparan preguntas frecuentes — 4 chips, probe confirma `chips_count: 4`
- [x] 3.5 Tope de turnos por sesión (~8) que invita a contacto directo al alcanzarse — `MAX_TURNS=8` (`index.html:897`)

## 4. qr-apunta-al-sitio-aws

- [x] 4.1 Definir URL destino (CloudFront actual o dominio canónico) — única fuente de verdad — `https://d3r3bnavnwzqaw.cloudfront.net` (commit `26964ca`)
- [x] 4.2 Regenerar `assets/img/QR.png` apuntando a esa URL, conservando estilo, EC-H, logo ≤25%, zona de silencio, alto contraste — hecho en `26964ca` (verificación de bits no repetida en esta auditoría; decodificación exitosa con logo central es evidencia indirecta de que la EC tolera el logo)
- [x] 4.3 **Verificar legibilidad**: decodificado en esta auditoría con OpenCV (`cv2.QRCodeDetector`) → `https://d3r3bnavnwzqaw.cloudfront.net` exacto. No se probó con lector físico de celular (sin hardware disponible en el entorno del agente)
- [x] 4.4 Regenerar el CV (`cv/cv.html` → PDF) con el QR actualizado — hecho en `26964ca` (`cv/CV_JuanValentinAlducin.pdf` regenerado en el mismo commit)

## 5. Verificación y reporte (OBLIGATORIO — EL AGENTE EJECUTA)

- [x] 5.1 Backend: probar el endpoint (curl) con preguntas en-alcance y fuera-de-alcance; verificar CORS y que no hay key en front/repo — 3 escenarios + CORS, ver reporte 2026-09-20
- [x] 5.2 Widget: flujo en navegador + 3 breakpoints; fallback ante error — probe headless en 1280/768/480 (ver reporte); fallback verificado por código
- [x] 5.3 QR: escaneo abre el sitio AWS; estilo preservado — decodificación por software confirma la URL; estilo preservado desde `26964ca`
- [x] 5.4 Reporte en `openspec/changes/asistente-ia-portafolio/reports/AAAA-MM-DD-<capability>.md` — `reports/2026-09-20-verificacion-implementacion.md`

## 6. Documentación y cierre (OBLIGATORIO)

- [x] 6.1 Actualizar `README.md` / `CLAUDE.md` / `docs/` (endpoint, deploy del backend, costo/budgets) — secciones nuevas agregadas en esta auditoría; `cv/README.md` corregido (el QR ya no dice que apunta al repo)
- [ ] 6.2 Consolidar con la capability `asistente-ia-portafolio` de `mejoras-portafolio-ai-native` (evitar duplicación) — **pendiente**: el spec duplicado sigue en `openspec/changes/mejoras-portafolio-ai-native/specs/asistente-ia-portafolio/`, y `openspec/specs/` no tiene ningún capability `asistente-ia-*` (nunca se sincronizó). Requiere `/opsx:sync` + retirar/superseder el spec duplicado
- [ ] 6.3 Archivar el cambio cuando backend + widget + QR estén implementados y verificados — **no archivar todavía**: falta 1.4 (reserved concurrency), 6.2 (consolidación de specs) y decidir la desalineación QR vs. URL canónica (og/JSON-LD/sitemap siguen en `jalducin.github.io`, ver reporte)
