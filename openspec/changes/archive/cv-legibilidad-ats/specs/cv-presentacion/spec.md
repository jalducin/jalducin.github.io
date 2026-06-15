# Capability: cv-presentacion (delta)

## MODIFIED Requirements

### Requirement: Tipografía legible al imprimir (mínimo 8.5pt) en 1 página
El CV (`cv/cv.html`, `cv/cv-en.html`) DEBE usar una tipografía legible al imprimir: **ningún texto por debajo
de 8.5pt** (≈11.3px), cuerpo a ~8.5–9pt, encabezados/títulos prominentes, manteniendo **1 página Oficio**.

#### Scenario: Tamaños mínimos
- **WHEN** se revisa el CSS del CV
- **THEN** el cuerpo (resumen, bullets, descripciones, skills) es ≥ 11.3px (8.5pt) y los encabezados de sección
  y el nombre son notablemente más grandes (headings ~14px, role ~13px, nombre ~22px con el nombre completo)
- **AND** el CV se mantiene en **1 página** (verificado por conteo real del árbol de páginas del PDF)

#### Scenario: Estrategia de espacio para 1 página
- **WHEN** se necesita más espacio para subir la letra
- **THEN** se acortan descripciones de proyectos a 1 línea, Idiomas va a la columna derecha, el QR de Portafolio
  va en el header (arriba-derecha) y se podan cursos/bullets de menor impacto — sin reducir la letra bajo 8.5pt

### Requirement: Header con QR y etiqueta alineados
El header DEBE alinear arriba (`align-items:flex-start`) de modo que cada QR (LinkedIn arriba-izquierda,
Portafolio arriba-derecha) tenga su etiqueta directamente debajo y alineada con el nombre.

#### Scenario: QR + caption juntos
- **WHEN** se renderiza el encabezado
- **THEN** el QR y su `<figcaption>` forman un bloque alineado al tope, junto al nombre (sin desfase)

### Requirement: CV optimizado para ATS
El CV DEBE ser parseable por ATS: PDF con capa de texto, datos de contacto como **texto** (no solo QR),
encabezados estándar y los QR marcados `aria-hidden` para que los parsers omitan sus captions.

#### Scenario: Contacto y parseo
- **WHEN** un ATS extrae el texto del PDF
- **THEN** obtiene nombre completo, teléfono, email, portafolio, LinkedIn y GitHub como texto
- **AND** las `<figure class="qr">` llevan `aria-hidden="true"`
- **AND** el contenido no contiene texto corrupto/duplicado (p. ej. residuos de escapes)
