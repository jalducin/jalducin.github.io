# Design: migrar-backend-portafolio

## Context

- Estado verificado 2026-10-01: `https://vd4c00py15…` y `https://tekik4wm8e…` no resuelven (curl exit 6). El
  widget cae siempre en su `catch`; el formulario cae en su fallback `mailto` (sigue funcionando).
- Supabase (MCP, 2026-10-01): org `gbjvahsnbkecstsiyffb` con `Fidello` y `Fidello QAS` **ACTIVE_HEALTHY** e
  `IMMEX` **INACTIVE**. El plan free permite 2 proyectos activos **por organización**.
- Decisiones del dueño (2026-10-01): plataforma = **Supabase en organización nueva**; modelo = **ninguno**
  ("simular respuestas con una base tipo skills.md, un RAG tipo bot"); correo = **Resend free + fila en tabla**.
- Restricciones del repo: HTML/CSS/JS vanilla, CSS y JS embebidos, sin npm en el sitio, i18n obligatorio para
  texto visible, sin nombres internos del empleador, responsive 992/768/480.

## Goals / Non-Goals

**Goals:** chat funcionando otra vez con costo $0 y sin backend; formulario que no pierda mensajes; cero
secretos en repo/front; que nada dependa ya de AWS; mismo UX y bilingüismo.

**Non-Goals:** no se reintroduce un LLM; no se toca Fidello (ni PROD ni QAS); no se migra el hosting del sitio
(sigue GitHub Pages + CloudFront); no se construye panel de administración de mensajes.

## Decisions

### D1. Asistente: recuperación en el cliente, sin LLM ni backend
Alternativas: (a) Edge Function con API de Anthropic — descartada: el dueño pidió explícitamente algo más
simple y sin costo; (b) Edge Function con el mismo bot determinista — descartada: añade red, CORS, cold start
y un despliegue más para algo que no necesita servidor; (c) **elegida**: todo en el navegador.
- Fuente: `assistant/knowledge.md` (Markdown con bloques `## <id>`, línea `tags:` y secciones `en:`/`es:`).
- Build: `scripts/assistant/build_kb.py` → `<script type="application/json" id="assistant-kb">` en `index.html`.
- Runtime (~45 líneas): normaliza (minúsculas, sin acentos/puntuación), tokeniza, puntúa cada entrada
  `score = 3·(tags que aparecen en la pregunta) + 1·(tokens compartidos con la respuesta)`, normaliza por
  longitud de la pregunta; devuelve la mejor si `score >= UMBRAL` (2), si no el mensaje honesto con sugerencias.
- Idioma: usa `window.__getLang()` del i18n ya existente; los chips y el saludo se traducen con `data-i18n`.
- Beneficio lateral: el asistente funciona offline y en `file://`, así que las verificaciones headless lo
  prueban de verdad (antes dependían del endpoint).

### D2. Contacto: Supabase en organización nueva
- Organización nueva (2 slots free) → proyecto `portfolio` (región `us-east-1`, cercana a CloudFront). **No se
  pausa ni se borra nada de Fidello**: PROD es un piloto en cafeterías reales (ver `CLAUDE.md`).
- `supabase/functions/contact/index.ts` (Deno): valida → honeypot → rate limit por `ip_hash` (5/h) →
  `insert` en `contact_messages` → envía con Resend → `update sent=true`.
- Orden "guardar antes de enviar" a propósito: si Resend falla, el mensaje no se pierde y el visitante recibe
  `{"ok":true,"queued":true}`.
- `ip_hash` = SHA-256 de IP + sal (secreto): permite rate limiting sin almacenar la IP.
- RLS activo sin políticas: solo `service_role` (dentro de la función) accede. `anon` no lee nada.
- Migración SQL versionada en `supabase/migrations/`; despliegue por CI con el CLI de Supabase.

### D3. Qué se retira
`backend/assistant/` y `contact-api/` salen del repo (quedan en git y en el archivo del cambio);
`deploy-assistant.yml` y `deploy-contact-api.yml` se eliminan; `deploy-contact.yml` los reemplaza.
`profile.txt` dejaba de tener sentido (era el grounding del LLM) → su contenido pasa a ser responsabilidad de
`assistant/knowledge.md`, que se escribe **derivado de `llms.txt`** para no duplicar la fuente de verdad.

### D4. Orden de ejecución (porque hay bloqueos externos)
1. **Ahora, sin dependencias:** asistente local + retiro del `ASSISTANT_URL` + specs/docs/CI del asistente.
   Esto repara lo único que hoy está visiblemente roto.
2. **Cuando el dueño cree la org/proyecto y la key de Resend:** desplegar la Edge Function y cambiar
   `CONTACT_ENDPOINT`. Mientras tanto el formulario sigue con `mailto` (funciona hoy).
3. **Al final, con aprobación:** limpieza en AWS (rol `jalducin-assistant-lambda-role`, log group
   `/aws/lambda/jalducin-assistant`) y borrado de `MIGRACION-BACKEND-SUPABASE.md`.

## Risks / Trade-offs

- [Respuestas menos "inteligentes" que un LLM] → se mitiga con una base amplia (≥18 entradas), alias por
  entrada y un mensaje honesto cuando no hay match; nunca inventa. Es también más predecible para un
  reclutador.
- [La base queda desactualizada respecto a `llms.txt`] → `audit` comprueba que las entradas clave (rol actual,
  proyectos) coincidan con `llms.txt`; regla documentada en `docs/frontend-standards.md`.
- [+~8 KB en `index.html`] → despreciable; no hay petición de red que ahorrar.
- [Resend sin dominio propio solo envía al correo de la cuenta] → es justo el caso de uso (avisar al dueño).
- [Bloqueo externo] → el paso 1 entrega valor sin esperar a nadie.

## Migration Plan
Rama `feature/migrar-backend-portafolio` → paso 1 → merge y deploy → paso 2 cuando lleguen las credenciales →
paso 3 limpieza → `/opsx:verify` y archivar. Rollback: `git revert` del merge (el sitio es estático).

## Open Questions
Ninguna bloqueante para el paso 1. Pendientes del dueño: `project ref` de Supabase y API key de Resend.
