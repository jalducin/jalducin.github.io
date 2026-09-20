# Reporte Step 5/6 — Pruebas, verificación de estado y verificación manual UI

- Fecha: 2026-09-19
- Cambio: portafolio-bilingue
- Agente: frontend-developer (Claude Code)
- Rama: `feature/portafolio-bilingue` (desde `main` @ `a31eaea`)

## Comandos ejecutados
- `python scripts/mark_i18n.py` — marcado `data-i18n*` (187 elementos + 47 atributos → 214 claves tras depurar invariantes)
- `python scripts/build_dict.py` — diccionario ES (192 claves), botón `#lang-btn`, runtime, palette, terminal (idempotente)
- `python scripts/audit_i18n.py` — 47 checks heredados + 10 checks i18n
- `python scripts/probe_i18n.py` — 18 probes headless (Chrome 152)
- `python scripts/shots_es.py` — 15 capturas ES (5 vistas × 1280/768/480) + probe de overflow/botón
- `python scripts/sync_specs.py` — deltas → `openspec/specs/`
- `openspec validate portafolio-bilingue`

## Resultados de pruebas
- `audit_i18n.py`: **57 checks · 57 PASS · 0 FAIL** (antes del cambio: los 10 checks i18n en FAIL por diseño)
- `probe_i18n.py`: **18/18 PASS** — `?lang=es`; nav/h2/niveles/badge/placeholders en ES; headline invariante;
  EN restaurado byte a byte tras es→en→es→en; tab activa conservada; `__showTab`/`__downloadCV`/4 `a[data-cv]`/
  terminal/form/palette intactos; persistencia en `localStorage`; `navigator.language` es-MX → ES;
  preferencia EN gana a navigator; `?lang=es` gana a preferencia; `localStorage` bloqueado (clave `lang`) → sin
  errores y el toggle funciona; terminal `lang es` / `lang` / `lang xx` (error amable) / `help` / `idioma en`.
- `shots_es.py`: **15/15 PASS** — sin overflow horizontal, botón visible y dentro del viewport en los 3 anchos.
- Duración total: ~4 min.

## Verificación de estado
- Antes: `main` @ `a31eaea`; `index.html` 83 551 bytes; 0 `data-i18n`.
- Después: `index.html` 110 893 bytes (+27 KB: diccionario ES + runtime); 214 claves (192 traducidas + 22
  invariantes: líneas "Stack:", tecnologías, WhatsApp/LinkedIn, badges de blog); `<html lang="en">` por defecto.
- Estado restaurado: N/A (sin datos mutados); temporales `_probe_i18n.html`, `_shot_es.html` eliminados.

## Verificación manual UI/frontend (EL AGENTE EJECUTÓ)
Capturas en `reports/shots/es_*_{1280,768,480}.png`. Revisadas: `es_experience_480.png` (timeline en español,
botón "EN" en la barra), resto generadas con probe PASS. Incidencia resuelta durante la implementación: el
diccionario JSON quedó inicialmente después del script de runtime (ES vacío) → se ancló antes del primer
`<script>` del body; y `build_dict.py` duplicaba el botón/CSS al re-ejecutarse → guardas de idempotencia.
Decisión de UX: el botón vive como hijo directo de `<nav>` para ser visible en la barra también en móvil (no
solo dentro del menú hamburguesa).

## Resultado
- Step 5 (pruebas) y Step 6 (verificación manual): **PASS**
- Bloqueos: ninguno
