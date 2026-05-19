# PLAN.md — Plan Técnico del Portafolio

## jalducin.github.io · Portafolio Personal

---

## Stack (no negociable)

- **HTML5 + CSS3 + JavaScript Vanilla** — sin frameworks
- **GitHub Pages** — despliegue estático desde rama `main`
- **Sin build step** — archivos listos para servir directamente

---

## Estructura de archivos

```
jalducin.github.io/
├── index.html                         ← Portafolio principal (single-page)
├── CV_JuanValentinAlducin.pdf         ← CV en español (descarga directa)
├── assets/                            ← Imágenes y recursos
├── logo.png                           ← Logo
├── README.md                          ← Descripción del repo
├── SPEC.md                            ← Qué contiene el sitio
├── PLAN.md                            ← Este archivo
├── TASKS.md                           ← Pendientes y mejoras
└── CLAUDE.md                          ← Instrucciones para Claude Code
```

---

## Decisiones de arquitectura

### Single-page
- `index.html` es la única página HTML. Toda la navegación es intra-página via `href="#section"`.
- El CV completo se descarga como PDF estático (`CV_JuanValentinAlducin.pdf`) desde el botón de la sección Contact.

### Estilos
- CSS embebido en `<style>` dentro del HTML para simplicidad de despliegue (sin archivos `.css` separados que puedan perderse en GitHub Pages).
- Variables CSS custom properties para mantener consistencia de paleta.
- Media queries propios: breakpoints en 992px, 768px y 480px.

### Fondo binario matrix
- `<canvas id="matrix-bg">` fixed, z-index:-1. Lluvia binaria sutil (OPC≈0.07) en dark mode; oculta en light mode via CSS. El contenedor es `rgba(13,17,23,0.82)` semi-transparente para dejar ver la lluvia.
- Tipografía: h1 y h2 usan `'Courier New', monospace` con `text-shadow` glow en `--primary`.
- Prefijo `> ` en `section h2::before` para look terminal.
- Botones (`.btn`) con `font-family: 'Courier New'` y `letter-spacing` para feel de terminal.

### Navbar
- Sticky con `position: sticky; top: 0`.
- Burger menu en móvil con toggle de clase `open` en `<nav>`.

### Timeline de experiencia
- Dos columnas en desktop (left/right alternados).
- Una columna en móvil con la línea vertical desplazada a la izquierda.

### Cards de proyectos
- Grid CSS `auto-fit minmax(260px, 1fr)`.
- Efecto hover: `translateY(-8px) scale(1.04)` + barrido de luz con `::before`.

---

## Contenido de datos (fuente de verdad)

- **`index.html`** — contiene todo el contenido del portafolio directamente en el HTML (experiencia, proyectos, skills, educación, certificaciones, idiomas, contacto). Actualizar aquí cuando cambia cualquier dato.
- **`CV_JuanValentinAlducin.pdf`** — CV en español. Archivo estático, actualización manual subiendo el archivo al repo.

### Experiencia (cronológica inversa)
1. **Podemos Progresar** — Sept 2025 · Presente · Software Engineer (construyendo Enkoth, plataforma full serverless)
2. **Redsis** — Ene 2022 – Sept 2025 · Retail Engineer / Software Engineer (GK POS multi-país)
3. **Softtek** — Mar 2017 – Ene 2022 · Software Developer (SAP ERP/HANA, AMS)

### Proyectos destacados
1. Enkoth — Full serverless webhook platform (Podemos Progresar, en desarrollo activo)
2. dataMasterGK — Python/Flask ETL para GK Software
3. socket-chat — Chat en tiempo real Node.js + WebSocket
4. MetalShop — Ecommerce FastAPI + frontend metálico
5. Inventarios — Inventario Spring Boot + WebSocket + Thymeleaf
