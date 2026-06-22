# CLAUDE.md — Instrucciones para Claude Code
## jalducin.github.io · Portafolio Personal

---

## Rol

Eres el desarrollador del sitio de portafolio personal de **Juan Valentin Alducin Vázquez**, publicado en GitHub Pages.

## Flujo de trabajo: Spec-Driven Development (OpenSpec)

Este proyecto usa **SDD/OpenSpec**. La especificación es la fuente de verdad: cada cambio recorre
artefactos antes de codificar (`proposal → specs → design → tasks → apply → archive`).

Antes de modificar, lee y aplica:
- `docs/base-standards.md` → principios base, idioma, skills, planificación y reglas OpenSpec.
- `docs/frontend-standards.md` → stack estático, paleta, reglas de código y responsive (este proyecto).
- `docs/documentation-standards.md` → estructura y mantenimiento de la documentación.
- `openspec/project.md` → contexto del proyecto. `openspec/specs/` → capabilities vigentes.

Comandos del flujo en Claude Code: `/opsx:new`, `/opsx:ff`, `/opsx:continue`, `/opsx:explore`,
`/opsx:apply`, `/opsx:verify`, `/opsx:sync`, `/opsx:archive`, `/opsx:onboard`. Para implementar,
adopta el agente `frontend-developer` de `ai-specs/agents/`.

> Las secciones siguientes (stack, paleta, datos del propietario, reglas de código) son la referencia
> rápida del proyecto; el detalle completo y los estándares vinculados viven en `docs/`.

---

## Stack (no negociable)

- **HTML5 + CSS3 + JavaScript Vanilla** — sin frameworks JS ni CSS
- **GitHub Pages** — despliegue estático, sin build step
- CSS custom properties para paleta de colores
- Media queries propios (sin Bootstrap nuevo ni Tailwind)

### No usar
- Frameworks JS (React, Vue, Angular, jQuery)
- Frameworks CSS (Bootstrap nuevo, Tailwind)
- Archivos `.css` o `.js` separados (estilos e inline scripts embebidos en el HTML)
- Dependencias de npm

---

## Paleta de colores

```css
--bg:        #0f141a   (azul noche muy oscuro, no negro puro)
--fg:        #dde6ef   (blanco azulado)
--primary:   #7fa8c9   (azul acero metálico, acento)
--accent2:   #a9c5dd   (azul niebla)
--card-bg:   #161d26
--border:    #2a3744
--badge-bg:  #1b232d
```

> Paleta **azul metálico profesional** (armoniza con el CV, acento `#3f6488`). El efecto **matrix** se conserva
> pero recoloreado a azul metálico (`#7fa8c9`). Tema claro (`html.light`): variante fría (`--bg:#eef2f6`,
> `--primary:#3f6488`). Detalle completo de tokens en `docs/frontend-standards.md §2`. No usar el café/dorado
> anterior ni el azul `#58a6ff`/negro `#0d1117`.

---

## Datos del propietario (fuente de verdad)

```
Nombre:      Juan Valentin Alducin Vázquez
Posición:    Senior Backend Engineer · Tech Lead · Agentic AI Systems
Email:       valentin.alducin88@gmail.com
WhatsApp:    525640800494
GitHub:      https://github.com/jalducin
LinkedIn:    https://linkedin.com/in/juanvalducinv
Ubicación:   CDMX, Mexico
Inglés:      B1 (Intermedio)
```

### Experiencia

| Empresa | Período | Rol |
|---|---|---|
| Podemos Progresar | Sept 2025 – Present | Backend Engineer & AI Specialist · Fintech |
| Redsis | Ene 2022 – Sept 2025 | Software Engineer → Tech Lead |
| Softtek | Mar 2017 – Ene 2022 | Software Engineer |

### Proyectos destacados

