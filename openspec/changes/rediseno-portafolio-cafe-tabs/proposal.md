## Why

El portafolio se ve demasiado oscuro (casi negro) y el propietario quiere una identidad más cálida y
elegante alineada con su CV (café/dorado), conservando el efecto matrix que es su sello. Además quiere una
navegación tipo "menú" (una sección a la vez) y una sección única/divertida que lo diferencie.

## What Changes

- **Paleta café elegante**: base cálida (café/carbón, no negro puro), acento café-dorado y un ámbar claro;
  el **efecto matrix se conserva pero recoloreado a ámbar**. **BREAKING** visual: cambia la paleta del sitio.
- **Navegación por secciones (tabs)**: el menú muestra **una sección a la vez** (las demás se ocultan); el
  ítem activo se resalta. El hero (nombre/tagline/resumen) permanece visible arriba.
- **Sección Terminal interactiva**: nueva sección donde el visitante escribe comandos (`whoami`, `ls
  projects`, `cat cv`, `skills`, `sdd`, `help`, `clear`) y navega; con algún easter egg. On-brand.

## Capabilities

### New Capabilities
- `paleta-cafe-elegante`: tokens de color cálidos (café/dorado/ámbar) + matrix recoloreado, accesible.
- `navegacion-por-secciones`: navegación tipo tabs (una sección visible a la vez) con estado activo.
- `terminal-interactiva`: sección de terminal con comandos y easter eggs, en vanilla JS.

### Modified Capabilities
(ninguna con requisitos previos en `openspec/specs/`; se construye sobre el sitio actual)

## Impact

- **Código**: `index.html` (CSS de paleta, matrix JS recoloreado, CSS+JS de tabs, sección+CSS+JS de terminal).
- **Docs**: `docs/frontend-standards.md` y `CLAUDE.md` (§paleta) deben actualizarse a la nueva paleta.
- **Restricciones**: HTML/CSS/JS vanilla, sin frameworks; responsive 992/768/480; mantener accesibilidad
  (foco, `prefers-reduced-motion`, contraste AA) y el asistente IA + widget intactos.
- **Despliegue**: por CI/CD (push a main → S3+CloudFront). El CV (cv/) no cambia en este cambio.
