# cv-contenido-claro Specification

## Purpose
TBD - created by archiving change cv-claridad. Update Purpose after archive.
## Requirements
### Requirement: Titular único y resumen breve
El CV (`cv/cv.html`, `cv/cv-en.html`) SHALL mostrar el **titular híbrido acordado** (decisión del 2026-09-20):
`Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI` — 3 bloques separados por `|` — y un
resumen de **≤ 300 caracteres** (≈ 2 líneas). El titular SHALL ser el mismo en ES y EN y coincidir con la línea
`Role:` de `llms.txt`.

#### Scenario: Titular consistente
- **WHEN** se compara el titular de `cv.html`, `cv-en.html` y la línea `Role:` de `llms.txt`
- **THEN** los tres son idénticos a `Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI`

#### Scenario: Resumen breve
- **WHEN** se mide el texto del resumen en cada idioma
- **THEN** tiene ≤ 300 caracteres

### Requirement: Experiencia acotada
La sección de experiencia SHALL limitar los bullets a: **≤ 4** en el rol actual, **≤ 2** en cada rol previo
(Podemos 2025–2026 y Redsis) y **1** en Softtek. Las líneas `Stack:` por rol SHALL eliminarse (la sección
Habilidades ya lista las tecnologías). Fechas, títulos de rol y empresas SHALL conservarse.

#### Scenario: Conteo de bullets por rol
- **WHEN** se cuentan los `<li>` de cada entrada de experiencia
- **THEN** el rol actual tiene ≤ 4, Podemos 2025–2026 ≤ 2, Redsis ≤ 2 y Softtek 1
- **AND** no hay elementos `.stack` dentro de la experiencia

#### Scenario: Nombre del rol unificado
- **WHEN** se busca el título del rol actual en `cv.html`, `cv-en.html` y `llms.txt`
- **THEN** aparece como `Service Support Tech Lead & AI Specialist` y no existe la cadena `IA Specialist`

### Requirement: Habilidades en 5 categorías con evidencia
La sección Habilidades SHALL tener **exactamente 5 categorías** — Backend, Cloud & Serverless, Datos,
SRE & Automatización, IA aplicada (EN: Backend, Cloud & Serverless, Data, SRE & Automation, Applied AI) — y
listar solo tecnologías presentes en los niveles Own, Build u Operate del inventario de `llms.txt`. Las
tecnologías en *Learning* y las soft skills NO SHALL aparecer.

#### Scenario: Taxonomía
- **WHEN** se cuentan los bloques `.skill` del CV
- **THEN** hay 5, con los nombres de categoría indicados

#### Scenario: Solo tecnologías con evidencia
- **WHEN** se cruza cada tecnología listada contra el inventario Own/Build/Operate de `llms.txt`
- **THEN** todas aparecen en ese inventario y ninguna está en *Learning*

### Requirement: Tres proyectos destacados con evidencia verificable
La sección Proyectos SHALL mostrar **3 proyectos destacados**, en este orden: **platform-STALD**, **Fidello** y
**Monitoreo-Cloud**. Cada uno lleva una descripción de ≤ 2 líneas, al menos una cifra verificable (pruebas,
PRs, cambios OpenSpec, fuentes) y su enlace (repo o deep dive) como texto. Una línea final "Otros" SHALL
nombrar VoltGrid, Trackion y dataMasterGK con su enlace de GitHub. Pyzzeria NO SHALL aparecer.

#### Scenario: Proyectos y orden
- **WHEN** se lista `.ptitle` del CV
- **THEN** los títulos son platform-STALD, Fidello y Monitoreo-Cloud en ese orden
- **AND** existe una línea "Otros"/"Other" con VoltGrid, Trackion y dataMasterGK
- **AND** la cadena `Pyzzeria` no aparece en `cv.html`, `cv-en.html` ni `llms.txt`

#### Scenario: Cada proyecto tiene enlace y cifra
- **WHEN** se revisa cada proyecto destacado
- **THEN** incluye un enlace como texto y al menos un número verificable en su repositorio

### Requirement: Solo afirmaciones vigentes
El CV y `llms.txt` SHALL describir el estado de cada proyecto sin afirmar actividad que ya no es vigente. En
particular, Fidello NO SHALL presentarse como "piloto en beta", "cloud beta" ni "validado en cafeterías reales";
se describe por lo que se construyó. Ningún proyecto SHALL anunciar "Live Demo" si su URL no responde.

#### Scenario: Fidello sin estado de piloto activo
- **WHEN** se buscan en `cv.html`, `cv-en.html` y `llms.txt` las cadenas `beta`, `cafeterías reales`,
  `real coffee shops` y `Live Demo`
- **THEN** no hay coincidencias

### Requirement: Privacidad de platform-STALD
La descripción de platform-STALD SHALL presentarlo como plataforma educativa construida con SDD y agentes de
IA, sin nombres, correos, datos, capturas ni conteos de alumnos o alumnas (usuarios menores de edad), y sin
enlaces al repositorio privado de datos.

#### Scenario: Sin datos de menores
- **WHEN** se revisa el texto de platform-STALD en el CV y `llms.txt`
- **THEN** describe la arquitectura, el tooling de agentes (subagentes, skills, hooks) y cifras de ingeniería
  (commits/PRs, cambios OpenSpec, pruebas), y no contiene datos de personas ni el repo `platform-STALD-data`

### Requirement: Formación agrupada
La sección de cursos SHALL tener **≤ 3 líneas**: una para Anthropic Academy (Claude Code in Action · Intro to
MCP · Agent Skills · Subagents, 2026), una para Vanderbilt (Claude Code: Software Engineering with Generative
AI Agents, 2026) y una para AWS (Generative AI Applications with Amazon Bedrock, 2026).

#### Scenario: Cursos compactos
- **WHEN** se cuentan los bloques `.course`
- **THEN** son ≤ 3 y la línea de Anthropic nombra los 4 cursos indicados

### Requirement: llms.txt como fuente del mensaje
`llms.txt` SHALL actualizarse **antes** que el CV y reflejar el mismo titular, rol, proyectos (STALD agregado,
Pyzzeria retirado, Fidello sin estado de piloto activo) y formación, respetando la regla de privacidad del
empleador.

#### Scenario: Auditoría de privacidad del empleador
- **WHEN** se ejecuta `openspec/changes/archive/2026-09-19-cv-portafolio-sre-automation/scripts/audit.py`
- **THEN** no reporta nombres de sistemas internos, personas, IDs ni conteos de clientes en `llms.txt`,
  `cv.html` ni `cv-en.html`

