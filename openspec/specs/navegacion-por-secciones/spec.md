# Capability: navegacion-por-secciones

## Requirements

### Requirement: Navegación por secciones (una a la vez)

El sitio SHALL mostrar **una sección a la vez** controlada por el menú (estilo tabs). Al elegir un ítem del
menú, MUST mostrarse esa sección y ocultarse las demás; el hero (nombre/tagline/resumen) permanece visible.

#### Scenario: Cambiar de sección
- **WHEN** el visitante hace clic en un ítem del menú (AI Method, Experience, Projects, Skills, Languages,
  Education, Contact, Terminal)
- **THEN** solo se muestra la sección correspondiente y las demás quedan ocultas
- **AND** el ítem activo del menú se resalta (estado activo)

#### Scenario: Estado inicial y enlaces profundos
- **WHEN** se carga el sitio (con o sin hash en la URL)
- **THEN** se muestra una sección por defecto (p. ej. AI Method) o la indicada por el hash si existe
- **AND** los atajos/anclas existentes siguen llevando a la sección correcta (mostrándola)

#### Scenario: Accesible y responsive
- **WHEN** se navega por teclado y en móvil
- **THEN** los ítems del menú son accesibles (foco visible, `aria-current` en el activo), funciona el
  menú hamburguesa en móvil y respeta 992/768/480px
- **AND** la sección visible recibe foco/scroll al inicio al cambiar
