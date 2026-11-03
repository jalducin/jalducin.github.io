## Why

El CV se volvió denso: titular con cuatro roles, ~70 tecnologías en 10 categorías, 6 proyectos y hoja Oficio
llena a 8.5pt. Un reclutador (humano o ATS) no identifica la fortaleza principal en 10 segundos, y hoy cualquiera
puede listar buzzwords de IA; lo que distingue es la **evidencia verificable**. Además, el CV afirma cosas que ya
no son vigentes (Fidello como "piloto en beta con cafeterías reales", Pyzzeria como "Live Demo" cuya URL de
CloudFront ya no responde) y omite la mejor evidencia de agentic engineering del propietario: **platform-STALD**.

Es el Sprint 1 de tres (CV → portafolio → LinkedIn): el CV y `llms.txt` fijan el mensaje del que derivan los
otros dos.

## What Changes

- **`llms.txt` primero** (fuente de verdad del perfil): titular, resumen corto, platform-STALD como
  proyecto, Fidello sin afirmar piloto activo, Pyzzeria retirado.
- **BREAKING (formato)**: el CV y sus PDFs pasan de **Oficio (216×340 mm) a A4 (210×297 mm)**, 1 página.
- Titular híbrido acordado el 2026-09-20 (`Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI`),
  idéntico en CV ES/EN y `llms.txt` (hoy `llms.txt` usa otra variante), y resumen de ≤ 2 líneas (≤ ~300 caracteres).
- Experiencia acotada: ≤ 4 bullets en el rol actual, ≤ 2 en cada rol previo, 1 en Softtek; se quitan líneas
  de "Stack:" redundantes con Habilidades.
- Habilidades: de 10 categorías a **5** (Backend, Cloud & Serverless, Datos, SRE & Automatización, IA aplicada),
  solo tecnologías con evidencia en el inventario `#hard-skills`. Las soft skills salen de la lista.
- Proyectos: **3 destacados** (platform-STALD, Fidello, Monitoreo-Cloud), cada uno con enlace y una cifra
  verificable, más una línea "Otros" (VoltGrid, Trackion, dataMasterGK). **Se retira Pyzzeria.**
- Formación agrupada: 1 línea de Anthropic Academy (Claude Code in Action · Intro to MCP · Agent Skills ·
  Subagents) + Vanderbilt (Claude Code) + AWS (Bedrock). "Claude Code 101" no se lista (lo cubre "in Action").
- Unificar el nombre del rol: **"AI Specialist"** en ambos idiomas (no "IA Specialist").
- platform-STALD se describe sin nombres, datos ni capturas de alumnos (usuarios menores de edad).
- Regenerar ambos PDFs con `cv/build.ps1` (A4) y sincronizar el borrador `cv/CV_JuanValentinAlducin.md`.

## Capabilities

### New Capabilities
- `cv-contenido-claro`: reglas de contenido del CV — titular único, límites de extensión por sección,
  taxonomía de 5 categorías con evidencia, 3 proyectos con enlace verificable, formación agrupada, solo
  afirmaciones vigentes y privacidad de usuarios menores en platform-STALD.

### Modified Capabilities
- `cv-presentacion`: el CV cabe en **1 página A4** (antes Oficio); la regla de cabida pasa a altura del
  `.sheet` ≤ 297 mm y el build genera PDFs A4.

## Impact

- Archivos: `llms.txt`, `cv/cv.html`, `cv/cv-en.html`, `cv/CV_JuanValentinAlducin.md`, `cv/build.ps1`
  (comentario de tamaño), PDFs `cv/CV_JuanValentinAlducin.pdf` y `_EN.pdf`.
- Docs: `CLAUDE.md` (sección PDF del CV y tabla de proyectos), `docs/frontend-standards.md` (tamaño Oficio →
  A4), `cv/README.md`.
- **Fuera de alcance (Sprint 2)**: `index.html`, `assistant/knowledge.md` y el blog. Al cambiar `llms.txt`, el
  sitio y el chatbot quedan temporalmente desalineados (siguen mostrando Pyzzeria y el titular anterior) hasta
  el cambio `portafolio-claridad`. Las specs `proyecto-fidello`, `posicionamiento-ai-native` y
  `skills-y-formacion` se ajustan en ese sprint.
- Sin dependencias nuevas. El PDF EN modificado sin commitear (28 KB, build roto del 2026-10-14) se descarta y
  se regenera.
