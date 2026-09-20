# Capability: experiencia-actualizada (delta)

## MODIFIED Requirements

### Requirement: Rol Podemos Progresar alineado al CV

La experiencia en Podemos Progresar SHALL presentarse como dos entradas cronológicas con los títulos y
logros del CV vigente —*Service Support Tech Lead & AI Specialist* (rol actual) y *Backend Support
Specialist* (rol anterior)—, redactadas **con evidencia** (confiabilidad, automatización, SQL/ETL, IA) y en
**lenguaje genérico**: sin nombres propios de sistemas internos, personas, bases de datos ni IDs. Enkoth se
conserva como mención ligera de tooling serverless interno (Lambda · Step Functions · EventBridge).

#### Scenario: Título y stack del rol actual coinciden con el CV
- **WHEN** un visitante lee la entrada actual de Podemos Progresar en la timeline
- **THEN** el título del rol es "Service Support Tech Lead & AI Specialist" y el badge "Current" muestra
  "Jul 2026 – Present"
- **AND** el stack visible incluye Python, PostgreSQL, SQL, AWS (Lambda, Step Functions, CloudWatch, RDS),
  n8n, Grafana, Sentry, Claude API, Docker y Notion/Asana/Freshdesk APIs
- **AND** el stack NO incluye Kubernetes, Amazon Kendra ni AWS Kiro

#### Scenario: Bullets del rol actual reflejan liderazgo, confiabilidad, automatización e IA
- **WHEN** se revisan los bullets del rol actual de Podemos
- **THEN** un bullet describe el liderazgo del equipo de Service Support resolviendo bugs, incidentes
  críticos y deuda técnica end-to-end con SDD + Claude API, acortando el ciclo de revisión (sin porcentaje)
- **AND** un bullet describe el **sistema de post-mortems** (severidad P0–P3, 5 Whys, blameless, rúbrica de
  auto-evaluación) con seguimiento de compromisos y tablero de gobierno en vivo (atrasos, subtareas abiertas,
  escalaciones N3/N4, semáforo de indicador vs. meta) con visibilidad ejecutiva
- **AND** un bullet describe la **metodología de uptime/downtime mensual** (flota de sistemas × minutos
  reales; downtime = impacto real al usuario), sin publicar la cifra de uptime
- **AND** un bullet describe **automatización con n8n (workflow SDK)** e integraciones Freshdesk → Notion →
  Slack / Asana (cursor sobre ingesta, alertas de atrasos y picos de tickets) y pipelines spec-driven
- **AND** un bullet describe la **arquitectura de flujos de IA** (Claude, OpenAI, Gemini, Bedrock) en el SDLC
  y el diseño de un Skill de routing automático de tickets (clasificación multi-dimensión con revisión
  humana en baja confianza)
- **AND** un bullet describe la participación en **trenes de liberación semanales** coordinando validación y
  despliegue entre plataformas (descritas genéricamente: core banking, originación, app de campo)
- **AND** un bullet describe la operación/diagnóstico de AWS (Step Functions, Lambda, CloudWatch Logs
  Insights, RDS) con SLAs de primera respuesta <10 min y resolución crítica <2 h
- **AND** ningún bullet contiene nombres de sistemas internos (p. ej. "SCI", "Spore", "Hipatia", "Mambu
  Tools"), de personas, de bases de datos ni identificadores de incidentes

#### Scenario: El rol anterior en Podemos permanece visible con evidencia
- **WHEN** un visitante recorre la timeline por debajo del rol actual
- **THEN** existe una entrada "Backend Support Specialist" en Podemos Progresar con el rango
  "Sept 2025 – Jun 2026"
- **AND** sus bullets incluyen: gestión de incidentes N2 con RCA/post-mortems asistidos por IA; autoresolución
  N1 habilitada vía transferencia de conocimiento (sin porcentaje); **ETL semanal idempotente en PostgreSQL** (backup →
  limpieza → actualización → bitácora, con pre-validación) y deduplicación de identidades; enlace técnico
  central (Python, Django, FastAPI, PostgreSQL)
- **AND** no se mencionan nombres de bases de datos, bancos, ni conteos de registros de clientes

#### Scenario: Enkoth se conserva como hito de producción
- **WHEN** se revisa la experiencia
- **THEN** Enkoth permanece como mención ligera de tooling serverless interno (AWS Lambda · Step Functions ·
  EventBridge) para webhooks e integraciones, dentro del rol actual, sin card de proyecto propia

#### Scenario: CV (ES/EN) y portafolio cuentan la misma historia
- **WHEN** se comparan los bullets del CV (`cv/cv.html`, `cv/cv-en.html`) con la timeline de `index.html`
- **THEN** el CV contiene un subconjunto compactado (≤ 6 bullets rol actual, ≤ 3 rol anterior) de los mismos
  hechos, sin hechos que no estén en el portafolio
- **AND** las fechas y títulos coinciden en las cuatro fuentes (CV ES, CV EN, `index.html`, `llms.txt`)

