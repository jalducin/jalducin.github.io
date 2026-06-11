# Capability: experiencia-actualizada

## Requirements

### Requirement: Rol Podemos Progresar alineado al CV

La entrada de experiencia de Podemos Progresar SHALL usar el título y los logros del CV vigente
(*Backend Engineer & AI Specialist*), conservando Enkoth como hito de agentic engineering que
llegó a producción.

#### Scenario: Título y stack de Podemos coinciden con el CV
- **WHEN** un visitante lee la entrada de Podemos Progresar en la timeline
- **THEN** el título del rol es coherente con "Backend Engineer & AI Specialist"
- **AND** el badge "Current" sigue presente con el rango "Sept 2025 – Present"
- **AND** el stack visible incluye Python, Django, FastAPI, PostgreSQL, AWS Serverless, Docker y n8n

#### Scenario: Bullets reflejan métricas e integración de IA en el SDLC
- **WHEN** se revisan los bullets de Podemos
- **THEN** al menos un bullet describe la aplicación de Spec-Driven Development a bugs/deuda técnica/
  incidentes con reducción del ciclo de revisión (~40%)
- **AND** un bullet describe integración de Claude (SDD) y Gemini en el SDLC (specs, análisis estático,
  debugging, documentación)
- **AND** un bullet describe gestión de incidentes con RCA/postmortem asistido por IA y 80% de
  autoresolución N1
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
