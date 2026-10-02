# Backend del formulario de contacto (Supabase)

Único backend del portafolio. El asistente del sitio **no** usa backend (ver `assistant/knowledge.md`).

El repositorio es la fuente de verdad: lo que está aquí es lo que debe estar desplegado. El dashboard de
Supabase nunca es la fuente de verdad.

## Qué hay

| Archivo | Qué es |
|---|---|
| `migrations/20261002000000_contact_messages.sql` | Tabla `contact_messages` con RLS habilitado y **sin políticas** (solo `service_role` escribe/lee) + índices |
| `functions/contact/index.ts` | Edge Function (Deno): CORS → validación → honeypot → rate limit → INSERT → Resend → `sent=true` |

## Proyecto

- Organización `haljordan's Org` (free) · proyecto **Portafolio** · ref `eolsklubeywfmuyrtxla` · región `us-west-2`
- Endpoint público: `https://eolsklubeywfmuyrtxla.supabase.co/functions/v1/contact`
- Consumido desde `index.html` (`CONTACT_ENDPOINT`). Si la petición falla, el formulario cae a `mailto`.
- Desplegado con `verify_jwt = false` (es un formulario público); la función implementa sus propias
  protecciones: allowlist de orígenes, honeypot, validación y rate limiting.

## Secretos (Edge Function secrets, nunca en el repo)

| Secreto | Obligatorio | Default | Para qué |
|---|---|---|---|
| `RESEND_API_KEY` | no | — | Enviar el correo. **Sin ella el mensaje se guarda igual** y la respuesta es `{ok:true,queued:true}` |
| `TO_EMAIL` | no | `valentin.alducin88@gmail.com` | Destinatario |
| `FROM_EMAIL` | no | `onboarding@resend.dev` | Remitente (dominio de pruebas de Resend) |
| `IP_SALT` | recomendable | `jalducin-portfolio` | Sal del hash de IP para el rate limiting |

Se cargan en: Project Settings → Edge Functions → Secrets, o con
`supabase secrets set RESEND_API_KEY=...`.

## Desplegar

Desde los artefactos de este directorio, sin CI (decisión del proyecto: la función cambia pocas veces al año):

```bash
supabase link --project-ref eolsklubeywfmuyrtxla
supabase db push                       # aplica migrations/
supabase functions deploy contact --no-verify-jwt
```

## Verificar

```bash
U=https://eolsklubeywfmuyrtxla.supabase.co/functions/v1/contact
O=https://jalducin.github.io
curl -s -X OPTIONS -D- -H "Origin: $O" -H "Access-Control-Request-Method: POST" $U | head -1   # 204
curl -s -X POST -H "Content-Type: application/json" -H "Origin: $O" \
  -d '{"name":"X","email":"x@x.com","subject":"s","message":"m","website":""}' $U              # {"ok":true}
curl -s -X POST -H "Content-Type: application/json" -H "Origin: $O" \
  -d '{"name":"x","email":"no-es-email","subject":"x","message":"x"}' $U                        # 400
```

La tabla no es legible con la clave pública: `GET /rest/v1/contact_messages` con la `anon`/publishable
responde `401 permission denied` (RLS sin políticas). Para leer los mensajes se usa el dashboard o SQL con
`service_role`.
