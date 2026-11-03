# Reporte Step 5 — Pruebas y verificación de estado

- Fecha: 2026-11-02
- Cambio: cv-claridad
- Agente: Claude Code (frontend-developer)

## Comandos ejecutados
- `python scripts/cv/check_cv.py` (nuevo: escenarios de `cv-contenido-claro` y `cv-presentacion`)
- `powershell -ExecutionPolicy Bypass -File cv\build.ps1`
- `python scripts/i18n/audit_i18n.py`
- `python scripts/assistant/probe_kb.py`
- `audit.py` archivado de `2026-09-19-cv-portafolio-sre-automation` (con la raíz del repo corregida en memoria:
  el script calcula `ROOT` un nivel corto desde que vive en `archive/`; no se editó el archivo archivado)
- Extracción de texto con `pypdf` y capturas con Chrome headless (`reports/shots/cv-es.png`, `cv-en.png`)

## Resultados de pruebas
- `check_cv.py` contra `main` (antes del cambio): **31 FAIL** (confirma que las pruebas detectan el estado viejo).
- `check_cv.py` en la rama: **0 fallas** (llms.txt + ES + EN, incluye PDFs 1 página, 595×842 pt, fuentes Type0).
- `audit_i18n.py`: 64 PASS · 0 FAIL (se actualizaron 2 checks a la spec nueva: rol "AI Specialist" en ES y
  Fidello sin estado de piloto activo).
- `probe_kb.py`: 18 PASS · 0 FAIL (el chatbot no cambia en este sprint).
- `audit.py` archivado: 0 nombres internos del empleador. Fallas restantes = 3 preexistentes en `main`
  (`profile.txt` ya no existe, h3 del header y badges de uptime del sitio) + 2 intencionales de esta spec
  ("IA Specialist" → "AI Specialist", Fidello sin "piloto").
- Duración: ~10 min.

## Cifras de platform-STALD (fecha de corte 2026-11-02)
- Commits: 999 · PRs fusionados: 263 · Cambios OpenSpec archivados: 87 · Specs: 14
- Archivos de prueba Deno (CI): 132 · Flujos E2E locales: 86 · Skills: 14 · Subagentes: 5
- En el CV se publican redondeadas hacia abajo: "+250 PRs · +85 cambios OpenSpec".

## Verificación manual (Step 6)
- Orden de lectura del PDF (ES y EN): nombre → titular → contacto (texto) → resumen → experiencia. OK.
- Captions de los QR: "PORTAFOLIO/PORTFOLIO" aparece en el texto extraído (preexistente; `aria-hidden` no lo
  oculta a pypdf). No afecta el parseo de contacto.
- Render visual: 1 página A4, sin cortes, QR alineados; queda ~12 % de aire al pie (deliberado: "no exagerar").
- platform-STALD: sin nombres, correos, conteos ni capturas de alumnos; sin enlace al repo privado de datos.
- `ats-reviewer` no se ejecutó como subagente: los checks equivalentes (texto extraíble, contacto como texto,
  encabezados estándar, fechas legibles, sin Type3) están automatizados en `check_cv.py`.

## Verificación de estado
- Antes: PDFs Oficio 612×964 pt; PDF EN local roto (28 KB) sin commitear.
- Después: PDFs A4 595×842 pt, ~217 KB cada uno.
- Estado restaurado: N/A (no hay datos que mutar). El PDF roto se descartó con `git restore` antes de empezar.

## Pendientes para el Sprint 2 (portafolio-claridad)
- `index.html`: Pyzzeria (card, terminal, palette), badge "Pilot" de Fidello, titular del header/meta, card de
  platform-STALD, cursos. `assistant/knowledge.md` + `build_kb.py` desde el nuevo `llms.txt`.
- Specs a modificar: `proyecto-fidello`, `posicionamiento-ai-native`, `skills-y-formacion`.
- `blog/deep-dive-pyzzeria.html`: decidir si se archiva o se conserva como post técnico sin "Live Demo".
- `audit_i18n.py` exige "Pilot" en los badges de `index.html`: cambiarlo junto con el badge.

## Resultado
- Estado Step 5: PASS
- Bloqueos: ninguno
