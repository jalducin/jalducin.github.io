# Base de conocimiento — "Ask my portfolio"

> Fuente editable del asistente del sitio. Se compila con `python scripts/assistant/build_kb.py`, que inyecta el
> JSON en `<script type="application/json" id="assistant-kb">` dentro de `index.html`. **No hay LLM**: el widget
> recupera la entrada que mejor coincide con la pregunta.
>
> Formato por entrada: `## <id>`, luego `tags:` (palabras clave ES+EN separadas por coma; son las que puntúan),
> luego `en:` y `es:` con la respuesta (2–4 frases, en el tono del CV).
>
> Reglas: derivar el contenido de `llms.txt` (fuente de verdad del perfil) · nunca nombres de sistemas internos
> del empleador, personas, bases de datos ni IDs · nunca inventar datos que no estén en el CV o el portafolio.

## perfil
tags: who is juan, quien es juan, quien es, headline, titular, perfil, profile, summary, resumen, about juan, acerca de, agentic ai, senior backend engineer
en: Juan Valentin Alducin Vázquez is a Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI with 10+ years in Python, SQL and AWS, based in CDMX, Mexico. He works on operational reliability (post-mortem process, runbooks, monthly uptime tracking), automates part of the operation with n8n, and builds software with Spec-Driven Development (SDD/OpenSpec) and AI agents (Claude Code). Today he is Service Support Tech Lead & AI Specialist at Podemos Progresar, where he coordinates the Service Support team.
es: Juan Valentin Alducin Vázquez es Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI con más de 10 años en Python, SQL y AWS, en CDMX, México. Trabaja en la confiabilidad de la operación (proceso de post-mortems, runbooks, control mensual de uptime), automatiza parte de la operación con n8n y construye software con Spec-Driven Development (SDD/OpenSpec) y agentes de IA (Claude Code). Hoy es Service Support Tech Lead & AI Specialist en Podemos Progresar, donde coordina el equipo de Service Support.

## rol-actual
tags: current role, rol actual, puesto, trabajo actual, job, title, position, service support, tech lead, podemos, now, ahora, donde trabaja, where does he work, empleo, releases, liberaciones, release train, tren de liberacion, despliegues, deployments, coordina
en: Juan is Service Support Tech Lead & AI Specialist at Podemos Progresar (fintech/microfinance) since July 2026. He coordinates the Service Support team (bugs, critical incidents and technical debt) and applied Spec-Driven Development with the Claude API to the diagnosis → implementation flow to speed up reviews. He takes part in building the post-mortem process, keeps the monthly uptime/downtime tracking under the methodology set by leadership, and participates in the weekly release trains coordinated by Engineering, validating deployments from Service Support.
es: Juan es Service Support Tech Lead & AI Specialist en Podemos Progresar (fintech/microfinanzas) desde julio de 2026. Coordina el equipo de Service Support (bugs, incidentes críticos y deuda técnica) y aplicó Spec-Driven Development con Claude API al flujo diagnóstico → implementación para agilizar revisiones. Participa en la construcción del proceso de post-mortems, lleva el control mensual de uptime/downtime bajo la metodología definida por el liderazgo y participa en los trenes de liberación semanales coordinados por Ingeniería, validando despliegues desde Service Support.

## rol-anterior
tags: previous role, rol anterior, antes, before, backend support specialist, historia, trayectoria, career, experiencia previa, n2
en: Before the current role he was Backend Support Specialist at the same company (Sept 2025 – Jun 2026): N2 incident management with RCAs and AI-assisted post-mortems, knowledge transfer that let the N1 team resolve autonomously, and ownership of a weekly idempotent PostgreSQL cleanup ETL with schema changes versioned in Liquibase.
es: Antes del rol actual fue Backend Support Specialist en la misma empresa (sept 2025 – jun 2026): gestión de incidentes N2 con RCAs y post-mortems asistidos por IA, transferencia de conocimiento para que N1 resolviera de forma autónoma, y dueño de un ETL semanal idempotente en PostgreSQL con cambios de esquema versionados en Liquibase.

