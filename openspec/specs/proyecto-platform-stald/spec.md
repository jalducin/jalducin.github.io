# proyecto-platform-stald Specification

## Purpose
TBD - created by archiving change portafolio-claridad. Update Purpose after archive.
## Requirements
### Requirement: Card de platform-STALD como proyecto principal
La sección de proyectos destacados SHALL mostrar primero una card **platform-STALD** que la presente como
plataforma educativa construida con SDD y agentes de IA (subagentes revisor y verificador, skills, hook
PreToolUse), con cifras verificables (+250 PRs, +85 cambios OpenSpec, pruebas en CI + E2E), su stack (Deno
Deploy, TypeScript, Supabase, JS vanilla) y enlace a `https://github.com/jalducin/platform-STALD`, en EN (DOM) y
ES (`#i18n-es`).

#### Scenario: STALD es el primer proyecto
- **WHEN** un visitante abre la sección de proyectos destacados
- **THEN** la primera card es platform-STALD, con enlace al repo y su texto traducido al cambiar a ES

#### Scenario: Sin datos de menores
- **WHEN** se revisa la card y la entrada del chatbot
- **THEN** no contienen nombres, correos, capturas ni conteos de alumnos, ni el repo privado de datos

### Requirement: Pyzzeria retirado del sitio
`index.html` y la base del chatbot NO SHALL mostrar Pyzzeria ni enlazar a su demo de CloudFront. El post
`blog/deep-dive-pyzzeria.html` MAY conservarse como artículo técnico con un aviso de demo retirada.

#### Scenario: Sin demo muerta
- **WHEN** se busca `cloudfront.net` en `index.html`, `assistant/knowledge.md` y `blog/`
- **THEN** no hay enlaces a la demo de Pyzzeria

