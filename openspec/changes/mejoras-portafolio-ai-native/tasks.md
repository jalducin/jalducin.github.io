> Implementación incremental: cada capability puede ir en su propia rama `feature/<capability>` con los
> pasos obligatorios (ver `.claude/rules/openspec-tasks-mandatory-steps.md`). Orden por ROI.

## 0. Preparación (OBLIGATORIO — SIEMPRE PRIMERO, por capability)

- [x] 0.1 Leer `openspec/config.yaml`, `docs/base-standards.md` y `docs/frontend-standards.md`
- [x] 0.2 Crear la feature branch de la capability a implementar (`feature/mejoras-portafolio-quickwins`)

## 1. contacto-funcional (BUG — primero) ✅

- [x] 1.1 Quitar `formspree.io/f/YOUR_FORM_ID`; el form ahora compone un `mailto` (funciona sin backend)
- [x] 1.2 Añadir "Copy Email" y CTAs (email, WhatsApp, LinkedIn) sin placeholders
- [x] 1.3 Confirmar 0 `YOUR_FORM_ID`/formspree en el HTML

## 2. social-og-image ✅

- [x] 2.1 Crear `cv/og.html` (1200×630) y generar `assets/img/og-image.png` con Chrome headless
- [x] 2.2 Añadir `og:image`/`twitter:image` y cambiar `twitter:card` a `summary_large_image`
- [x] 2.3 (comando de regeneración documentado en el commit / build pattern)

## 3. seo-tecnico ✅

- [x] 3.1 Crear `robots.txt` (permitir + referenciar sitemap) y `sitemap.xml` válido
- [x] 3.2 Añadir `<link rel="canonical">` en `index.html`

## 4. accesibilidad-y-rendimiento ✅ (Lighthouse pendiente de corrida formal)

- [x] 4.1 `aria-label` en iconos-enlace; foco visible (`:focus-visible`); `alt` en imágenes
- [x] 4.2 Respetar `prefers-reduced-motion` (matrix sin animar + media query global)
- [ ] 4.3 Correr Lighthouse y cerrar gaps restantes (objetivo ~100) — pendiente: sin CLI `lighthouse` en la máquina (ver reporte 2026-09-20)

## 5. command-palette ✅

- [x] 5.1 Paleta Cmd/Ctrl+K en vanilla JS (búsqueda, navegación a secciones, acciones)
- [x] 5.2 Teclado (↑↓/Enter/Esc), cierre por overlay; respeta la paleta de colores

## 5b. organizacion-de-archivos ✅

- [x] 5b.1 Mover `QR.png → assets/img/` y `CV_JuanValentinAlducin.pdf → cv/`
- [x] 5b.2 Actualizar TODAS las referencias (index.html, cv.html, build.ps1, llms.txt, CLAUDE.md, docs, README) — 0 rotas
- [x] 5b.3 Verificar HTTP 200 en nuevas rutas y que el sitio/CV funcionan

## 6. asistente-ia-portafolio — **superseded** por el cambio `openspec/changes/asistente-ia-portafolio` (widget ya en `index.html`; no se reimplementa aquí)

- [x] 6.1 Crear proxy serverless (AWS Lambda) a Claude; key SOLO en el entorno de la Lambda
- [x] 6.2 Usar `llms.txt` como contexto/base de conocimiento; manejar fuera-de-alcance sin inventar
- [x] 6.3 Rate-limit + caché + tope de presupuesto; degradar con CTAs ante límite/fallo
- [x] 6.4 Widget de chat en vanilla JS (fetch al endpoint), accesible y responsive

## 7. case-study-sdd

- [x] 7.1 Página "Anatomía de un cambio" (`blog/anatomia-de-un-cambio.html`) con el flujo proposal→…→archive del cambio real `2026-09-19-cv-portafolio-sre-automation`
- [x] 7.2 Enlazar/resumir los artefactos (fragmentos reales + enlaces a GitHub); card en Writing (`wri.h34`, ES en `es.py`), entrada en `llms.txt` y `sitemap.xml`; estilos del blog y responsive

## 8. project-deep-dives

- [x] 8.1 Vistas de detalle de Fidello y **Pyzzeria** (Problema→Enfoque→Arquitectura→Decisiones→Resultado) — Enkoth no: sistema interno del empleador (ver design.md «Desviaciones»)
- [x] 8.2 Diagramas de arquitectura SVG inline; Fidello sin botón de código (demo a solicitud); botones "Deep dive ↗" en las cards (`proj.a8`/`proj.a9`)

## 9. Verificación y reporte (OBLIGATORIO — EL AGENTE EJECUTA, por capability)

- [x] 9.1 Render headless (Chrome) de las 3 páginas nuevas y de Writing/Projects en 1280/768/480; capturas revisadas (case-study-sdd y project-deep-dives)
- [ ] 9.2 Lighthouse donde aplique (omitido: sin CLI; documentado en el reporte); el asistente IA se prueba contra su endpoint antes de exponerlo (superseded, cambio `asistente-ia-portafolio`)
- [x] 9.3 Reporte `openspec/changes/mejoras-portafolio-ai-native/reports/2026-09-20-case-study-y-deep-dives.md` (audit i18n 57/57, probes 18/18, enlaces, balance de tags, capturas)

## 10. Documentación (OBLIGATORIO — consistencia documental)

- [x] 10.1 `docs/frontend-standards.md §4.1` (patrón de páginas del blog, case study y deep dives), `CLAUDE.md` (deep dives en la tabla de proyectos, nota Enkoth), `README.md` (`blog/` en la estructura)
- [x] 10.2 0 enlaces relativos rotos (script de verificación en el reporte); cifras de Fidello/Pyzzeria tomadas de `CLAUDE.md`/`llms.txt` (fuente única)

## 11. Cierre

- [ ] 11.1 Merge incremental a `main` y verificar en GitHub Pages
- [ ] 11.2 Archivar el cambio cuando todas las capabilities estén implementadas
