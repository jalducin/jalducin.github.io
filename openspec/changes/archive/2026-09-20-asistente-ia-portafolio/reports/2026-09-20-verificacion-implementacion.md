# Reporte — Verificación de la implementación real vs. specs (`asistente-ia-portafolio`)

- Fecha: 2026-09-20
- Cambio: `asistente-ia-portafolio`
- Agente: `frontend-developer` (auditoría post-deploy, sin tocar `app.py` ni workflows)
- Rama: `feature/verificar-asistente-ia` (worktree `.claude/worktrees/agent-a69f81ff19134213c`)

## Contexto

El asistente "Ask my portfolio" está desplegado y funcionando en producción desde hace meses (primer
deploy exitoso de `deploy-assistant.yml`: 2026-06-15; último: 2026-09-20), pero el cambio OpenSpec nunca
se cerró. Esta auditoría mapea las 4 specs y las 30 tareas de `tasks.md` contra la implementación real,
ejecuta las verificaciones posibles (endpoint en vivo, config AWS de solo lectura, render headless del
widget, QR) y corrige gaps documentales de bajo riesgo.

## Comandos ejecutados

```
git checkout -b feature/verificar-asistente-ia
curl -X POST https://vd4c00py15.execute-api.us-east-2.amazonaws.com  (pregunta en alcance)
curl -X POST https://vd4c00py15.execute-api.us-east-2.amazonaws.com  (pregunta fuera de alcance — receta)
curl -X POST https://vd4c00py15.execute-api.us-east-2.amazonaws.com  (JSON malformado)
curl -X POST https://vd4c00py15.execute-api.us-east-2.amazonaws.com  (JSON válido sin campo "question")
curl -X POST https://vd4c00py15.execute-api.us-east-2.amazonaws.com  (repetición exacta de (a) -> valida caché)
curl -i -X POST / -X OPTIONS  (headers CORS y preflight)
aws lambda get-function --function-name jalducin-assistant --region us-east-2
aws lambda get-function-concurrency --function-name jalducin-assistant --region us-east-2
aws dynamodb describe-table --table-name jalducin-assistant --region us-east-2
aws dynamodb describe-time-to-live --table-name jalducin-assistant --region us-east-2
aws budgets describe-budgets --account-id 957266312835
aws budgets describe-notifications-for-budget --account-id 957266312835 --budget-name alerta-free-tier
gh run list --workflow=deploy-assistant.yml --limit 5
python -c "import cv2; ... QRCodeDetector().detectAndDecode(...)"  (assets/img/QR.png, QR-linkedin.png)
git log --all --oneline -- assets/img/QR.png cv/cv.html
cp llms.txt backend/assistant/profile.txt  (mismo paso que hace el CI) + PYTHONIOENCODING=utf-8 python scripts/i18n/audit_i18n.py
Chrome headless --dump-dom / --screenshot en 1280/768/480 con click inyectado sobre #ai-fab
```

## Evidencia por spec (requirement -> evidencia)

### `asistente-ia-backend`

