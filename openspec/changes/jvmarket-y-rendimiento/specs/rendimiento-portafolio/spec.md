## ADDED Requirements

### Requirement: Mejoras de rendimiento del portafolio

El portafolio SHALL aplicar mejoras de rendimiento sin romper estética ni funcionalidad (tabs, terminal,
asistente, paleta, a11y).

#### Scenario: Conexiones externas optimizadas
- **WHEN** se cargan iconos servidos por CDN externa (jsdelivr)
- **THEN** el `<head>` incluye `preconnect`/`dns-prefetch` a esa CDN para reducir latencia de DNS/handshake

#### Scenario: Imágenes diferidas y sin layout shift
- **WHEN** la página tiene imágenes (iconos de skills, etc.)
- **THEN** usan `loading="lazy"` y `decoding="async"` y tienen dimensiones (width/height) para evitar
  reflujo/layout shift

#### Scenario: Matrix pausado en segundo plano
- **WHEN** la pestaña del navegador no está visible (`document.hidden`)
- **THEN** la animación matrix se pausa (no consume CPU) y se reanuda al volver
- **AND** se mantiene el respeto a `prefers-reduced-motion`
