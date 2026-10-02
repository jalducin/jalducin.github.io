# Capability: contacto-backend-supabase

## Purpose

Backend del formulario de contacto en Supabase: una Edge Function que valida, guarda el mensaje con RLS y lo
envía por correo, con secretos fuera del repositorio y sin tocar los proyectos de Fidello.

## Requirements

### Requirement: Edge Function de contacto en Supabase

El formulario de contacto SHALL ser atendido por una Edge Function de Supabase (`supabase/functions/contact`)
desplegada en un proyecto propio del portafolio, en una **organización distinta** a la de Fidello. El proyecto
de Fidello (PROD y QAS) NO se modifica, ni se pausa, ni se reutiliza.

#### Scenario: Contrato compatible con el front actual
- **WHEN** el front hace `POST` a la función con `{name, email, subject, message, website}`
- **THEN** responde `200 {"ok": true}` en éxito y `4xx` con `{"error": "..."}` ante entrada inválida
- **AND** responde CORS para `https://jalducin.github.io` y para el origen de CloudFront, y `204` al preflight
- **AND** el front conserva su fallback `mailto` si la petición falla

#### Scenario: Validación y honeypot
- **WHEN** llega una petición con `website` no vacío (honeypot), email inválido, campos faltantes o `message`
  de más de 5 000 caracteres
- **THEN** se rechaza sin enviar correo ni escribir fila, con `4xx` y mensaje breve
- **AND** no se devuelve traza ni detalle interno

#### Scenario: Límite de abuso
- **WHEN** una misma IP envía más de 5 mensajes en una hora
- **THEN** la función responde `429` con un mensaje claro y no envía correo

### Requirement: Persistencia con RLS y envío de correo

Cada mensaje válido SHALL guardarse en la tabla `contact_messages` **antes** de intentar el envío, de modo que
ningún mensaje se pierda si el proveedor de correo falla; el envío se hace con **Resend** (plan gratuito) al
correo del dueño.

#### Scenario: Tabla protegida
- **WHEN** se revisa el esquema
- **THEN** `contact_messages` tiene `id`, `created_at`, `name`, `email`, `subject`, `message`, `ip_hash`,
  `sent` (boolean) y `error` (texto, nullable)
- **AND** la tabla tiene RLS habilitado **sin políticas públicas**: solo `service_role` (la función) escribe y
  lee; las claves `anon`/`publishable` no pueden leer mensajes

#### Scenario: Degradación si el correo falla
- **WHEN** Resend devuelve error o no hay API key configurada
- **THEN** la fila queda guardada con `sent = false` y el `error`, y la función responde `200 {"ok": true,
  "queued": true}` para no perder el mensaje del visitante
- **AND** el incidente es visible consultando la tabla

#### Scenario: Secretos fuera del repo y del front
- **WHEN** se inspeccionan el repositorio y el JS del sitio
- **THEN** no aparece ninguna API key (Resend ni Supabase `service_role`); solo la URL pública de la función
- **AND** los secretos viven como Edge Function secrets del proyecto y como secretos del repositorio en CI

### Requirement: Despliegue reproducible

El despliegue de la función y las migraciones SHALL ser reproducible desde el repositorio (`supabase/`), sin
pasos manuales en la consola más allá de crear el proyecto y cargar los secretos.

#### Scenario: Artefactos versionados y despliegue desde el repo
- **WHEN** se necesita recrear o actualizar el backend del formulario
- **THEN** la migración (`supabase/migrations/*.sql`) y la función (`supabase/functions/contact/index.ts`) viven
  en el repositorio y son la fuente de verdad; el dashboard de Supabase nunca lo es
- **AND** el despliegue se hace desde esos artefactos (conector de Supabase o `supabase functions deploy`), sin
  workflow de CI: la función cambia pocas veces al año y el proyecto evita infraestructura innecesaria
  (decisión del dueño, 2026-10-02)
- **AND** los workflows de AWS (`deploy.yml`, `deploy-assistant.yml`, `deploy-contact-api.yml`) ya no existen
