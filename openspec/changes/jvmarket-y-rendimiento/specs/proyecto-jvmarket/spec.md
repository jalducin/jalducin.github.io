## ADDED Requirements

### Requirement: Proyecto JV Market (desplegado en AWS) en portafolio y CV

El portafolio y el CV SHALL presentar el proyecto como **JV Market** (no "MetalShop"), descrito como
e-commerce full-stack **desplegado en AWS**, con stack real y enlaces en vivo. NO debe quedar ninguna
referencia "MetalShop" ni el encuadre de "solo práctica/WIP" para este proyecto.

#### Scenario: Card del portafolio actualizada
- **WHEN** un visitante abre la sección de proyectos del portafolio
- **THEN** existe una card **"JV Market"** que lo describe como e-commerce full-stack (auth JWT, productos,
  carrito, checkout, panel admin) **desplegado en AWS** (API Gateway + Lambda, frontend S3+CloudFront)
- **AND** incluye enlaces en vivo: **Live Demo** (storefront CloudFront) y **API docs** (Swagger)
- **AND** el stack visible incluye FastAPI · JWT · SQLite/PostgreSQL · AWS (Lambda · API Gateway · S3/CloudFront)

#### Scenario: CV y fuentes de verdad actualizadas
- **WHEN** se revisa `cv/cv.html` (PDF regenerado), `llms.txt` y `CLAUDE.md`
- **THEN** el proyecto aparece como **JV Market** desplegado en AWS (no MetalShop), con stack coherente
- **AND** `llms.txt` menciona los enlaces en vivo para que el asistente IA los pueda referir

#### Scenario: Sin referencias obsoletas
- **WHEN** se busca "MetalShop" en el sitio/CV/llms/CLAUDE
- **THEN** no hay coincidencias (queda solo "JV Market")
