## Context

`index.html` es un único archivo estático (CSS en `<style>`, JS al final) en S3+CloudFront. Hoy: paleta
oscura azul (`--bg:#0d1117`, `--primary:#58a6ff`) + matrix azul; secciones apiladas con scroll y anclas;
nav fijo arriba. Hay un asistente IA (widget) y command palette que deben seguir funcionando.

## Goals / Non-Goals

**Goals:** paleta café elegante (no negro puro) con matrix recoloreado a ámbar; navegación tipo tabs (una
sección a la vez); sección Terminal interactiva; mantener matrix, asistente, command palette, responsive y a11y.
**Non-Goals:** no cambiar el CV (`cv/`), ni el backend del asistente; no añadir frameworks/dependencias.

## Decisions

- **Tokens de color (tema oscuro):** `--bg:#17120e`, `--card-bg:#221a13`, `--border:#3a2e22`,
  `--badge-bg:#2a2017`, `--fg:#e8ddcf`, `--primary:#c8924a` (café-dorado), `--accent2:#e0a96d` (ámbar).
  Tema claro (`html.light`): crema cálido (`--bg:#f4ece0`, `--card-bg:#fbf6ee`, `--fg:#2b2118`,
  `--primary:#9a6b2f`). *Estrategia:* casi todo usa `var(--primary)`; los glows hardcoded
  `rgba(88,166,255,*)` se reemplazan por `rgba(200,146,74,*)` y los `#58a6ff` literales por `#c8924a`.
- **Matrix recoloreado:** color de "lluvia" a ámbar (`#c8924a`/`#e0a96d`) y el fillStyle de fondo al nuevo
  `#17120e`. Mantiene `prefers-reduced-motion` y `html.light` ocultándolo.
- **Tabs (una sección a la vez):** cada `<section>` principal recibe `.tabpage`; por defecto ocultas
  (`display:none`) salvo `.active`. JS mapea cada ítem del nav → grupo de secciones a mostrar
  (Skills agrupa `hard-skills`+`soft-skills`). Click en nav → muestra ese grupo, oculta el resto, marca
  `aria-current`, hace scroll al inicio del contenido. Estado inicial: hash de la URL o `ai-method`.
  El **hero** (header) permanece siempre visible. *Alternativa descartada:* scroll-snap (el usuario eligió tabs).
- **Terminal:** nueva `<section id="terminal" class="tabpage">` con salida + línea de input. JS vanilla con
  un diccionario de comandos (`help`, `whoami`, `ls projects`, `cat cv`, `skills`, `contact`, `sdd`,
  `clear`) + easter eggs (`sudo hire-me`, `matrix`). Historial con ↑/↓, autoscroll. Sin datos sensibles.
- **Compatibilidad:** el widget del asistente (fixed) y la command palette (Cmd/Ctrl+K) no se tocan; la
  paleta nueva también aplica a ellos vía variables.

## Risks / Trade-offs

- **Tabs ocultan secciones del scroll** → el IntersectionObserver `fade-in` deja de tener sentido por
  sección; se aplica `visible` a la sección activa al mostrarla. [Riesgo] SEO: el contenido sigue en el DOM
  (display:none), indexable; los crawlers leen el HTML completo.
- **Reemplazos de color hardcoded** → riesgo de dejar algún azul; mitigación: grep final de `88,166,255` y
  `#58a6ff` debe quedar vacío (salvo el CV, que no se toca).
- **Contraste** del café-dorado sobre café oscuro → validar AA; ajustar `--primary`/`--fg` si hace falta.

## Migration Plan

1. Branch `feature/rediseno-cafe-tabs`.
2. Implementar paleta + matrix; luego tabs; luego terminal.
3. Verificación manual (serve, 3 breakpoints, tabs cambian, terminal responde, widget+palette OK, 0 azules).
4. Actualizar docs (paleta) en el mismo PR. Merge → CI/CD despliega.
Rollback: revertir el commit (un solo archivo + docs).

## Open Questions

- ¿La sección por defecto al cargar es "AI Method" o un breve "Home"? (Default: AI Method.)
- ¿Terminal como una pestaña más del menú o también como atajo flotante? (Default: pestaña del menú.)