| Proyecto | Stack | Repo |
|---|---|---|
| Fidello | React 18 · TypeScript · Vite · Tailwind · Supabase · PL/pgSQL · Edge Functions (Deno) · Google Wallet passes (RS256 JWT) · Feature Flags · Vitest | privado/seed |
| VoltGrid | FastAPI · SQLAlchemy 2.0 async · PostgreSQL 16 (RLS) · Next.js 14 · TypeScript · Tailwind · WebSockets · Docker · Kubernetes (Kustomize) — SaaS multi-tenant EV charging | jalducin/voltgrid |
| Trackion | Python 3.12 · AWS Lambda · API Gateway · Serverless Framework · PostgreSQL · JWT · SSM · Grafana — helpdesk serverless white-label (local Docker; sin demo en vivo) | jalducin/Trackion |
| JV Market (ex-MetalShop) | Python · FastAPI · JWT · SQLite/PostgreSQL · AWS (Lambda · API Gateway · S3/CloudFront) — e-commerce streetwear/sneakers (Click & Collect + wishlist), desplegado (Live Demo) | jalducin/EcommerceJVAV |
| Monitoreo-Cloud | Grafana · Docker · n8n · PostgreSQL · AWS CloudWatch · Lambda · S3 — stack de observabilidad multi-fuente (AWS serverless + Docker local + tickets/SLA de Trackion), self-hosted | jalducin/monitoreo-cloud |
| dataMasterGK | Python 3.12 · Flask · Pandas · openpyxl · SQLite · Paramiko (SFTP) · Jinja2 — middleware ETL retail (Excel→GK XML, 4 interfaces, SFTP/FTP), rediseñado con SDD (pipeline idempotente, seguridad) | jalducin/dataMasterGK |

> Enkoth (tooling serverless interno en Podemos: Lambda · Step Functions · EventBridge) se menciona de forma
> ligera dentro de la experiencia actual, no como proyecto destacado independiente. Inventarios y socket-chat
> se retiraron del portafolio por considerarse obsoletos para la narrativa AI-native / AWS serverless.

---

## Reglas de código

- CSS embebido en `<style>` dentro del HTML (no archivos externos)
- JavaScript inline o en `<script>` al final del body

---

## PDF del CV (self-hosted, sin enhancv)

El CV se genera **dentro del repo** desde fuentes HTML editables (bilingüe ES/EN), sin depender de enhancv ni suscripciones:
- `cv/cv.html` (ES) y `cv/cv-en.html` (EN) — fuentes editables (formato estilo enhancv "hexagon", **tamaño Oficio 216×340 mm**, 1 página, ATS-friendly). Idiomas va en la columna derecha (Español Nativo + Inglés).
- `cv/hex-bg.svg` — fondo de hexágonos. `cv/build.ps1` — regenera **ambos** PDFs con Chrome/Edge headless (`--user-data-dir` único por PDF).
- `cv/CV_JuanValentinAlducin.pdf` (ES) y `cv/CV_JuanValentinAlducin_EN.pdf` (EN) — artefactos; los que descarga `index.html`. Versionados en el repo.
- Descarga con **sufijo mes-año dinámico** (JS vanilla): el archivo se entrega como `CV_JuanValentinAlducin_AAAA-MM.pdf` / `..._EN_AAAA-MM.pdf`. El botón EN aparece en Contact, command palette y terminal (`cat cv en`).

Flujo: editar `cv/cv.html` y/o `cv/cv-en.html` → ejecutar `cv\build.ps1` → commitear los HTML y los PDFs.
El PDF **no se genera en el navegador del visitante** (no hay JS de generación en el sitio); es un build step manual.
Para diseño/fidelidad usar el agente `design-specialist` (`ai-specs/agents/`).

---

## Nunca hacer

- Agregar dependencias npm o CDN de frameworks pesados
- Romper el diseño responsive (siempre verificar los tres breakpoints: 992, 768, 480px)
- Cambiar la paleta de colores sin documentarlo aquí
- Editar el PDF a mano: el CV se edita en `cv/cv.html` y se regenera; nunca se modifica el binario directamente
- Generar PDFs en el navegador del visitante (JS al vuelo en el sitio) — el PDF es un build step, no runtime
