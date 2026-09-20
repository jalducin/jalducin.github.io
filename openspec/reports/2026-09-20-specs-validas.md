# Reporte — Specs válidas (`openspec validate --specs`)

- Fecha: 2026-09-20
- Rama: `feature/specs-validas`
- Agente: Claude (general-purpose, worktree aislado)
- Alcance: `openspec/specs/*/spec.md` (20 capabilities), `openspec/schemas/spec-driven/`, `docs/documentation-standards.md`

## Problema

`openspec validate --specs` fallaba en las 20 specs principales (`openspec/specs/*/spec.md`) — no 19 como se
estimó inicialmente, el repo tiene 20 carpetas de capability — con:

```
Spec must have a Purpose section. Missing required sections. Expected headers: "## Purpose" and "## Requirements".
```

Causa raíz: al archivar los cambios que crearon estas capabilities, los `spec.md` principales quedaron sin
`## Purpose`. El template de spec delta en `openspec/schemas/spec-driven/templates/spec.md` tampoco incluía
esa sección, así que cualquier capability nueva creada a partir de él repetiría el mismo problema.

## Diagnóstico adicional (más allá de "falta Purpose")

Al corregir el primer archivo (`cv-presentacion`) se descubrieron dos clases de error adicionales que el
validador reporta *después* de resolver el error de Purpose (aparentemente reporta un solo error a la vez
en estos casos), agnósticas del contenido:

1. **5 archivos** conservaban el encabezado de spec delta (`## ADDED Requirements` / `## MODIFIED
   Requirements`) en vez de `## Requirements` en el spec principal — probablemente copiados directo del
   `specs/<capability>/spec.md` de un `change/` sin pasar por el merge de `openspec archive`. El validador
   **no** reconoce esos encabezados como la sección Requirements: `proyecto-monitoreo-cloud`,
   `proyecto-voltgrid`, `proyecto-trackion`, `seccion-writing`, `cv-presentacion` (este último además tenía
   `# Capability: cv-presentacion (delta)` en el título).
2. **13 requirements** en 6 archivos usaban únicamente "DEBE/DEBEN" (español) sin la palabra clave literal
   `SHALL`/`MUST` que exige el validador: `cv-descarga-multidioma` (3), `proyecto-trackion` (1),
   `cv-presentacion` (2), `seccion-writing` (5), `proyecto-monitoreo-cloud` (1), `proyecto-voltgrid` (1).

Verificado con `openspec validate --specs --strict` y grep dirigido que **no** hay otros errores de formato
(headers `###`/`####` correctos en las 20 specs — 93 escenarios, todos con `#### Scenario:` exacto; ningún
`### Scenario` con 3 hashtags).

## Cambios aplicados

Por cada uno de los 20 `openspec/specs/<capability>/spec.md`:

- Se agregó `## Purpose` (título en inglés por requisito del validador; cuerpo en español, 1–3 líneas)
  inmediatamente después de `# Capability: …` y antes de `## Requirements`, derivado del contenido real de
  los requirements de cada spec (qué garantiza y para quién). Ningún requirement ni scenario cambió de
  contenido.
- En los 5 archivos con encabezado delta, se renombró `## ADDED/MODIFIED Requirements` → `## Requirements`
  (cambio mínimo de encabezado, sin tocar requirements/escenarios). En `cv-presentacion` también se quitó el
  sufijo `(delta)` del título de capability.
