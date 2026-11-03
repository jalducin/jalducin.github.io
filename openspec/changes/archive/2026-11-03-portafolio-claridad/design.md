## Context

El sitio es un único `index.html` (EN en el DOM, ES en `#i18n-es`, base del chatbot en `#assistant-kb`
compilada desde `assistant/knowledge.md`). Fuente de verdad: `llms.txt` y `cv/cv-en.html` del Sprint 1.

## Decisions

1. **Trabajo en paralelo por archivos disjuntos**: un agente edita `index.html` (+ `audit_i18n.py`), otro
   `assistant/knowledge.md` y `blog/`; `build_kb.py` (que escribe en `index.html`) se corre al final, en serie.
2. **El post de Pyzzeria se conserva** con aviso de demo retirada: es contenido técnico válido y evita 404 en
   enlaces externos. Alternativa descartada: borrarlo.
3. **Sin rediseño visual** en este sprint (matrix/terminal/palette/chatbot se quedan): el objetivo es coherencia
   de contenido; simplificar la UI requiere decisión del propietario.
4. **Las cifras de STALD** son las del corte del 2026-11-02 (reporte de `cv-claridad`), redondeadas hacia abajo.

## Risks / Trade-offs

- [Dos agentes en el mismo árbol] → archivos disjuntos y QA final con `portfolio-qa-reviewer`.
- [Checks viejos en `audit_i18n.py`] → se actualizan a la regla nueva con comentario `# portafolio-claridad`.
