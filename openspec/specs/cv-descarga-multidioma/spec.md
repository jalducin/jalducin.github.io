# Capability: cv-descarga-multidioma

## ADDED Requirements

### Requirement: Descarga del CV con sufijo mes-año dinámico
Al descargar el CV desde el portafolio, el nombre de archivo DEBE incluir un sufijo **mes-año** calculado
al vuelo con la fecha actual (formato `AAAA-MM`), sin build step ni generación del PDF en el navegador.

#### Scenario: Descarga del CV en español
- **WHEN** un visitante usa cualquier acción de descarga del CV en español
- **THEN** el archivo descargado se nombra `CV_JuanValentinAlducin_AAAA-MM.pdf` (p. ej. `..._2026-06.pdf`)
- **AND** el binario servido es el artefacto estático `cv/CV_JuanValentinAlducin.pdf` versionado en el repo

#### Scenario: Sufijo dinámico
- **WHEN** cambia el mes/año del sistema del visitante
- **THEN** el sufijo del nombre de descarga refleja el mes-año actual sin cambios de código

### Requirement: Versión del CV en inglés descargable
El portafolio DEBE ofrecer la descarga del CV en **inglés** donde aplique (sección Contact, command palette
y terminal), sirviendo `cv/CV_JuanValentinAlducin_EN.pdf`.

#### Scenario: Botón/acción EN
- **WHEN** un visitante usa la acción de descarga del CV en inglés
- **THEN** se descarga `CV_JuanValentinAlducin_EN_AAAA-MM.pdf` desde `cv/CV_JuanValentinAlducin_EN.pdf`
- **AND** la sección Contact muestra ambos botones (ES y EN), y existe comando de terminal `cat cv en`

#### Scenario: Build de ambos PDFs
- **WHEN** se ejecuta `cv/build.ps1`
- **THEN** se regeneran los dos PDFs: `CV_JuanValentinAlducin.pdf` (desde cv.html) y
  `CV_JuanValentinAlducin_EN.pdf` (desde cv-en.html), ambos de 1 página
