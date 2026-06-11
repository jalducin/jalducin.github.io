# Capability: proyecto-fidello

## Requirements

### Requirement: Card de proyecto estrella Fidello

La sección de proyectos destacados SHALL incluir una card para **Fidello — Loyalty Card System** como
proyecto estrella AI-native, posicionada de forma prominente (primera o entre las primeras), con el
contenido del CV vigente.

#### Scenario: Fidello aparece como proyecto destacado con su descripción
- **WHEN** un visitante navega a la sección de proyectos destacados
- **THEN** existe una card con título "Fidello — Loyalty Card System"
- **AND** la descripción comunica: sistema multi-negocio de tarjetas de fidelidad digital, gestión de
  puntos y roles diferenciados (Owner, Manager, Employee), mobile-first vía QR sin instalación
- **AND** menciona los elementos de seguridad: autenticación JWT, WebSockets en tiempo real, RLS
  multi-tenant y QR tokens con TTL 60s + fingerprint SHA-256 contra replay attacks
- **AND** indica que fue desarrollado 100% bajo Spec-Driven Development (SDD/OpenSpec)

#### Scenario: Stack de Fidello visible
- **WHEN** se lee la sección técnica (`.tech`) de la card de Fidello
- **THEN** se listan: React 18, TypeScript 5.5, Vite, Tailwind CSS, Supabase (PostgreSQL + Auth +
  PostgREST + Realtime), PL/pgSQL, Edge Functions (Deno) y Vitest

#### Scenario: Card coherente con el sistema de diseño existente
- **WHEN** se renderiza la card de Fidello
- **THEN** reutiliza las clases `.card`, `.card-badge`, `.tech` y (si aplica) `.btn` existentes
- **AND** respeta la paleta de colores (`docs/frontend-standards.md` §2) sin estilos nuevos ad hoc
- **AND** se mantiene el layout responsive de la grilla de proyectos en 992/768/480px

#### Scenario: Enlace de repositorio condicional
- **WHEN** la card incluye un enlace "View Code"
- **THEN** apunta al repositorio público de Fidello si existe; si el repo es privado o aún no público,
  la card se muestra sin botón de código (igual que Enkoth) en lugar de un enlace roto
