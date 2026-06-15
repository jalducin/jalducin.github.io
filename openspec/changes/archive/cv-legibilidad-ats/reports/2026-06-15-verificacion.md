# Reporte — verificación y 3 agentes (cv-legibilidad-ats)

- Fecha: 2026-06-15
- Cambio: cv-legibilidad-ats

## Verificación
- PDFs regenerados con `cv/build.ps1` (`--headless=new`).
- **1 página** por conteo real del árbol de páginas: **ES=1, EN=1**.
- Bullet 4 de Podemos (ES) corregido (estaba triplicado por un `&` en un sed de reemplazo).

## Resultados de los 3 agentes

### 🎨 design-specialist → 7.5/10 · APTO CON OBSERVACIONES
- **CRÍTICO**: bullet 4 de Podemos (`cv/cv.html:114`) triplicado/corrupto → **CORREGIDO** (reescrito limpio).
- Medio/leve: header QR caption algo pegado al borde; columna izquierda densa; `section margin 1px` casi nulo
  → **aplicado** `section margin 1px→3px` para más respiro. Resto cosmético.
- Confirmó: cabe en 1 página, jerarquía clara, paleta navy/acento sin residuos.

### 🤖 ats-reviewer → 7.5/10 · APTO CON OBSERVACIONES
- PASS: capa de texto, contacto como texto (tel/email/portafolio/LinkedIn/GitHub), headings estándar, orden de
  lectura del DOM coherente, fechas, nombre de archivo, keywords.
- **ALTO**: mismo bullet corrupto → **CORREGIDO**.
- **Medio**: captions de QR aparecían como palabras sueltas en el parseo → **aplicado** `aria-hidden="true"` en los QR.
- **Bajo**: acentos como `?` en `pdftotext` v4 (artefacto de extractor viejo; ATS modernos manejan UTF-8). Monitorear.

### 🛡️ compliance-reviewer → no disponible en sesión (registry)
- Validación **manual = APTO**: sin secretos/credenciales, PII solo la pública del dueño, claims consistentes,
  marcas nominativas, sin enlaces a backends caídos. Sin cambios de contenido legal en este change.

## Resultado
- Estado: **PASS / APTO CON OBSERVACIONES** (la observación crítica fue corregida). 1 página ES/EN.
