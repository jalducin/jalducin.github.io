## ADDED Requirements

### Requirement: El QR apunta al sitio en AWS conservando el estilo

El código QR del CV (`assets/img/QR.png`) SHALL codificar la URL del **sitio en AWS** (la distribución
CloudFront, p. ej. `https://d3r3bnavnwzqaw.cloudfront.net`, o el dominio canónico vigente), en lugar del
repositorio. MUST conservar el **mismo estilo visual** del QR actual (módulos negros con el ícono/logo
"JVAV" del robot al centro) para mantener la identidad.

#### Scenario: Escanear el QR abre el sitio en AWS
- **WHEN** alguien escanea el QR del CV
- **THEN** se abre la URL del sitio en AWS (CloudFront / dominio canónico), no la del repositorio de GitHub

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
- **THEN** coincide con la URL canónica del sitio usada en el resto (JSON-LD, og, sitemap); si más adelante
  se adopta dominio propio, el QR se regenera para apuntar a ese dominio

### Requirement: El QR DEBE ser escaneable de forma fiable (verificado)

El QR SHALL ser legible por lectores reales de celular. El ícono central NO debe romper la decodificación.
Es un requisito duro: un QR bonito que no escanea es un defecto.

#### Scenario: Parámetros que garantizan lectura
- **WHEN** se genera el QR con logo central
- **THEN** usa **corrección de errores nivel H** (~30%) para tolerar el logo
- **AND** el ícono central ocupa como máximo ~20-25% del área (sin cubrir patrones de posición/timing)
- **AND** mantiene **zona de silencio** (quiet zone ≥ 4 módulos) y **alto contraste** (módulos oscuros sobre fondo claro)

#### Scenario: Verificación con lector real (OBLIGATORIO)
- **WHEN** se termina el QR
- **THEN** se **decodifica/escanea** (lector de celular y/o decodificador de software) y abre la URL del sitio AWS
- **AND** no se da por terminado hasta confirmar que al menos un lector real lo lee correctamente
