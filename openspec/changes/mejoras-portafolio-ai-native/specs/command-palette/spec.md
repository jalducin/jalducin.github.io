## ADDED Requirements

### Requirement: Paleta de comandos (Cmd/Ctrl+K)

El sitio SHALL ofrecer una paleta de comandos para navegar y ejecutar acciones rápidas, implementada en
JavaScript vanilla (sin frameworks).

#### Scenario: Abrir y navegar con la paleta
- **WHEN** el visitante presiona `Cmd+K` (macOS) o `Ctrl+K` (Windows/Linux)
- **THEN** se abre una paleta con búsqueda que lista secciones (Experience, Projects, Skills, etc.) y
  acciones (Descargar CV, Contacto)
- **AND** seleccionar un resultado navega a la sección o ejecuta la acción, y `Esc` la cierra

#### Scenario: Accesible y no intrusiva
- **WHEN** la paleta está abierta
- **THEN** es navegable por teclado (flechas + Enter), tiene foco atrapado y respeta la paleta de colores
- **AND** no interfiere con el uso normal del sitio cuando está cerrada