## experiencia-total
tags: experience, experiencia, years, años, cuanto tiempo, how long, seniority, background, trayectoria completa, redsis, softtek, gk pos, retail
en: 10+ years in backend and distributed systems. Podemos Progresar (fintech, since 2025), Redsis (2022–2025) as Software Engineer → Tech Lead leading the multi-country GK POS cloud Go-Live in Peru, Colombia and Bolivia, and Softtek (2017–2022) with SAP ERP/HANA, ETL and SAP BO dashboards.
es: +10 años en backend y sistemas distribuidos. Podemos Progresar (fintech, desde 2025), Redsis (2022–2025) como Software Engineer → Tech Lead liderando el Go-Live cloud de GK POS en Perú, Colombia y Bolivia, y Softtek (2017–2022) con SAP ERP/HANA, ETL y dashboards en SAP BO.

## sre-confiabilidad
tags: sre, reliability, confiabilidad, uptime, downtime, post-mortem, postmortem, incidentes, incidents, runbooks, sla, observability, observabilidad, blameless, on call
en: He takes part in building the post-mortem process (P0–P3 severity, 5 Whys, blameless) with a tracking dashboard for delays, escalations and progress against the goal. He calculates and keeps the monthly uptime/downtime tracking (fleet × real minutes; downtime = real impact) under the methodology defined by leadership, and standardizes runbooks and least-privilege access. SLA targets: first response under 10 minutes, critical resolution under 2 hours.
es: Participa en la construcción del proceso de post-mortems (severidad P0–P3, 5 Whys, blameless) con un tablero de seguimiento de atrasos, escalaciones y avance contra la meta. Calcula y lleva el control mensual de uptime/downtime (flota × minutos reales; downtime = impacto real) bajo la metodología definida por el liderazgo, y estandariza runbooks y accesos de mínimo privilegio. Metas de SLA: primera respuesta en menos de 10 minutos y resolución crítica en menos de 2 horas.

## automatizacion-n8n
tags: automation, automatizacion, n8n, workflow, pipelines, integraciones, integrations, freshdesk, notion, asana, slack, webhooks, rpa
en: He automates part of the operation with n8n: Freshdesk → Notion → Slack, a watcher for post-mortem delays and alerts on ticket spikes. In his own projects n8n also feeds Monitoreo-Cloud, collecting data for Grafana dashboards.
es: Automatiza parte de la operación con n8n: Freshdesk → Notion → Slack, vigilancia de atrasos de post-mortems y alertas por picos de tickets. En sus proyectos propios n8n también alimenta Monitoreo-Cloud, recolectando datos para los dashboards de Grafana.

## ia-sdd
tags: ai, ia, inteligencia artificial, claude, anthropic, openai, gemini, bedrock, llm, rag, agents, agentes, sdd, spec driven, openspec, prompt, skill, copilot
en: At work he uses AI (Claude, OpenAI, Gemini) for specs, analysis, debugging and documentation, applied SDD with the Claude API to the diagnosis → implementation flow to speed up reviews, and is developing an AI Skill to classify and route tickets with human review when confidence is low. In his own projects he works with Spec-Driven Development (OpenSpec), where the spec is the contract, and builds agentic tooling with Claude Code — subagents, skills, hooks and MCP — showcased in platform-STALD.
es: En el trabajo usa IA (Claude, OpenAI, Gemini) en specs, análisis, debugging y documentación, aplicó SDD con Claude API al flujo diagnóstico → implementación para agilizar revisiones y está desarrollando un Skill de IA para clasificar y rutear tickets con revisión humana cuando la confianza es baja. En sus proyectos propios trabaja con Spec-Driven Development (OpenSpec), donde la spec es el contrato, y construye tooling agéntico con Claude Code —subagentes, skills, hooks y MCP—, visible en platform-STALD.

## stack-niveles
tags: stack, skills, habilidades, tecnologias, technologies, que sabe, what does he know, nivel, level, dominio, herramientas, tools
en: His stack is published by honest level of mastery. Own: PostgreSQL and advanced SQL, idempotent production ETL, runbooks, Spec-Driven Development. Build: Python (FastAPI, Django, Flask, pytest), n8n, Grafana, Claude API and Claude Code (subagents, skills, hooks, MCP), OpenAI/Gemini APIs, Docker, GitHub Actions, Supabase, Deno, React/TypeScript. Operate: AWS, Sentry, MySQL, SAP, GK POS, post-mortem process, monthly uptime/downtime tracking. Learning: IaC (Terraform/CDK), QuickSight, synthetic checks.
es: Su stack se publica por nivel honesto de dominio. Dueño: PostgreSQL y SQL avanzado, ETL idempotente en producción, runbooks, Spec-Driven Development. Construyo: Python (FastAPI, Django, Flask, pytest), n8n, Grafana, Claude API y Claude Code (subagentes, skills, hooks, MCP), APIs de OpenAI/Gemini, Docker, GitHub Actions, Supabase, Deno, React/TypeScript. Opero: AWS, Sentry, MySQL, SAP, GK POS, proceso de post-mortems, control mensual de uptime/downtime. Aprendiendo: IaC (Terraform/CDK), QuickSight, synthetic checks.

