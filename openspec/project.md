# Contexto del proyecto

> Contexto para los agentes de IA sobre el portafolio personal de Juan Valentin Alducin Vázquez.

## Qué es

Sitio de portafolio profesional de **Juan Valentin Alducin Vázquez** (Software Engineer · Application
Support Coordinator), publicado en [jalducin.github.io](https://jalducin.github.io). Presenta su
experiencia laboral, proyectos destacados, skills, educación y la descarga directa del CV en PDF.

## Stack tecnológico

- Lenguaje(s): HTML5, CSS3, JavaScript Vanilla.
- Framework(s): ninguno (sin React/Vue/Angular/jQuery, sin Bootstrap/Tailwind).
- Base de datos: no aplica (sitio estático).
- Otros: GitHub Pages (hosting estático), CV en PDF estático precargado.

## Arquitectura

Sitio estático **single-page**: todo el contenido, estilos (`<style>`) y scripts (`<script>`) viven
embebidos en `index.html`. Sin build step ni dependencias npm. Despliegue automático vía GitHub Pages
desde la rama `main`. El CV (`CV_JuanValentinAlducin.pdf`) es un archivo estático que se actualiza
manualmente subiéndolo al repo; nunca se genera al vuelo.

## Convenciones

- Idioma: documentación y comentarios en español; identificadores según convención del lenguaje.
- Commits: conventional commits.
- Ramas: `feature/[change-name]`.
- Estándares por área: `docs/frontend-standards.md`.
- Paleta de colores y datos del propietario: fuente de verdad en `docs/frontend-standards.md` y `CLAUDE.md`.

## Comandos clave

- Instalar dependencias: no aplica (sin npm).
- Ejecutar pruebas: no aplica (verificación manual en navegador).
- Levantar el proyecto: abrir `index.html` en el navegador, o servir la carpeta
  (`python -m http.server` / extensión Live Server). Verificar los 3 breakpoints responsive: 992, 768, 480px.
