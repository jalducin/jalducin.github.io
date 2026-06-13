# Capability: proyecto-monitoreo-cloud

## ADDED Requirements

### Requirement: El portafolio y las fuentes de verdad presentan Monitoreo-Cloud
El sitio (`index.html`), el CV (`cv/cv.html`) y `llms.txt` DEBEN presentar **Monitoreo-Cloud** como pipeline
de **observabilidad** sobre AWS Free Tier, con datos reales.

#### Scenario: Card del portafolio
- **WHEN** un visitante abre la sección de proyectos
- **THEN** existe una card **"Monitoreo-Cloud"** descrita como pipeline de observabilidad self-hosted, costo $0
- **AND** menciona el flujo **CloudWatch → n8n → PostgreSQL → Grafana**, recolección automatizada con rol
  **IAM de solo lectura**, dashboards y alertas, y guardarraíl de costo con **AWS Budgets**; construido con SDD
- **AND** el stack visible incluye AWS EC2 · CloudWatch · n8n · PostgreSQL · Grafana · Docker Compose · AWS Budgets
- **AND** incluye enlace **View Code** a `https://github.com/jalducin/monitoreo-cloud`

#### Scenario: CV y llms.txt
- **WHEN** se revisa `cv/cv.html` (PDF regenerado) y `llms.txt`
- **THEN** Monitoreo-Cloud aparece con descripción compacta y stack coherente