## backend-lenguajes
tags: backend, python, fastapi, django, flask, sql, postgresql, postgres, api, rest, lenguajes, languages, programming, base de datos, database, etl
en: Backend is his core: Python (FastAPI, Django, Flask) and advanced SQL on PostgreSQL, plus MySQL, SQL Server, MongoDB and DynamoDB. He owns a weekly idempotent cleanup ETL in production (backup → cleanup → update → audit log, pre-validated against expected counts) and versions schema changes with Liquibase.
es: El backend es su núcleo: Python (FastAPI, Django, Flask) y SQL avanzado sobre PostgreSQL, además de MySQL, SQL Server, MongoDB y DynamoDB. Es dueño de un ETL semanal idempotente en producción (respaldo → limpieza → actualización → bitácora, pre-validado contra conteos esperados) y versiona cambios de esquema con Liquibase.

## aws-cloud
tags: aws, cloud, serverless, lambda, step functions, cloudwatch, rds, s3, eventbridge, dynamodb, api gateway, infraestructura, infrastructure, nube
en: At work he diagnoses and operates AWS (CloudWatch Logs Insights, RDS) and reviews Sentry, using diagnosis and post-deployment skills created by the infrastructure lead to detect post-deployment errors and estimate impact. He has also built his own serverless projects (Trackion on Lambda + API Gateway with the Serverless Framework, and Monitoreo-Cloud observing Lambda/S3 through CloudWatch). Infrastructure as Code (Terraform/CDK) is his declared learning edge, not something he claims to own.
es: En el trabajo diagnostica y opera AWS (CloudWatch Logs Insights, RDS) y revisa Sentry, usando skills de diagnóstico y post-despliegue creados por el líder de infraestructura para detectar errores post-despliegue y estimar el daño. También ha construido proyectos serverless propios (Trackion con Lambda + API Gateway y Serverless Framework, y Monitoreo-Cloud observando Lambda/S3 vía CloudWatch). La infraestructura como código (Terraform/CDK) es su frente declarado de aprendizaje, no algo que diga dominar.

## proyectos
tags: projects, proyectos, que proyectos, what projects, portfolio projects, proyectos del portafolio, side projects, featured projects, proyectos destacados, github, repos, repositorios, que ha construido, what has he built
en: His featured projects, in order: platform-STALD (educational platform built 100% with SDD and Claude Code agents, his agentic-engineering showcase), Fidello (multi-tenant digital loyalty on Supabase), VoltGrid (multi-tenant SaaS for EV charging operators), Trackion (white-label serverless help desk), Monitoreo-Cloud (self-hosted Grafana observability) and dataMasterGK (retail ETL middleware). All are built with Spec-Driven Development; ask about any of them by name.
es: Sus proyectos destacados, en orden: platform-STALD (plataforma educativa construida 100% con SDD y agentes de Claude Code, su vitrina de ingeniería agéntica), Fidello (fidelidad digital multi-tenant sobre Supabase), VoltGrid (SaaS multi-tenant para operadores de carga eléctrica), Trackion (mesa de ayuda serverless white-label), Monitoreo-Cloud (observabilidad self-hosted con Grafana) y dataMasterGK (middleware ETL retail). Todos se construyen con Spec-Driven Development; pregunta por cualquiera por su nombre.

## platform-stald
tags: stald, platform-stald, plataforma educativa, educational platform, agentes, agents, subagentes, subagents, skills, hooks, claude code, deno, proyecto personal, pasatiempo, hobby, agentic engineering, ingenieria agentica
en: platform-STALD is a personal project: an educational platform Juan built as a hobby and uses to practice technologies and AI: Spec-Driven Development with Claude Code (subagents, skills and hooks), real-time multiplayer games and CI tests. Stack: Deno Deploy, TypeScript, Supabase (PostgreSQL with RLS, Auth, Realtime) and vanilla JS. No student data is published. Code: https://github.com/jalducin/platform-STALD
es: platform-STALD es un proyecto personal: una plataforma educativa que Juan hizo como pasatiempo y usa para practicar tecnologías e IA: Spec-Driven Development con Claude Code (subagentes, skills y hooks), juegos multijugador en tiempo real y pruebas en CI. Stack: Deno Deploy, TypeScript, Supabase (PostgreSQL con RLS, Auth, Realtime) y JS vanilla. No se publican datos de alumnos. Código: https://github.com/jalducin/platform-STALD

