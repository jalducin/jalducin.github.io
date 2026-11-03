## Why

El Sprint 1 (`cv-claridad`, ya en `main`) dejó el CV y `llms.txt` alineados, pero el sitio y el chatbot siguen
mostrando Pyzzeria (demo de CloudFront borrada), Fidello como "Pilot · cloud beta" y no mencionan platform-STALD,
la mejor evidencia de agentic engineering. El sitio debe decir lo mismo que el CV.

## What Changes

- `index.html`: card de **platform-STALD** como primer proyecto; Fidello sin badge de piloto; **se retira
  Pyzzeria** (card, terminal, palette, metadatos); titular, metadatos y certificaciones iguales al CV; Deno Deploy
  y Claude Code (subagents, skills, hooks, MCP) en el nivel Build.
- `assistant/knowledge.md` → recompilado al bloque `assistant-kb`: entrada de STALD, sin Pyzzeria, Fidello sin piloto.
- Blog: `deep-dive-pyzzeria.html` se conserva como artículo técnico con aviso de demo retirada y sin enlaces a
  la demo; los demás posts dejan de enlazarla.
- `scripts/i18n/audit_i18n.py`: checks actualizados a las reglas nuevas.
- Sin cambios de diseño (matrix, terminal, palette y chatbot se quedan; decisión pendiente del propietario).

## Capabilities

### New Capabilities
- `proyecto-platform-stald`: card de platform-STALD como proyecto principal, sin datos de alumnos; Pyzzeria retirado.

### Modified Capabilities
- `proyecto-fidello`: deja de ser "proyecto estrella / piloto en beta"; segundo lugar y sin estado de piloto.
- `skills-y-formacion`: certificaciones iguales a las del CV (Anthropic Academy, Vanderbilt, AWS Bedrock).

## Impact

`index.html`, `assistant/knowledge.md`, `blog/*.html`, `scripts/i18n/audit_i18n.py`, `CLAUDE.md`. Sin dependencias.
