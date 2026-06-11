## Why

El CV en PDF (`CV_JuanValentinAlducin.pdf`) se actualizó y reposiciona a Juan Valentin como
**Senior Software Engineer | AI-native Development**: nuevas métricas de impacto (−40% en ciclo de
revisión, 80% de autoresolución de incidentes N1, respuesta <15 min), reordenamiento de experiencia
(Redsis pasa a *Software Engineer → Tech Lead*; Podemos a *Backend Support Engineer & IA Specialist*),
y un proyecto estrella nuevo (**Fidello**, 100% Spec-Driven Development). El portafolio
(`index.html`) quedó desfasado respecto a esta fuente de verdad. Además, varios documentos del proyecto
tienen datos obsoletos (WhatsApp e inglés). Aprovechamos para reforzar el posicionamiento de *agentic
engineer* haciendo que el propio sitio demuestre rigor AI-native.

## What Changes

- **Reposicionamiento del header y resumen** al mensaje *AI-native Development* del CV, con métricas reales.
- **Experiencia actualizada**: títulos, orden y bullets alineados al CV. Se **mantiene Enkoth** (llegó a
  producción; hito de aprendizaje agentic) y se reencuadra como tal. **BREAKING** de contenido: cambian
  títulos de roles visibles.
- **Nuevo proyecto estrella Fidello**: card destacada (loyalty multi-negocio, QR mobile-first, RLS
  multi-tenant, QR tokens TTL 60s + fingerprint SHA-256, Supabase, 100% SDD/OpenSpec).
- **Skills y formación**: taxonomía de skills alineada al CV (añadir EC2, CloudWatch, GCP, Supabase,
  SQL Server, Hana SQL, DynamoDB, OpenAI/Gemini API, Agentic Workflows, Prompt Engineering, LLM
  Integration); añadir formación *Inglés Avanzado — Quick Learning*; reconciliar certificaciones.
- **Hardening agentic** (recomendaciones aprobadas): sección *How I build with AI* con metodología SDD y
  métricas, datos estructurados **JSON-LD Schema.org Person**, **`llms.txt`** + meta AI-readable, y
  **badges de métricas** (40% / 80% / <15 min).
- **Corrección de datos obsoletos** en docs: WhatsApp `+52 5643540747 → 525640800494` e inglés `A2 → B1`
  en `CLAUDE.md` y `docs/frontend-standards.md`.

## Capabilities

### New Capabilities
- `posicionamiento-ai-native`: mensaje del header, tagline, resumen y metadatos sociales alineados al CV.
- `experiencia-actualizada`: títulos, orden, bullets y métricas de los tres roles, conservando Enkoth.
- `proyecto-fidello`: card del proyecto estrella Fidello en la sección de proyectos destacados.
- `skills-y-formacion`: taxonomía de skills, educación y certificaciones alineadas al CV.
- `agentic-engineering-hardening`: sección metodológica AI-native + capa machine-readable (JSON-LD,
  `llms.txt`, meta) + badges de métricas.

### Modified Capabilities
<!-- openspec/specs/ está vacío: no hay capabilities previas con requisitos a modificar. -->
(ninguna)

## Impact

- **Archivos de código**: `index.html` (único entregable del sitio; contenido, `<style>`, `<script>`,
  `<head>`), nuevo archivo estático `llms.txt`.
- **Documentación**: `CLAUDE.md`, `docs/frontend-standards.md` (corrección de datos canónicos),
  `README.md` (si cambia la descripción del portafolio).
- **Datos**: ninguno persistente (sitio estático). El PDF del CV no se modifica (es la fuente de verdad).
- **Despliegue**: GitHub Pages desde `main`; sin build step, sin dependencias nuevas.
- **Restricciones**: no romper responsive (992/768/480px), no añadir frameworks ni npm, CSS/JS embebidos.
