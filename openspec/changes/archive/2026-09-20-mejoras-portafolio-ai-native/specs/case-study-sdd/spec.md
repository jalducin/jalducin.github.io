## ADDED Requirements

### Requirement: Caso de estudio del flujo SDD del propio repo

El sitio SHALL incluir una pieza "Anatomía de un cambio" que muestre cómo se construye el portafolio con
Spec-Driven Development (OpenSpec), usando un cambio real del repositorio como ejemplo.

#### Scenario: Recorrido del flujo con artefactos reales
- **WHEN** un visitante abre el caso de estudio
- **THEN** se presenta el flujo `proposal → specs → design → tasks → apply → archive` con un cambio real
  del repo (p. ej. `actualizar-portafolio-cv-ai-native`)
- **AND** cada etapa enlaza o resume el artefacto correspondiente (proposal/specs/design/tasks)

#### Scenario: Coherente con el sistema de diseño
- **WHEN** se renderiza la pieza
- **THEN** reutiliza estilos existentes y es responsive (992/768/480px), sin frameworks nuevos
