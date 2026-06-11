## ADDED Requirements

### Requirement: Vistas de detalle de proyectos con arquitectura

El sitio SHALL ofrecer, para los proyectos insignia (Fidello y Enkoth), una vista de detalle que vaya más
allá de la card: Problema → Enfoque → Arquitectura (diagrama) → Decisiones técnicas → Resultado.

#### Scenario: Deep-dive accesible desde la card
- **WHEN** un visitante abre el detalle de Fidello o Enkoth
- **THEN** ve secciones de Problema, Enfoque, Arquitectura, Decisiones y Resultado
- **AND** incluye un diagrama de arquitectura (SVG) representando los componentes clave (p. ej. Supabase +
  RLS multi-tenant para Fidello; Lambda + Step Functions + EventBridge + webhooks para Enkoth)

#### Scenario: Sin enlaces rotos para repos privados
- **WHEN** el proyecto tiene repositorio privado
- **THEN** la vista no muestra enlaces "View Code" rotos; ofrece "demo a solicitud" o descripción sin enlace

#### Scenario: Coherente con el diseño y responsive
- **WHEN** se renderiza el deep-dive
- **THEN** reutiliza la paleta y estilos existentes y funciona en 992/768/480px, sin frameworks nuevos
