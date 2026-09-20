# Design: retirar-metricas-y-jvmarket

## Context
Cambio de contenido dirigido por el propietario; no hay decisión técnica nueva. Se aplica sobre `main` tras
mergear `feature/case-study-y-deep-dives` para evitar conflictos en `index.html`/`es.py`.

## Decisions
- D1. Las cifras se sustituyen por redacción cualitativa equivalente ("acortando el ciclo de revisión",
  "habilité la autoresolución en N1", "metodología de uptime/downtime por impacto real"); no se dejan huecos.
- D2. Se conservan los SLAs (<10 min / <2 h): el propietario no los mencionó y son compromisos, no porcentajes
  de mejora.
- D3. La tarjeta "Measurable impact" se renombra "Operational SLAs & practices" (EN) / "SLAs y prácticas
  operativas" (ES) y lista SLAs + 2 prácticas para no quedar con 2 líneas.
- D4. JV Market se elimina por completo (no se oculta); las claves i18n se retiran de `es.py` para que
  `build_dict.py` no reporte huérfanas.
- D5. `audit_i18n.py`: el check "uptime en badges/impacto" pasa a "sin cifras 40%/80%/99.95 en index, llms,
  CV y diccionario" y se añade "sin JV Market".

## Risks / Trade-offs
- [Perder gancho cuantitativo en el header] → los SLAs y las prácticas (post-mortems, uptime methodology,
  n8n) mantienen el mensaje; decisión del propietario.
