# Capability: agentic-engineering-hardening (delta)

## MODIFIED Requirements

### Requirement: Datos estructurados JSON-LD (Schema.org Person)

El `<head>` de `index.html` SHALL incluir un bloque JSON-LD válido de tipo `Person` (Schema.org) para
que buscadores y agentes/LLMs interpreten el perfil de forma estructurada, alineado al posicionamiento
híbrido.

#### Scenario: JSON-LD Person válido y consistente
- **WHEN** un crawler o agente parsea el `<script type="application/ld+json">`
- **THEN** el JSON es válido y de `@type: Person`
- **AND** `jobTitle` es "Senior Backend Engineer · Tech Lead · SRE & Automation · Agentic AI"
- **AND** incluye `name`, `email`, `url`, `sameAs` (GitHub, LinkedIn), `address` (CDMX, Mexico) y
  `knowsAbout` con las skills clave del inventario (incluye "Site Reliability Engineering", "Post-mortems",
  "n8n", "Automation"; excluye "Amazon Kendra" y "AWS Kiro")
- **AND** los valores coinciden con la fuente de verdad (sin datos obsoletos)

### Requirement: Capa AI-readable (`llms.txt` y meta)

El proyecto SHALL exponer un archivo estático `llms.txt` en la raíz del sitio con un resumen del perfil
orientado a agentes/LLMs, y meta tags coherentes en `index.html`. `backend/assistant/profile.txt` es una
copia exacta de `llms.txt` generada por el workflow de deploy del asistente.

#### Scenario: llms.txt presente y descriptivo
- **WHEN** un agente solicita `/llms.txt`
- **THEN** el archivo existe y resume en Markdown: quién es, posicionamiento híbrido (Backend · SRE &
  Automation · Agentic AI), principios de trabajo ("How I work"), stack por niveles, experiencia (ambos
  roles de Podemos con lenguaje genérico), proyectos (Fidello como piloto con cifras), métricas y enlaces
- **AND** el contenido es consistente con `index.html`, el CV y el JSON-LD (una sola fuente de verdad por
  dato; los demás enlazan/derivan, no contradicen)
- **AND** no contiene nombres de sistemas internos del empleador, personas, bases de datos ni IDs

#### Scenario: Meta description AI-readable
- **WHEN** se inspecciona el `<head>`
- **THEN** existe `<meta name="description">` con un resumen coherente del perfil híbrido

### Requirement: Badges de métricas

El sitio SHALL destacar visualmente las métricas de impacto del CV mediante badges, reutilizando el
sistema de diseño existente.

#### Scenario: Badges de métricas visibles y consistentes
- **WHEN** un visitante ve el header o la sección de metodología/experiencia
- **THEN** se muestran badges con "−40% code review time", "80% N1 self-resolution", "<10 min first
  response" y "99.95% monthly uptime"
- **AND** la tarjeta "Measurable impact" de la sección de metodología lista las mismas cuatro métricas
- **AND** los badges reutilizan estilos existentes (p. ej. `.tl-badge` / `.card-badge` / `.soft-list`) y
  respetan la paleta y el responsive
