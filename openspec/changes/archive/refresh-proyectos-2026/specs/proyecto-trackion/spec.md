# Capability: proyecto-trackion

## ADDED Requirements

### Requirement: El portafolio y las fuentes de verdad presentan Trackion
El sitio (`index.html`), el CV (`cv/cv.html`) y `llms.txt` DEBEN presentar **Trackion** como mesa de ayuda
**serverless white-label** con módulo de integración de APIs abierto, con datos reales y enlace en vivo.

#### Scenario: Card del portafolio
- **WHEN** un visitante abre la sección de proyectos
- **THEN** existe una card **"Trackion"** descrita como helpdesk serverless white-label
- **AND** menciona: ticketing end-to-end (categorizar/priorizar/asignar/historial, estados
  `open→in_progress→resolved→closed`), **catálogos administrables**, **módulo de integración de APIs abierto**
  (webhooks genéricos de entrada + dispatch de eventos de dominio de salida) y **monitoreo con Grafana**; SDD
- **AND** el stack visible incluye Python 3.12 · AWS Lambda · API Gateway (HTTP API) · Serverless Framework ·
  PostgreSQL (pg8000) · JWT (PyJWT) · SSM Parameter Store · Grafana · vanilla JS
- **AND** incluye badge de desplegado y enlace **Live Demo** a `https://dkzxcb6ja48r3.cloudfront.net`
- **AND** NO se expone públicamente Swagger/`/docs` de la API

#### Scenario: CV y llms.txt
- **WHEN** se revisa `cv/cv.html` (PDF regenerado) y `llms.txt`
- **THEN** Trackion aparece con descripción compacta y stack coherente
