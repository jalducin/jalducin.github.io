# Capability: agentic-engineering-hardening (delta)

## MODIFIED Requirements

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

