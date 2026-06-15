# Tasks — blog-writing-y-mejoras

## Step 0 — Feature branch (PRIMERO)
- [x] `feature/blog-y-mejoras`.

## Step 1 — Self-host de íconos
- [x] Descargar 20 SVGs devicon a `assets/img/icons/`; reescribir `src` y quitar preconnect/dns-prefetch a jsdelivr.

## Step 2 — Blog "Writing"
- [x] Crear `blog/sdd-openspec.html`, `blog/docker-observability-local.html`, `blog/grafana-multi-source.html` (tema azul metálico + OG).
- [x] Sección/tab "Writing" en index.html: nav, GROUPS, cards, command palette y comandos terminal `writing`/`blog`.

## Step 3 — Mejoras UX
- [x] Spotlight de cursor (z-index:-1, prefers-reduced-motion / hover:none).
- [x] Bloque "Now" en How I Build with AI.
- [x] Easter egg `mundial`/`worldcup`; corregir texto del matrix (azul).

## Step 4 — CV doble QR
- [x] Generar `assets/img/QR-linkedin.png` (decodificación verificada).
- [x] Embeber mini QR LinkedIn en cv.html y cv-en.html; regenerar PDFs (1 página).

## Step 5 — Fuentes de verdad
- [x] `llms.txt` (sección Writing) y `docs/frontend-standards.md` (blog + íconos self-host).

## Step 6 — Verificación (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] Render del tab Writing + una página de blog + spotlight (Chrome headless).
- [x] Verificar 1 página en ambos CVs y QR LinkedIn decodificable.
- [x] Reporte en `specs/blog-writing-y-mejoras/reports/AAAA-MM-DD-verificacion.md`.

## Step 7 — Revisión de diseño (design-specialist) — OBLIGATORIO
- [x] Render + crítica de la sección Writing, páginas de blog y spotlight (contraste AA, consistencia).

## Step 8 — Validación de contenido (compliance-reviewer) — OBLIGATORIO
- [x] Barrido de secretos/credenciales, PII, claims, marcas/IP y licencias; aplicar fixes de alta confianza.

## Step 9 — Promover specs y archivar
- [x] Merge a main, promover spec, archivar el cambio, push (CI/CD).