| Requirement | Evidencia | Estado |
|---|---|---|
| Backend proxy, credencial solo en backend | `backend/assistant/app.py:25` (`boto3.client("bedrock-runtime")`, IAM — sin API key); `index.html:886` solo expone la URL del endpoint | PASS |
| Respuesta a pregunta del perfil | curl (a): "¿En qué rol está Juan actualmente?" -> 200, "Service Support Tech Lead & AI Specialist en Podemos Progresar" (correcto) | PASS |
| CORS a orígenes del sitio | `app.py:45-54` (`_cors`); header `access-control-allow-origin: https://d3r3bnavnwzqaw.cloudfront.net` confirmado en respuesta real; env `ALLOWED_ORIGINS=https://d3r3bnavnwzqaw.cloudfront.net,https://jalducin.github.io` (AWS, solo lectura) | PASS |
| Grounding / no inventar | curl (b): "receta de tacos al pastor" -> declina, sin inventar, ofrece contacto | PASS |
| Resistencia a prompt-injection / on-topic | `app.py:38-39` (system prompt instruye ignorar cambios de rol / fuga de prompt); no se hizo llamada adicional en vivo para no exceder el presupuesto de peticiones del endpoint (evidencia por código) | PASS (por código) |
| Modelo económico + max_tokens acotado | `app.py:16,18` `MODEL_ID=us.anthropic.claude-haiku-4-5-20251001-v1:0`, `MAX_TOKENS=400`; confirmado en `Environment.Variables` de AWS | PASS |
| Reserved concurrency baja | `aws lambda get-function-concurrency` -> sin `ReservedConcurrentExecutions` (no configurada) | **FAIL — gap real** |
| Budgets avisan al correo | `aws budgets describe-budgets` -> 3 budgets activos (`alerta-free-tier`, `personal-tier0-alert`, `plataforma-ingles-dev`); `describe-notifications-for-budget` -> notificación `ACTUAL > $0.01` configurada | PASS (no se confirmó el email suscriptor exacto, fuera de alcance de esta auditoría) |
| Degradación elegante | `app.py:142-144` (catch de Bedrock -> mensaje con contacto, sin stacktrace); curl (c) confirma 400 limpio sin stacktrace ante payload inválido | PASS |
| Sin RAG, contexto embebido | `app.py:28-29,41` (`profile.txt` completo en el system prompt) | PASS |
| Caché de respuestas | curl repetido de (a) -> `"cached": true` en la segunda llamada; `app.py:119-127` | PASS |
| Rate limiting por IP + tope global | `app.py:108-117`; tabla DynamoDB `jalducin-assistant` `PAY_PER_REQUEST` + TTL `ttl` `ENABLED` (AWS, solo lectura); no se probó con ráfagas (instrucción explícita) | PASS (config verificada, no cargada) |

### `asistente-ia-chat-widget`

| Requirement | Evidencia | Estado |
|---|---|---|
| Widget vanilla, fetch al backend, loading, Enter | `index.html:729-738` (markup), `index.html:902-914` (`ask()`, estado "escribiendo…", `form submit`) | PASS |
| Responsive / paleta | `.ai-panel{width:min(380px,92vw)...}` (`index.html:212`) usa `var(--card-bg)`, `var(--border)`; probe headless en 1280/768/480: `overflow_x_after_open: false` en los tres anchos | PASS |
| Accesible: teclado, foco, Esc | Probe DOM headless: `fab_aria_label="Abrir asistente de IA"`, `panel_aria_label="Asistente de IA"`, `panel_role="dialog"`, `focus_on_input_after_open: true`, `panel_closed_after_escape: true` en 1280/768/480 | PASS |
| `prefers-reduced-motion` | El widget no tiene animaciones propias (solo `display:none/flex`); el matrix-bg sí respeta `prefers-reduced-motion` (`index.html:766-770`), no aplica directamente al panel | PASS (n/a: sin animación que mitigar) |
| Degradación si backend falla | `index.html:911-913` (catch de `fetch` -> mensaje + contacto) | PASS (por código; no se forzó un fallo real del backend para no desestabilizar producción) |
| Credencial nunca en el front | `index.html:886` solo contiene `ASSISTANT_URL` (URL pública), sin key | PASS |
| Chips de preguntas sugeridas | `index.html:896,899` — 4 chips (`CHIPS` array); probe: `chips_count: 4` | PASS |
| Tope de turnos por sesión | `index.html:897,904` — `MAX_TURNS=8`, mensaje de contacto al llegar al tope | PASS (por código) |

### `cicd-asistente-aws`

| Requirement | Evidencia | Estado |
|---|---|---|
| Deploy automático git -> AWS | `.github/workflows/deploy-assistant.yml:6-10` (paths trigger) + `:46-51` (`aws lambda update-function-code`); `gh run list` -> 5+ runs `success`, el más reciente 2026-09-20 | PASS |
| OIDC sin llaves estáticas | `deploy-assistant.yml:13-14,32-35` (`id-token: write`, `role-to-assume: arn:aws:iam::957266312835:role/gh-actions-portfolio-deploy`) | PASS |
| Permiso mínimo del rol | No se auditó la policy IAM completa (el classifier del sandbox bloqueó la exploración de políticas IAM por tratarse de "credential exploration"); se confirmó por evidencia indirecta que el rol solo hace `update-function-code` en los workflows (`deploy.yml` para S3/CloudFront, `deploy-assistant.yml` para Lambda) | PASS (parcial — no verificado el JSON de la policy) |

