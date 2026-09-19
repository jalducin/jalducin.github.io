# Capability: proyecto-fidello (delta)

## MODIFIED Requirements

### Requirement: Card de proyecto estrella Fidello

La sección de proyectos destacados SHALL incluir una card para **Fidello — Loyalty Card System** como
proyecto estrella AI-native y **piloto en beta cloud**, posicionada de forma prominente (primera), con las
cifras de ingeniería reales del repositorio y el stack completo.

#### Scenario: Fidello aparece como piloto con su descripción
- **WHEN** un visitante navega a la sección de proyectos destacados
- **THEN** existe una card con título "Fidello — Loyalty Card System"
- **AND** los badges son "★ AI-native · 100% SDD" y "🧪 Pilot · cloud beta" (reemplaza "🚧 In active
  development")
- **AND** la descripción comunica: plataforma multi-negocio de fidelidad digital (sellos vía QR, sin
  instalación), actores diferenciados (guest, cliente registrado, empleado/caja, dueño/manager, super-admin),
  billetera multi-negocio, niveles/tiers y canje, alta self-service de negocios, KPIs/analítica, encuestas
  de satisfacción y reporte mensual programado (`pg_cron`) para la plataforma
- **AND** menciona la seguridad: RLS multi-tenant, lógica en RPC PL/pgSQL `SECURITY DEFINER`, QR tokens
  con TTL + fingerprint SHA-256 anti-replay, rate limiting en funciones anónimas, auditoría sin PII y feature
  flags (global + override por negocio)
- **AND** NO presenta Google Wallet, WhatsApp ni Google OAuth como funciones activas (están construidas pero
  apagadas/sin credenciales); si se mencionan, se etiquetan "built, flag off"
- **AND** indica que fue desarrollado 100 % bajo Spec-Driven Development (SDD/OpenSpec)

#### Scenario: Cifras de ingeniería verificables
- **WHEN** se lee la card de Fidello
- **THEN** muestra, como texto o mini-badges, al menos: 793 pruebas (337 de base de datos contra Postgres real
  + 456 de pantalla), 91 migraciones SQL, 22 tablas, 7 Edge Functions, 5 tareas `pg_cron`, 97 cambios
  OpenSpec (85 archivados), 28 journeys con runbook gemelo, CI con 2 jobs bloqueantes (frontend + BD) y
  ambientes QAS/PROD
- **AND** indica que los flujos principales fueron validados por producto en cafeterías reales (piloto)
- **AND** las cifras coinciden con el paquete de revisión de arquitectura del 2026-09-17 (migración 091) y se
  documentan en `design.md` con su origen

#### Scenario: Stack de Fidello visible y completo
- **WHEN** se lee la sección técnica (`.tech`) de la card de Fidello
- **THEN** se listan: React 18, TypeScript, Vite 5, Tailwind 3, React Router 7, PWA (`vite-plugin-pwa` /
  Workbox, code-splitting), WCAG AA, html5-qrcode, Supabase (PostgreSQL 15 + Auth + PostgREST + Realtime),
  RLS, PL/pgSQL `SECURITY DEFINER`, Edge Functions (Deno), `pg_cron`, Vitest + Testing Library + msw + harness
  `pg`, ESLint, GitHub Actions, Vercel (QAS/PROD), Supabase CLI + Docker
- **AND** se menciona el uso de 5 agentes IA especializados (backend, frontend, security-reviewer,
  solution-architect, product-strategy) y 28 journeys con runbook gemelo como parte de la práctica SDD

#### Scenario: Card coherente con el sistema de diseño existente
- **WHEN** se renderiza la card de Fidello
- **THEN** reutiliza las clases `.card`, `.card-badge`, `.tech` y (si aplica) `.btn` existentes
- **AND** respeta la paleta de colores (`docs/frontend-standards.md` §2) sin estilos nuevos ad hoc
- **AND** se mantiene el layout responsive de la grilla de proyectos en 992/768/480px

#### Scenario: Enlace de repositorio condicional
- **WHEN** la card incluye un enlace "View Code"
- **THEN** apunta al repositorio público de Fidello si existe; si el repo es privado (caso actual), la card
  se muestra sin botón de código en lugar de un enlace roto

#### Scenario: CV y llms.txt reflejan el estado de piloto
- **WHEN** se lee la entrada de Fidello en el CV (ES/EN) y en `llms.txt`
- **THEN** se indica "piloto en beta cloud" (ES) / "cloud beta pilot" (EN) y al menos una cifra de
  ingeniería (793 pruebas o 91 migraciones), con el stack compactado por espacio
