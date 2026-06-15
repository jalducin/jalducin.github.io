# Capability: seccion-writing (y mejoras de UX)

## ADDED Requirements

### Requirement: Sección Writing con páginas de blog dedicadas
El portafolio DEBE incluir una sección/tab **Writing** que liste posts (título, fecha, tags, tiempo de
lectura, extracto) y enlace a **páginas dedicadas** `/blog/<slug>.html`, cada una con el tema azul metálico,
contenido legible y **OG tags** propios. Mantiene el stack vanilla (sin frameworks ni build step).

#### Scenario: Sección Writing en el portafolio
- **WHEN** un visitante abre el tab "Writing"
- **THEN** ve tarjetas de posts con título, fecha, tags y tiempo de lectura, cada una enlazando a su página
- **AND** el nav resalta "Writing" como sección activa (sistema de tabs)
- **AND** existe acción en command palette y comandos de terminal `writing`/`blog`

#### Scenario: Páginas de blog dedicadas
- **WHEN** se abre `/blog/<slug>.html`
- **THEN** la página usa el tema azul metálico, es legible (ancho de lectura acotado) y tiene OG/canonical propios
- **AND** existen al menos 3 posts: SDD/OpenSpec, Docker (observabilidad local) y Grafana multi-fuente

### Requirement: Mejoras de UX (spotlight, Now) accesibles
El sitio DEBE incluir un **spotlight** de cursor sutil y un bloque **"Now"**, sin perjudicar accesibilidad.

#### Scenario: Spotlight de cursor
- **WHEN** el visitante mueve el cursor (dispositivo con hover, sin reduced-motion)
- **THEN** un glow azul tenue sigue el cursor en una capa de fondo (`z-index:-1`, `pointer-events:none`)
- **AND** se desactiva con `prefers-reduced-motion` y en dispositivos táctiles (`hover: none`)

#### Scenario: Bloque Now
- **WHEN** se abre el tab "How I Build with AI"
- **THEN** se muestra un bloque "Now" con la actividad actual (trabajo, proyectos locales, estudios)

### Requirement: Dependencias self-host (sin CDN de íconos)
Los íconos de tecnología DEBEN servirse localmente, sin depender de `cdn.jsdelivr.net`.

#### Scenario: Íconos locales
- **WHEN** se carga Hard Skills
- **THEN** los SVGs provienen de `assets/img/icons/` (no de jsdelivr) y no existe preconnect/dns-prefetch a jsdelivr

### Requirement: CV con doble QR (portafolio + LinkedIn)
El CV (ES y EN) DEBE mostrar dos mini-QR: portafolio y **LinkedIn**, ambos escaneables, manteniendo 1 página Oficio.

#### Scenario: QR de LinkedIn
- **WHEN** se revisa el encabezado del CV
- **THEN** hay dos QR con etiqueta (Portafolio/Portfolio y LinkedIn); el de LinkedIn decodifica a `linkedin.com/in/juanvalducinv`
- **AND** el CV se mantiene en 1 página

### Requirement: Validación de contenido (no problemático)
El contenido publicado DEBE estar libre de secretos/credenciales, claims falsos y usos de marca riesgosos.

#### Scenario: Revisión final
- **WHEN** se concluye el cambio
- **THEN** no hay credenciales/llaves expuestas, los datos de contacto son los públicos del dueño,
  los claims (métricas, stacks) son consistentes con su experiencia, y los nombres de marca se usan de forma
  nominativa (sin sugerir afiliación); los íconos devicon (MIT) se redistribuyen localmente
