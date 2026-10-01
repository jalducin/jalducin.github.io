# Traspaso: migrar el backend del portafolio (asistente IA + formulario de contacto) fuera de AWS

> Nota de traspaso del 2026-10-01. Es la entrada para un cambio OpenSpec de este repo (`/opsx:new`).
> No es documentación vigente: cuando el cambio se archive, borra este archivo o muévelo al cambio.

## 1. Situación actual (verificada el 2026-10-01, solo lectura)

- **El backend en AWS ya no existe.** El 2026-10-01, entre las 13:26 y las 13:41 (CDMX), el usuario IAM
  `jalducin88` lo borró en una limpieza de la cuenta `957266312835`, junto con recursos de pyzzeria, enkoth-tickets,
  soporte, metalshop y plataforma-ingles. Según CloudTrail se borró:

  | Recurso | Nombre | Lo usaba |
  |---|---|---|
  | Lambda | `jalducin-assistant` | Asistente "Ask my portfolio" (Bedrock, Claude Haiku 4.5) |
  | API Gateway HTTP | `vd4c00py15` | `ASSISTANT_URL` en `index.html` |
  | DynamoDB | `jalducin-assistant` | Caché de respuestas y límites de uso |
  | Lambda | `jalducin-contact-api-dev-contact` | Formulario de contacto (envía correo con SES) |
  | API Gateway HTTP | `tekik4wm8e` | `…/contact` en `index.html` |

- **Lo que sigue en AWS:** el rol IAM `jalducin-assistant-lambda-role` (creado el 2026-06-12) y el grupo de logs
  `/aws/lambda/jalducin-assistant`. Bórralos cuando termines la migración.
- **Lo que ve hoy un visitante:** el chat contesta siempre "Ahora mismo no puedo responder. Escríbele a Juan…"
  (el `catch` del widget) y el formulario de contacto no envía.
- **Uso real:** el asistente tuvo 8 invocaciones en septiembre de 2026. Solo falló el 2026-06-12, el día de la
  configuración, porque faltaba el formulario de caso de uso de Anthropic en Bedrock; después funcionó.
- **Workflows de CI que hoy fallarían:**
  - `.github/workflows/deploy-assistant.yml` solo hace `update-function-code` y la función ya no existe;
  - `.github/workflows/deploy-contact-api.yml` sí recrearía el stack con `serverless deploy`, pero en AWS.

## 2. Objetivo

Mover el asistente y el formulario de contacto a un backend **gratuito** (el dueño propone **Supabase**), sin
cambiar la experiencia del visitante ni el stack del sitio (HTML, CSS y JS vanilla en GitHub Pages).

## 3. Restricciones que hay que respetar

1. **Supabase free admite solo 2 proyectos activos por organización.** La organización `jalducin's Org` (plan
   free) ya tiene esos 2:

   | Proyecto | Estado |
   |---|---|
   | `Fidello` (`rmbojwpyvognmbswnbgk`) | activo |
   | `Fidello QAS` (`xozsrcnjnugwbrrrwoeb`) | activo |
   | `IMMEX` (`ljcjdmxtazegtakfzkge`) | pausado |

   - **No se toca nada de Fidello**: ni pausarlo, ni agregarle funciones, ni tablas.
   - Para un proyecto del portafolio en Supabase hay tres caminos:
     - reusar el lugar de `IMMEX`, si ya no se usa;
     - una organización nueva (cada una tiene sus 2 proyectos gratis);
     - pasar a un plan de pago.
   - **El dueño debe decidir esto antes de diseñar.**
2. **El modelo de IA no es gratis en ningún hosting.** Supabase no ofrece Claude. Las opciones son:
   - API de Anthropic (Claude Haiku) con una API key guardada como secreto de la función;
   - Bedrock con llaves de un usuario IAM (de larga duración; menos seguro que el rol que tenía la Lambda);
   - quitar el chat.

   Con los límites actuales (500 consultas al día como máximo) el costo esperado es de centavos al mes.
3. **El correo del formulario:** SES era de AWS. Fuera de AWS hacen falta otra de estas opciones:
   - un proveedor con plan gratis (p. ej. Resend, que permite enviar al correo de la cuenta sin dominio propio);
   - guardar los mensajes en una tabla y revisarlos ahí.
4. **Sin secretos en el repo ni en el front.** Las llaves van como secretos de la plataforma, nunca en
   `index.html`.
5. **Alternativa gratuita sin el límite de proyectos:** Deno Deploy (el dueño ya lo usa en otro proyecto) o
   Cloudflare Workers. Considérala si Supabase no tiene lugar.

## 4. Contrato que el front ya espera (no lo rompas)

- **Asistente:**
  - petición: `POST <ASSISTANT_URL>`, body `{ "question": "<texto ≤ 500>" }`;
  - respuesta: `{ "answer": "...", "cached"?: true, "limited"?: true, "error"?: true }`; con 429 también se
    manda `answer`;
  - CORS para `https://jalducin.github.io`.
- **Contacto:** `POST …/contact`. Revisa `contact-api/handler.py` para el body exacto y las respuestas.
- **Reglas del asistente a conservar** (`backend/assistant/app.py`):
  - el system prompt está anclado al perfil (`llms.txt` → `profile.txt`), sin RAG, y responde en el idioma de la
    pregunta, en 2–4 frases;
  - protección contra prompt injection;
  - límites: 10 por minuto por IP, 50 por día por IP y 500 por día en total;
  - caché de 7 días para preguntas normalizadas;
  - `max_tokens` de 400;
  - si falla el modelo, responde con un mensaje de contacto (nunca un error crudo).

## 5. Plan sugerido (cambio OpenSpec en este repo)

1. **Decisiones del dueño** (ver §3): plataforma y proyecto, modelo de IA y vía de correo.
2. `/opsx:new migrar-backend-portafolio` con proposal, specs (modifica `asistente-ia-backend` y la del contacto),
   design y tasks, con los pasos obligatorios de este repo.
3. **Backend:**
   - Si es Supabase: dos Edge Functions (`assistant`, `contact`), una tabla `assistant_cache` con TTL y otra
     `rate_limits` (o una sola tabla con `pk`, `c`, `expires_at`), con RLS activado y solo `service_role`
     escribiendo. Los secretos van en Edge Function secrets.
   - Si es Deno Deploy: una app separada con las dos rutas y Deno KV para caché y límites.
4. **Front:** cambiar `ASSISTANT_URL` y la URL de contacto en `index.html` (y en el diccionario ES si las repite).
   Nada más.
5. **CI:** reemplazar `deploy-assistant.yml` y `deploy-contact-api.yml` por el despliegue de la plataforma nueva,
   o borrarlos. `profile.txt` se sigue generando desde `llms.txt`.
6. **Verificación:**
   - pregunta real desde `https://jalducin.github.io` (CORS);
   - pregunta repetida → `cached`;
   - ráfaga → 429 con `answer`;
   - modelo caído → mensaje de contacto;
   - formulario → llega el correo (o queda la fila).
7. **Limpieza en AWS** (al final, con aprobación del dueño): el rol `jalducin-assistant-lambda-role`, el grupo de
   logs `/aws/lambda/jalducin-assistant`, el rol OIDC `gh-actions-portfolio-deploy` si ya no se usa, y
   actualizar `backend/assistant/README.md` y `contact-api/README.md`.
8. Archivar el cambio y borrar este archivo.

## 6. Mientras se migra

Opcional: si la migración va a tardar, oculta el botón del chat o cambia su texto inicial, y deja el correo y
LinkedIn como contacto directo, para que nadie vea un chat que no responde.
