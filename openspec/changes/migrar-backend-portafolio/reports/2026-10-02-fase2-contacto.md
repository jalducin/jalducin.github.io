# Reporte Fase 2 — Formulario de contacto en Supabase

- Fecha: 2026-10-02 · Cambio: migrar-backend-portafolio · Agente: frontend-developer (Claude Code)
- Proyecto: `Portafolio` (`eolsklubeywfmuyrtxla`), org `haljordan's Org` (free), `us-west-2`

## Decisión de alcance (dueño, 2026-10-02)
Sin CI ni `SUPABASE_ACCESS_TOKEN` en GitHub: "este repo es más simple, no requiere gran cosa" y
"controlemos todo por repo local con SDD". Los artefactos (`supabase/migrations/`, `supabase/functions/`)
son la fuente de verdad y el despliegue se hace desde ellos. La spec `contacto-backend-supabase` se alineó
(escenario "Artefactos versionados y despliegue desde el repo" sustituye al de CI).

## Comandos ejecutados
- `apply_migration contact_messages` (conector Supabase) → tabla + 2 índices + RLS sin políticas + `revoke all`
- `deploy_edge_function contact` (`verify_jwt=false`, v1 ACTIVE)
- `curl` × 5 contra el endpoint; `curl` × 2 contra PostgREST con la clave publicable
- Probe headless del formulario real desde `file://` y desde `http://localhost:5500`
- `execute_sql` para verificar las filas

## Resultados
| Caso | Esperado | Obtenido |
|---|---|---|
| Preflight `OPTIONS` con Origin del sitio | 204 + ACAO | **204**, `Access-Control-Allow-Origin: https://jalducin.github.io` |
| Envío válido | 200 y fila guardada | **200** `{"ok":true,"queued":true}` + fila con `sent=false`, `error="RESEND_API_KEY no configurada"` |
| Honeypot (`website` lleno) | 200 sin fila | **200** `{"ok":true}`, sin fila |
| Email inválido | 400 sin fila | **400** `{"error":"invalid email"}`, sin fila |
| JSON malformado | 400 sin traza | **400** `{"error":"invalid json"}` |
| `anon` lee la tabla | denegado | **401** `permission denied for table contact_messages` |
| `anon` inserta | denegado | **401** `permission denied` |
| Formulario desde `file://` (origen no permitido) | fallback `mailto` | cae al fallback, mensaje "Abriendo tu app de correo…" |
| Formulario desde `http://localhost:5500` (origen permitido) | éxito y reset | **"✓ Message sent! I will reply soon."**, formulario reseteado, fila en la tabla |

## Estado
- `index.html`: `CONTACT_ENDPOINT` apunta a la Edge Function; el fallback `mailto` sigue intacto.
- Pendiente opcional del dueño: cargar `RESEND_API_KEY` (y `IP_SALT`) como Edge Function secrets. Sin ella el
  sistema ya **no pierde mensajes**: quedan en la tabla con `error` explicando por qué no se envió el correo.
- Quedan 2 filas de prueba en `contact_messages` (los envíos de verificación); el borrado se declinó al pedir
  confirmación, así que se dejan para que el dueño las elimine desde el dashboard si quiere.

## Resultado: PASS · Bloqueos: ninguno
