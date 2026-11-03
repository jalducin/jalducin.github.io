# Tasks — portafolio-claridad (Sprint 2)

## 0. Crear feature branch (SIEMPRE PRIMERO)
- [x] 0.1 Crear y cambiar a `feature/portafolio-claridad` desde `main` (con `cv-claridad` ya fusionado).

## 1. Sitio (index.html) — agente "sitio"
- [x] 1.1 Card de platform-STALD primero (EN + ES), sin datos de alumnos.
- [x] 1.2 Fidello sin badge ni texto de piloto; segundo lugar.
- [x] 1.3 Retirar Pyzzeria (card, terminal, palette, metadatos).
- [x] 1.4 Titular, metadatos, certificaciones y nivel Build alineados al CV.

## 2. Chatbot y blog — agente "chatbot y blog"
- [x] 2.1 `assistant/knowledge.md`: entrada STALD, sin Pyzzeria, Fidello sin piloto, certificaciones.
- [x] 2.2 `blog/deep-dive-pyzzeria.html` con aviso de demo retirada; otros posts sin enlaces a la demo.
- [x] 2.3 Recompilar `python scripts/assistant/build_kb.py` (en serie, después de 1.x).

## 3. Revisar y actualizar pruebas existentes (OBLIGATORIO)
- [x] 3.1 `scripts/i18n/audit_i18n.py`: checks a la regla nueva (Fidello sin Pilot, STALD presente, sin Pyzzeria).

## 4. Ejecutar pruebas y verificar estado (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] 4.1 `audit_i18n.py`, `probe_kb.py` y `scripts/cv/check_cv.py` en verde.
- [x] 4.2 grep: 0 `pyzzeria`/`cloudfront.net` en `index.html` y `knowledge.md`; ninguno enlazando la demo en `blog/`.
- [x] 4.3 Reporte en `reports/AAAA-MM-DD-step-4-pruebas-y-verificacion.md`.

## 5. Verificación manual (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] 5.1 Capturas a 1280/768/480 px de la sección de proyectos.
- [x] 5.2 Agente `portfolio-qa-reviewer`: enlaces, anclas, consola, comandos de terminal/palette.
- [x] 5.3 Chatbot responde sobre STALD y no menciona Pyzzeria (`probe_kb.py`).

## 6. Actualizar documentación técnica (OBLIGATORIO)
- [x] 6.1 `CLAUDE.md`: estado del sitio alineado (STALD, Fidello, Pyzzeria retirado).
- [x] 6.2 0 enlaces rotos.
