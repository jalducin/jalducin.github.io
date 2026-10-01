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

## rol-actual
tags: current role, rol actual, puesto, trabajo actual, job, title, position, service support, tech lead, podemos, now, ahora, donde trabaja, where does he work, empleo
en: Juan is Service Support Tech Lead & AI Specialist at Podemos Progresar (fintech/microfinance) since July 2026. He leads the Service Support team end-to-end — bugs, critical incidents and technical debt — with Spec-Driven Development and the Claude API. He also built the post-mortem system and the monthly uptime methodology the team runs on.
es: Juan es Service Support Tech Lead & IA Specialist en Podemos Progresar (fintech/microfinanzas) desde julio de 2026. Lidera el equipo de Service Support de punta a punta —bugs, incidentes críticos y deuda técnica— con Spec-Driven Development y Claude API. También construyó el sistema de post-mortems y la metodología de uptime mensual con la que opera el equipo.

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
en: Reliability is his signature. He designed a blameless post-mortem system (P0–P3 severity, 5 Whys, self-assessment rubric) with a live governance dashboard showing delays, open subtasks and escalations, plus a monthly uptime/downtime methodology where downtime means real user impact, not ticket closure. SLAs: first response under 10 minutes, critical resolution under 2 hours.
es: La confiabilidad es su firma. Diseñó un sistema de post-mortems blameless (severidad P0–P3, 5 Whys, rúbrica de autoevaluación) con un tablero de gobierno en vivo que expone atrasos, subtareas abiertas y escalaciones, además de una metodología mensual de uptime/downtime donde el downtime es impacto real al usuario, no cierre de ticket. SLAs: primera respuesta en menos de 10 minutos y resolución crítica en menos de 2 horas.

## automatizacion-n8n
tags: automation, automatizacion, n8n, workflow, pipelines, integraciones, integrations, freshdesk, notion, asana, slack, webhooks, rpa
en: He automates operations with n8n (workflow SDK): Freshdesk → Notion → Slack with an ingestion cursor, a post-mortem delay watcher and ticket-spike alerts. His rule of two: any manual report done more than twice becomes a spec-driven pipeline where n8n orchestrates, Python computes and the result lands in Notion.
es: Automatiza la operación con n8n (workflow SDK): Freshdesk → Notion → Slack con cursor de ingesta, vigilante de atrasos de post-mortems y alertas por picos de tickets. Su regla de las dos veces: todo reporte manual hecho más de dos veces se convierte en un pipeline spec-driven donde n8n orquesta, Python calcula y el resultado queda en Notion.

## ia-sdd
tags: ai, ia, inteligencia artificial, claude, anthropic, openai, gemini, bedrock, llm, rag, agents, agentes, sdd, spec driven, openspec, prompt, skill, copilot
en: He works AI-native: generative AI (Claude, OpenAI, Gemini, Bedrock) is the copilot across his SDLC — spec generation, static analysis, automated debugging and documentation — through Spec-Driven Development (OpenSpec), where the spec is the contract and every change flows through versioned artifacts. He is also designing an AI Skill for automatic ticket routing with human review on low confidence.
es: Trabaja AI-native: la IA generativa (Claude, OpenAI, Gemini, Bedrock) es el copiloto de todo su SDLC —generación de specs, análisis estático, debugging automatizado y documentación— mediante Spec-Driven Development (OpenSpec), donde la spec es el contrato y cada cambio pasa por artefactos versionados. También diseña un Skill de IA para el ruteo automático de tickets con revisión humana en baja confianza.

## stack-niveles
tags: stack, skills, habilidades, tecnologias, technologies, que sabe, what does he know, nivel, level, dominio, herramientas, tools
en: His stack is published by honest level of mastery. Own: PostgreSQL and advanced SQL, idempotent production ETL, post-mortem and uptime methodology, runbooks, Spec-Driven Development. Build: Python (FastAPI, Django, Flask, pytest), n8n, Grafana, Claude/OpenAI/Gemini APIs, Docker, GitHub Actions, Supabase, React/TypeScript. Operate: AWS, Sentry, MySQL, SAP, GK POS. Learning: IaC (Terraform/CDK), QuickSight, synthetic checks.
es: Su stack se publica por nivel honesto de dominio. Dueño: PostgreSQL y SQL avanzado, ETL idempotente en producción, metodología de post-mortems y uptime, runbooks, Spec-Driven Development. Construyo: Python (FastAPI, Django, Flask, pytest), n8n, Grafana, APIs de Claude/OpenAI/Gemini, Docker, GitHub Actions, Supabase, React/TypeScript. Opero: AWS, Sentry, MySQL, SAP, GK POS. Aprendiendo: IaC (Terraform/CDK), QuickSight, synthetic checks.

