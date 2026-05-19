# SPEC.md — Especificación del Portafolio

## jalducin.github.io · Portafolio Personal

---

## Descripción general

Sitio estático publicado en GitHub Pages. Presenta el perfil profesional de **Juan Valentin Alducin Vázquez** con experiencia, proyectos, habilidades, educación y descarga directa del CV en PDF.

---

## Páginas

### `index.html` — Portafolio principal (single page)
Secciones navegables mediante navbar sticky (con toggle dark/light y burger menu):
1. **Header** — Nombre, rol, ubicación, bio, links (email, GitHub, LinkedIn, WhatsApp)
2. **Experience** — Timeline de trabajo: Podemos Progresar, Redsis, Softtek
3. **Featured Projects** — Cards de proyectos con tech stack y link a GitHub
4. **Hard Skills** — Grid de iconos de tecnologías (devicons CDN) + sub-sección "Tech Stack & Tools" con badges categorizados (Backend & APIs, AWS & Serverless, Enterprise Integrations, Retail & POS, Python Tooling & Testing, AI & Knowledge, Workflow & Management)
5. **Soft Skills** — Badges de habilidades blandas
6. **Languages** — Español nativo / Inglés B1
7. **Education & Certifications** — Formación y cursos recientes
8. **Contact** — Botones (incluye descarga directa del CV en PDF) + formulario Formspree async

Características transversales:
- Animaciones fade-in por sección al hacer scroll (IntersectionObserver)
- Toggle dark/light mode persistido en localStorage
- Favicon SVG inline con iniciales JA
- Fondo matrix: canvas con lluvia binaria (0s y 1s) en dark mode, oculto en light mode
- Tipografía monospace con glow en títulos (`h1` y secciones `h2`) y prefijo `> ` en secciones
- Efecto glow en cards hover, timeline dots y botones

### `CV_JuanValentinAlducin.pdf` — CV en español (archivo estático)
- Se sirve directamente como archivo estático; **no se genera al vuelo**
- Se actualiza manualmente subiendo el archivo al repositorio

---

## Proyectos en el portafolio

| Proyecto | Stack | GitHub |
|---|---|---|
| Enkoth | Python · FastAPI · AWS Lambda · Step Functions · EventBridge · Serverless Framework · PostgreSQL RDS · Webhooks · SDD | (interno, en desarrollo activo) |
| dataMasterGK | Python · Flask · SQLite · Paramiko · Docker | jalducin/dataMasterGK |
| socket-chat | Node.js · Express · WebSocket · JavaScript | jalducin/socket-chat |
| MetalShop (EcommerceJVAV) | Python · FastAPI · SQLAlchemy · PostgreSQL · Docker · pytest | jalducin/EcommerceJVAV |
| Inventarios | Java · Spring Boot · Spring Data JPA · WebSocket · H2 · Thymeleaf · Maven | jalducin/Inventarios |

---

## Paleta de colores (dark mode)

```
--bg:         #0d1117   ← Fondo principal
--fg:         #c9d1d9   ← Texto principal
--primary:    #58a6ff   ← Azul GitHub
--card-bg:    #161b22   ← Cards y navbar
--border:     #30363d   ← Bordes
--badge-bg:   #21262d   ← Badges
```

---

## Restricciones

- Sin frameworks JS ni CSS (Bootstrap nuevo, Tailwind, React, etc.)
- Compatible con GitHub Pages (solo archivos estáticos)
- Responsivo: mobile-first con media queries propios
- Todos los links externos abren en `_blank`
- El PDF del CV (`CV_JuanValentinAlducin.pdf`) debe existir en la raíz del repo
- El PDF **nunca** se genera al vuelo; se actualiza manualmente
- El botón de descarga en `index.html` apunta directamente al archivo estático
