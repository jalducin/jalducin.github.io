# Proposal — blog-writing-y-mejoras

## Why

Inspirado en portafolios de referencia (brittanychiang.com — sección "Writing", nav con sección activa;
bruno-simon.com — un detalle interactivo memorable), el portafolio gana credibilidad técnica con un **blog**
propio y unos toques de UX, manteniendo el stack vanilla (sin frameworks ni build).

## What changes

- **Blog "Writing"**: nueva sección/tab que lista posts (título, fecha, tags, tiempo de lectura, extracto)
  y enlaza a **páginas dedicadas** `/blog/<slug>.html` (tema azul metálico, OG tags por post). Posts iniciales:
  SDD/OpenSpec, Docker (observabilidad local), Grafana multi-fuente.
- **Nav activo**: el tab "Writing" se integra al sistema de tabs; el nav resalta la sección activa (ya existente).
- **Spotlight de cursor**: glow azul sutil que sigue el cursor (`z-index:-1`, no intercepta clics),
  desactivado con `prefers-reduced-motion` y en dispositivos táctiles.
- **Sección "Now"**: bloque compacto en "How I Build with AI" con en qué trabaja/estudia actualmente.
- **Self-host de íconos**: los 20 SVGs de devicon pasan a `assets/img/icons/`; se elimina la dependencia y el
  preconnect a `cdn.jsdelivr.net`.
- **CV (ES/EN)**: segundo **mini QR de LinkedIn** junto al QR del portafolio (decodificación verificada);
  PDFs regenerados (1 página).
- **Terminal**: comandos `writing`/`blog` y easter egg `mundial`/`worldcup`; corrige el texto del matrix (azul).

## Impact

- Nuevos archivos: `blog/*.html`, `assets/img/icons/*.svg`, `assets/img/QR-linkedin.png`.
- `index.html`, `cv/cv.html`, `cv/cv-en.html`, `llms.txt`, `docs/frontend-standards.md`.
- Sin dependencias nuevas; menos terceros (sin jsdelivr). Despliegue por CI/CD (push a `main` → AWS).
