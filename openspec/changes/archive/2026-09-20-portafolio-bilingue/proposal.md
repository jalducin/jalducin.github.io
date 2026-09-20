# Proposal: portafolio-bilingue

## Why

El portafolio está solo en inglés mientras que el mercado principal del candidato (CDMX, reclutadores de
fintech y consultoras mexicanas) y su LinkedIn están en español. El CV ya es bilingüe (ES/EN); el sitio
no. Un selector de idioma ES/EN en la propia página, sin duplicar HTML ni añadir build step, cierra esa
brecha y mantiene una sola fuente de verdad para el contenido.

## What Changes

- **Selector de idioma ES/EN** en la barra de navegación (junto al toggle de tema) y en la command palette.
  Cambia todo el texto visible de `index.html` (nav, header, secciones, cards, timeline, skills, educación,
  contacto, footer) sin recargar la página.
- **Mecanismo i18n vanilla**: los elementos traducibles llevan `data-i18n="<clave>"`; el inglés vive en el
  DOM (fuente de verdad) y el español en un diccionario embebido
  `<script type="application/json" id="i18n-es">`. Atributos (`title`, `aria-label`, `placeholder`) se
  traducen vía `data-i18n-title`, `data-i18n-aria`, `data-i18n-placeholder`.
- **Persistencia y detección**: preferencia en `localStorage` (`lang`), parámetro `?lang=es|en`, y si no hay
  preferencia, `navigator.language` que empiece por `es` → español. `<html lang>` y `document.title` se
  actualizan.
- Nombres propios, tecnologías y el headline (`Senior Backend Engineer | Tech Lead · SRE & Automation |
  Agentic AI`) permanecen iguales en ambos idiomas.
- Se extiende el audit del proyecto con checks de cobertura i18n (claves huérfanas, claves sin traducción).

## Capabilities

### New Capabilities
- `idioma-portafolio`: selector ES/EN, mecanismo `data-i18n` + diccionario embebido, persistencia,
  detección de idioma y cobertura de traducción.

### Modified Capabilities
- `stack-por-niveles`: las etiquetas de nivel (Own/Build/Operate/Learning) se muestran en español
  (Dueño/Construyo/Opero/Aprendiendo) cuando el idioma activo es ES.
- `navegacion-por-secciones`: la navegación incluye el botón de idioma y conserva la tab activa al cambiar
  de idioma.
- `terminal-interactiva`: nuevo comando `lang es|en` (y `idioma`) que cambia el idioma desde la terminal.

## Impact

- `index.html`: atributos `data-i18n*` en ~250 elementos, bloque JSON con el diccionario ES (~35 KB), botón
  en nav, ~50 líneas de JS al final del body, entrada en command palette y terminal, CSS del botón.
- `llms.txt`: nota de que el sitio es bilingüe (ES/EN).
- `openspec/specs/*`: capability nueva + 3 deltas. `docs/frontend-standards.md`: regla de i18n para contenido
  nuevo. `CLAUDE.md`: referencia rápida.
- Sin dependencias; sin cambios en blog (`blog/*.html` sigue en inglés — fuera de alcance), CV ni paleta.
- Deploy automático a S3/CloudFront al hacer merge a `main`.
