# CV — fuente self-hosted (sin enhancv)

El CV del portafolio se genera **dentro del repo**, sin depender de enhancv ni de suscripciones.

## Archivos

- `cv.html` — **fuente editable** del CV (formato estilo enhancv "hexagon", tamaño Oficio, 1 página).
  Edita el texto aquí.
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

- **Tamaño Oficio (México): 216 × 340 mm** (definido en `@page` de `cv.html`).
- **ATS-friendly**: texto real (no imágenes), encabezados estándar, orden de lectura limpio, fuentes
  embebidas. El QR usa `assets/img/QR.png` y vincula al repositorio del portafolio.
- Diseño y fidelidad: ver el agente `design-specialist` en `ai-specs/agents/`.
- Datos del propietario (fuente de verdad): `CLAUDE.md` y `docs/frontend-standards.md`.
