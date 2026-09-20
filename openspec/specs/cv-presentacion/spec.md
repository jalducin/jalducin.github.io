# Capability: cv-presentacion

## Purpose

Garantiza que el CV en PDF (`cv/cv.html`, `cv/cv-en.html`) sea legible al imprimir, quepa en 1 página Oficio,
sea parseable por sistemas ATS y se genere con un build determinista y sin dependencias de red, para
reclutadores humanos y sistemas de selección automatizada.

## Requirements

### Requirement: Tipografía legible al imprimir (mínimo 8.5pt) en 1 página
El CV (`cv/cv.html`, `cv/cv-en.html`) SHALL usar una tipografía legible al imprimir: **ningún texto por debajo
de 8.5pt** (≈11.3px), cuerpo a ~8.5–9pt, encabezados/títulos prominentes, y MUST mantenerse en **1 página
Oficio**. El interlineado de listas de bullets (`ul.b li`) MAY reducirse hasta 1.22 para conservar la página.

#### Scenario: Tamaños mínimos
- **WHEN** se revisa el CSS del CV
- **THEN** el cuerpo (resumen, bullets, descripciones, skills) es ≥ 11.3px (8.5pt) y los encabezados de sección
  y el nombre son notablemente más grandes (headings ~14px, role ~13px, nombre ~22px con el nombre completo)
- **AND** `ul.b li` tiene `line-height` ≥ 1.22
- **AND** el CV se mantiene en **1 página** (verificado por conteo real del árbol de páginas del PDF)

#### Scenario: Estrategia de espacio para 1 página
- **WHEN** se necesita más espacio para el contenido nuevo (dos roles en Podemos, cifras de Fidello)
- **THEN** se compactan bullets a ≤ ~125 caracteres (2 líneas), se acortan descripciones de proyectos a
  1–2 líneas, la sección Idiomas se coloca en la columna con más holgura (hoy la izquierda, bajo Educación),
  el QR de Portafolio va en el header, el interlineado del cuerpo puede bajar hasta 1.25 y se podan bullets
  de menor impacto — sin reducir la letra bajo 8.5pt ni quitar datos de contacto, roles o fechas
- **AND** la regla de cabida verificada es: altura del `.sheet` ≤ 340 mm (medida en Chrome headless); el
  conteo real de páginas del PDF es la comprobación final

### Requirement: Header con QR y etiqueta alineados
El header SHALL alinear arriba (`align-items:flex-start`) de modo que cada QR (LinkedIn arriba-izquierda,
Portafolio arriba-derecha) tenga su etiqueta directamente debajo y alineada con el nombre.

#### Scenario: QR + caption juntos
- **WHEN** se renderiza el encabezado
- **THEN** el QR y su `<figcaption>` forman un bloque alineado al tope, junto al nombre (sin desfase)

### Requirement: CV optimizado para ATS
El CV SHALL ser parseable por ATS: PDF con capa de texto, datos de contacto como **texto** (no solo QR),
encabezados estándar y los QR marcados `aria-hidden` para que los parsers omitan sus captions.

#### Scenario: Contacto y parseo
- **WHEN** un ATS extrae el texto del PDF
- **THEN** obtiene nombre completo, teléfono, email, portafolio, LinkedIn y GitHub como texto
- **AND** las `<figure class="qr">` llevan `aria-hidden="true"`
- **AND** el contenido no contiene texto corrupto/duplicado (p. ej. residuos de escapes)

### Requirement: Tipografía del sistema y build determinista

El CV (`cv/cv.html`, `cv/cv-en.html`) SHALL usar exclusivamente tipografía del sistema
(`"Segoe UI", Arial, sans-serif`) y NO cargar web fonts externas (Google Fonts u otras), de modo que
`cv\build.ps1` produzca el mismo PDF con o sin red y las fuentes embebidas sean TrueType reales.

#### Scenario: Sin dependencias de red en el build
- **WHEN** se revisa el `<head>` de `cv/cv.html` y `cv/cv-en.html`
- **THEN** no existe ningún `<link>` a `fonts.googleapis.com` / `fonts.gstatic.com` ni `@import` de fuentes
- **AND** `font-family` del cuerpo inicia con `"Segoe UI"`

#### Scenario: Fuentes embebidas verificables
- **WHEN** se inspeccionan los objetos `/Font` del PDF generado
- **THEN** todas las fuentes son subconjuntos TrueType de Segoe UI (p. ej. `SegoeUI`, `SegoeUI-Bold`) y no
  hay fuentes `Type3`
- **AND** el PDF tiene exactamente 1 página (conteo real del árbol de páginas)

### Requirement: Borrador Markdown del CV sincronizado

El repositorio SHALL mantener `cv/CV_JuanValentinAlducin.md` como borrador editable (espejo del contenido
ES) para revisión humana y LinkedIn; NO es la fuente del PDF.

#### Scenario: El borrador refleja el CV vigente
- **WHEN** se compara `cv/CV_JuanValentinAlducin.md` con `cv/cv.html` tras un cambio de contenido
- **THEN** títulos de rol, fechas, bullets, educación, cursos, skills y proyectos coinciden en texto
- **AND** el archivo lleva un comentario inicial que indica que la fuente canónica es `cv/cv.html`
