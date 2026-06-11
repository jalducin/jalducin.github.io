## Context

El portafolio (`index.html`) es estático en GitHub Pages, vanilla, sin build step (ver
`docs/frontend-standards.md`). Ya está alineado al posicionamiento AI-native y con capa machine-readable
(JSON-LD, `llms.txt`). Este cambio agrupa mejoras de alto impacto inspiradas en portafolios top de AI/backend
engineers, para implementarse de forma incremental. La única pieza que requiere backend es el asistente IA.

## Goals / Non-Goals

**Goals:**
- Cerrar el bug del formulario de contacto (placeholder Formspree).
- Subir credibilidad (case study SDD, deep-dives con arquitectura, métricas con procedencia) y
  descubribilidad (SEO, social card, a11y).
- Demostrar el perfil agentic con el asistente IA "Ask my portfolio".
- Mantener las restricciones del proyecto (vanilla, sin frameworks/npm, responsive).

**Non-Goals:**
- No migrar a un framework ni añadir build step para las piezas estáticas.
- No exponer claves de API en el front.
- No implementar todo de golpe: cada capability se implementa y verifica por separado.

## Decisions

- **Asistente IA con proxy serverless (AWS Lambda) → Claude.** Es el terreno del propietario y mantiene la
  API key fuera del front. Base de conocimiento = `llms.txt` (cabe en contexto; RAG opcional más adelante).
  *Alternativa descartada*: llamar al LLM desde el front (expondría la key) o un bot 100% estático con
  respuestas fijas (no es realmente agentic).
- **Social card e og:image vía Chrome-headless**, reutilizando el pipeline ya montado para el CV
  (`cv/build.ps1`). Sin servicios de terceros en runtime.
- **Diagramas de arquitectura como SVG** (pre-renderizados, p. ej. desde Mermaid a SVG) para no añadir JS
  de librerías al sitio.
- **Command palette en vanilla JS** (~paleta tipo Cmd+K), reutilizando estilos y paleta existentes.
- **Contacto**: conectar Formspree con ID real (mínimo cambio) y reforzar CTAs (copiar email, WhatsApp,
  LinkedIn). *Alternativa*: endpoint propio en Lambda (más control, más trabajo).
- **MetalShop**: proyecto de práctica personal; se mejorará aplicando **SDD y buenas prácticas** y se
  planea desplegar en AWS. Se refleja así en el CV y en la card del sitio (coherente con la marca).
- **Implementación incremental**: orden por ROI (contacto → og/seo/a11y → command palette → asistente IA →
  case study → deep-dives).

## Risks / Trade-offs

- **Costo/abuso del asistente IA** → rate-limit + caché de preguntas frecuentes + tope de presupuesto;
  degradar con CTAs si se supera el límite.
- **Privacidad de la key** → nunca en el front; solo en el entorno de la Lambda.
- **Duplicación de datos del perfil** (index.html, llms.txt, JSON-LD, CV) → una fuente de verdad por dato;
  el asistente lee de `llms.txt` para no contradecir.
- **Peso/rendimiento** de diagramas e interacciones → usar SVG ligero y respetar `prefers-reduced-motion`.

## Migration Plan

1. Implementar por capability en ramas `feature/<capability>` (cada una con sus pasos obligatorios).
2. Verificación manual en navegador (3 breakpoints) + Lighthouse donde aplique; el asistente IA se prueba
   contra su endpoint de staging antes de exponerlo.
3. Merge incremental a `main` → GitHub Pages publica. Rollback = revertir el commit de la capability.

## Open Questions

- ¿Endpoint del asistente IA: Lambda Function URL, API Gateway, o servicio gestionado? (Default: Lambda
  Function URL con rate-limit.)
- ¿Modelo para el asistente: Haiku (barato) por defecto, Sonnet para respuestas más ricas? (Default: Haiku.)
- ¿Case study sobre un cambio archivado fijo o el último archivado dinámicamente? (Default: uno fijo curado.)
- ¿Deep-dives como secciones en `index.html` o páginas separadas `/projects/<slug>.html`? (Default: páginas.)
