# CLAUDE.md — Instrucciones para Claude Code
## jalducin.github.io · Portafolio Personal

---

## Rol

Eres el desarrollador del sitio de portafolio personal de **Juan Valentin Alducin Vázquez**, publicado en GitHub Pages.
Consulta siempre los archivos de spec antes de modificar:
- `SPEC.md` → qué páginas existen, secciones y datos de contenido
- `PLAN.md` → arquitectura, decisiones de diseño y fuente de verdad de datos
- `TASKS.md` → qué está pendiente y en qué orden

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
Nombre:    Juan Valentin Alducin Vázquez
Email:     valentin.alducin88@gmail.com
WhatsApp:  +52 55 1060 3174
GitHub:    https://github.com/jalducin
LinkedIn:  https://linkedin.com/in/juanvalducinv
Ubicación: CDMX, Mexico
Inglés:    A2 (Técnico)
```

### Experiencia

| Empresa | Período | Rol |
|---|---|---|
| Podemos Progresar | Sept 2025 – Present | Application Support Coordinator (N2) · Fintech |
| Redsis | Ene 2022 – Sept 2025 | Retail Engineer |
| Softtek | Mar 2017 – Ene 2022 | Software Developer |

### Proyectos destacados

| Proyecto | Stack | Repo |
|---|---|---|
| dataMasterGK | Python · Flask · SQLite · Paramiko · Docker | jalducin/dataMasterGK |
| socket-chat | Node.js · Express · Socket.io · JS | jalducin/socket-chat |
| MetalShop | Python · FastAPI · SQLAlchemy · Docker | jalducin/EcommerceJVAV |
| Inventarios | Java · Spring Boot · WebSocket · H2 · Thymeleaf | jalducin/Inventarios |

---

## Reglas de código

- CSS embebido en `<style>` dentro del HTML (no archivos externos)
- JavaScript inline o en `<script>` al final del body
- El fondo binario de `cv.html` se implementa con `<canvas>` y requestAnimationFrame
- `@media print` en `cv.html` para ocultar el canvas y limpiar el layout al imprimir

---

## Nunca hacer

- Agregar dependencias npm o CDN de frameworks pesados
- Romper el diseño responsive (siempre verificar los tres breakpoints: 992, 768, 480px)
- Cambiar la paleta de colores sin actualizar ambas páginas (`index.html` y `cv.html`)
- Modificar los PDFs del CV (`*.pdf`) — solo se actualizan manualmente
