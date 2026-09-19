<!--
  Borrador editable del CV (ES) — refleja 1:1 el contenido de cv/cv.html al 2026-09-19.
  Fuente canónica del PDF: cv/cv.html (+ cv/cv-en.html). Edita aquí, y al terminar pásamelo para
  volcarlo a los HTML, regenerar los PDF (cv\build.ps1) y alinear index.html / llms.txt.
  Restricción del PDF: 1 página Oficio. Guía: bullets de ≤ ~125 caracteres caben en 2 líneas.
-->

# Juan Valentin Alducin Vázquez

**Senior Backend Engineer | Tech Lead | Agentic AI Systems**

- WhatsApp: +52 56 4080 0494
- Email: valentin.alducin88@gmail.com
- Web: https://jalducin.github.io
- LinkedIn: https://linkedin.com/in/juanvalducinv
- GitHub: https://github.com/jalducin
- Ubicación: CDMX, México

---

## Resumen

Senior Backend Engineer y Tech Lead con +10 años en APIs, sistemas distribuidos y cloud-native (Python, FastAPI, AWS Serverless). Especializado en IA generativa: agentes, RAG y LLMs (Claude, Gemini, OpenAI) con AWS AI/ML (Bedrock, Kendra). Pipelines de datos y ETL. Tech Lead en fintech y retail; acelero la entrega con SDD: -40% en revisión y 80% de autoresolución N1.

---

## Experiencia

### Service Support Tech Lead & IA Specialist — Podemos Progresar
07/2026 – Presente · CDMX

- Lidero el equipo de Service Support: bugs, incidentes críticos y deuda técnica end-to-end con SDD + Claude API (-40% en revisión).
- Arquitecto flujos de IA (Claude, OpenAI, Gemini) en todo el SDLC: specs, análisis estático, debugging y documentación.
- Construí el tablero de post-mortems en vivo desde Asana (atrasos, escalaciones N3/N4, semáforo ITG) y reportes para dirección.
- Diseño tooling serverless interno (Enkoth — Lambda · Step Functions · EventBridge) y automatizaciones n8n (Asana, Freshdesk, Slack).
- Trenes de liberación semanales (SCI, Spore, Hipatia, Mambu Tools) y AWS: primera respuesta <10 min, crítica <2 h.

**Stack:** Python · Django · FastAPI · PostgreSQL · AWS Serverless · AWS Glue · Claude API · Docker · n8n · Grafana

### Backend Support Specialist — Podemos Progresar
09/2025 – 06/2026 · CDMX

- Lideré incidentes N2 con RCAs y postmortems técnicos asistidos por IA que previnieron fallos recurrentes.
- Habilité 80% de autoresolución en N1 vía transferencia de conocimiento; fui el enlace técnico central del área.

### Software Engineer > Tech Lead — Redsis
01/2022 – 09/2025 · CDMX

- Desarrollé APIs REST (Python, Java, PHP) integrando GK POS con ERPs/CRMs vía XML/SFTP en 3 países LATAM.
- Lideré el Go-Live cloud de GK POS (Perú, Colombia, Bolivia): cronogramas, stakeholders negocio/TI, preventa y capacitación local.
- Dirigí el equipo funcional-técnico: estrategia de pruebas (unitarias, regresión, integración) y calidad por release.

**Stack:** Python · Java · PHP · GK POS · GK OmniPOS · XML · SFTP · Docker · ETL

### Software Engineer — Softtek
03/2017 – 01/2022 · CDMX

- Implementé facturación, portales cliente y ETLs con SAP ERP/HANA y dashboards ejecutivos en SAP BO.
- Soporte AMS a Retail GK (correctivo/evolutivo) bajo Scrum, con SLA al 98%.

**Stack:** Python · PHP · .NET · SAP ERP/HANA · SAP BO · ETL · Web Services · Scrum

---

## Educación

### Ingeniería en Sistemas Computacionales — Instituto Tecnológico de Orizaba
2006 – 2011 · Orizaba, México

---

## Capacitación / Cursos

