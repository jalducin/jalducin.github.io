# Proposal: retirar-metricas-y-jvmarket

## Why
El propietario decidió (2026-09-20) no publicar porcentajes de mejora en CV ni portafolio (~40 % menos tiempo de
revisión, 80 % de autoresolución N1, 99.95 % de uptime en julio 2026) y retirar el proyecto JV Market del
portafolio. Las specs vigentes exigen ambas cosas, así que el cambio debe formalizarse.

## What Changes
- Se retiran las tres cifras de: header y badges de `index.html`, tarjeta "Measurable impact", bullets de
  Podemos, meta/OG/JSON-LD, `llms.txt`, diccionario ES, CV ES/EN (PDFs regenerados). Se conservan los SLAs
  (<10 min primera respuesta, <2 h resolución crítica) y la redacción cualitativa.
- Se elimina la card de JV Market (`index.html`), su entrada en `llms.txt`, su fila en `CLAUDE.md`, sus claves
  ES y su mención en la terminal (`ls projects`).
- Audit i18n actualizado (checks de cifras / JV Market).

## Capabilities
### New Capabilities
(ninguna)
### Modified Capabilities
- `agentic-engineering-hardening`: badges y tarjeta de impacto sin porcentajes.
- `experiencia-actualizada`: bullets de Podemos sin cifras.
- `posicionamiento-ai-native`: resumen sin porcentajes.
- `proyecto-jvmarket`: requirement REMOVED.

## Impact
`index.html`, `scripts/i18n/es.py` (+ `build_dict.py`), `llms.txt`/`profile.txt`, `cv/cv.html`, `cv/cv-en.html`,
PDFs, `CLAUDE.md`, `scripts/i18n/audit_i18n.py`, specs. Deploy automático al mergear.