## proyecto-fidello
tags: fidello, loyalty, lealtad, fidelidad, tarjeta de lealtad, loyalty card, supabase, rls, qr, sellos, stamps, cafeterias, coffee
en: Fidello is a multi-business digital loyalty platform (stamps via QR, nothing to install), deployed to QAS/PROD on Vercel + Supabase. All business rules live in PostgreSQL (multi-tenant RLS, PL/pgSQL SECURITY DEFINER RPC, anti-replay QR tokens, feature flags). Engineering: 793 tests (337 against a real database), 91 migrations, 97 OpenSpec changes and 28 journeys with twin runbooks. The repository is private (demo on request) and there is a deep dive on the site.
es: Fidello es una plataforma multi-negocio de fidelidad digital (sellos vía QR, sin instalar nada), desplegada en QAS/PROD sobre Vercel + Supabase. Todas las reglas de negocio viven en PostgreSQL (RLS multi-tenant, RPC en PL/pgSQL SECURITY DEFINER, tokens QR anti-replay, feature flags). Ingeniería: 793 pruebas (337 contra base real), 91 migraciones, 97 cambios OpenSpec y 28 journeys con runbook gemelo. El repositorio es privado (demo bajo solicitud) y hay un deep dive en el sitio.

## proyecto-voltgrid
tags: voltgrid, ev, charging, carga, electrico, saas, multi tenant, rbac, sso, oidc, kubernetes, next
en: VoltGrid is a multi-tenant, white-label SaaS for EV charging-station operators: live station status over WebSocket, tenant isolation with PostgreSQL Row-Level Security, RBAC plus SSO (OIDC), analytics and an installable PWA. Built 100% with Spec-Driven Development; the code is public on GitHub.
es: VoltGrid es un SaaS multi-tenant white-label para operadores de estaciones de carga eléctrica: estado en vivo por WebSocket, aislamiento por tenant con Row-Level Security de PostgreSQL, RBAC más SSO (OIDC), analítica y PWA instalable. Construido 100% con Spec-Driven Development; el código es público en GitHub.

## proyecto-trackion
tags: trackion, help desk, mesa de ayuda, ticketing, tickets, soporte, serverless help desk, grafana sla
en: Trackion is a white-label serverless help desk: end-to-end ticketing, admin-managed catalogs and an open API-integration module (inbound webhooks plus outbound domain events) to plug any external system without touching the core, with Grafana dashboards for tickets and SLA. Runs locally via Docker; code on GitHub.
es: Trackion es una mesa de ayuda serverless white-label: ticketing end-to-end, catálogos administrables y un módulo abierto de integración de APIs (webhooks entrantes y eventos de dominio salientes) para conectar cualquier sistema externo sin tocar el núcleo, con dashboards de tickets y SLA en Grafana. Corre en local con Docker; código en GitHub.

## proyecto-monitoreo
tags: monitoreo, monitoring, observabilidad, observability, grafana, docker, cloudwatch, dashboards, metricas, metrics
en: Monitoreo-Cloud is a self-hosted observability stack (Grafana + Docker) with a single pane over three sources: AWS serverless via CloudWatch, local Docker containers, and application data such as tickets and SLA, collected automatically with n8n and a read-only IAM role.
es: Monitoreo-Cloud es un stack de observabilidad self-hosted (Grafana + Docker) con una sola vista sobre tres fuentes: AWS serverless vía CloudWatch, contenedores Docker locales y datos de aplicación como tickets y SLA, recolectados automáticamente con n8n y un rol IAM de solo lectura.

## proyecto-datamaster
tags: datamastergk, datamaster, etl, gk, retail, middleware, excel, xml, sftp, flask, integracion
en: dataMasterGK is retail ETL middleware that automates master-data integration into GK Software: it watches directories, transforms Excel into GK XML across four interfaces and transmits over SFTP/FTP, with a Flask panel, a scheduler and SQLite auditing. Re-engineered under SDD into an idempotent single-pass pipeline with security hardening.
es: dataMasterGK es un middleware ETL retail que automatiza la integración de datos maestros en GK Software: vigila directorios, transforma Excel a XML de GK en cuatro interfaces y transmite vía SFTP/FTP, con panel Flask, scheduler y auditoría en SQLite. Rediseñado bajo SDD como pipeline idempotente de una sola pasada y con endurecimiento de seguridad.

