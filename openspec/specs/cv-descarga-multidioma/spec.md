# Capability: cv-descarga-multidioma (delta)

## MODIFIED Requirements

### Requirement: Ícono representativo de CV/résumé en los botones de descarga
Los botones de descarga del CV en el hero (ES y EN) DEBEN usar un ícono **de currículum/résumé**
(una hoja con un busto de persona — cabeza y hombros — y líneas de texto), NO una flecha de "subir/upload".

#### Scenario: Ícono del botón de CV
- **WHEN** un visitante ve los botones de descarga del CV en el hero
- **THEN** el glifo es un ícono tipo résumé (hoja + persona), renderizado en **dorado** (`--primary`)
- **AND** se conservan las etiquetas **ES** y **EN** que distinguen cada idioma
- **AND** NO aparece una flecha de "subir/upload" como glifo

#### Scenario: Comportamiento de descarga intacto
- **WHEN** se usa cualquiera de los dos botones
- **THEN** la descarga sigue funcionando con el sufijo mes-año dinámico
  (`CV_JuanValentinAlducin_AAAA-MM.pdf` / `..._EN_AAAA-MM.pdf`) y los atributos `data-cv` / `download`
- **AND** el ícono es **SVG inline** (sin CDN) y hereda el color con `currentColor`
