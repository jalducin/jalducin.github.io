# Proposal: migrar-backend-portafolio

## Why

El 2026-10-01 el backend en AWS del portafolio desapareció en una limpieza de la cuenta `957266312835`: se
borraron la Lambda `jalducin-assistant`, su API Gateway (`vd4c00py15`), la tabla DynamoDB de caché/límites, la
Lambda del formulario (`jalducin-contact-api-dev-contact`) y su API (`tekik4wm8e`). Verificado el 2026-10-01:
ambos endpoints ya no resuelven. Hoy el chat "Ask my portfolio" responde siempre el mensaje de error del
`catch` y el formulario cae a su fallback `mailto`. Además el motivo de fondo es el costo de AWS: el dueño
quiere un backend gratuito y sin mantenimiento.

## What Changes

- **Asistente sin LLM ni backend (decisión del dueño, 2026-10-01):** el widget pasa de llamar a un endpoint
  con Claude en Bedrock a resolver la respuesta **en el navegador** contra una base de conocimiento curada
  ("RAG tipo bot"): recuperación por coincidencia de palabras clave sobre entradas Q&A bilingües. Fuente
  editable en Markdown (`assistant/knowledge.md`), compilada a un `<script type="application/json"
  id="assistant-kb">` embebido en `index.html` (mismo patrón que el diccionario i18n). **Costo $0, sin API
  key, sin CORS, sin límites de uso, funciona también en `file://`.**
- **Formulario de contacto en Supabase:** Edge Function `contact` en un proyecto nuevo (organización nueva, 2
  slots gratis; **no se toca Fidello**), que guarda cada mensaje en la tabla `contact_messages` (RLS activo,
  solo `service_role` escribe) y envía el correo con **Resend** (plan gratuito, destino el correo del dueño).
  El fallback `mailto` del front se conserva.
- **Front:** se retira `ASSISTANT_URL`; `CONTACT_ENDPOINT` apunta a la Edge Function. Sin otros cambios de UX:
  mismos chips, mismo panel, mismos textos (bilingües vía `data-i18n`).
- **CI/CD y limpieza:** se retiran `.github/workflows/deploy-assistant.yml` y `deploy-contact-api.yml` y se
  reemplaza por el despliegue de la Edge Function; `backend/assistant/` y `contact-api/` se archivan dentro
  del cambio. En AWS quedan por borrar (con aprobación): rol `jalducin-assistant-lambda-role` y el log group
  `/aws/lambda/jalducin-assistant`.
- Se borra `MIGRACION-BACKEND-SUPABASE.md` al archivar el cambio (es nota de traspaso, no documentación).

## Capabilities

### New Capabilities
- `asistente-local-retrieval`: bot de recuperación sin LLM — base de conocimiento curada, compilación a JSON
  embebido, algoritmo de coincidencia, respuestas bilingües y degradación honesta cuando no hay match.
- `contacto-backend-supabase`: Edge Function de contacto, persistencia con RLS, envío de correo, validación,
  honeypot y rate limiting; sin secretos en el repo ni en el front.

### Modified Capabilities
- `asistente-ia-chat-widget`: el widget deja de hacer `fetch` a un backend; resuelve localmente y conserva
  accesibilidad, degradación y ausencia de secretos.

### Removed Capabilities
- `asistente-ia-backend`: ya no existe backend de LLM para el asistente.
- `cicd-asistente-aws`: ya no hay Lambda que desplegar.

## Impact

- `index.html` (widget, `CONTACT_ENDPOINT`, KB embebida), `assistant/knowledge.md` (nuevo),
  `scripts/assistant/build_kb.py` (nuevo), `scripts/i18n/*` (claves nuevas del widget si aplica).
- `supabase/functions/contact/index.ts` + `supabase/migrations/*.sql` (nuevos, en este repo).
- `.github/workflows/`: se elimina `deploy-assistant.yml` y `deploy-contact-api.yml`; se agrega
  `deploy-contact.yml` (Supabase CLI con `SUPABASE_ACCESS_TOKEN`).
- `backend/assistant/`, `contact-api/`: se retiran del repo (quedan en el historial y en el archivo del cambio).
- `CLAUDE.md` (sección del asistente), `docs/frontend-standards.md`, `llms.txt`, specs.
- **Bloqueos externos (acciones del dueño):** crear la organización y el proyecto de Supabase y entregar el
  `project ref`; crear la API key de Resend. Mientras tanto el formulario sigue con el fallback `mailto`.
