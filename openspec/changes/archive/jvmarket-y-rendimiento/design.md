## Context

`index.html` (estático, S3+CloudFront) ya tiene tabs, terminal, asistente IA y paleta café. El proyecto
e-commerce se renombró a **JV Market** y está desplegado en AWS. La card actual dice "MetalShop · práctica WIP".

## Decisions

- **JV Market:** card del portafolio y entrada del CV reescritas: e-commerce full-stack **en producción en
  AWS**. Stack: FastAPI · JWT (python-jose/bcrypt) · SQLite (dev)/PostgreSQL (prod) · AWS Lambda + API
  Gateway (SAM) · frontend S3+CloudFront. Enlaces: **Live Demo** = `https://d3rw1q49m6mvnq.cloudfront.net/`,
  **API docs** = `https://cizs8fa7lf.execute-api.us-east-2.amazonaws.com/dev/api/docs`. Se quita el badge
  "práctica WIP" (ahora está desplegado). Repo sigue `jalducin/EcommerceJVAV` (privado/seed) — no se enlaza si no es público.
- **Rendimiento:** (1) `preconnect` + `dns-prefetch` a `cdn.jsdelivr.net`; (2) `loading="lazy"` +
  `decoding="async"` + width/height en `<img>` de iconos; (3) matrix: en el loop, si `document.hidden` no
  pintar (o pausar el intervalo y reanudar con `visibilitychange`). Self-host de iconos y minify quedan como
  futuro (no rompen nada, pero añaden scope).

## Risks / Trade-offs

- [Riesgo] El admin dashboard puede requerir login → enlazar el **storefront** (root) como demo, no /admin.
- [Riesgo] Dejar alguna mención "MetalShop" → grep final debe quedar en 0 (fuera de historial/archive).
- Self-host de iconos eliminaría jsdelivr por completo (mejor), pero faltan SVGs (django/mongodb/github) →
  diferido; por ahora preconnect mitiga.

## Migration Plan
1. Branch. 2. Actualizar contenido JV Market + regenerar CV. 3. Performance. 4. Verificar (links 200, grep
MetalShop=0, render). 5. Commit → push → CI/CD despliega. 6. Archivar.
