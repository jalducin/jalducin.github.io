## ADDED Requirements

### Requirement: Accesibilidad y rendimiento altos

El sitio SHALL cumplir buenas prácticas de accesibilidad y rendimiento, apuntando a puntajes Lighthouse
altos (objetivo ~100 en Accesibilidad y Best Practices) sin romper la estética actual.

#### Scenario: Accesibilidad básica cubierta
- **WHEN** se audita el sitio (Lighthouse / revisión a11y)
- **THEN** todas las imágenes informativas tienen `alt`, los iconos-enlace tienen `aria-label`, y el foco
  de teclado es visible y navegable
- **AND** el contraste de texto cumple WCAG AA en ambos temas (oscuro y claro)

#### Scenario: Rendimiento sin regresiones
- **WHEN** se mide el rendimiento de la página
- **THEN** no hay recursos que bloqueen de forma evidente el render y la animación matrix no degrada la
  usabilidad (respeta `prefers-reduced-motion` cuando esté activo)
