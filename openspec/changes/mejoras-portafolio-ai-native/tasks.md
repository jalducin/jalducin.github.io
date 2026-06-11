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
- [ ] 4.3 Correr Lighthouse y cerrar gaps restantes (objetivo ~100)

## 5. command-palette ✅

- [x] 5.1 Paleta Cmd/Ctrl+K en vanilla JS (búsqueda, navegación a secciones, acciones)
- [x] 5.2 Teclado (↑↓/Enter/Esc), cierre por overlay; respeta la paleta de colores

## 5b. organizacion-de-archivos ✅

- [x] 5b.1 Mover `QR.png → assets/img/` y `CV_JuanValentinAlducin.pdf → cv/`
- [x] 5b.2 Actualizar TODAS las referencias (index.html, cv.html, build.ps1, llms.txt, CLAUDE.md, docs, README) — 0 rotas
- [x] 5b.3 Verificar HTTP 200 en nuevas rutas y que el sitio/CV funcionan

## 6. asistente-ia-portafolio

- [ ] 6.1 Crear proxy serverless (AWS Lambda) a Claude; key SOLO en el entorno de la Lambda
- [ ] 6.2 Usar `llms.txt` como contexto/base de conocimiento; manejar fuera-de-alcance sin inventar
- [ ] 6.3 Rate-limit + caché + tope de presupuesto; degradar con CTAs ante límite/fallo
- [ ] 6.4 Widget de chat en vanilla JS (fetch al endpoint), accesible y responsive

## 7. case-study-sdd

- [ ] 7.1 Página/sección "Anatomía de un cambio" con el flujo proposal→…→archive de un cambio real del repo
- [ ] 7.2 Enlazar/resumir los artefactos; reutilizar estilos y responsive

## 8. project-deep-dives

- [ ] 8.1 Vistas de detalle de Fidello y Enkoth (Problema→Enfoque→Arquitectura→Decisiones→Resultado)
- [ ] 8.2 Diagramas de arquitectura en SVG; sin enlaces rotos para repos privados (demo a solicitud)

## 9. Verificación y reporte (OBLIGATORIO — EL AGENTE EJECUTA, por capability)

- [ ] 9.1 Servir el sitio localmente y verificar la capability en navegador + 3 breakpoints (992/768/480)
- [ ] 9.2 Lighthouse donde aplique; el asistente IA se prueba contra su endpoint antes de exponerlo
- [ ] 9.3 Crear el reporte en `openspec/changes/mejoras-portafolio-ai-native/reports/AAAA-MM-DD-<capability>.md`

## 10. Documentación (OBLIGATORIO — consistencia documental)

- [ ] 10.1 Actualizar `docs/frontend-standards.md` / `CLAUDE.md` / `README.md` según la capability
- [ ] 10.2 Verificar 0 enlaces rotos y una sola fuente de verdad por dato

## 11. Cierre

- [ ] 11.1 Merge incremental a `main` y verificar en GitHub Pages
- [ ] 11.2 Archivar el cambio cuando todas las capabilities estén implementadas
