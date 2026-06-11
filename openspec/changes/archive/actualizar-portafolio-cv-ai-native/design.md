## Context

El portafolio es un sitio estático single-page (`index.html`) en GitHub Pages, sin build step ni
dependencias. La fuente de verdad del contenido es `CV_JuanValentinAlducin.pdf`, que se actualizó con un
reposicionamiento AI-native. Restricciones del proyecto (`docs/frontend-standards.md`): HTML5/CSS3/JS
Vanilla, CSS en `<style>` y JS en `<script>` embebidos, paleta fija, responsive en 992/768/480px, sin
frameworks ni npm. El idioma del sitio se mantiene en **inglés** (decisión del propietario), traduciendo
el contenido nuevo del CV (que es español-first).

Datos canónicos detectados como obsoletos en la documentación (a corregir en este cambio):
`CLAUDE.md` y `docs/frontend-standards.md` listan WhatsApp `+52 5643540747` (el sitio ya usa
`525640800494`) e inglés `A2` (el CV/sitio ya indican `B1`).

## Goals / Non-Goals

**Goals:**
- Sincronizar `index.html` con el CV vigente (posicionamiento, experiencia, skills, formación).
- Añadir Fidello como proyecto estrella y conservar Enkoth como hito de producción.
- Reforzar el posicionamiento agentic con metodología visible + capa machine-readable (JSON-LD, llms.txt)
  + badges de métricas, sin romper el diseño.
- Dejar la documentación del proyecto consistente con la fuente de verdad (sin datos obsoletos).

**Non-Goals:**
- No se migra el sitio a español ni se añade toggle ES/EN (decisión: mantener inglés).
- No se modifica el PDF del CV (es la fuente de verdad; se actualiza manualmente).
- No se introducen frameworks, dependencias npm, archivos `.css`/`.js` externos ni build step.
- No se rediseña la estética matrix/binario ni la paleta.

## Decisions

- **Idioma: inglés.** El contenido nuevo del CV (español) se traduce a inglés para mantener consistencia
  con el sitio actual. *Alternativa descartada*: bilingüe con toggle (mayor complejidad, no solicitada).
- **Enkoth se conserva.** Aunque el CV de una página lo omitió, llegó a producción y es un hito de
  aprendizaje agentic; se mantiene en experiencia Podemos y como card de proyecto, reencuadrado como
  "shipped to production". *Alternativa descartada*: alinear 1:1 con el CV eliminándolo.
- **Fidello sin botón de código si el repo es privado.** Igual que Enkoth, se evita un enlace roto;
  el botón "View Code" se añade solo si existe repo público.
- **JSON-LD inline en `<head>`.** Un único `<script type="application/ld+json">` de tipo Person; sin
  librerías. *Alternativa descartada*: microdata inline en el HTML (más ruidoso y frágil).
- **`llms.txt` como archivo estático en la raíz.** Texto/Markdown breve derivado de la misma información;
  el sitio, el JSON-LD y `llms.txt` comparten una sola fuente de verdad por dato (los demás enlazan).
- **Badges con estilos existentes.** Reutilizar `.tl-badge`/`.card-badge`/`.soft-list`; no crear un
  sistema de componentes nuevo.
- **Sección "How I build with AI" como nueva `<section>`** con su entrada en el `nav`, siguiendo el
  patrón `fade-in` e `IntersectionObserver` ya presentes.
- **Corrección de datos canónicos** (WhatsApp, inglés) en `CLAUDE.md` y `docs/frontend-standards.md`
  dentro de este mismo cambio (regla de consistencia documental, base-standards §6).

## Risks / Trade-offs

- **Métricas no verificables externamente (40% / 80% / <15 min)** → Se presentan tal como en el CV del
  propietario; no se inflan ni inventan. Si el propietario las ajusta en el CV, se sincronizan aquí.
- **Inconsistencia CV (1 página) vs sitio (más amplio)** → Aceptada y explícita: el sitio es un superset
  curado del CV (mantiene Enkoth/MetalShop/Inventarios/socket-chat). Documentado para evitar "drift".
- **Duplicación de datos entre `index.html`, JSON-LD y `llms.txt`** → Riesgo de desincronización futura;
  se mitiga listando en `tasks.md` la verificación cruzada y declarando una fuente de verdad por dato.
- **`llms.txt` es una convención emergente, no un estándar formal** → Bajo costo/alto upside para el
  statement agentic; si cambia la convención, es un archivo trivial de actualizar.
- **Cambios de títulos de roles** → Es un cambio de contenido visible; no afecta anclas de navegación
  (los `id` de sección no cambian).

## Migration Plan

1. Crear `feature/actualizar-portafolio-cv-ai-native` desde `main`.
2. Implementar por capability (ver `tasks.md`), verificando responsive tras cada bloque visual.
3. Verificación manual en navegador (3 breakpoints) + validación de JSON-LD y `llms.txt`.
4. Actualizar documentación (corrección de datos canónicos) en el mismo PR.
5. Merge a `main` → GitHub Pages publica automáticamente. *Rollback*: revertir el commit de merge
   (sitio estático, sin estado ni migraciones).

## Open Questions

- **¿Existe repositorio público de Fidello** para enlazar "View Code", o se omite el botón? (Default:
  omitir hasta que haya repo público.)
- **¿Confirmar el título exacto del rol Podemos** en el sitio: "Backend Support Engineer & IA Specialist"
  (literal del CV) o conservar el matiz "Support & Automation"? (Default: usar el del CV.)
- **¿Se retira "Understanding the World Through Data · edX"** del sitio (no está en el CV) o se conserva
  por ser verídica? (Default: conservar si es verídica.)
