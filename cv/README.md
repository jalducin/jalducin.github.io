# CV — fuente self-hosted (sin enhancv)

El CV del portafolio se genera **dentro del repo**, sin depender de enhancv ni de suscripciones.

## Archivos

- `cv.html` (ES) y `cv-en.html` (EN) — **fuentes editables** del CV (formato estilo enhancv "hexagon",
  tamaño Oficio, 1 página). Edita el texto aquí.
- `CV_JuanValentinAlducin.md` — borrador editable en Markdown (espejo del contenido ES) para ajustar
  texto cómodamente y luego volcarlo a los HTML; **no** es la fuente del PDF.
- `hex-bg.svg` — patrón de hexágonos de fondo.
- `build.ps1` — regenera el PDF con Chrome/Edge headless.
- El PDF resultante se escribe en `cv/CV_JuanValentinAlducin.pdf`, que es el archivo que
  descarga el sitio (`index.html` → botón "Download CV").

## Regenerar el PDF

```powershell
powershell -ExecutionPolicy Bypass -File cv\build.ps1
```

O manual:

```powershell
& "$env:ProgramFiles\Google\Chrome\Application\chrome.exe" --headless --disable-gpu `
  --no-pdf-header-footer --print-to-pdf="cv\CV_JuanValentinAlducin.pdf" "cv\cv.html"
```

## Notas

- **Tipografía: "Segoe UI" (fuente del sistema), sin Google Fonts.** Antes el HTML cargaba Rubik desde
  fonts.googleapis.com; en el build headless a veces llegaba y a veces no, y con Rubik (más ancha) el CV
  saltaba a 2 páginas. Con la fuente del sistema el build es determinista y el PDF embebe TrueType real
  (mejor para ATS que los Type3 que genera Chrome con web fonts).
- **Tamaño Oficio (México): 216 × 340 mm** (definido en `@page` de `cv.html`).
- **ATS-friendly**: texto real (no imágenes), encabezados estándar, orden de lectura limpio, fuentes
  embebidas. El QR usa `assets/img/QR.png` y apunta al sitio en AWS (CloudFront,
  `https://d3r3bnavnwzqaw.cloudfront.net`) — corrección de errores H, ícono JVAV centrado, verificado con
  decodificador (ver `openspec/changes/asistente-ia-portafolio/specs/qr-apunta-al-sitio-aws/`).
- Diseño y fidelidad: ver el agente `design-specialist` en `ai-specs/agents/`.
- Datos del propietario (fuente de verdad): `CLAUDE.md` y `docs/frontend-standards.md`.
