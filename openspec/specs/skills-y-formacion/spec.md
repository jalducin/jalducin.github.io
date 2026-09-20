# Capability: skills-y-formacion

## Purpose

Garantiza que las secciones de skills, educación y certificaciones del portafolio reflejen, con evidencia
real, la misma información que el CV vigente, sin listar tecnologías o títulos sin respaldo.

## Requirements

### Requirement: Taxonomía de skills alineada al CV

La sección de skills SHALL reflejar las habilidades con evidencia de uso, organizadas por nivel de
dominio (ver capability `stack-por-niveles`); la sección Habilidades del CV (ES/EN) MUST ser un subconjunto
compacto de ese inventario. No se listan tecnologías sin evidencia. Las categorías propias del sitio con
contexto (Retail & POS, Enterprise Integrations) se conservan dentro del nivel que corresponda.

#### Scenario: Skills de IA generativa completas y con evidencia
- **WHEN** un visitante lee las skills de IA del sitio o del CV
- **THEN** se incluyen: Claude API / Claude Code, OpenAI API, Gemini API, Amazon Bedrock, Prompt
  Engineering, LLM Integration, AI Agents / Skills, RAG, Agentic Workflows, SDD / OpenSpec
- **AND** NO se incluyen Amazon Kendra ni AWS Kiro

#### Scenario: Cloud, observabilidad y bases de datos según evidencia
- **WHEN** se revisan Cloud/Serverless, Observabilidad y Bases de datos
- **THEN** Cloud incluye AWS Lambda, Step Functions, EventBridge, CloudWatch (Logs Insights), RDS, S3, EC2,
  Serverless Framework, GitHub Actions, Docker, Supabase y, como base, Azure y GCP
- **AND** Observabilidad incluye Grafana, Sentry, CloudWatch, post-mortems / uptime / runbooks (SRE)
- **AND** Bases de datos incluye PostgreSQL, MySQL, SQL Server, MongoDB, SAP HANA, DynamoDB y Liquibase
- **AND** Kubernetes NO aparece en skills generales (solo en la card de VoltGrid)

#### Scenario: Lenguajes, frameworks, automatización y calidad
- **WHEN** se revisan lenguajes, frameworks, automatización y calidad
- **THEN** lenguajes incluyen Python, SQL, PHP, JavaScript, TypeScript y Java
- **AND** frameworks incluyen FastAPI, Django, Flask, React, Next.js y Node.js
- **AND** automatización incluye n8n (workflow SDK), APIs Freshdesk / Notion / Asana / Slack, webhooks
  serverless y pipelines spec-driven
- **AND** calidad incluye pytest (mocks), Vitest, SonarQube, ESLint y flujo de Merge Requests / CI

### Requirement: Educación actualizada con formación de inglés

La sección de educación SHALL incluir la formación vigente del CV, agregando *Inglés Avanzado — Quick
Learning*.

#### Scenario: Educación lista los programas del CV
- **WHEN** un visitante lee la sección de educación
- **THEN** aparecen: Ingeniería en Sistemas Computacionales (Instituto Tecnológico de Orizaba, 2006–2011)
  e Inglés Avanzado (Quick Learning, en curso)
- **AND** no aparece la Maestría en DevOps (IEU), retirada del CV en septiembre de 2026

### Requirement: Certificaciones reconciliadas con el CV

La lista de certificaciones SHALL coincidir con la del CV, manteniendo coherencia con la fuente de verdad.

#### Scenario: Certificaciones del CV presentes
- **WHEN** un visitante lee certificaciones y cursos
- **THEN** aparecen: Generative AI with Amazon Bedrock (Coursera), Claude Code: SE with Gen AI Agents
  (Vanderbilt / Anthropic), Developing Applications in Python on AWS (Coursera) y GitHub Actions
  Bootcamp (Código Facilito)
- **AND** cualquier certificación adicional mostrada en el sitio que no esté en el CV se conserva solo si
  es verídica; no se inventan certificaciones
