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
├── cv.html                            ← CV interactivo con fondo binario
├── CV_JuanValentinAlducin.pdf         ← CV en español
├── CV_JuanValentinAlducin-English.pdf ← CV en inglés
├── assets/                            ← Imágenes y recursos
├── README.md                          ← Descripción del repo
├── SPEC.md                            ← Qué contiene el sitio
├── PLAN.md                            ← Este archivo
├── TASKS.md                           ← Pendientes y mejoras
└── CLAUDE.md                          ← Instrucciones para Claude Code
```

---

## Decisiones de arquitectura

### Single-page vs multi-page
- `index.html` es la página principal. Toda la navegación es intra-página via `href="#section"`.
- `cv.html` es una segunda página para el CV interactivo, con su propio diseño de fondo binario.

### Estilos
- CSS embebido en `<style>` dentro de cada HTML para simplicidad de despliegue (sin archivos `.css` separados que puedan perderse en GitHub Pages).
- Variables CSS custom properties para mantener consistencia de paleta.
- Media queries propios: breakpoints en 992px, 768px y 480px.

### Fondo binario (cv.html)
- Implementado con `<canvas>` + `setInterval` en JavaScript.
- Números binarios (0 y 1) en color primario con opacidad ~0.08 sobre fondo oscuro.
- Animación: columnas de binario que caen (estilo Matrix muy tenue). Se oculta en `@media print`.

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

- **`cv.html`** — contiene el objeto `const CV = {...}` al final del archivo. Es la única fuente de verdad del CV: editar ese objeto actualiza todo el renderizado al vuelo. No hay HTML de contenido en el body, solo los contenedores.
- **`index.html`** — contiene el contenido del portafolio directamente en el HTML. Actualizar en paralelo cuando cambia experiencia, proyectos o datos de contacto.

### Experiencia (cronológica inversa)
1. **Podemos Progresar** — Sept 2025 · Presente · Application Support Coordinator (N2) · Fintech
2. **Redsis** — Ene 2022 – Sept 2025 · Retail Engineer
3. **Softtek** — Mar 2017 – Ene 2022 · Software Developer

### Proyectos destacados
1. dataMasterGK — Python/Flask ETL para GK Software
2. socket-chat — Chat en tiempo real Node.js + Socket.io
3. MetalShop — Ecommerce FastAPI + frontend metálico
4. Inventarios — Inventario Spring Boot + WebSocket + Thymeleaf
