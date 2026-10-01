# Tasks: migrar-backend-portafolio

Agente ejecutor: `frontend-developer`. Bloques ≤ 2 h. El agente ejecuta todas las verificaciones.
Orden por D4: **Fase 1** (sin dependencias externas) → **Fase 2** (requiere credenciales del dueño) → **Fase 3**.

## 0. Preparación (OBLIGATORIO — SIEMPRE PRIMERO)
- [x] 0.1 Step 0 — Crear la feature branch `feature/migrar-backend-portafolio` desde `main` actualizado
- [x] 0.2 Leer `docs/*-standards.md`, `.claude/rules/openspec-tasks-mandatory-steps.md`, `scripts/i18n/README.md`,
      `MIGRACION-BACKEND-SUPABASE.md`, proposal, design y las 5 specs del cambio

## 1. Fase 1 — Asistente local (sin bloqueos)
- [x] 1.1 `assistant/knowledge.md`: ≥18 entradas bilingües (`id`, `tags`, `en:`, `es:`) derivadas de `llms.txt`,
      cubriendo los temas de la spec; sin nombres internos del empleador
- [x] 1.2 `scripts/assistant/build_kb.py`: compila `knowledge.md` → `<script type="application/json"
      id="assistant-kb">` en `index.html`; idempotente; falla si falta `en` o `es` en alguna entrada
- [x] 1.3 `index.html`: reemplazar el `fetch` del widget por la resolución local (D1); retirar `ASSISTANT_URL`;
      chips y saludo con `data-i18n`; mensaje de "sin coincidencia" con sugerencias + CTAs
- [x] 1.4 n/a: el widget traduce sus textos desde el objeto `T` del propio script (saludo, chips, mensajes),
      no desde `data-i18n`; no hubo textos visibles nuevos en el DOM
- [x] 1.5 Eliminar `.github/workflows/deploy-assistant.yml` y el directorio `backend/assistant/`

## 2. Revisar y actualizar pruebas existentes (OBLIGATORIO)
- [x] 2.1 `scripts/i18n/audit_i18n.py`: quitar el check de `profile.txt == llms.txt` (ya no existe) y agregar:
      `#assistant-kb` presente y parseable, ≥18 entradas con `en`/`es`, sin `ASSISTANT_URL`/`execute-api` en
      `index.html`, sin nombres internos en la base, entradas clave coherentes con `llms.txt`
- [x] 2.2 `scripts/assistant/probe_kb.py` (nuevo): probes headless del bot — 6 preguntas conocidas (ES y EN)
      devuelven la entrada esperada, 1 pregunta fuera de alcance cae en el mensaje honesto, 0 peticiones de red

## 3. Ejecutar pruebas y verificar estado (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] 3.1 Estado previo: `git rev-parse HEAD`, `curl` a ambos endpoints (confirmar que no resuelven)
- [x] 3.2 `audit_i18n.py` 0 FAIL · `probe_i18n.py` 18/18 · `probe_kb.py` 0 FAIL
- [x] 3.3 Reporte `reports/AAAA-MM-DD-fase1-asistente-local.md` con comandos, resultados y estado antes/después
- [x] 3.4 Marcar solo con todo en PASS y el reporte creado

## 4. Verificación manual UI (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] 4.1 Headless 1280/768/480 con el panel abierto, en EN y ES: saludo, chips, respuesta real a una pregunta,
      mensaje de "sin coincidencia"; sin overflow; `Esc` cierra; foco al input
- [x] 4.2 Caso de error: `#assistant-kb` vaciado en una copia temporal → el widget muestra el CTA de contacto y
      no lanza excepción (borrar la copia al terminar)
- [x] 4.3 Documentar con rutas de capturas en el reporte

## 5. Documentación (OBLIGATORIO)
- [x] 5.1 `CLAUDE.md`: reescribir la sección "Asistente IA" (sin Bedrock/Lambda/DynamoDB; bot local + cómo
      editar la base); `docs/frontend-standards.md`: patrón de la base de conocimiento
- [x] 5.2 `llms.txt` + regla de coherencia con `assistant/knowledge.md`; `README.md` si menciona el backend
- [x] 5.3 Sincronizar specs (2 nuevas, 1 MODIFIED, 2 REMOVED) y `openspec validate --specs` verde

## 6. Cierre Fase 1
- [x] 6.1 Commit + merge `--no-ff` a `main` + push; workflows en success; verificación en vivo (chat responde)

## 7. Fase 2 — Contacto en Supabase (BLOQUEADA por el dueño)
- [ ] 7.1 **Dueño**: crear organización nueva + proyecto `portfolio` y entregar el `project ref`; crear API key
      de Resend. (El agente no puede crear organizaciones.)
- [ ] 7.2 `supabase/migrations/0001_contact_messages.sql`: tabla + índices + RLS habilitado sin políticas
- [ ] 7.3 `supabase/functions/contact/index.ts`: validación, honeypot, rate limit por `ip_hash` (5/h), insert,
      Resend, `update sent`, CORS para `jalducin.github.io` y CloudFront
- [ ] 7.4 Secretos: `RESEND_API_KEY`, `TO_EMAIL`, `IP_SALT` como Edge Function secrets; `SUPABASE_ACCESS_TOKEN`
      y `SUPABASE_PROJECT_REF` como secretos del repositorio
- [ ] 7.5 `.github/workflows/deploy-contact.yml` (CLI de Supabase) y borrar `deploy-contact-api.yml` y `contact-api/`
- [~] 7.6 `index.html`: `CONTACT_ENDPOINT=''` desde el 2026-10-01 (el endpoint de AWS ya no existe, así que el
      formulario va directo al fallback `mailto` sin esperar un fetch fallido); se repuebla con la URL de la Edge
      Function al terminar la Fase 2
- [ ] 7.7 Verificación (EL AGENTE EJECUTA): envío válido → 200 y correo recibido + fila `sent=true`; honeypot →
      4xx sin fila; email inválido → 4xx; 6 envíos seguidos → 429; `anon` no puede leer `contact_messages`;
      reporte `reports/AAAA-MM-DD-fase2-contacto.md`

## 8. Fase 3 — Limpieza y cierre
- [ ] 8.1 Con aprobación del dueño: borrar en AWS el rol `jalducin-assistant-lambda-role` y el log group
      `/aws/lambda/jalducin-assistant`; revisar si `gh-actions-portfolio-deploy` sigue en uso (sí: despliega el sitio)
- [ ] 8.2 Borrar `MIGRACION-BACKEND-SUPABASE.md`
- [ ] 8.3 `/opsx:verify` y archivar el cambio