### `qr-apunta-al-sitio-aws`

| Requirement | Evidencia | Estado |
|---|---|---|
| QR apunta al sitio AWS | Decodificado con OpenCV (`cv2.QRCodeDetector`): `assets/img/QR.png` -> `https://d3r3bnavnwzqaw.cloudfront.net` (exacto) | PASS |
| Estilo preservado | Commit `26964ca` "QR del CV apunta al sitio AWS ... conservando estilo JVAV, escaneable (EC-H, verificado)" ya aplicado y en el historial de esta rama | PASS |
| CV usa el QR actualizado | `cv/cv.html:93` referencia `assets/img/QR.png` (fuente única); PDF regenerado en el mismo commit | PASS |
| Verificación con lector real | Verificado en esta auditoría con decodificador de software (OpenCV) — no con celular físico (sin acceso a hardware desde el entorno del agente); el commit `26964ca` ya documenta una verificación equivalente | PASS (software; sin lector físico) |
| EC-H, logo <=25%, quiet zone, alto contraste | No re-verificado a nivel de bits (harían falta los parámetros de generación); el decode exitoso con logo central es evidencia indirecta de que la corrección de errores tolera el logo | PASS (indirecta) |
| URL única de verdad (coincide con JSON-LD/og/sitemap) | **NO coincide**: `index.html` sigue con `og:url`, `canonical` y JSON-LD `"url"` apuntando a `https://jalducin.github.io` (líneas 13-15, 27-28), y `sitemap.xml`/`robots.txt` también. El QR apunta a CloudFront. `README.md:48` explica que "GitHub Pages se mantiene en paralelo por ahora (rollback)" — es un estado transicional documentado, no un descuido, pero el requirement literal de esta spec no se cumple | **FAIL — gap real (o decisión pendiente de ratificar)** |

## Gaps reales (no corregidos — requieren decisión/código/infra, fuera del alcance permitido a este agente)

1. **Reserved concurrency no configurada** en el Lambda `jalducin-assistant` (severidad: media — riesgo de
   costo si hay abuso; mitigado parcialmente por rate-limit en DynamoDB, pero ese control corre *después*
   de invocar el Lambda, no antes). Acción sugerida: `aws lambda put-function-concurrency
   --function-name jalducin-assistant --reserved-concurrent-executions 2` (fuera de este agente: es una
   mutación de infra en vivo, no pasa por el flujo git->AWS).
2. **QR vs. URL canónica del sitio (JSON-LD/og/sitemap) desalineados** (severidad: baja/media — no rompe
   nada, pero el scenario "URL única de verdad" de la spec no se cumple literalmente). Es consistente con
   el estado de transición documentado en `README.md` (GitHub Pages en paralelo por rollback), pero
   convendría que el cambio decida explícitamente: o el QR vuelve a apuntar al dominio canónico vigente, o
   se actualiza `og:url`/canonical/JSON-LD/sitemap a CloudFront cuando se retire el paralelismo con GitHub
   Pages. No se tocó `index.html`/`sitemap.xml` en esta auditoría por ser una decisión de producto/SEO más
   amplia que un fix de widget.
