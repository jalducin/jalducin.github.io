# Tasks — cv-claridad (Sprint 1: rediseño del CV)

## 0. Crear feature branch (SIEMPRE PRIMERO)
- [x] 0.1 Descartar el PDF EN roto sin commitear (`git restore cv/CV_JuanValentinAlducin_EN.pdf`; se regenera en 3.4).
- [x] 0.2 Crear y cambiar a `feature/cv-claridad` desde `main`.

## 1. Fuente de verdad: llms.txt
- [x] 1.1 Medir cifras de platform-STALD con fecha de corte (`git -C ../platform-STALD log --oneline | wc -l`,
      `gh pr list -R jalducin/platform-STALD --state merged --limit 1000 --json number -q length`, conteo de
      `openspec/changes/archive`) y anotarlas en el reporte; redondear hacia abajo con "+".
- [x] 1.2 Titular y línea `Role:` = `Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI`; resumen corto.
- [x] 1.3 Featured projects: agregar platform-STALD (sin datos de alumnos), quitar Pyzzeria, quitar de Fidello
      "pilot, cloud beta" y "validated by product in real coffee shops".
- [x] 1.4 Inventario Build: agregar Deno / Deno Deploy y Claude Code (subagents, skills, hooks, MCP).
- [x] 1.5 Agregar sección/línea de Certifications (Anthropic Academy, Vanderbilt, AWS Bedrock).

## 2. Contenido del CV (cv.html y cv-en.html, en paralelo)
- [x] 2.1 Titular y resumen (≤ 300 caracteres) según design.
- [x] 2.2 Experiencia: rol actual ≤ 4 bullets, Podemos 2025–26 ≤ 2, Redsis ≤ 2, Softtek 1; quitar líneas `Stack:`;
      "AI Specialist" en ambos idiomas.
- [x] 2.3 Habilidades: 5 categorías con evidencia (sin soft skills ni Learning).
- [x] 2.4 Proyectos: platform-STALD, Fidello, Monitoreo-Cloud con cifra + enlace; línea "Otros"; sin Pyzzeria.
- [x] 2.5 Cursos: 3 líneas (Anthropic Academy, Vanderbilt, AWS).
- [x] 2.6 Sincronizar `cv/CV_JuanValentinAlducin.md` con el contenido ES.

## 3. Formato A4 y build
- [x] 3.1 `@page { size: 210mm 297mm }` y `.sheet` a 210 mm en ambos HTML.
- [x] 3.2 Ajustar reparto de columnas si hace falta (Cursos a la derecha) hasta `.sheet` ≤ 297 mm.
- [x] 3.3 `cv/build.ps1`: comentario "tamaño A4".
- [x] 3.4 Regenerar ambos PDFs con `powershell -ExecutionPolicy Bypass -File cv\build.ps1`.

## 4. Revisar y actualizar pruebas existentes (OBLIGATORIO)
- [x] 4.1 El proyecto no tiene suite para el CV: crear `scripts/cv/check_cv.py` que verifique los escenarios de
      `cv-contenido-claro` y `cv-presentacion` (titular idéntico en 3 archivos, resumen ≤ 300, bullets por rol,
      sin `.stack` en experiencia, 5 `.skill`, orden de `.ptitle`, cadenas prohibidas — `Pyzzeria`, `IA Specialist`,
      `beta`, `cafeterías reales`, `real coffee shops`, `Live Demo` —, ≤ 3 `.course`, `@page` A4, PDFs de
      1 página con `/MediaBox` ≈ 595×842 y sin fuentes Type3).
- [x] 4.2 Confirmar que `check_cv.py` FALLA contra `main` (antes del cambio) y pasa después.

## 5. Ejecutar pruebas y verificar estado (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] 5.1 `python scripts/cv/check_cv.py` → todo PASS.
- [x] 5.2 Auditoría de privacidad del empleador:
      `python openspec/changes/archive/2026-09-19-cv-portafolio-sre-automation/scripts/audit.py` → sin hallazgos.
- [x] 5.3 Medir la altura del `.sheet` en Chrome headless (≤ 297 mm) en ES y EN.
- [x] 5.4 Verificar que el sitio sigue descargando los PDFs (rutas sin cambios) y que `scripts/i18n/audit_i18n.py`
      no se rompe por el cambio en `llms.txt`.
- [x] 5.5 Estado: el cambio no muta datos; confirmar `git status` limpio fuera de los archivos del cambio.
- [x] 5.6 Reporte: `reports/2026-11-02-step-5-pruebas-y-verificacion.md`.

## 6. Verificación manual (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] 6.1 Extraer el texto de ambos PDFs (pypdf/pdftotext) y verificar orden de lectura: nombre → contacto →
      resumen → experiencia; contacto como texto.
- [x] 6.2 Revisión ATS: cubierta por `check_cv.py` + extracción de texto (ver reporte; no se lanzó el subagente).
- [x] 6.3 Render a PNG de cada página y revisión visual (sin cortes, QR alineados, sin huecos grandes);
      guardar capturas en `reports/shots/`.
- [x] 6.4 Revisar a mano que el texto de platform-STALD no contiene datos de personas.

## 7. Actualizar documentación técnica (OBLIGATORIO)
- [x] 7.1 `CLAUDE.md`: sección PDF del CV (Oficio → A4) y tabla de proyectos (STALD agregado, Pyzzeria retirado,
      Fidello sin "piloto en beta").
- [x] 7.2 `docs/frontend-standards.md` y `cv/README.md`: tamaño A4; documentar `scripts/cv/check_cv.py`.
- [x] 7.3 Anotar en el reporte los pendientes del Sprint 2 (index.html, `assistant/knowledge.md`, specs
      `proyecto-fidello`, `posicionamiento-ai-native`, `skills-y-formacion`).
- [x] 7.4 Verificar 0 enlaces rotos a archivos movidos/renombrados (no se espera ninguno).
