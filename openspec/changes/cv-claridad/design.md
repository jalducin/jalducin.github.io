## Context

El CV vive en `cv/cv.html` (ES) y `cv/cv-en.html` (EN), maquetado estilo "hexagon" en Oficio a 2 columnas
(izquierda 55 %: Resumen, Experiencia, Educación, Idiomas, Cursos; derecha 45 %: Habilidades, Proyectos), y se
imprime con `cv/build.ps1` (Chrome headless). `llms.txt` es la fuente de verdad del perfil y alimenta la base del
chatbot del sitio (`assistant/knowledge.md`). Pasar a A4 quita ~43 mm de alto y 6 mm de ancho, lo que obliga a
recortar contenido (que es el objetivo del cambio).

## Goals / Non-Goals

**Goals:**
- Un CV que se lea en 10 segundos: titular, 2 líneas de resumen, experiencia corta, 5 categorías y 3 proyectos con evidencia.
- 1 página A4 en ES y EN, ≥ 8.5pt, parseable por ATS.
- `llms.txt` alineado (titular, proyectos, formación).

**Non-Goals:**
- `index.html`, blog, chatbot y LinkedIn (Sprints 2 y 3).
- Cambiar la paleta, la tipografía o el estilo "hexagon".

## Decisions

1. **`llms.txt` antes que el CV.** El CV se deriva de él; así el Sprint 2 recompila el chatbot sin reescribir
   contenido. Alternativa descartada: editar el CV y luego "copiar" a `llms.txt` (riesgo de divergencia).
2. **A4 con `@page { size: 210mm 297mm }`.** Chrome headless respeta `@page`, así que `build.ps1` no necesita
   `--paper-*`; solo cambia su comentario. `.sheet` pasa a `width:210mm; min-height:289mm`.
3. **Recortar contenido, no letra.** Se mantiene el mínimo de 11.3px; el espacio sale de quitar las líneas
   `Stack:` por rol, bajar a 5 categorías y a 3 proyectos.
4. **Layout de columnas sin cambios** salvo el reparto: izquierda Resumen, Experiencia, Educación, Idiomas;
   derecha Habilidades, Proyectos, Cursos (Cursos pasa a la derecha si la izquierda se desborda). Se ajusta en
   la verificación de altura.
5. **Enlaces como texto corto** (`github.com/jalducin/platform-STALD`) para que un ATS los extraiga y un
   humano los teclee.
6. **Cifras de STALD con fecha de corte.** Se toman de git/gh el día de implementar (comandos en tasks) y se
   redondean hacia abajo ("+250 PRs") para que sigan siendo ciertas al crecer.
7. **Monitoreo-Cloud como tercer destacado** (respalda "SRE & Automation" del titular). VoltGrid, Trackion y
   dataMasterGK van en una línea "Otros".

## Borrador de contenido (a validar con el propietario en apply)

**Resumen (ES):** Senior Backend Engineer y Tech Lead con +10 años en Python, SQL y AWS. Hago la operación
confiable y automatizada (post-mortems, runbooks, n8n) y construyo software con Spec-Driven Development y
agentes de IA.

**Summary (EN):** Senior Backend Engineer and Tech Lead with 10+ years in Python, SQL and AWS. I make
operations reliable and automated (post-mortems, runbooks, n8n) and build software with Spec-Driven
Development and AI agents.

**Rol actual (4 bullets):** liderazgo de Service Support con SDD + Claude; sistema de post-mortems y metodología
de uptime; automatización n8n Freshdesk → Notion → Slack y Skill de routing con revisión humana; trenes de
liberación semanales y operación AWS con SLA < 10 min / < 2 h.

**Habilidades (5):**
- Backend: Python (FastAPI, Django, Flask), SQL, TypeScript, REST/WebSocket
- Cloud & Serverless: AWS (Lambda, Step Functions, EventBridge, CloudWatch, RDS, S3), Supabase, Deno Deploy, Docker, GitHub Actions
- Datos: PostgreSQL (RLS, PL/pgSQL), ETL idempotente, Liquibase, DynamoDB
- SRE & Automatización: post-mortems, runbooks, SLAs, Grafana, Sentry, n8n
- IA aplicada: Claude Code (subagentes, skills, hooks, MCP), Claude API, Amazon Bedrock, SDD/OpenSpec

> Deno Deploy se agrega al inventario Build de `llms.txt` (evidencia: platform-STALD).

**Proyectos:**
- **platform-STALD — Plataforma educativa construida con agentes.** Portal, actividades en línea y juegos
  multijugador en tiempo real, construido 100 % con SDD y Claude Code: subagentes revisor y verificador, 14
  skills y un hook que bloquea commits de secretos y push a main. +250 PRs · 85+ cambios OpenSpec · pruebas
  unitarias en CI + E2E. Stack: Deno · TypeScript · Supabase (Postgres RLS, Auth, Realtime) · JS vanilla.
  `github.com/jalducin/platform-STALD`
- **Fidello — Loyalty Card System.** Fidelidad digital multi-negocio (QR mobile-first) con toda la lógica en
  PostgreSQL: RLS multi-tenant, RPC PL/pgSQL, QR anti-replay, feature flags. 793 pruebas · 91 migraciones · 100 %
  SDD. Stack: React · TypeScript · Supabase. Deep dive: `jalducin.github.io/blog/deep-dive-fidello.html`
- **Monitoreo-Cloud — Observabilidad.** Grafana + Docker sobre 3 fuentes (CloudWatch, Docker, tickets/SLA),
  recolección con n8n. `github.com/jalducin/monitoreo-cloud`
- **Otros:** VoltGrid (SaaS multi-tenant EV, FastAPI + Next.js) · Trackion (help desk serverless) ·
  dataMasterGK (ETL retail) — `github.com/jalducin`

## Risks / Trade-offs

- [El sitio queda desalineado de `llms.txt` entre sprints] → El Sprint 2 empieza al cerrar este; se anota en
  la proposal. El chatbot no se recompila aquí.
- [No cabe en A4 aun recortando] → Mover Cursos a la derecha y bajar `line-height` del cuerpo a 1.22 (permitido
  por la spec), nunca la letra.
- [Las cifras de STALD envejecen] → Redondear hacia abajo con "+".
- [STALD lo usan menores] → Ningún dato de personas; el repo público solo tiene código y specs. La auditoría
  de privacidad y una revisión manual lo cubren.
