# Capability: qr-apunta-al-sitio-aws (delta)

## MODIFIED Requirements

### Requirement: El QR apunta al sitio en AWS conservando el estilo

El código QR del CV (`assets/img/QR.png`) SHALL codificar la **URL canónica del sitio**,
`https://jalducin.github.io` (GitHub Pages), en lugar del repositorio o de un hosting dado de baja. Si en el
futuro hay dominio propio, el QR se regenera para apuntar a ese dominio. MUST conservar el **mismo estilo visual** del QR actual (módulos negros con el ícono/logo
"JVAV" del robot al centro) para mantener la identidad.

#### Scenario: Escanear el QR abre el sitio publicado
- **WHEN** alguien escanea el QR del CV
- **THEN** se abre `https://jalducin.github.io`, no el repositorio de GitHub ni una URL dada de baja
- **AND** la URL codificada se verifica decodificando la imagen (p. ej. `cv2.QRCodeDetector`) tras cada regeneración

#### Scenario: Estilo visual preservado
- **WHEN** se compara el nuevo QR con el actual
- **THEN** mantiene la estética (módulos negros, ícono "JVAV" del robot centrado, misma apariencia general)
- **AND** sigue siendo legible/escaneable (contraste y zona de silencio correctos)

#### Scenario: El CV usa el QR actualizado
- **WHEN** se regenera el CV (`cv/cv.html` → PDF)
- **THEN** el CV muestra el QR actualizado desde `assets/img/QR.png`
- **AND** una sola fuente de verdad para el QR (no copias divergentes)

#### Scenario: URL única de verdad
- **WHEN** se decide la URL destino del QR
- **THEN** el QR apunta al despliegue en AWS (`https://d3r3bnavnwzqaw.cloudfront.net`) porque el sitio se sirve
  desde ahí, mientras que la **URL canónica pública** (JSON-LD, `og:url`, `canonical`, `sitemap.xml`, CV y
  LinkedIn) se mantiene en `https://jalducin.github.io` por ser la marca del candidato y seguir GitHub Pages en
  paralelo (decisión del propietario, 2026-09-20)
- **AND** ambas URLs sirven el mismo `index.html` (mismo commit de `main`); si más adelante se adopta dominio
  propio, QR y canónica convergen en ese dominio y el QR se regenera

