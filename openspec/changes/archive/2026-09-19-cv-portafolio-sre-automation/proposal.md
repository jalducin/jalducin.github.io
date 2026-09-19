# Proposal: cv-portafolio-sre-automation

## Why

El CV y el portafolio venden un perfil "Backend + Agentic AI" genérico, mientras que la evidencia real del
último año en Podemos Progresar (sep 2025 → sep 2026) es otra: **confiabilidad/SRE** (sistema de
post-mortems, uptime mensual 99.95 %, runbooks), **automatización** (n8n con SDK, pipelines spec-driven,
integraciones Freshdesk/Notion/Asana/Slack), **SQL/ETL crítico en producción** e **IA aplicada** (Skill
de routing de tickets, SDD). Además, Fidello ya es un **piloto en beta cloud** con métricas duras (~790
pruebas, 89 migraciones, 97 cambios OpenSpec) que hoy ni se mencionan, y las skills listan tecnologías sin
evidencia de uso (Amazon Kendra, AWS Kiro). Con el cambio de rol reciente (Service Support Tech Lead & IA
Specialist) es el momento de alinear CV (1 página), portafolio, `llms.txt` y LinkedIn a lo que sí se hace.

## What Changes

- **Posicionamiento híbrido**: headline pasa de "Senior Backend Engineer | Tech Lead | Agentic AI Systems"
  a **"Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI"** en CV (ES/EN), header, `<title>`,
  Open Graph, JSON-LD, `llms.txt` y terminal (`whoami`). Resumen reescrito con la misma narrativa.
- **Experiencia Podemos reescrita con evidencia y en lenguaje genérico** (sin nombres propios de sistemas
  internos ni de personas): se retiran "SCI, Spore, Hipatia, Mambu Tools" y se describen como "core
  banking, app de campo, plataformas de originación/ciclo de crédito"; entran post-mortems, uptime 99.95 %
  (jul 2026), runbooks, ETL semanal idempotente, auditoría de errores (Sentry), n8n con SDK, Skill de
  routing. Métricas públicas vigentes se conservan (~40 % revisión, 80 % autoresolución N1, <10 min).
- **Skills con niveles honestos**: nueva presentación en el portafolio con la rúbrica Dueño / Construyo /
  Opero / Aprendiendo. Se retiran Amazon Kendra y AWS Kiro; Kubernetes queda solo en la card de VoltGrid.
  Entran: Liquibase, pytest+mocks, SonarQube, Sentry, n8n SDK, APIs Freshdesk/Notion/Asana, Chart.js,
  MySQL, Step Functions/CloudWatch Logs Insights (diagnóstico), IaC (aprendiendo).
- **Principios de trabajo** como bloque nuevo en "How I Build with AI": automatizar > operar (regla de las
  2 veces), confiabilidad como producto, estado fuera del código, cursor sobre ingesta.
- **Fidello como piloto**: badge "Piloto · beta cloud" (reemplaza "In active development"), cifras reales
  (~790 pruebas incl. integración DB contra Postgres real, 89 migraciones, 97 cambios OpenSpec, CI con 2 jobs
  bloqueantes, deploy QAS por workflow) y tech faltante (PWA, WCAG AA, RPC PL/pgSQL `SECURITY DEFINER`,
  `pg_cron`, rate limiting, Google Wallet, reportes email/WhatsApp, feature flags, tiers, 5 agentes IA).
- **CV 1 página (ES/EN)** regenerado con el nuevo contenido; tipografía del sistema (build determinista) queda
  formalizada en spec. Se actualiza `cv/CV_JuanValentinAlducin.md` (borrador editable) y el usuario lo usa
  como base para LinkedIn.
- Sincronización de fuentes de verdad: `llms.txt` → `profile.txt` (asistente), `CLAUDE.md`,
  `docs/frontend-standards.md §5`.

## Capabilities

### New Capabilities
- `stack-por-niveles`: sección de skills del portafolio organizada por nivel de dominio (Dueño / Construyo /
  Opero / Aprendiendo) con inventario verificable y sin tecnologías sin evidencia.
- `principios-de-trabajo`: bloque de principios de ingeniería (automatizar > operar, confiabilidad como
  producto, estado fuera del código, cursor sobre ingesta) en la sección de metodología.

### Modified Capabilities
- `posicionamiento-ai-native`: headline, resumen y metadatos pasan al posicionamiento híbrido Backend ·
  SRE & Automation · Agentic AI; el resumen incorpora confiabilidad/automatización con métricas.
- `experiencia-actualizada`: bullets de Podemos (ambos roles) reescritos con evidencia SRE/automatización/IA
  y en lenguaje genérico (prohibidos nombres de sistemas internos, personas, IDs y bases de datos).
- `skills-y-formacion`: taxonomía sin Kendra/Kiro, Kubernetes fuera de skills generales, nuevas
  tecnologías con evidencia; cursos sin cambios.
- `proyecto-fidello`: estado "piloto en beta cloud", cifras de ingeniería y stack ampliado.
- `agentic-engineering-hardening`: `llms.txt`, JSON-LD y badges reflejan el posicionamiento híbrido y la
  métrica de uptime.
- `cv-presentacion`: el CV usa tipografía del sistema (sin web fonts) para un build determinista y fuentes
  TrueType embebidas; conserva 1 página Oficio y ATS.

## Impact

- `index.html`: header, `<head>` (title/OG/JSON-LD), sección AI Method (principios), Experience (Podemos),
  Skills (reestructura con niveles → CSS nuevo embebido, responsive 992/768/480), card Fidello, terminal
  `whoami`.
- `cv/cv.html`, `cv/cv-en.html` → `cv/*.pdf` regenerados con `cv\build.ps1`; `cv/CV_JuanValentinAlducin.md`.
- `llms.txt` (→ Lambda del asistente vía `deploy-assistant.yml`), `CLAUDE.md`, `docs/frontend-standards.md`.
- Specs vigentes en `openspec/specs/` (deltas de este cambio) y memoria del agente.
- Sin dependencias nuevas; sin cambios de paleta. Deploy automático a S3/CloudFront al hacer merge a `main`.
