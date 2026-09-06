# Capability: experiencia-actualizada

## Requirements

### Requirement: Rol Podemos Progresar alineado al CV

La experiencia en Podemos Progresar SHALL presentarse como dos entradas cronológicas con los títulos
y logros del CV vigente —*Service Support Tech Lead & AI Specialist* (rol actual) y *Backend Support
Specialist* (rol anterior)—, conservando Enkoth como hito de agentic engineering que llegó a producción.

#### Scenario: Título y stack del rol actual coinciden con el CV
- **WHEN** un visitante lee la entrada actual de Podemos Progresar en la timeline
- **THEN** el título del rol es coherente con "Service Support Tech Lead & AI Specialist"
- **AND** el badge "Current" sigue presente con el rango "Jul 2026 – Present"
- **AND** el stack visible incluye Python, Django, FastAPI, PostgreSQL, AWS Serverless, Claude API, Docker y n8n

#### Scenario: El rol anterior en Podemos permanece visible
- **WHEN** un visitante recorre la timeline por debajo del rol actual
- **THEN** existe una entrada "Backend Support Specialist" en Podemos Progresar con el rango "Sept 2025 – Jun 2026"
- **AND** sus bullets incluyen gestión de incidentes N2 con RCA/postmortem asistido por IA y 80% de
  autoresolución N1 sin escalamiento senior

#### Scenario: Bullets del rol actual reflejan liderazgo, métricas e IA en el SDLC
- **WHEN** se revisan los bullets del rol actual de Podemos
- **THEN** al menos un bullet describe el liderazgo del equipo de Service Support resolviendo bugs/deuda
  técnica/incidentes con Spec-Driven Development y Claude API, con reducción del tiempo de revisión (~40%)
- **AND** un bullet describe la arquitectura de flujos de IA (Claude, OpenAI, Gemini) en el SDLC (specs,
  análisis estático, debugging, documentación)
- **AND** un bullet describe el tablero de gobierno de post-mortems con lectura en vivo desde Asana
  (atrasos, subtareas abiertas, escalaciones N3/N4 y semáforo ITG contra meta)
- **AND** un bullet describe la participación en los trenes de liberación semanales (SCI, Spore, Hipatia,
  Mambu Tools)
- **AND** un bullet describe operación de AWS (Lambda, RDS, Step Functions) con primera respuesta <10 min y resolución <2 h

#### Scenario: Enkoth se conserva como hito de producción
- **WHEN** se revisa la experiencia y/o los proyectos
- **THEN** Enkoth permanece visible y se describe como plataforma serverless que llegó a producción,
  desarrollada bajo SDD con Claude (no se elimina pese a no aparecer en el CV de una página)

### Requirement: Rol Redsis como Software Engineer → Tech Lead

La entrada de Redsis SHALL reflejar la progresión a *Tech Lead* y los logros de liderazgo del CV.

#### Scenario: Redsis muestra progresión a Tech Lead y logros de liderazgo
- **WHEN** un visitante lee la entrada de Redsis
- **THEN** el título refleja "Software Engineer → Tech Lead" con rango "Jan 2022 – Sept 2025"
- **AND** los bullets incluyen: APIs REST integrando GK POS con ERPs/CRMs vía XML/SFTP en 3 países LATAM;
  liderazgo técnico del Go-Live de GK POS en cloud (Perú, Colombia, Bolivia); pipeline ETL de promociones
  para GK OmniPOS; dirección del equipo funcional-técnico con estrategia de pruebas
- **AND** el stack incluye Python, Java, PHP, GK POS, GK OmniPOS, XML, SFTP, Docker y ETL

### Requirement: Rol Softtek consistente con el CV

La entrada de Softtek SHALL mantener los logros del CV (facturación, portales, ETL con SAP, dashboards
SAP BO, soporte AMS, Scrum con SLA 98%).

#### Scenario: Softtek refleja los logros del CV
- **WHEN** un visitante lee la entrada de Softtek
- **THEN** el rango es "Mar 2017 – Jan 2022" y los bullets cubren facturación/portales/ETL con SAP
  ERP/HANA, dashboards ejecutivos en SAP BO, soporte AMS a Retail GK y trabajo bajo Scrum
- **AND** el stack incluye Python, PHP, .NET, SAP ERP/HANA, SAP BO, ETL, Web Services y Scrum
