# Proposal — cv-legibilidad-ats

## Why

Una validación estilo reclutador (imprimir el CV) reveló que el cuerpo estaba **muy pequeño** (~7.2pt).
Hay que subir la tipografía a un tamaño legible al imprimir, **manteniendo 1 página Oficio** y el diseño,
y dejar el CV óptimo para **ATS** (texto extraíble, nombre completo, contacto como texto). Este cambio
**formaliza** (SDD) el trabajo iterativo reciente del CV y lo valida con los 3 agentes de revisión.

## What changes

- **Tipografía legible (escala 8.5/9/10pt, nada por debajo de 8.5pt)**: cuerpo 11.3px (~8.5pt), sub-labels 12px,
  encabezados 14px, role 13px, **nombre completo** 22px. Títulos grandes conservados.
- **Cabe en 1 página** recortando sin bajar de 8.5pt: descripciones de proyectos a 1 línea, Idiomas a la
  columna derecha, **QR de Portafolio movido al header** (arriba-derecha, junto al nombre), se quita el curso
  edX y un bullet de Redsis (se conserva lo de más impacto); resumen y bullets de Podemos más tersos.
- **Header alineado arriba** (`align-items:flex-start`): cada QR con su etiqueta debajo y alineado con el nombre.
- **ATS**: contacto como **texto** (tel, email, portafolio, LinkedIn, GitHub), `aria-hidden` en los QR para que
  los parsers omitan sus captions; nombre completo visible.
- **Fix crítico**: bullet 4 de Podemos en `cv/cv.html` quedó triplicado por un sed (`&` en reemplazo) → reescrito limpio.
- **build.ps1**: `--headless=new` (motor de impresión moderno).

## Impact

- Specs: modifica `cv-presentacion` (tamaños mínimos + header + ATS).
- Archivos: `cv/cv.html`, `cv/cv-en.html`, `cv/build.ps1`, PDFs regenerados.
- Despliegue por CI/CD (push a `main` → AWS).
