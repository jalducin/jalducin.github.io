## ADDED Requirements

### Requirement: Estructura de archivos profesional y agrupada

El repositorio SHALL organizar los archivos por tipo/propósito para verse profesional, sin dejar binarios
sueltos en la raíz. Imágenes agrupadas, el CV (PDF) junto a su fuente, y la raíz reservada a entrada del
sitio, metadatos y documentación.

Estructura objetivo:
- `assets/img/` — imágenes (p. ej. `QR.png`, `og-image.png`). `assets/icons/` — iconos de tecnologías.
- `cv/` — fuente del CV (`cv.html`, `hex-bg.svg`, `build.ps1`, `README.md`) **y** el PDF generado
  (`CV_JuanValentinAlducin.pdf`).
- Raíz — `index.html`, `llms.txt`, `robots.txt`, `sitemap.xml`, `README.md`, archivos de agentes
  (`AGENTS.md`/`CLAUDE.md`/`GEMINI.md`), `.gitignore`, y carpetas del sistema (`docs/`, `openspec/`,
  `ai-specs/`, `.claude/`, `.gemini/`).

#### Scenario: La raíz no tiene binarios sueltos
- **WHEN** se lista la raíz del repo
- **THEN** no hay imágenes ni PDFs sueltos en la raíz (las imágenes viven en `assets/img/`, el PDF del CV
  en `cv/`)
- **AND** `index.html` permanece en la raíz (requisito de GitHub Pages)

#### Scenario: Cero referencias rotas tras mover archivos
- **WHEN** se mueve un archivo a su nueva ubicación
- **THEN** se actualizan TODAS sus referencias: enlaces de descarga del CV en `index.html`, `og:image` /
  JSON-LD `image`, ruta del QR en `cv/cv.html`, salida de `cv/build.ps1`, y menciones en `llms.txt`,
  `README.md`, `CLAUDE.md`, `docs/frontend-standards.md`, `sitemap.xml`
- **AND** una verificación (grep + carga local) confirma 0 enlaces rotos

#### Scenario: El sitio y el CV siguen funcionando
- **WHEN** se sirve el sitio tras la reorganización
- **THEN** el botón "Download CV" descarga el PDF desde su nueva ruta, el QR del CV resuelve, y la
  social card / JSON-LD apuntan a imágenes existentes (HTTP 200)
