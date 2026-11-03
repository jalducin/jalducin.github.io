# Capability: skills-y-formacion (delta)

## MODIFIED Requirements

### Requirement: Certificaciones reconciliadas con el CV

La lista de certificaciones SHALL coincidir con la del CV, manteniendo coherencia con la fuente de verdad.

#### Scenario: Certificaciones del CV presentes
- **WHEN** un visitante lee certificaciones y cursos
- **THEN** aparecen: Anthropic Academy (Claude Code in Action · Intro to MCP · Agent Skills · Subagents, 2026),
  Claude Code: Software Engineering with Generative AI Agents (Vanderbilt University, 2026) y Generative AI
  Applications with Amazon Bedrock (AWS, 2026)
- **AND** cualquier certificación adicional mostrada en el sitio que no esté en el CV se conserva solo si
  es verídica; no se inventan certificaciones
