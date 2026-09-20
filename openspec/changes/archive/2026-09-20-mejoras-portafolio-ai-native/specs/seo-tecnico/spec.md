## ADDED Requirements

### Requirement: Indexabilidad técnica del sitio

El sitio SHALL exponer los artefactos SEO estándar para ser correctamente rastreado e indexado.

#### Scenario: robots.txt y sitemap presentes
- **WHEN** un crawler solicita `/robots.txt`
- **THEN** existe y permite el rastreo, referenciando `/sitemap.xml`
- **AND** `/sitemap.xml` existe, es XML válido e incluye la URL canónica del sitio

#### Scenario: URL canónica declarada
- **WHEN** se inspecciona el `<head>` de `index.html`
- **THEN** existe `<link rel="canonical">` apuntando a `https://jalducin.github.io`
- **AND** los metadatos (title, description, og) no contienen datos obsoletos