- En los 6 archivos con "DEBE/DEBEN" sin SHALL/MUST, se sustituyó la palabra por `SHALL` en la frase
  normativa del requirement (mismo patrón ya usado en el resto del repo, p. ej. "El sitio ... SHALL
  presentar"). No se tocó ningún scenario ni el resto del texto.

Template y config:

- `openspec/schemas/spec-driven/templates/spec.md`: se agregó una sección `## Purpose` (con comentario guía)
  antes de `## ADDED Requirements`, y una nota recordando usar SHALL/MUST en el texto del requirement.
- `openspec/schemas/spec-driven/schema.yaml` (artifact `specs`): se agregó instrucción explícita de incluir
  `## Purpose` en capabilities nuevas (se copia tal cual al spec principal al archivar) y una aclaración de
  que "debe/deben" en español no basta — el validador exige la palabra clave en inglés.
- `docs/documentation-standards.md`: nueva sección "Artefactos OpenSpec" documentando que cada spec principal
  lleva `## Purpose` + `## Requirements`, requirements con SHALL/MUST y scenarios con `####`, validados con
  `openspec validate --specs`.

Validado: `openspec schema validate spec-driven` → `✓ Schema 'spec-driven' is valid`.

## Comandos ejecutados

- `openspec validate --specs --json` (diagnóstico inicial y por archivo)
- `openspec validate <capability> --type spec --json` (iterativo, por archivo, durante las correcciones)
- `openspec validate --specs` / `openspec validate --specs --strict`
- `openspec validate --changes --json` (antes y después, para detectar regresión)
- `openspec schema validate spec-driven`
- `git diff --stat`

## Resultado — `openspec validate --specs`

Antes:

```
Totals: 0 passed, 20 failed (20 items)
```

Después:

```
- Validating...
✓ spec/agentic-engineering-hardening
✓ spec/cv-descarga-multidioma
✓ spec/cv-presentacion
✓ spec/experiencia-actualizada
✓ spec/hosting-aws-tier0
✓ spec/idioma-portafolio
✓ spec/navegacion-por-secciones
✓ spec/paleta-azul-metalico
✓ spec/posicionamiento-ai-native
✓ spec/principios-de-trabajo
✓ spec/proyecto-fidello
✓ spec/proyecto-jvmarket
✓ spec/proyecto-monitoreo-cloud
✓ spec/proyecto-trackion
✓ spec/proyecto-voltgrid
✓ spec/rendimiento-portafolio
✓ spec/seccion-writing
✓ spec/skills-y-formacion
✓ spec/stack-por-niveles
✓ spec/terminal-interactiva
Totals: 20 passed, 0 failed (20 items)
```

`openspec validate --specs --strict` → mismo resultado, `20 passed, 0 failed`.

## Resultado — `openspec validate --changes` (no debe empeorar)

Antes y después, sin cambios:

```
✓ change/asistente-ia-portafolio
✓ change/mejoras-portafolio-ai-native
Totals: 2 passed, 0 failed (2 items)
```

## `git diff --stat`

```
 docs/documentation-standards.md                      |  6 ++++++
 openspec/schemas/spec-driven/schema.yaml             | 13 ++++++++++++-
 openspec/schemas/spec-driven/templates/spec.md       |  8 +++++++-
 openspec/specs/agentic-engineering-hardening/spec.md |  6 ++++++
 openspec/specs/cv-descarga-multidioma/spec.md        | 11 ++++++++---
 openspec/specs/cv-presentacion/spec.md               | 14 ++++++++++----
 openspec/specs/experiencia-actualizada/spec.md       |  6 ++++++
 openspec/specs/hosting-aws-tier0/spec.md             |  5 +++++
 openspec/specs/idioma-portafolio/spec.md             |  5 +++++
 openspec/specs/navegacion-por-secciones/spec.md      |  5 +++++
 openspec/specs/paleta-azul-metalico/spec.md          |  5 +++++
 openspec/specs/posicionamiento-ai-native/spec.md     |  6 ++++++
 openspec/specs/principios-de-trabajo/spec.md         |  5 +++++
 openspec/specs/proyecto-fidello/spec.md              |  6 ++++++
 openspec/specs/proyecto-jvmarket/spec.md             |  5 +++++
 openspec/specs/proyecto-monitoreo-cloud/spec.md      |  9 +++++++--
 openspec/specs/proyecto-trackion/spec.md             |  9 +++++++--
 openspec/specs/proyecto-voltgrid/spec.md             |  9 +++++++--
 openspec/specs/rendimiento-portafolio/spec.md        |  5 +++++
 openspec/specs/seccion-writing/spec.md               | 18 ++++++++++++------
 openspec/specs/skills-y-formacion/spec.md            |  5 +++++
 openspec/specs/stack-por-niveles/spec.md             |  5 +++++
 openspec/specs/terminal-interactiva/spec.md          |  5 +++++
 23 files changed, 150 insertions(+), 21 deletions(-)
```

## Fuera de alcance (no tocado)

- `index.html`, `cv/`, `llms.txt` y cualquier archivo fuera de `openspec/specs/`, `openspec/schemas/`,
  `docs/` y este reporte.
- `terminal-interactiva/spec.md` menciona "respeta la paleta café/ámbar" en un scenario, contenido obsoleto
  frente a `paleta-azul-metalico` (que sustituyó la paleta café por azul metálico). No se tocó porque el
  validador no lo señala como error de formato y la tarea pedía no modificar contenido de
  requirements/scenarios salvo lo estrictamente necesario para pasar el validador.
