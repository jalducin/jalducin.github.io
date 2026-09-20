# Capability: agentic-engineering-hardening

## Purpose

Garantiza que el portafolio comunique el método de trabajo AI-native/agentic del candidato (SDD, datos
estructurados para agentes/LLMs, métricas verificables) tanto a reclutadores humanos como a crawlers y
asistentes de IA que evalúan el perfil.

## Requirements

### Requirement: Sección "How I build with AI" (metodología agentic)

El sitio SHALL incluir una sección dedicada que explique el método de trabajo AI-native / agentic del
candidato, demostrando el *cómo* con prácticas y resultados operativos, no solo declarando herramientas.

#### Scenario: La sección comunica el método y las métricas
- **WHEN** un visitante navega a la sección de metodología AI-native
- **THEN** se describe el flujo Spec-Driven Development (proposal → specs → design → tasks → apply →
  archive) como práctica central
- **AND** se mencionan las herramientas (Claude/Anthropic, Gemini, OpenAI) como copilotos del SDLC
- **AND** se muestran los SLAs operativos: primera respuesta <10 min y resolución de incidentes críticos <2 h
- **AND** NO se publican porcentajes de mejora (reducción de revisión, autoresolución N1, uptime): retirados por
  decisión del propietario el 2026-09-20

#### Scenario: La sección es accesible desde la navegación
- **WHEN** se carga el sitio
- **THEN** existe un enlace de navegación hacia la sección de metodología AI-native
- **AND** la sección respeta el sistema de diseño y el responsive (992/768/480px)

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

El sitio SHALL destacar visualmente los SLAs operativos del CV mediante badges, reutilizando el sistema de
diseño existente, sin porcentajes de mejora.

#### Scenario: Badges de métricas visibles y consistentes
- **WHEN** un visitante ve el header o la sección de metodología/experiencia
- **THEN** se muestran badges con "<10 min first response" y "<2 h critical resolution" (y opcionalmente
  prácticas como "blameless post-mortems" / "spec-driven pipelines"), sin "40%", "80%" ni "99.95%"
- **AND** la tarjeta "Measurable impact" pasa a "Operational SLAs & practices" y lista los mismos SLAs y prácticas
- **AND** los badges reutilizan estilos existentes (p. ej. `.tl-badge` / `.card-badge` / `.soft-list`) y
  respetan la paleta y el responsive
