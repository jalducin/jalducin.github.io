# Design: cv-portafolio-sre-automation

## Context

Estado actual (main `bb7ad40`, 2026-09-19):
- CV ES/EN (`cv/cv.html`, `cv/cv-en.html`) en 1 página Oficio con tipografía del sistema (Segoe UI); dos
  entradas de Podemos ya separadas; maestría retirada. Bullets del rol actual ya compactados a ~125 chars.
- `index.html` single-page con tabs (`GROUPS`): header, `#ai-method` (Now + flujo SDD + grilla de 4 cards),
  `#experience` (timeline alternada), `#featured-projects`, `#hard-skills` (icons-grid + bloques
  `.soft-list` por categoría), `#education`, terminal.
- `llms.txt` es la fuente del asistente (Lambda) vía `deploy-assistant.yml`; `profile.txt` es copia.
- Restricciones: HTML/CSS/JS vanilla, CSS embebido, paleta azul metálico intacta, responsive 992/768/480,
  1 página en el PDF, ATS, sin nombres internos del empleador (decisión del usuario: "solo genérico").

Insumos: dos hojas de "stack real" del usuario (evidencia por nivel), lectura del repo de Fidello
(`c:/Desarrollo/Node_JS/fidello02-seed-repo`, rama SDD) y el **paquete de revisión de arquitectura**
(`c:/Desarrollo/Node_JS/fidello-revision-arquitectura`, generado 2026-09-17 desde la rama
`feature/ernesto-journey-alignment`, migración 091). Cifras canónicas (del paquete, más recientes que la rama
SDD): 793 pruebas = 337 de base de datos + 456 de pantalla, 100 % verdes · 91 migraciones · 22 tablas ·
7 Edge Functions · 5 tareas `pg_cron` · 28 journeys con runbook gemelo (F-001…F-020 validados por producto en
cafeterías reales) · ambientes QAS y PROD (Vercel + Supabase Cloud) · 97 cambios OpenSpec (85 archivados,
contados en el repo: `ls openspec/changes/archive | wc -l`) · 415 commits (`git log --oneline | wc -l`).
Honestidad: Google Wallet, Google OAuth, Resend y WhatsApp están **construidos pero apagados / sin
credenciales**; Sentry sin proveedor (el frontend reporta a `log_frontend_error`). No se venden como activos.

## Goals / Non-Goals

**Goals:**
- Un solo relato en las 5 fuentes (CV ES, CV EN, `index.html`, `llms.txt`, JSON-LD): Backend · SRE &
  Automation · Agentic AI, sustentado en evidencia y sin datos internos.
- Skills verificables por nivel; retirar tecnologías sin evidencia.
- Fidello presentado como piloto con cifras reales.
- CV sigue en 1 página; build determinista; ATS-friendly.
- Borrador `.md` sincronizado para que el usuario lo use en LinkedIn.

**Non-Goals:**
- No se cambia la paleta, la navegación por tabs, el blog ni el resto de cards de proyectos (salvo VoltGrid,
  que no cambia: conserva Kubernetes).
- No se crea card de Enkoth ni sección nueva de "SRE" independiente.
- No se rediseña el layout del CV (dos columnas, hexágonos, QRs).
- No se automatiza la sincronización `.md` ↔ HTML (sigue siendo manual, documentada).

## Decisions