## educacion-cursos
tags: education, educacion, estudios, degree, carrera, universidad, cursos, courses, certificaciones, certifications, anthropic academy, vanderbilt, bedrock, maestria
en: He holds a degree in Computer Systems Engineering from Instituto Tecnológico de Orizaba (2006–2011), and is taking Advanced English at Quick Learning. Certifications (2026): Anthropic Academy — Claude Code in Action, Introduction to Model Context Protocol, Introduction to Agent Skills and Introduction to Subagents; Claude Code: Software Engineering with Generative AI Agents (Vanderbilt University); and Generative AI Applications with Amazon Bedrock (AWS).
es: Es Ingeniero en Sistemas Computacionales por el Instituto Tecnológico de Orizaba (2006–2011) y cursa Inglés Avanzado en Quick Learning. Certificaciones (2026): Anthropic Academy — Claude Code in Action, Introduction to Model Context Protocol, Introduction to Agent Skills e Introduction to Subagents; Claude Code: Software Engineering with Generative AI Agents (Vanderbilt University); y Generative AI Applications with Amazon Bedrock (AWS).

## idiomas
tags: languages, idiomas, ingles, english, spanish, español, nivel de ingles, bilingue, b1, b2
en: Spanish is his native language and his English is B1, with B2-level technical reading and writing — he works daily with documentation, specs and code in English. This site is bilingual: you can switch language from the navigation bar.
es: El español es su lengua nativa y su inglés es B1, con lectura y escritura técnica a nivel B2 — trabaja a diario con documentación, specs y código en inglés. Este sitio es bilingüe: puedes cambiar el idioma desde la barra de navegación.

## contacto
tags: contact, contacto, email, correo, whatsapp, linkedin, hire, contratar, reclutador, recruiter, hablar, talk, oportunidad, vacante, disponibilidad, available
en: The fastest way is email: valentin.alducin88@gmail.com. He is also on LinkedIn (/in/juanvalducinv), GitHub (/jalducin) and WhatsApp (+52 56 4080 0494). The Contact section of this site has a form and one-click buttons — he is open to hearing about backend, SRE/platform and AI-native roles.
es: Lo más rápido es el correo: valentin.alducin88@gmail.com. También está en LinkedIn (/in/juanvalducinv), GitHub (/jalducin) y WhatsApp (+52 56 4080 0494). La sección de Contacto de este sitio tiene formulario y botones directos — está abierto a escuchar oportunidades de backend, SRE/plataforma y AI-native.

## cv-descarga
tags: cv, resume, curriculum, hoja de vida, pdf, descargar, download, bajar
en: You can download his CV in Spanish or English from the buttons at the top of the page or from the Contact section — both are one-page, ATS-friendly PDFs and the file arrives stamped with the current month.
es: Puedes descargar su CV en español o inglés desde los botones de la parte superior de la página o desde la sección de Contacto — ambos son PDF de una página, ATS-friendly, y el archivo llega con el mes actual en el nombre.

## ubicacion
tags: location, ubicacion, donde vive, where, mexico, cdmx, remote, remoto, zona horaria, timezone, reubicacion, relocation
en: He is based in Mexico City (CDMX), Mexico, and works hybrid/remote in the Central time zone, which overlaps with most of the Americas.
es: Vive en Ciudad de México (CDMX), México, y trabaja híbrido/remoto en zona horaria del Centro, que se traslapa con casi toda América.

## este-sitio
tags: este sitio, this site, portfolio, portafolio, como esta hecho, how is it built, tecnologia del sitio, website, assistant, asistente, bot, chat
en: This portfolio is handwritten HTML, CSS and vanilla JavaScript — no frameworks, no build step — published on GitHub Pages, and every change to it goes through the same Spec-Driven Development flow as his other projects. This assistant itself runs fully in your browser against a curated knowledge base: no LLM call, no backend, no tracking.
es: Este portafolio es HTML, CSS y JavaScript vanilla escritos a mano —sin frameworks ni build step— publicado en GitHub Pages, y cada cambio pasa por el mismo flujo de Spec-Driven Development que sus otros proyectos. Este asistente corre por completo en tu navegador contra una base de conocimiento curada: sin llamadas a un LLM, sin backend y sin rastreo.
