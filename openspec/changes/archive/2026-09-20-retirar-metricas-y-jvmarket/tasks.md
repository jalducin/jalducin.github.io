# Tasks: retirar-metricas-y-jvmarket

## 0. Preparación (OBLIGATORIO — SIEMPRE PRIMERO)
- [x] 0.1 Step 0 — Rama `feature/retirar-metricas-y-jvmarket` desde `main` tras mergear las ramas paralelas

## 1. Contenido
- [x] 1.1 CV ES/EN sin 40 %/80 %/99.95 %; PDFs regenerados (1 página)
- [x] 1.2 `llms.txt`/`profile.txt` sin cifras y sin JV Market; `CLAUDE.md` sin la fila de JV Market y con la nota
- [x] 1.3 `index.html`: header, badges, tarjeta de impacto, bullets, meta/OG/JSON-LD sin cifras; card JV Market
      eliminada; `ls projects` sin JV-Market
- [x] 1.4 `scripts/i18n/es.py`: traducciones sin cifras; claves de JV Market retiradas; `build_dict.py`

## 2. Revisar y actualizar pruebas existentes (OBLIGATORIO)
- [x] 2.1 `scripts/i18n/audit_i18n.py`: check de uptime → check "sin cifras" + "sin JV Market"

## 3. Ejecutar pruebas y verificar estado (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] 3.1 `audit_i18n.py` 0 FAIL; `probe_i18n.py` 18/18; PDFs 1 página sin cifras; reporte en `reports/`

## 4. Verificación manual (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] 4.1 Render headless de header/AI Method/Projects (1280/480) en EN y ES: sin cifras, sin JV Market, grilla de
      proyectos sin hueco

## 5. Documentación (OBLIGATORIO)
- [x] 5.1 Specs sincronizadas (3 deltas + REMOVED de `proyecto-jvmarket`), `openspec validate --specs` verde

## 6. Cierre
- [x] 6.1 Push a `main`, workflows en success, verificación en vivo, archivar
