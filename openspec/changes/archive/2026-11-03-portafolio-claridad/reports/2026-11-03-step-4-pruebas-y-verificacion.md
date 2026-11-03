# Reporte Step 4 — Pruebas y verificación de estado

- Fecha: 2026-11-03
- Cambio: portafolio-claridad
- Agentes: orquestador + 3 subagentes (sitio, chatbot/blog, QA `portfolio-qa-reviewer`) y 2 más para la corrección
  "Podemos sin exagerar" pedida por el propietario a mitad del sprint.

## Comandos ejecutados
- `python scripts/i18n/build_dict.py` · `python scripts/assistant/build_kb.py`
- `python scripts/i18n/audit_i18n.py` · `python scripts/i18n/probe_i18n.py` · `python scripts/assistant/probe_kb.py`
- `python scripts/cv/check_cv.py` (tras regenerar los PDFs con `cv\build.ps1`)
- grep de frases exageradas y de `pyzzeria`/`cloudfront.net`

## Resultados
- audit_i18n 69/69 · probe_i18n 18/18 · probe_kb 18/18 (conteo de KB 21 → 23) · check_cv 0 fallas.
- 0 "built the post-mortem / defined the methodology / lidero / construí / definí / creé el sistema" en
  index.html, llms.txt, CV ES/EN, knowledge.md y docs/linkedin.
- 0 `pyzzeria` en index.html (incluye la KB del chatbot). `blog/deep-dive-pyzzeria.html` se conserva con aviso de
  demo retirada y sin enlace a CloudFront.
- QA (`portfolio-qa-reviewer`): FUNCIONAL; 0 anclas huérfanas, 0 assets faltantes, 0 errores de consola (EN, ES y
  5 posts); 6 cards sin desborde a 992/768/480/360 px. Nota baja: `sitemap.xml` sigue listando el post de Pyzzeria
  (se conserva a propósito: la página existe).

## Cambio de alcance (pedido del propietario, 2026-11-03)
La experiencia actual en Podemos se reescribió con su redacción: coordina (no lidera), participa en la
transformación de post-mortems, calcula el uptime con la metodología del liderazgo, automatiza parte de la
operación, desarrolla (en curso) el Skill de ruteo, participa en trenes coordinados por Ingeniería. Post-mortems y
uptime pasan de Own a Operate. Aplicado en CV ES/EN (+ PDFs), `llms.txt`, `index.html`, `knowledge.md` y LinkedIn.

## Verificación de estado
- No hay datos que mutar. Estado restaurado: N/A.

## Resultado
- Estado Step 4: PASS · Bloqueos: ninguno
