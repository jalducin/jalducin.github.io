## Why

El portafolio ya está alineado al posicionamiento AI-native, pero hay (a) un **bug en vivo** (el formulario
de contacto apunta a un placeholder de Formspree y no envía) y (b) oportunidades de alto impacto, vistas en
los mejores portafolios de AI/backend engineers, para **demostrar** el perfil agentic (no solo declararlo) y
subir credibilidad, SEO y experiencia de usuario. Este cambio captura esas mejoras como specs para
implementarlas de forma incremental.

## What Changes

- **Arreglar el contacto** (BUG): el form usa `formspree.io/f/YOUR_FORM_ID` (no funciona). Conectar un
  endpoint real o sustituir por copiar-email + CTAs. **BREAKING** del comportamiento actual del form.
- **Social card (og:image)**: generar una imagen Open Graph propia (mismo pipeline Chrome-headless del CV).
- **SEO técnico**: `robots.txt`, `sitemap.xml`, `<link rel="canonical">`.
- **Accesibilidad y rendimiento**: pasar Lighthouse a ~100 (alt, contraste tema claro, aria-labels, foco).
- **Command palette (Cmd/Ctrl+K)**: navegación rápida on-brand, vanilla JS.
- **Asistente IA "Ask my portfolio"**: chat que responde sobre el perfil usando `llms.txt` como base, vía
  proxy serverless (AWS Lambda) a la API de Claude. Prueba viva del perfil agentic.
- **Case study de SDD**: página "Anatomía de un cambio" que muestra el flujo OpenSpec real del repo.
- **Project deep-dives**: vistas de detalle (Problema → Enfoque → Arquitectura → Resultado) con diagramas
  para Fidello y Enkoth.

## Capabilities

### New Capabilities
- `contacto-funcional`: el contacto funciona de extremo a extremo (sin placeholders rotos).
- `social-og-image`: previsualización social con imagen propia.
- `seo-tecnico`: indexabilidad (robots, sitemap, canonical).
- `accesibilidad-y-rendimiento`: a11y y Lighthouse altos.
- `command-palette`: navegación por paleta de comandos.
- `asistente-ia-portafolio`: asistente IA sobre el perfil (proxy serverless + Claude).
- `case-study-sdd`: caso de estudio del flujo SDD del propio repo.
- `project-deep-dives`: páginas de detalle de proyectos con arquitectura.
- `organizacion-de-archivos`: estructura de archivos profesional (imágenes en `assets/img/`, CV en `cv/`).

### Modified Capabilities
(ninguna — se construyen sobre las capabilities ya vigentes en `openspec/specs/`)

## Impact

- **Código**: `index.html` (form, command palette, og/canonical, a11y), nuevos estáticos (`robots.txt`,
  `sitemap.xml`, `og-image` y su generador, páginas de case study / deep-dives), assets de diagramas (SVG).
- **Serverless** (solo para el asistente IA): función AWS Lambda como proxy a Claude (la API key NUNCA en el
  front). Fuera de este repo o documentada como dependencia externa.
- **Restricciones**: respetar `docs/frontend-standards.md` — HTML/CSS/JS vanilla, sin frameworks ni npm,
  GitHub Pages estático, responsive 992/768/480px. El asistente IA es la única pieza con backend.
- **Riesgos**: costo/abuso del endpoint IA (mitigar con rate-limit, caché y tope de presupuesto).
