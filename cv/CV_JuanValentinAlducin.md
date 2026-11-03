<!--
  Borrador editable del CV (ES) — refleja 1:1 el contenido de cv/cv.html al 2026-11-02 (cambio cv-claridad).
  Fuente canónica del PDF: cv/cv.html (+ cv/cv-en.html). Edita aquí, y al terminar pásamelo para
  volcarlo a los HTML, regenerar los PDF (cv\build.ps1) y alinear index.html / llms.txt.
  Restricción del PDF: 1 página A4. Límites: rol actual ≤ 4 bullets, roles previos ≤ 2, Softtek 1;
  5 categorías de habilidades; 3 proyectos + "Otros". Verificación: python scripts/cv/check_cv.py
-->

# Juan Valentin Alducin Vázquez

**Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI**

- WhatsApp: +52 56 4080 0494
- Email: valentin.alducin88@gmail.com
- Web: https://jalducin.github.io
- LinkedIn: https://linkedin.com/in/juanvalducinv
- GitHub: https://github.com/jalducin
- Ubicación: CDMX, México

---

## Resumen

Senior Backend Engineer y Tech Lead con +10 años en Python, SQL y AWS. Trabajo en la confiabilidad y
automatización de la operación (post-mortems, runbooks, n8n) y construyo software con Spec-Driven Development y agentes de IA.

## Experiencia

### Service Support Tech Lead & AI Specialist — Podemos Progresar
07/2026 - Presente · CDMX

- Coordino Service Support (bugs, incidentes críticos y deuda técnica) y apliqué SDD con Claude API al flujo diagnóstico → implementación.
- Participo en la transformación de post-mortems (P0–P3, 5 Whys, blameless) y llevo el control mensual de uptime/downtime.
- Automatizo parte de la operación con n8n (Freshdesk → Notion → Slack) y desarrollo un Skill de IA para rutear tickets.
- Valido despliegues en los trenes de liberación semanales; opero AWS (CloudWatch, RDS) y Sentry; SLA <10 min, crítica <2 h.

### Backend Support Specialist — Podemos Progresar
09/2025 - 06/2026 · CDMX

- Incidentes N2 con RCAs y post-mortems asistidos por IA; transferencia de conocimiento para resolver en N1.
- ETL semanal idempotente en PostgreSQL (respaldo → limpieza → actualización → bitácora) y deduplicación de identidades.

### Software Engineer > Tech Lead — Redsis
01/2022 - 09/2025 · CDMX

- APIs REST (Python, Java, PHP) que integran GK POS con ERPs/CRMs vía XML/SFTP en 3 países de LATAM.
- Lideré el Go-Live cloud de GK POS (Perú, Colombia, Bolivia) y al equipo funcional-técnico: pruebas y calidad por release.

### Software Engineer — Softtek
03/2017 - 01/2022 · CDMX

- Facturación, portales y ETLs con SAP ERP/HANA, dashboards en SAP BO y soporte AMS con SLA al 98 %.

## Educación

### Ingeniería en Sistemas Computacionales — Instituto Tecnológico de Orizaba
2006 - 2011 · Orizaba, México

## Idiomas

- Español — Nativo
- Inglés — B1 · B2 lectura/escritura técnica

## Habilidades

- **Backend:** Python (FastAPI, Django, Flask), SQL, TypeScript, REST/WebSocket
- **Cloud & Serverless:** AWS (Lambda, Step Functions, EventBridge, CloudWatch, RDS, S3), Supabase, Deno Deploy, Docker, GitHub Actions
- **Datos:** PostgreSQL (RLS, PL/pgSQL), ETL idempotente, Liquibase, DynamoDB
- **SRE & Automatización:** Post-mortems, runbooks, SLAs, Grafana, Sentry, n8n
- **IA aplicada:** Claude Code (subagentes, skills, hooks, MCP), Claude API, Amazon Bedrock, SDD/OpenSpec

## Proyectos

### platform-STALD — Plataforma educativa
Portal, actividades en línea y juegos multijugador en tiempo real, hecho 100 % con SDD y Claude Code: subagentes
revisor y verificador, 14 skills y un hook que bloquea secretos y push a main. +250 PRs · +85 cambios OpenSpec ·
pruebas en CI + E2E.
Deno · TypeScript · Supabase (Postgres RLS, Auth, Realtime) · github.com/jalducin/platform-STALD

### Fidello — Loyalty Card System
Fidelidad digital multi-negocio (QR mobile-first) con la lógica en PostgreSQL: RLS multi-tenant, RPC PL/pgSQL,
QR anti-replay y feature flags. 793 pruebas · 91 migraciones · 100 % SDD.
React · TypeScript · Supabase · PL/pgSQL · jalducin.github.io/blog/deep-dive-fidello.html

### Monitoreo-Cloud — Observabilidad
Observabilidad self-hosted (Grafana + Docker) sobre 3 fuentes: CloudWatch, contenedores Docker y tickets/SLA;
recolección con n8n.
Grafana · Docker · n8n · PostgreSQL · CloudWatch · github.com/jalducin/monitoreo-cloud

**Otros:** VoltGrid (SaaS multi-tenant de carga EV, FastAPI + Next.js) · Trackion (help desk serverless) ·
dataMasterGK (ETL retail) — github.com/jalducin

## Certificaciones

- Claude Code in Action — Anthropic · 2026
- Introduction to Model Context Protocol — Anthropic · 2026
- Introduction to Agent Skills — Anthropic · 2026
- Introduction to Subagents — Anthropic · 2026
- Claude Code: Software Engineering with Generative AI Agents — Vanderbilt University · 2026
- Generative AI Applications with Amazon Bedrock — AWS · 2026
- Developing Applications in Python on AWS — Coursera · 2025
- GitHub Actions Bootcamp — Código Facilito · 2025
