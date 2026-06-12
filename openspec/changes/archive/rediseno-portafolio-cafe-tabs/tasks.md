## 0. Preparación (OBLIGATORIO — PRIMERO)

- [x] 0.1 Leer `docs/base-standards.md`, `docs/frontend-standards.md`, `openspec/config.yaml`
- [x] 0.2 Crear feature branch `feature/rediseno-cafe-tabs`

## 1. paleta-cafe-elegante

- [x] 1.1 Actualizar tokens CSS (`:root` y `html.light`) a la paleta café/dorado/ámbar
- [x] 1.2 Reemplazar glows/acentos hardcoded (`rgba(88,166,255,*)` → `rgba(200,146,74,*)`, `#58a6ff` → `#c8924a`)
- [x] 1.3 Recolorear el matrix (color de lluvia ámbar + fillStyle de fondo `#17120e`)
- [x] 1.4 Verificar contraste AA y tema claro cálido

## 2. navegacion-por-secciones (tabs)

- [x] 2.1 Marcar secciones como `.tabpage` (ocultas salvo `.active`) y añadir ítem "Terminal" al nav
- [x] 2.2 JS de tabs: click en nav → muestra grupo (Skills = hard+soft), oculta resto, `aria-current`, scroll al inicio
- [x] 2.3 Estado inicial (hash o AI Method); atajos/anclas siguen funcionando; hamburguesa en móvil

## 3. terminal-interactiva

- [x] 3.1 Sección Terminal (HTML + CSS on-brand) con salida + input
- [x] 3.2 JS de comandos (`help`, `whoami`, `ls projects`, `cat cv`, `skills`, `contact`, `sdd`, `clear`) + desconocido
- [x] 3.3 Easter eggs (`sudo hire-me`, `matrix`) + historial ↑/↓ + autoscroll

## 4. Verificación (OBLIGATORIO — EL AGENTE EJECUTA)

- [x] 4.1 Servir local; verificar tabs (una a la vez + activo), terminal responde, widget+command palette OK
- [x] 4.2 3 breakpoints (992/768/480); `prefers-reduced-motion`; grep `88,166,255`/`#58a6ff` → 0 (fuera de cv/)
- [x] 4.3 Reporte en `openspec/changes/rediseno-portafolio-cafe-tabs/reports/AAAA-MM-DD-verificacion.md`

## 5. Documentación + cierre (OBLIGATORIO)

- [x] 5.1 Actualizar paleta en `CLAUDE.md` y `docs/frontend-standards.md`
- [x] 5.2 Commit + merge a main (CI/CD despliega) + archivar el cambio
