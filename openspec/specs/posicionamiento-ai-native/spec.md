# Capability: posicionamiento-ai-native

## Requirements

### Requirement: Header alineado al posicionamiento AI-native del CV

El header del sitio SHALL reflejar el posicionamiento del CV vigente: *Senior Software Engineer* con
énfasis en *AI-native Development*. El nombre, el tagline y la ubicación/idioma MUST coincidir con la
fuente de verdad (`CV_JuanValentinAlducin.pdf` y `docs/frontend-standards.md`).

#### Scenario: Tagline del header refleja AI-native Development
- **WHEN** un visitante carga `index.html`
- **THEN** el subtítulo (`header h3`) presenta "Senior Software Engineer" junto a "AI-native Development"
  como eje principal del posicionamiento
- **AND** la línea de ubicación muestra "CDMX, Mexico" y nivel de inglés "B1"

#### Scenario: Datos de contacto consistentes con la fuente de verdad
- **WHEN** se revisan los enlaces del header (email, WhatsApp, descarga de CV)
- **THEN** el email es `valentin.alducin88@gmail.com`
- **AND** el enlace de WhatsApp usa el número `525640800494`
- **AND** el botón de descarga apunta a `CV_JuanValentinAlducin.pdf` con atributo `download`

### Requirement: Resumen profesional alineado al CV

El párrafo de resumen SHALL comunicar el mensaje del CV: +10 años en backend, integración de
Generative AI / LLMs (Claude, Gemini, OpenAI) como copiloto central del SDLC, impulso de Spec-Driven
Development y las métricas de impacto verificables.

#### Scenario: Resumen comunica IA como núcleo del SDLC y métricas
- **WHEN** un visitante lee el resumen del header
- **THEN** el texto menciona +10 años de experiencia backend y la integración de IA generativa (Claude,
  Gemini, OpenAI) como parte central del flujo de ingeniería
- **AND** referencia Spec-Driven Development (SDD) como práctica
- **AND** incluye al menos una métrica de impacto (reducción del ciclo de revisión ~40% y/o 80% de
  autoresolución de incidentes)

### Requirement: Metadatos sociales y de pestaña consistentes

Los metadatos (`<title>`, Open Graph y Twitter Card) SHALL reflejar el posicionamiento AI-native para
una previsualización coherente al compartir el enlace.

#### Scenario: Open Graph y title coherentes con el posicionamiento
- **WHEN** un crawler o red social lee el `<head>` de `index.html`
- **THEN** `og:title`/`twitter:title` y `<title>` incluyen el nombre completo y el rol Senior Software
  Engineer con énfasis AI-native
- **AND** `og:description`/`twitter:description` resumen el perfil sin datos obsoletos