## backend-lenguajes
tags: backend, python, fastapi, django, flask, sql, postgresql, postgres, api, rest, lenguajes, languages, programming, base de datos, database, etl
en: Backend is his core: Python (FastAPI, Django, Flask) and advanced SQL on PostgreSQL, plus MySQL, SQL Server, MongoDB and DynamoDB. He owns a weekly idempotent cleanup ETL in production (backup → cleanup → update → audit log, pre-validated against expected counts) and versions schema changes with Liquibase.
es: El backend es su núcleo: Python (FastAPI, Django, Flask) y SQL avanzado sobre PostgreSQL, además de MySQL, SQL Server, MongoDB y DynamoDB. Es dueño de un ETL semanal idempotente en producción (respaldo → limpieza → actualización → bitácora, pre-validado contra conteos esperados) y versiona cambios de esquema con Liquibase.

## aws-cloud
tags: aws, cloud, serverless, lambda, step functions, cloudwatch, rds, s3, eventbridge, dynamodb, api gateway, infraestructura, infrastructure, nube
en: On AWS he diagnoses and operates Lambda, Step Functions, CloudWatch Logs Insights, RDS, S3 and EventBridge, and he has shipped his own serverless projects (Pyzzeria on Lambda + Step Functions + DynamoDB, this portfolio on S3 + CloudFront). Infrastructure as Code (Terraform/CDK) is his declared learning edge, not something he claims to own.
es: En AWS diagnostica y opera Lambda, Step Functions, CloudWatch Logs Insights, RDS, S3 y EventBridge, y ha desplegado proyectos serverless propios (Pyzzeria con Lambda + Step Functions + DynamoDB, este portafolio en S3 + CloudFront). La infraestructura como código (Terraform/CDK) es su frente declarado de aprendizaje, no algo que diga dominar.

## proyecto-fidello
tags: fidello, loyalty, lealtad, fidelidad, supabase, rls, qr, piloto, pilot, cafeterias, coffee, estrella, flagship, proyecto principal
en: Fidello is his flagship: a multi-business digital loyalty platform, currently a cloud-beta pilot in real coffee shops. All business rules live in PostgreSQL (multi-tenant RLS, PL/pgSQL SECURITY DEFINER RPC, anti-replay QR tokens, feature flags). Engineering: 793 tests (337 against a real database), 91 migrations, 97 OpenSpec changes and 28 journeys with twin runbooks. There is a deep dive on the site.
es: Fidello es su proyecto estrella: una plataforma multi-negocio de fidelidad digital, hoy un piloto en beta cloud en cafeterías reales. Todas las reglas de negocio viven en PostgreSQL (RLS multi-tenant, RPC en PL/pgSQL SECURITY DEFINER, tokens QR anti-replay, feature flags). Ingeniería: 793 pruebas (337 contra base real), 91 migraciones, 97 cambios OpenSpec y 28 journeys con runbook gemelo. Hay un deep dive en el sitio.

## proyecto-pyzzeria
tags: pyzzeria, pizza, demo, live demo, websocket, step functions, dynamodb, sam, tracking, demo en vivo
en: Pyzzeria is the live demo of the portfolio: a serverless pizza-ordering app where you build an order and watch it move through its states in about 70 seconds over WebSocket, driven by a Step Functions Express workflow, with orders in DynamoDB and the frontend on S3 + CloudFront. Demo only, no real payments. There is a deep dive and a live link on the site.
es: Pyzzeria es la demo en vivo del portafolio: una app serverless de pedidos de pizza donde armas el pedido y lo ves avanzar por sus estados en unos 70 segundos vía WebSocket, orquestado por un workflow Step Functions Express, con los pedidos en DynamoDB y el frontend en S3 + CloudFront. Solo demo, sin pagos reales. Hay un deep dive y enlace en vivo en el sitio.

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
tags: education, educacion, estudios, degree, carrera, universidad, cursos, courses, certificaciones, certifications, coursera, bedrock course, maestria
en: He holds a degree in Computer Systems Engineering from Instituto Tecnológico de Orizaba (2006–2011), and is taking Advanced English at Quick Learning. Recent training: Claude Code — Software Engineering with Gen AI Agents (Vanderbilt/Anthropic, 2026), Generative AI with Amazon Bedrock (Coursera, 2026), Developing Applications in Python on AWS (Coursera, 2025) and a GitHub Actions bootcamp.
es: Es Ingeniero en Sistemas Computacionales por el Instituto Tecnológico de Orizaba (2006–2011) y cursa Inglés Avanzado en Quick Learning. Formación reciente: Claude Code — Software Engineering with Gen AI Agents (Vanderbilt/Anthropic, 2026), Generative AI with Amazon Bedrock (Coursera, 2026), Developing Applications in Python on AWS (Coursera, 2025) y un bootcamp de GitHub Actions.

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
en: This portfolio is handwritten HTML, CSS and vanilla JavaScript — no frameworks, no build step — deployed to AWS S3 + CloudFront from GitHub Actions, and every change to it goes through the same Spec-Driven Development flow as his other projects. This assistant itself runs fully in your browser against a curated knowledge base: no LLM call, no backend, no tracking.
es: Este portafolio es HTML, CSS y JavaScript vanilla escritos a mano —sin frameworks ni build step— desplegado en AWS S3 + CloudFront desde GitHub Actions, y cada cambio pasa por el mismo flujo de Spec-Driven Development que sus otros proyectos. Este asistente corre por completo en tu navegador contra una base de conocimiento curada: sin llamadas a un LLM, sin backend y sin rastreo.
