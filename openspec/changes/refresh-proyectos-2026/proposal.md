# Proposal — refresh-proyectos-2026

## Why

El portafolio y el CV deben reflejar el set de proyectos vigente de Juan Valentin:

- **Enkoth** no se terminó como producto; debe dejar de presentarse como proyecto destacado
  "shipped to production" y reducirse a una **mención ligera** dentro del rol actual en Podemos Progresar.
- Dos proyectos quedaron **obsoletos** para la narrativa AI-native / AWS serverless y se retiran del
  portafolio: **Inventarios** (Java/Spring Boot) y **socket-chat** (Node/WebSocket).
- Entran **tres proyectos nuevos** que sustituyen a Enkoth y amplían las skills demostrables:
  - **VoltGrid** — SaaS multi-tenant white-label para operadores de carga de autos eléctricos.
  - **Trackion** — mesa de ayuda serverless white-label con módulo de integración de APIs abierto.
  - **Monitoreo-Cloud** — pipeline de observabilidad AWS Free Tier (CloudWatch → n8n → PostgreSQL → Grafana).
- Los nuevos proyectos **suman skills** que hoy no están visibles: **Next.js 14**, **Kubernetes (Kustomize)**,
  **Grafana (observabilidad)**, **n8n** (visible en CV), **SSO/OIDC**, **SQLAlchemy 2.0 async**, RLS multi-tenant.

## What changes

- **index.html** (portafolio):
  - Quitar las cards de **Enkoth**, **Inventarios** y **socket-chat**.
  - Agregar cards de **VoltGrid**, **Trackion** y **Monitoreo-Cloud** con stack real y enlaces.
  - Suavizar el bullet de **Enkoth** en la experiencia de Podemos (mención ligera, sin "shipped to production").
  - Hard Skills: agregar íconos **Next.js**, **Kubernetes**, **Grafana** y entradas en Tech Stack
    (Next.js 14, Kubernetes/Kustomize, Grafana, SSO/OIDC).
  - Terminal: actualizar `ls projects`.
- **cv/cv.html** (+ regenerar `cv/CV_JuanValentinAlducin.pdf`):
  - Demote de Enkoth a mención en experiencia; agregar los 3 proyectos compactando para mantener **1 página Oficio**.
  - Habilidades: agregar **n8n, Grafana, Kubernetes, Next.js, observabilidad**.
- **llms.txt**: actualizar Featured projects (quitar obsoletos, demote Enkoth, agregar 3) y Core stack.
- **CLAUDE.md** y **docs/frontend-standards.md**: actualizar tabla de proyectos destacados.

## Impact

- Specs afectadas: nuevas `proyecto-voltgrid`, `proyecto-trackion`, `proyecto-monitoreo-cloud`;
  modificadas `experiencia-actualizada` (Enkoth ligero) y `skills-y-formacion` (skills nuevas).
- Sin cambios de stack del sitio (HTML/CSS/JS vanilla). Sin dependencias nuevas.
- Despliegue automático vía CI/CD (push a `main` → GitHub Actions → AWS).
