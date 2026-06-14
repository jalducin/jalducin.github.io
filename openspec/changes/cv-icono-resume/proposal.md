# Proposal — cv-icono-resume

## Why

El ícono actual de los botones de descarga del CV en el hero es una **flecha hacia arriba sobre un documento**,
que se lee más como *"subir/upload"* que como *"descargar mi CV"*. No es adecuado (no es "adoc") para la acción.
Se quiere un ícono **más representativo de un currículum/résumé**: una **hoja con un busto de persona**
(el ícono clásico de CV), en **dorado** acorde a la paleta café.

## What changes

- **index.html** (hero, `.header-links`): reemplazar el glifo SVG de los **dos** botones de CV (ES y EN)
  por un ícono **résumé** = página con un busto de persona (cabeza + hombros) y un par de líneas de texto.
  - Se conserva: color dorado (`currentColor` = `--primary`), las etiquetas **ES**/**EN**, el hover elegante,
    los atributos `download` con sufijo mes-año dinámico y los `data-cv`.
  - Sin flecha de "subir/descargar" (el contexto + etiqueta ES/EN ya comunican la acción).
- Sin cambios de comportamiento (descarga), sólo el glifo visual.

## Impact

- Spec afectada: `cv-descarga-multidioma` (presentación del control de descarga).
- Sin dependencias nuevas; SVG inline (sin CDN). No cambia el flujo de build del PDF.
- Despliegue automático vía CI/CD (push a `main` → GitHub Actions → AWS).
