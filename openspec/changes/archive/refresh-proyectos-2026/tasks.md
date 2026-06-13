# Tasks — refresh-proyectos-2026

## Step 0 — Crear feature branch (SIEMPRE PRIMERO)
- [x] Crear y cambiar a `feature/refresh-proyectos-2026`.

## Step 1 — Portafolio (index.html)
- [x] Suavizar el bullet de Enkoth en la experiencia de Podemos (mención ligera, sin "shipped to production").
- [x] Quitar las cards de Enkoth, Inventarios y socket-chat.
- [x] Agregar cards de VoltGrid, Trackion (Live Demo) y Monitoreo-Cloud con stack real y enlaces.
- [x] Hard Skills: agregar íconos Next.js, Kubernetes, Grafana; entradas Next.js 14, Kubernetes (Kustomize), Grafana, SSO/OIDC.
- [x] Terminal: actualizar `ls projects`.

## Step 2 — CV (cv/cv.html) + PDF
- [x] Demote de Enkoth a mención en experiencia de Podemos.
- [x] Agregar VoltGrid, Trackion y Monitoreo-Cloud compactando descripciones para mantener 1 página Oficio.
- [x] Habilidades: agregar n8n, Grafana, Kubernetes, Next.js y observabilidad.
- [x] Regenerar `cv/CV_JuanValentinAlducin.pdf` con Chrome/Edge headless.

## Step 3 — Fuentes de verdad
- [x] `llms.txt`: actualizar Featured projects (quitar obsoletos, demote Enkoth, agregar 3) y Core stack.
- [x] `CLAUDE.md` y `docs/frontend-standards.md`: actualizar tabla de proyectos destacados.

## Step 4 — Revisar y actualizar pruebas existentes (OBLIGATORIO)
- [x] El proyecto no tiene suite automatizada; la verificación es manual (frontend-standards §6). N/A pruebas unitarias.

## Step 5 — Ejecutar verificación y verificar estado (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] Verificar que no quedan referencias a Enkoth (card), Inventarios ni socket-chat en `index.html`.
- [x] Verificar que VoltGrid, Trackion y Monitoreo-Cloud están presentes en index.html, cv.html y llms.txt.
- [x] Regenerar PDF y verificar que el CV mantiene **1 página**.
- [x] Render del sitio (screenshot de la sección de proyectos) con paleta café.
- [x] Crear reporte en `specs/refresh-proyectos-2026/reports/AAAA-MM-DD-step-5-verificacion.md`.

## Step 6 — Verificación manual UI/frontend (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] Confirmar que las cards renderizan y los enlaces (View Code / Live Demo) apuntan a los repos/URLs correctos.
- [x] Revisar los tres breakpoints (992 / 768 / 480px) no se rompen con las nuevas cards.

## Step 7 — Actualizar documentación técnica (OBLIGATORIO)
- [x] Sincronizar CLAUDE.md y docs/frontend-standards.md con el set de proyectos vigente (0 enlaces rotos, fuente canónica única).

## Step 8 — Promover specs y archivar
- [x] Merge a main, promover specs nuevas/modificadas a `openspec/specs/`, archivar el cambio, push (CI/CD despliega).
