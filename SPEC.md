# SPEC.md — Especificación del Portafolio

## jalducin.github.io · Portafolio Personal

---

## Descripción general

Sitio estático publicado en GitHub Pages. Presenta el perfil profesional de **Juan Valentin Alducin Vázquez** con experiencia, proyectos, habilidades, educación y un CV interactivo descargable.

---

## Páginas

### `index.html` — Portafolio principal
Secciones navegables mediante navbar sticky (con toggle dark/light y burger menu):
1. **Header** — Nombre, rol, ubicación, bio, links (email, GitHub, LinkedIn, WhatsApp)
2. **Experience** — Timeline de trabajo: Podemos Progresar, Redsis, Softtek
3. **Featured Projects** — Cards de proyectos con tech stack y link a GitHub
4. **Hard Skills** — Grid de iconos de tecnologías (devicons CDN)
5. **Soft Skills** — Badges de habilidades blandas
6. **Languages** — Español nativo / English A2
7. **Education & Certifications** — Formación y cursos recientes
8. **Contact** — Botones + formulario Formspree async (descarga CV ES/EN)

Características transversales:
- Animaciones fade-in por sección al hacer scroll (IntersectionObserver)
- Toggle dark/light mode persistido en localStorage
- Favicon SVG inline con iniciales JA
- Fondo matrix: canvas con lluvia binaria (0s y 1s) en dark mode, oculto en light mode
- Tipografía monospace con glow en títulos (`h1` y secciones `h2`) y prefijo `> ` en secciones
- Efecto glow en cards hover, timeline dots y botones

### `cv.html` — CV Interactivo
- Diseño matrix: fondo binario animado (lluvia de 0s y 1s) más pronunciado que en index.html
- Tipografía monospace con glow en header y secciones; prefijo `> ` en cada sección
- Misma paleta de colores del portafolio (dark mode)
- Layout de CV profesional: datos, experiencia, proyectos, skills, educación
- Botones de descarga directa de los PDFs estáticos (ES y EN)
- Compatible con `@media print`

### `CV_JuanValentinAlducin.pdf` — CV en español (archivo estático)
### `CV_JuanValentinAlducin-English.pdf` — CV en inglés (archivo estático)
- Se sirven directamente como archivos estáticos; **no se generan al vuelo**
- Se actualizan manualmente subiendo los archivos al repositorio

---

## Proyectos en el portafolio

| Proyecto | Stack | GitHub |
|---|---|---|
| dataMasterGK | Python · Flask · SQLite · Paramiko · Docker | jalducin/dataMasterGK |
| socket-chat | Node.js · Express · Socket.io · JavaScript | jalducin/socket-chat |
| MetalShop (EcommerceJVAV) | Python · FastAPI · SQLAlchemy · Docker | jalducin/EcommerceJVAV |
| Inventarios | Java · Spring Boot · WebSocket · H2 · Thymeleaf | jalducin/Inventarios |

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
- Los PDFs del CV (`CV_JuanValentinAlducin.pdf` y `CV_JuanValentinAlducin-English.pdf`) deben existir en la raíz del repo
- Los PDFs **nunca** se generan al vuelo; se actualizan manualmente
- Los botones de descarga en `index.html` y `cv.html` apuntan directamente a estos archivos estáticos
