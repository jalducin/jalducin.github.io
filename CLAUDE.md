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
--bg:        #17120e   (café muy oscuro, no negro puro)
--fg:        #e8ddcf   (crema)
--primary:   #c8924a   (café-dorado, acento)
--accent2:   #e0a96d   (ámbar claro)
--card-bg:   #221a13
--border:    #3a2e22
--badge-bg:  #2a2017
```

> Paleta **café elegante** (armoniza con el CV). El efecto **matrix** se conserva pero recoloreado a ámbar.
> Tema claro (`html.light`): variante cálida crema. No usar el azul `#58a6ff`/negro `#0d1117` anteriores.

---

## Datos del propietario (fuente de verdad)

```
Nombre:      Juan Valentin Alducin Vázquez
Posición:    Senior Software Engineer · AI-native Development
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
| Fidello | React 18 · TypeScript · Vite · Tailwind · Supabase · PL/pgSQL · Edge Functions (Deno) · Vitest | privado/seed |
| Enkoth | Python · FastAPI · AWS Lambda · Step Functions · EventBridge · Serverless Framework | privado (Podemos) |
| dataMasterGK | Python · Flask · SQLite · Paramiko · Docker | jalducin/dataMasterGK |
| socket-chat | Node.js · Express · Socket.io · JS | jalducin/socket-chat |
| JV Market (ex-MetalShop) | Python · FastAPI · JWT · SQLite/PostgreSQL · AWS (Lambda · API Gateway · S3/CloudFront) — desplegado | jalducin/EcommerceJVAV |
| Inventarios | Java · Spring Boot · WebSocket · H2 · Thymeleaf | jalducin/Inventarios |

---

## Reglas de código

- CSS embebido en `<style>` dentro del HTML (no archivos externos)
- JavaScript inline o en `<script>` al final del body

---

## PDF del CV (self-hosted, sin enhancv)

El CV se genera **dentro del repo** desde una fuente HTML editable, sin depender de enhancv ni suscripciones:
- `cv/cv.html` — fuente editable (formato estilo enhancv "hexagon", **tamaño Oficio 216×340 mm**, 1 página, ATS-friendly).
- `cv/hex-bg.svg` — fondo de hexágonos. `cv/build.ps1` — regenera el PDF con Chrome/Edge headless.
- `cv/CV_JuanValentinAlducin.pdf` — artefacto resultante; es el que descarga `index.html`. Versionado en el repo.

Flujo: editar `cv/cv.html` → ejecutar `cv\build.ps1` (o el comando Chrome headless) → commitear el HTML y el PDF.
El PDF **no se genera en el navegador del visitante** (no hay JS de generación en el sitio); es un build step manual.
Para diseño/fidelidad usar el agente `design-specialist` (`ai-specs/agents/`).

---

## Nunca hacer

- Agregar dependencias npm o CDN de frameworks pesados
- Romper el diseño responsive (siempre verificar los tres breakpoints: 992, 768, 480px)
- Cambiar la paleta de colores sin documentarlo aquí
- Editar el PDF a mano: el CV se edita en `cv/cv.html` y se regenera; nunca se modifica el binario directamente
- Generar PDFs en el navegador del visitante (JS al vuelo en el sitio) — el PDF es un build step, no runtime
