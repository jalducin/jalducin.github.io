# Capability: posicionamiento-ai-native

## Purpose

Garantiza que el header, el resumen y los metadatos del portafolio comuniquen el posicionamiento híbrido
(Senior Backend Engineer · Tech Lead · SRE & Automation · Agentic AI) alineado al CV vigente, para
reclutadores, crawlers y redes sociales.

## Requirements

### Requirement: Header alineado al posicionamiento AI-native del CV

El header del sitio SHALL reflejar el posicionamiento **híbrido** del CV vigente: *Senior Backend Engineer*
con eje *Tech Lead · SRE & Automation* y *Agentic AI*. El nombre, el tagline y la ubicación/idioma MUST
coincidir con la fuente de verdad (`cv/cv.html`, `cv/cv-en.html`, `CLAUDE.md`, `docs/frontend-standards.md`).

#### Scenario: Tagline del header refleja el posicionamiento híbrido
- **WHEN** un visitante carga `index.html`
- **THEN** el subtítulo (`header h3`) presenta exactamente los tres ejes: "Senior Backend Engineer",
  "Tech Lead · SRE & Automation" y "Agentic AI"
- **AND** la línea de ubicación muestra "CDMX, Mexico" y nivel de inglés "B1"
- **AND** el tagline del CV (`.tagline`) en ES y EN usa el mismo texto:
  "Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI"

#### Scenario: Datos de contacto consistentes con la fuente de verdad
- **WHEN** se revisan los enlaces del header (email, WhatsApp, descarga de CV)
- **THEN** el email es `valentin.alducin88@gmail.com`
- **AND** el enlace de WhatsApp usa el número `525640800494`
- **AND** los botones de descarga apuntan a `cv/CV_JuanValentinAlducin.pdf` y `cv/CV_JuanValentinAlducin_EN.pdf`
  con atributo `download`

### Requirement: Resumen profesional alineado al CV

El párrafo de resumen SHALL comunicar el mensaje del CV: +10 años en backend y sistemas distribuidos;
**confiabilidad y automatización** como firma actual (post-mortems, uptime, runbooks, pipelines n8n /
spec-driven); IA generativa (Claude, Gemini, OpenAI) como copiloto del SDLC con Spec-Driven Development; y
métricas de impacto verificables.

#### Scenario: Resumen comunica confiabilidad, automatización, IA y métricas
- **WHEN** un visitante lee el resumen del header
- **THEN** el texto menciona +10 años de experiencia backend
- **AND** menciona confiabilidad/SRE (post-mortems, uptime) y automatización (n8n, pipelines spec-driven)
- **AND** referencia la integración de IA generativa (Claude, Gemini, OpenAI) y Spec-Driven Development (SDD)
- **AND** incluye al menos dos métricas de impacto entre: ~40 % menos tiempo de revisión, 80 % de
  autoresolución N1, primera respuesta <10 min, uptime mensual 99.95 %
- **AND** no menciona programas académicos en curso (la Maestría en DevOps fue retirada)

### Requirement: Metadatos sociales y de pestaña consistentes

Los metadatos (`<title>`, Open Graph, Twitter Card, `meta description`, `meta keywords`) SHALL reflejar el
posicionamiento híbrido para una previsualización coherente al compartir el enlace.

#### Scenario: Open Graph y title coherentes con el posicionamiento
- **WHEN** un crawler o red social lee el `<head>` de `index.html`
- **THEN** `og:title`/`twitter:title` y `<title>` incluyen el nombre completo y
  "Senior Backend Engineer · Tech Lead · SRE & Automation · Agentic AI"
- **AND** `og:description`/`twitter:description`/`meta description` resumen el perfil híbrido sin datos
  obsoletos (sin maestría, sin Kendra/Kiro)
- **AND** `meta keywords` incluye "SRE", "reliability", "post-mortems", "n8n", "automation", "Spec-Driven
  Development" además de las keywords AI/AWS existentes
- **AND** el comando `whoami` de la terminal devuelve el mismo headline