- **Claude Code: SE with Gen AI Agents** — Vanderbilt / Anthropic · 2026
- **Generative AI with Amazon Bedrock** — Coursera · 2026
- **Developing Applications in Python on AWS** — Coursera · 2025
- **GitHub Actions Bootcamp** — Código Facilito · 2025

---

## Habilidades

| Categoría | Detalle |
|---|---|
| Lenguajes | Python, PHP, JavaScript, TypeScript, Java, SQL |
| Frameworks & APIs | Django, FastAPI, Flask, React, Next.js 14, Node.js, REST APIs, SSO/OIDC, Microservices, Event-Driven Architecture |
| Cloud · DevOps · Observabilidad | AWS (Lambda, RDS, S3, Step Functions, EC2, CloudWatch), Serverless Framework, Kubernetes, CI/CD (GitHub Actions), Docker, n8n, Grafana, Supabase |
| Bases de datos | PostgreSQL, MySQL, SQL Server, MongoDB, SAP HANA, DynamoDB |
| Datos & ETL | Pipelines ETL, AWS Glue, SFTP/XML, Pandas/openpyxl, SAP ETL |
| IA & Generative AI | Claude/OpenAI/Gemini APIs, Prompt Engineering, LLM Integration, RAG, AI Agents, Agentic Workflows, Amazon Bedrock, Amazon Kendra, AWS Kiro, SDD/OpenSpec |
| Gestión | Scrum, Jira, Asana, Notion, Postman |
| Soft Skills | Liderazgo Técnico, Mentoring, Comunicación Ejecutiva, Gestión de Stakeholders, Ownership, Resolución de Problemas |

---

## Idiomas

- **Español** — Nativo
- **Inglés** — B1 · B2 lectura/escritura técnica

---

## Proyectos

### Fidello — Loyalty Card System
Fidelidad digital multi-negocio (roles, QR mobile-first): JWT, RLS multi-tenant, QR anti-replay, passes de Google Wallet (JWT RS256) y feature flags administrables. 100% SDD · en evolución.
**Stack:** React 18 · TypeScript · Vite · Tailwind · Supabase · PL/pgSQL · Edge Functions (Deno) · Vitest

### Monitoreo-Cloud — Observabilidad
Observabilidad self-hosted (Grafana + Docker) sobre 3 fuentes: AWS serverless (CloudWatch), Docker local y tickets/SLA de Trackion. SDD.
**Stack:** Grafana · Docker · n8n · PostgreSQL · AWS CloudWatch · Lambda · S3

### VoltGrid — EV Charging Platform
SaaS multi-tenant white-label de carga EV: tiempo real (WebSocket), RLS, RBAC + SSO (OIDC), analytics y PWA. 100% SDD.
**Stack:** FastAPI · SQLAlchemy 2.0 async · PostgreSQL 16 (RLS) · Next.js 14 · TypeScript · WebSockets · Docker · Kubernetes

### Trackion — Serverless Help Desk
Mesa de ayuda serverless white-label: ticketing end-to-end, catálogos y módulo de integración de APIs abierto; dashboards Grafana. SDD.
**Stack:** Python 3.12 · AWS Lambda · API Gateway · Serverless Framework · PostgreSQL · JWT · SSM · Grafana

### Pyzzeria — Pedidos serverless (Live Demo)
Demo serverless de pedidos de pizza con tracking en vivo: WebSocket + Step Functions Express (~70s), DynamoDB y OpenAPI/Swagger; desplegado en CloudFront. 100% SDD.
**Stack:** Python 3.12 · FastAPI · Mangum · AWS Lambda · API Gateway (HTTP+WS) · DynamoDB · Step Functions · SAM · CloudFront

### dataMasterGK — Middleware ETL (GK Retail)
Middleware ETL retail para GK: Excel > XML de GK (4 interfaces) vía SFTP/FTP, panel Flask y auditoría SQLite. Rediseñado con SDD (idempotente, seguridad).
**Stack:** Python 3.12 · Flask · Pandas · openpyxl · SQLite · Paramiko (SFTP)
