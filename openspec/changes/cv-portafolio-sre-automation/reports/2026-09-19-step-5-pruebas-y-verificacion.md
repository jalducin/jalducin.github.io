# Reporte Step 5/6 — Pruebas, verificación de estado y verificación manual UI

- Fecha: 2026-09-19
- Cambio: cv-portafolio-sre-automation
- Agente: frontend-developer (Claude Code)
- Rama: `feature/cv-portafolio-sre-automation` (desde `main` @ `bb7ad40`)

## Comandos ejecutados

- `python openspec/changes/cv-portafolio-sre-automation/scripts/audit.py` — antes y después de los cambios
- `python openspec/changes/cv-portafolio-sre-automation/scripts/patch_index.py` — edición de `index.html`
- `python openspec/changes/cv-portafolio-sre-automation/scripts/patch_cv.py` — edición de `cv/cv.html`, `cv/cv-en.html`
- `powershell -ExecutionPolicy Bypass -File cv\build.ps1` — regeneración de PDFs (3 iteraciones)
- `python openspec/changes/cv-portafolio-sre-automation/scripts/measure_cv.py cv.html cv-en.html` — altura de columnas
- `python openspec/changes/cv-portafolio-sre-automation/scripts/shots.py` — capturas headless + probes DOM/JS
- `python openspec/changes/cv-portafolio-sre-automation/scripts/sync_specs.py` — sync de deltas a `openspec/specs/`
- `openspec validate cv-portafolio-sre-automation` — artefactos válidos
- `cp llms.txt backend/assistant/profile.txt`

## Resultados de pruebas (audit.py = suite del proyecto, no hay pruebas unitarias)

- Antes de los cambios: 47 checks · 18 PASS · 29 FAIL (esperado: headline viejo, nombres internos en CV/sitio,
  Kendra/Kiro, sin niveles ni principios, sin cifras de Fidello)
- Después: **47 checks · 47 PASS · 0 FAIL** (exit 0)
- Checks agregados en este cambio (task 4.1): 4 principios en `index.html` y `llms.txt`, leyenda de niveles,
  Kubernetes solo en VoltGrid, badges de Fidello con cifras, uptime en ≥2 lugares, piloto en CV ES/EN/llms,
  `profile.txt == llms.txt`, fuentes TrueType Segoe UI en PDF, PDF sin nombres internos.
- Duración: ~25 s por corrida

## Verificación de estado

- Antes: `main` @ `bb7ad40`; PDFs 243 876 / 243 440 bytes, 1 página; `llms.txt` con headline "Agentic AI Systems".
- Después: PDFs 247 032 / 246 407 bytes, **1 página cada uno**, fuentes `SegoeUI`, `SegoeUI-Bold`, `SegoeUIBlack`;
  `.sheet` medido 339.3 mm (izq 298.5 / der 292.2 ES; der 288.5 EN).
- Estado restaurado: N/A (sin datos mutados; archivos temporales `_shot_index.html`, `_v*.html/.pdf`,
  `_head_*.html/.pdf` eliminados; `git status` solo muestra archivos del cambio).

## Verificación manual UI/frontend (EL AGENTE EJECUTÓ)

Capturas en `reports/shots/`: `{ai-method,experience,featured-projects,hard-skills}_{1280,992,768,480}.png`,
`cv.png`, `cv-en.png`.

| Check | Resultado |
|---|---|
| Overflow horizontal a 480 px (4 vistas) | `scrollW == innerW` en las 4 vistas. **Hallazgo previo corregido:** `#experience` desbordaba 12 px (`.timeline-item{width:100%;margin-left:2rem}` en ≤768 px) también en `bb7ad40`; fix `width:calc(100% - 2rem)`. |
| Skills por niveles | `levels=4`, leyenda visible, 2 columnas en 1280/992 y 1 columna en 768/480 (`hard-skills_*.png`) |
| Principios | `principles=4` dentro de `#ai-method` (`ai-method_*.png`) |
| Fidello piloto | badges "Pilot · cloud beta" + 6 mini-badges de cifras (`fidelloMetrics=6`), `.tech` ampliada, sin Google Wallet |
| Descarga de CV | 4 enlaces `a[data-cv]` → `CV_JuanValentinAlducin[_EN]_2026-09.pdf`; `window.__showTab` presente |
| Secciones/IDs | `missingSections=` vacío (los 10 IDs de `GROUPS` existen), `dupIds=` vacío |
| Caso de error: `#seccion-inexistente` | cae en la tab `ai-method` (nav activa `#ai-method`) |
| Caso de error: nombre prohibido | `audit.py` detecta `SCI/Spore/Hipatia/Mambu` en el PDF previo (corrida "antes") |
| CV ES/EN | 1 página; tagline híbrido; 6+3 bullets de Podemos; Idiomas bajo Educación; Fidello con "Piloto en beta cloud · 793 pruebas · 91 migraciones" |
| Texto extraíble del PDF (ATS) | contiene nombre, teléfono, email, roles, fechas, Redsis, Softtek; sin nombres internos |

Incidencia de implementación: con el contenido nuevo el CV saltó a 2 páginas (Chrome mueve el flex `.cols`
completo a la página 2 cuando `.sheet` > 340 mm). Se movió Idiomas a la columna izquierda, se acortó el
resumen a 4 líneas y se bajó `line-height` 1.28 → 1.25; regla calibrada documentada en `design.md` D7 y en
la spec `cv-presentacion`.

## Resultado

- Estado Step 5 (pruebas) y Step 6 (verificación manual): **PASS**
- Bloqueos: ninguno
