# Capability: agentic-engineering-hardening

## Requirements

### Requirement: Sección "How I build with AI" (metodología agentic)

El sitio SHALL incluir una sección dedicada que explique el método de trabajo AI-native / agentic del
candidato, demostrando el *cómo* con métricas verificables, no solo declarando herramientas.

#### Scenario: La sección comunica el método y las métricas
- **WHEN** un visitante navega a la sección de metodología AI-native
- **THEN** se describe el flujo Spec-Driven Development (proposal → specs → design → tasks → apply →
  archive) como práctica central
- **AND** se mencionan las herramientas (Claude/Anthropic, Gemini, OpenAI) como copilotos del SDLC
- **AND** se muestran las métricas de impacto: ~40% de reducción del ciclo de revisión, 80% de
  autoresolución de incidentes N1, primera respuesta <10 min y resolución de incidentes <2 h

#### Scenario: La sección es accesible desde la navegación
- **WHEN** se carga el sitio
- **THEN** existe un enlace de navegación hacia la sección de metodología AI-native
- **AND** la sección respeta el sistema de diseño y el responsive (992/768/480px)

### Requirement: Datos estructurados JSON-LD (Schema.org Person)

El `<head>` de `index.html` SHALL incluir un bloque JSON-LD válido de tipo `Person` (Schema.org) para
que buscadores y agentes/LLMs interpreten el perfil de forma estructurada.

#### Scenario: JSON-LD Person válido y consistente
- **WHEN** un crawler o agente parsea el `<script type="application/ld+json">`
- **THEN** el JSON es válido y de `@type: Person`
- **AND** incluye al menos `name`, `jobTitle` (Senior Software Engineer, AI-native), `email`, `url`,
  `sameAs` (GitHub, LinkedIn), `address` (CDMX, Mexico) y `knowsAbout` (skills clave)
- **AND** los valores coinciden con la fuente de verdad (sin datos obsoletos de WhatsApp o inglés)

### Requirement: Capa AI-readable (`llms.txt` y meta)

El proyecto SHALL exponer un archivo estático `llms.txt` en la raíz del sitio con un resumen del perfil
orientado a agentes/LLMs, y meta tags coherentes en `index.html`.

#### Scenario: llms.txt presente y descriptivo
- **WHEN** un agente solicita `/llms.txt`
- **THEN** el archivo existe y resume en texto plano/Markdown: quién es, posicionamiento AI-native,
  stack principal, métricas y enlaces (GitHub, LinkedIn, CV)
- **AND** el contenido es consistente con `index.html`, el CV y el JSON-LD (una sola fuente de verdad por
  dato; los demás enlazan/derivan, no contradicen)

#### Scenario: Meta description AI-readable
- **WHEN** se inspecciona el `<head>`
- **THEN** existe `<meta name="description">` con un resumen coherente del perfil AI-native

### Requirement: Badges de métricas

El sitio SHALL destacar visualmente las métricas de impacto del CV mediante badges, reutilizando el
sistema de diseño existente.

#### Scenario: Badges de métricas visibles y consistentes
- **WHEN** un visitante ve el header o la sección de metodología/experiencia
- **THEN** se muestran badges con "−40% ciclo de revisión", "80% autoresolución N1" y "<10 min primera respuesta"
- **AND** los badges reutilizan estilos existentes (p. ej. `.tl-badge` / `.card-badge` / `.soft-list`) y
  respetan la paleta y el responsive
- **AND** las cifras coinciden exactamente con las del CV (sin inventar ni redondear de más)