### D1. Headline híbrido y su forma exacta
- Sitio (`header h3`, `<title>`, OG, JSON-LD `jobTitle`, `whoami`):
  `Senior Backend Engineer · Tech Lead · SRE & Automation · Agentic AI`
  (en `header h3` con los separadores `&nbsp;|&nbsp;` existentes: "Senior Backend Engineer | Tech Lead · SRE
  & Automation | Agentic AI").
- CV `.tagline` ES/EN: `Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI`.
- Alternativas: "SRE first" (descartada: saca de búsquedas backend) y mantener el actual (descartada: no
  refleja la evidencia). Decisión del usuario 2026-09-19.

### D2. Mapa de lenguaje genérico (interno → público)
| Interno (NO usar) | Público |
|---|---|
| SCI, Alejandría, Strauss | "plataforma de ciclo de crédito / integración con core banking (Step Functions)" |
| Spore | "app de campo (Android) para formalización y KYC" |
| Hipatia, Mambu Tools, Mambu | "core banking (LMS)" / "herramientas de core banking" |
| LUCI / Aleph, DANIEL | "back-office de originación y renovación" / "control de desembolsos" |
| Círculo de Crédito | "buró de crédito (API)" — genérico aceptado por el usuario |
| Freshdesk, Notion, Asana, Slack, Sentry, n8n, Grafana | Se conservan: son herramientas SaaS de terceros, no sistemas internos |
| Enkoth | Se conserva como nombre de tooling propio (regla de `CLAUDE.md`), descrito genéricamente |
| Nombres de BD, bancos, IDs `INC-…`, IDs de workflow, ~24,965 CURPs, nombres de personas | Prohibidos |

Se implementa una verificación automática (grep) en tasks para que la regla no dependa de memoria.

### D3. Contenido de experiencia (rol actual) — borrador base
Portafolio (EN, 7 bullets; el CV toma 5–6 compactados):
1. Lead the Service Support team end-to-end (bugs, critical incidents, tech debt) with SDD + Claude API — cut code
   review time ~40% by redesigning the diagnose-to-implement cycle.
2. Built the post-mortem system (P0–P3 severity, 5 Whys, blameless, self-assessment rubric) with a live
   governance dashboard (delays, open subtasks, N3/N4 escalations, KPI traffic light vs. target) for leadership.
3. Defined the monthly uptime/downtime methodology (fleet × real minutes; downtime = real user impact) — 99.95% in
   July 2026 — plus runbook standardization and least-privilege access model.
4. Automate operations with n8n (workflow SDK): Freshdesk → Notion → Slack with ingestion cursor, post-mortem delay
   watcher, ticket-spike alerts; spec-driven pipelines (n8n orchestrates, Python computes, FastAPI, Notion sink).
5. Architect AI flows (Claude, OpenAI, Gemini, Bedrock) across the SDLC; designing an automatic ticket-routing Skill
   (multi-dimension classification, squad routing, human review on low confidence).
6. Take part in weekly release trains, coordinating validation and deployment across core banking, origination
   and field-app platforms; internal serverless tooling (Enkoth — Lambda · Step Functions · EventBridge).
7. Diagnose and operate AWS (Step Functions, Lambda, CloudWatch Logs Insights, RDS) and audit error tracking
   (Sentry) — SLAs: first response <10 min, critical resolution <2 h.

Rol anterior (3 bullets): N2 incidents + AI-assisted RCAs/post-mortems; 80% N1 self-resolution via knowledge
transfer; weekly idempotent PostgreSQL cleanup ETL (backup → delete → update → audit log, pre-validated) and
identity deduplication; central technical liaison (Python, Django, FastAPI, PostgreSQL).

**CV (ES, 6 + 3 bullets, ≤ 120 chars c/u — decisión del usuario 2026-09-19: los trenes de liberación se
quedan; se fusionan post-mortems + uptime en un bullet):**
1. Lidero Service Support: bugs, incidentes críticos y deuda técnica end-to-end con SDD + Claude API (-40 % en revisión).
2. Sistema de post-mortems (P0–P3, blameless, tablero en vivo) y metodología de uptime mensual: 99.95 % en jul 2026.
3. Automatización con n8n (SDK): Freshdesk → Notion → Slack, alertas de atrasos y picos; pipelines spec-driven.
4. Flujos de IA (Claude, OpenAI, Gemini, Bedrock) en el SDLC; Skill de routing de tickets con revisión humana.
5. Trenes de liberación semanales: validación y despliegue entre core banking, originación y app de campo.
6. AWS (Step Functions, Lambda, CloudWatch, RDS) y tooling serverless interno (Enkoth); SLA: respuesta <10 min, crítica <2 h.
Rol anterior: (1) N2 + RCAs/post-mortems con IA; 80 % autoresolución N1. (2) ETL semanal idempotente en PostgreSQL
(respaldo → limpieza → actualización → bitácora) y deduplicación de identidades. (3) Enlace técnico central
(Python, Django, FastAPI, PostgreSQL). EN: traducción 1:1 con el mismo límite de caracteres.
Fuera del CV (solo portafolio): runbooks/mínimo privilegio, auditoría Sentry (queda en skills), cursor de ingesta.

### D4. Skills por niveles — estructura HTML/CSS
- Se **conserva** `icons-grid` (se retira el ícono de Kubernetes; Laravel se retira por falta de evidencia).
- Se **reemplaza** el bloque "Tech Stack & Tools" por `.level-grid` con 4 `.level` (Own / Build / Operate /
  Learning). Cada `.level` = `h3.level-title` (con `span.level-dot` decorativo `aria-hidden`) + `p.level-def` +
  `ul.soft-list` (reutilizada). Marca visual por nivel solo con opacidad/borde de tokens existentes:
  Own `border-color: var(--primary)`, Build `var(--accent2)`, Operate `var(--border)`, Learning borde punteado.
- Leyenda: un `p` con las 4 definiciones encima de la grilla (texto, no solo color → a11y).
- CSS: `.level-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1.2rem}` → 1 columna en ≤768px.
- Alternativa descartada: tabla (peor en móvil) y pestañas JS (más código, menos escaneable).

### D5. Principios de trabajo — ubicación
Nuevo bloque `.principles` dentro de `#ai-method`, después de `.sdd-flow` y antes de `.ai-method-grid`, como
`ul` de 4 `li` con `<strong>` + texto, estilo `.now-card` (reutilizado) con encabezado "How I work". Se
replica en `llms.txt` bajo "## How I work".

### D6. Fidello como piloto
- Badges: `★ AI-native · 100% SDD` y `🧪 Pilot · cloud beta`.
- Cifras como mini-badges `.card-badge` en una fila: `793 tests (337 DB + 456 UI)`, `91 migrations`,
  `22 tables · 7 Edge Functions · 5 cron jobs`, `97 OpenSpec changes`, `28 journeys + runbooks`,
  `QAS/PROD`. Descripción reescrita según spec; `.tech` ampliada.
- Se quita "Google Wallet passes" de la descripción (construido, apagado). Feature flags sí (activo).
- Se añade una línea sobre el **paquete de revisión de arquitectura** (documento para revisión externa sin
  abrir código: piezas, dónde vive cada regla, despliegue, límites de escala y recomendación) como evidencia
  de práctica de documentación/arquitectura.
- CV: `Piloto en beta cloud · 793 pruebas · 91 migraciones` en `.pdesc` (1 línea extra máx.).

### D7. Estrategia de espacio en el CV (1 página)
Presupuesto medido con la fuente del sistema: columna izquierda ≈ 290 mm, derecha ≈ 305 mm. **Techo real
calibrado en implementación: `.sheet` ≤ 340 mm** (343.6 mm ya produce 2 páginas: Chrome mueve el flex `.cols`
completo a la página 2). Resultado final: sheet 339.3 mm (izq 298.5 / der 292.2) tras mover Idiomas a la
columna izquierda, resumen a 4 líneas y `line-height` del cuerpo 1.28 → 1.25.
Entradas nuevas: +1 bullet rol actual ≈ +8 mm, +1 bullet rol anterior (ETL) ≈ +8 mm, Fidello +1 línea ≈ +4 mm
(derecha). Compensación: hueco de la maestría (≈ 11 mm ya liberado), resumen a 4 líneas, bullets de
Redsis/Softtek ya compactos. No se quita ningún bullet del rol actual (los trenes de liberación se quedan). Verificación
por conteo de páginas del PDF (pypdf) en cada iteración; nunca bajar de 11.3px.

### D8. Sincronización de fuentes
Orden de edición: `index.html` (fuente de la narrativa) → `llms.txt` (deriva) → `cv/cv.html` → `cv/cv-en.html`
→ `cv\build.ps1` → `cv/CV_JuanValentinAlducin.md` → `CLAUDE.md` / `docs/frontend-standards.md §5` / specs.
`profile.txt` se regenera con `cp llms.txt backend/assistant/profile.txt` (mismo comando del workflow).

## Risks / Trade-offs

- [Perder matching ATS por quitar Kendra/Kiro/K8s] → Se compensa con keywords con evidencia (SRE,
  post-mortems, n8n, Step Functions, Sentry, SonarQube, Liquibase); K8s sigue indexable en VoltGrid.
- [Nombre genérico pierde credibilidad frente a nombres de sistemas] → Se usan categorías reconocibles
  ("core banking", "buró de crédito") y métricas duras (99.95 %, <10 min).
- [CV no cabe en 1 página con el contenido nuevo] → D7; el portafolio conserva la versión completa.
- [Cifras de Fidello quedan obsoletas] → Se documenta la fecha y el comando en este design; se actualizan
  cuando se toque la card.
- [Regresión responsive por CSS nuevo en skills] → Capturas headless en 992/768/480 en verificación manual.
- [Inconsistencia entre las 5 fuentes] → Script de auditoría (grep de headline, fechas, nombres prohibidos)
  ejecutado en el paso de verificación.

## Migration Plan

1. Feature branch → edits en el orden D8 → build PDF → verificaciones (páginas, fuentes, grep, headless).
2. Merge a `main` → `deploy.yml` (S3 + CloudFront) y `deploy-assistant.yml` (llms.txt → Lambda) automáticos.
3. Rollback: `git revert` del merge; los PDFs anteriores vuelven con el revert (están versionados).

## Open Questions

- Ninguna bloqueante. Pendiente del usuario (no bloquea): confirmar en LinkedIn el cierre del rol anterior
  (jun vs. jul 2026); el sitio y el CV usan jun 2026.
