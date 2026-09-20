## ADDED Requirements

### Requirement: Imagen Open Graph propia

El sitio SHALL exponer una imagen social (`og:image`) propia para que el enlace se previsualice de forma
profesional al compartirse. La imagen MUST generarse con el mismo pipeline estático del CV (Chrome/Edge
headless desde una fuente HTML), sin servicios de terceros en runtime.

#### Scenario: Metadatos de imagen presentes y válidos
- **WHEN** un crawler o red social lee el `<head>` de `index.html`
- **THEN** existen `og:image` (y `twitter:image`) apuntando a un archivo del sitio de 1200×630 px
- **AND** `twitter:card` es `summary_large_image`

#### Scenario: La imagen es coherente y reproducible
- **WHEN** se inspecciona el artefacto de la social card
- **THEN** muestra el nombre, el tagline AI-native y la URL del sitio, consistente con el resto del perfil
- **AND** existe una fuente HTML versionada y un comando documentado para regenerarla
