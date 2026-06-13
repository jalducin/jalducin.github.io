# Capability: cv-presentacion

## ADDED Requirements

### Requirement: Idiomas en la columna derecha del CV
La sección **Idiomas** del CV (`cv/cv.html` y `cv/cv-en.html`) DEBE ubicarse en la **columna derecha**,
e incluir **Español (Nativo)** e **Inglés (B1 · B2 lectura y escritura técnica)**.

#### Scenario: Render del CV
- **WHEN** se renderiza el CV a PDF
- **THEN** la sección Idiomas aparece en la columna derecha (no en la izquierda)
- **AND** lista Español (Nativo, 5/5) e Inglés (3/5)
- **AND** el CV se mantiene en **1 página** tamaño Oficio (216×340 mm)

#### Scenario: CV en inglés equivalente
- **WHEN** se revisa `cv/cv-en.html`
- **THEN** existe con el mismo diseño y secciones que el CV en español, con el contenido traducido al inglés
- **AND** Languages lista Spanish (Native) y English (B1 · B2 technical reading & writing)
