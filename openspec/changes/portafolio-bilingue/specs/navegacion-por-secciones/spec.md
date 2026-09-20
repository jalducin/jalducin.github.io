# Capability: navegacion-por-secciones (delta)

## ADDED Requirements

### Requirement: Botón de idioma en la navegación

La barra de navegación SHALL incluir un botón de idioma junto al toggle de tema, accesible por teclado, con
`aria-label` bilingüe y texto que indica el idioma destino ("ES" / "EN"). Cambiar de idioma MUST conservar la
sección activa y funcionar dentro del menú hamburguesa en móvil.

#### Scenario: Cambio de idioma sin perder la sección
- **WHEN** el visitante está en la sección Projects y pulsa el botón de idioma
- **THEN** los textos de nav y de la sección cambian de idioma y Projects sigue siendo la sección activa
- **AND** en ≤768px el botón es visible dentro del menú desplegado y en la barra
