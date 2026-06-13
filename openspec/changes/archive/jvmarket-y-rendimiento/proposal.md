## Why

El proyecto e-commerce de Juan **cambió de nombre (MetalShop → JV Market)** y ya está **desplegado en AWS**
(API en API Gateway + Lambda, frontend en S3+CloudFront). El portafolio y el CV deben reflejarlo, con
enlaces en vivo (demo + API docs). Además se aprovecha para una pasada de **rendimiento** en el sitio.

## What Changes

- **Renombrar MetalShop → JV Market** en portafolio (`index.html`), CV (`cv/cv.html`), `llms.txt` y
  `CLAUDE.md`; reencuadrarlo de "práctica WIP" a **full-stack desplegado en AWS**, con stack real
  (FastAPI · JWT · SQLite/PostgreSQL · AWS Lambda + API Gateway + S3/CloudFront) y **enlaces en vivo**
  (storefront + API docs Swagger). Regenerar el PDF del CV.
- **Rendimiento del portafolio**: `preconnect`/`dns-prefetch` a la CDN de iconos, `loading="lazy"` +
  `decoding="async"` + dimensiones en imágenes, y **pausar el matrix cuando la pestaña no está visible**.

## Capabilities

### New Capabilities
- `proyecto-jvmarket`: el proyecto figura como **JV Market** (desplegado en AWS) en CV/portafolio/docs con enlaces en vivo.
- `rendimiento-portafolio`: mejoras de performance (preconnect, lazy/async imágenes, matrix pausado en background).

### Modified Capabilities
(ninguna con requisitos previos; ajustes de contenido y rendimiento sobre el sitio actual)

## Impact

- **Código**: `index.html` (card del proyecto + head preconnect + imágenes + matrix JS), `cv/cv.html` (+PDF),
  `llms.txt`, `CLAUDE.md`.
- **Restricciones**: HTML/CSS/JS vanilla, sin frameworks; mantener tabs, terminal, asistente, paleta café, a11y, responsive.
- **Despliegue**: push a GitHub → CI/CD (S3+CloudFront). El CV se regenera con Chrome headless.
- **Enlaces en vivo** (verificados 200): storefront `https://d3rw1q49m6mvnq.cloudfront.net/`,
  API docs `https://cizs8fa7lf.execute-api.us-east-2.amazonaws.com/dev/api/docs`.