3. **Duplicación de specs sin consolidar (tarea 6.2)**: `openspec/changes/mejoras-portafolio-ai-native/specs/asistente-ia-portafolio/spec.md`
   sigue existiendo como una versión temprana/menos detallada del mismo capability, y `openspec/specs/`
   (capabilities archivadas) no tiene ninguna entrada `asistente-ia-*` todavía — el cambio nunca se
   sincronizó. Acción sugerida: `/opsx:sync` de las 4 specs de este cambio a `openspec/specs/`, retirar el
   spec duplicado de `mejoras-portafolio-ai-native` (o marcarlo `REMOVED`/superseded) y entonces
   `/opsx:archive`. No se ejecutó en esta sesión porque es una acción de ciclo de vida OpenSpec más amplia
   que "verificar y documentar", y hacerlo a medias (sin resolver el gap #1) dejaría el archivo
   inconsistente con la realidad.
4. **Permiso mínimo del rol de CI no auditado a nivel de policy JSON** (el sandbox de este agente bloqueó
   la exploración de políticas IAM). Evidencia indirecta (los workflows solo llaman `update-function-code`
   / `s3 sync` + `cloudfront create-invalidation`) sugiere que está acotado, pero no se confirmó el
   documento de policy.

## Gaps corregidos en esta auditoría (documentales, bajo riesgo)

- `cv/README.md`: corregida la nota que decía que el QR "vincula al repositorio del portafolio" — ya
  apunta al sitio AWS (verificado por decodificación).
- `README.md`: nueva sección "Asistente IA ('Ask my portfolio')" documentando backend, CI/CD y controles
  de costo (no existía ninguna mención).
- `CLAUDE.md`: nueva sección "Asistente IA ('Ask my portfolio')" con la misma información, siguiendo el
  patrón de las secciones existentes (stack, CV).
- `openspec/changes/asistente-ia-portafolio/design.md`: nota de implementación — el cómputo real es API
  Gateway HTTP API (no Function URL, como decía la decisión original) y se documenta el gap de reserved
  concurrency, para que el registro de decisiones no contradiga lo desplegado.

## Widget — verificación headless (Chrome, 3 breakpoints)

Render con `--headless=new --dump-dom` sobre una copia de `index.html` con un script inyectado que hace
`click()` sobre `#ai-fab` y corre probes de accesibilidad/overflow. Resultado idéntico en los tres anchos:

```
1280px: overflow_x_after_open=false · focus_on_input_after_open=true · panel_closed_after_escape=true · chips_count=4
 768px: overflow_x_after_open=false · focus_on_input_after_open=true · panel_closed_after_escape=true · chips_count=4
 480px: overflow_x_after_open=false · focus_on_input_after_open=true · panel_closed_after_escape=true · chips_count=4
```

No se modificó `index.html` (el widget ya cumple; no había gaps de front que corregir).

## i18n

`PYTHONIOENCODING=utf-8 python scripts/i18n/audit_i18n.py` -> **57/57 PASS** (regenerando primero
`backend/assistant/profile.txt` desde `llms.txt`, el mismo paso que hace el CI — `profile.txt` está en
`.gitignore` y no existe en checkouts locales, por lo que el check "profile.txt == llms.txt" falla en
frío; no es una regresión de esta auditoría). No se tocó `index.html`, por lo que no se requería re-auditar
i18n, pero se corrió igual como control.

## Resultado

- Estado del cambio: **NO listo para archivar tal cual** — 3 gaps reales (severidad media/baja) más la
  tarea de consolidación de specs (6.2) pendiente. Backend, widget, CI/CD y QR funcionan correctamente en
  producción y están verificados con evidencia en vivo.
- Bloqueos para archivar: (1) reserved concurrency, (2) desalineación QR/URL canónica, (3) sync/dedup de
  specs contra `mejoras-portafolio-ai-native` y `openspec/specs/`.

## Addendum 2026-09-20 (cierre de gaps, ejecutado por el agente principal)
- Reserved concurrency: no aplicable en esta cuenta (`ConcurrentExecutions=10`, AWS exige ≥10 no reservadas → `InvalidParameterValueException`). Control equivalente aplicado: throttling del stage `$default` del HTTP API `vd4c00py15` → `ThrottlingRateLimit=2`, `ThrottlingBurstLimit=5` (`aws apigatewayv2 update-stage`), verificado con `get-stages`; preflight OPTIONS sigue 204.
- URL canónica: decisión del propietario — QR → CloudFront (donde se sirve), canónica pública → `https://jalducin.github.io`; scenario "URL única de verdad" actualizado en la spec.
- Specs sincronizadas a `openspec/specs/` (4 capabilities, `validate --specs` 24/24).
