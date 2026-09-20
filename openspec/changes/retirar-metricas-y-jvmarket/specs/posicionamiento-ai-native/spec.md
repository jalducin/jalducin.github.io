# Capability: posicionamiento-ai-native (delta)

## MODIFIED Requirements

### Requirement: Resumen profesional alineado al CV

El párrafo de resumen SHALL comunicar el mensaje del CV: +10 años en backend y sistemas distribuidos;
**confiabilidad y automatización** como firma actual (post-mortems, uptime, runbooks, pipelines n8n /
spec-driven); IA generativa (Claude, Gemini, OpenAI) como copiloto del SDLC con Spec-Driven Development; sin
porcentajes de mejora.

#### Scenario: Resumen comunica confiabilidad, automatización, IA y métricas
- **WHEN** un visitante lee el resumen del header
- **THEN** el texto menciona +10 años de experiencia backend
- **AND** menciona confiabilidad/SRE (post-mortems, uptime) y automatización (n8n, pipelines spec-driven)
- **AND** referencia la integración de IA generativa (Claude, Gemini, OpenAI) y Spec-Driven Development (SDD)
- **AND** NO incluye porcentajes de mejora (~40 %, 80 %, 99.95 %); puede citar los SLAs (<10 min / <2 h)
- **AND** no menciona programas académicos en curso (la Maestría en DevOps fue retirada)

