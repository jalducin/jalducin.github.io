# scripts/i18n — herramientas del portafolio bilingüe

Origen: cambio OpenSpec `2026-09-20-portafolio-bilingue`. Se promueven aquí porque se usan en cada cambio
que toque texto visible de `index.html`.

| Script | Uso |
|---|---|
| `es.py` | Diccionario ES (`ES`) + `INVARIANTES` + `TITLES`. **Aquí se agregan las traducciones de contenido nuevo.** |
| `mark_i18n.py` | Marca elementos traducibles con `data-i18n*` (idempotente) y extrae `en.json`. Solo si agregas bloques grandes. |
| `build_dict.py` | Regenera el JSON `#i18n-es` en `index.html` a partir de `es.py` (idempotente). Falla si hay claves huérfanas o sin traducir no declaradas invariantes. |
| `audit_i18n.py` | 57 checks de consistencia (headline, fechas, nombres internos, PDFs, i18n). Debe dar 0 FAIL antes de merge. |
| `probe_i18n.py` | 18 probes headless del selector de idioma. |
| `shots_es.py` | Capturas ES en 1280/768/480 (salida en `scripts/i18n/shots/`, ignorada por git). |

Flujo para contenido nuevo: añade el HTML con `data-i18n="<sec>.<tag><n>"` → entrada en `ES` de `es.py` →
`python scripts/i18n/build_dict.py` → `python scripts/i18n/audit_i18n.py` → `python scripts/i18n/probe_i18n.py`.
