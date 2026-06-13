# Capability: proyecto-voltgrid

## ADDED Requirements

### Requirement: El portafolio y las fuentes de verdad presentan VoltGrid
El sitio (`index.html`), el CV (`cv/cv.html`) y `llms.txt` DEBEN presentar **VoltGrid** como plataforma
SaaS **multi-tenant white-label** para operadores de estaciones de carga de autos eléctricos, con datos reales.

#### Scenario: Card del portafolio
- **WHEN** un visitante abre la sección de proyectos
- **THEN** existe una card **"VoltGrid"** descrita como SaaS multi-tenant white-label para carga de EV
- **AND** menciona: tiempo real por **WebSocket** (fallback a polling), aislamiento por **Row Level Security (RLS)**
  de PostgreSQL, **RBAC** (superadmin/org_admin/operator/viewer) + **SSO (OIDC)**, analytics (uptime, kWh,
  export CSV), **scheduler** de estados auditable y **PWA** instalable; construido con SDD
- **AND** el stack visible incluye FastAPI · SQLAlchemy 2.0 async · asyncpg · Alembic · PostgreSQL 16 (RLS) ·
  Next.js 14 · TypeScript · Tailwind · WebSockets · Docker · Kubernetes (Kustomize) · GitHub Actions
- **AND** incluye enlace **View Code** a `https://github.com/jalducin/voltgrid`

#### Scenario: CV y llms.txt
- **WHEN** se revisa `cv/cv.html` (PDF regenerado) y `llms.txt`
- **THEN** VoltGrid aparece con descripción compacta y stack coherente, manteniendo el CV en **1 página Oficio**
