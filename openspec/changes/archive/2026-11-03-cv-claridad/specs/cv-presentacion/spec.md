# Capability: cv-presentacion (delta)

## MODIFIED Requirements

### Requirement: Tipografía legible al imprimir (mínimo 8.5pt) en 1 página
El CV (`cv/cv.html`, `cv/cv-en.html`) SHALL usar una tipografía legible al imprimir: **ningún texto por debajo
de 8.5pt** (≈11.3px), cuerpo a ~8.5–9pt, encabezados/títulos prominentes, y MUST mantenerse en **1 página A4
(210×297 mm)**. El interlineado de listas de bullets (`ul.b li`) MAY reducirse hasta 1.22 para conservar la
página.

#### Scenario: Tamaños mínimos
- **WHEN** se revisa el CSS del CV
- **THEN** el cuerpo (resumen, bullets, descripciones, skills) es ≥ 11.3px (8.5pt) y los encabezados de sección
  y el nombre son notablemente más grandes (headings ~14px, role ~13px, nombre ~22px con el nombre completo)
- **AND** `ul.b li` tiene `line-height` ≥ 1.22
- **AND** el CV se mantiene en **1 página** (verificado por conteo real del árbol de páginas del PDF)

#### Scenario: Tamaño de página A4
- **WHEN** se revisa la regla `@page` de `cv.html` y `cv-en.html` y el `/MediaBox` de ambos PDFs
- **THEN** `@page` declara `size: 210mm 297mm` (o `A4`)
- **AND** el `/MediaBox` de cada PDF mide ≈ 595×842 pt

#### Scenario: Estrategia de espacio para 1 página
- **WHEN** el contenido no cabe en la página
- **THEN** se recorta contenido según `cv-contenido-claro` (límites de bullets, 5 categorías, 3 proyectos)
  antes de tocar la tipografía, sin reducir la letra bajo 8.5pt ni quitar datos de contacto, roles o fechas
- **AND** la regla de cabida verificada es: altura del `.sheet` ≤ 297 mm (medida en Chrome headless); el
  conteo real de páginas del PDF es la comprobación final
