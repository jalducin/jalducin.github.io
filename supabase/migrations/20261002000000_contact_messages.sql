-- Mensajes del formulario de contacto del portafolio.
-- Cambio OpenSpec: migrar-backend-portafolio (capability contacto-backend-supabase).
-- La Edge Function escribe con service_role; nadie más puede leer ni escribir.

create table if not exists public.contact_messages (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  name        text        not null,
  email       text        not null,
  subject     text        not null,
  message     text        not null,
  ip_hash     text,                      -- SHA-256 de IP + sal: permite rate limiting sin guardar la IP
  sent        boolean     not null default false,
  error       text
);

comment on table  public.contact_messages is 'Mensajes del formulario de jalducin.github.io. Se guarda ANTES de enviar el correo para no perder ninguno.';
comment on column public.contact_messages.ip_hash is 'SHA-256(ip + IP_SALT). No se almacena la IP en claro.';

create index if not exists contact_messages_created_at_idx on public.contact_messages (created_at desc);
create index if not exists contact_messages_ip_hash_idx    on public.contact_messages (ip_hash, created_at desc);

-- RLS habilitado y SIN políticas: anon/authenticated no pueden leer ni escribir.
-- service_role (la Edge Function) ignora RLS por diseño.
alter table public.contact_messages enable row level security;

revoke all on public.contact_messages from anon, authenticated;
