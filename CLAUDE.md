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
--bg:        #0d1117
--fg:        #c9d1d9
--primary:   #58a6ff
--card-bg:   #161b22
--border:    #30363d
--badge-bg:  #21262d
```

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
| Podemos Progresar | Sept 2025 – Present | Backend Support Engineer & AI Specialist · Fintech |
| Redsis | Ene 2022 – Sept 2025 | Software Engineer → Tech Lead |
| Softtek | Mar 2017 – Ene 2022 | Software Engineer |

### Proyectos destacados

| Proyecto | Stack | Repo |
|---|---|---|
| Fidello | React 18 · TypeScript · Vite · Tailwind · Supabase · PL/pgSQL · Edge Functions (Deno) · Vitest | privado/seed |
| Enkoth | Python · FastAPI · AWS Lambda · Step Functions · EventBridge · Serverless Framework | privado (Podemos) |
| dataMasterGK | Python · Flask · SQLite · Paramiko · Docker | jalducin/dataMasterGK |
| socket-chat | Node.js · Express · Socket.io · JS | jalducin/socket-chat |
| MetalShop | Python · FastAPI · SQLAlchemy · Docker | jalducin/EcommerceJVAV |
| Inventarios | Java · Spring Boot · WebSocket · H2 · Thymeleaf | jalducin/Inventarios |

---

## Reglas de código

- CSS embebido en `<style>` dentro del HTML (no archivos externos)
- JavaScript inline o en `<script>` al final del body

---

## PDF del CV

El CV en PDF es un archivo estático precargado en el repositorio:
- `CV_JuanValentinAlducin.pdf` — versión en español

El botón de descarga en `index.html` apunta directamente a este archivo con el atributo `download`. El PDF **nunca se genera al vuelo**.

---

## Nunca hacer

- Agregar dependencias npm o CDN de frameworks pesados
- Romper el diseño responsive (siempre verificar los tres breakpoints: 992, 768, 480px)
- Cambiar la paleta de colores sin documentarlo aquí
- Modificar el PDF del CV (`CV_JuanValentinAlducin.pdf`) — solo se actualiza manualmente subiendo el archivo al repo
- Generar PDFs con JavaScript/librerías al vuelo — los PDFs son siempre archivos estáticos
