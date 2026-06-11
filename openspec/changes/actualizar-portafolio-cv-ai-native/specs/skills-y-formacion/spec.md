## ADDED Requirements

### Requirement: Taxonomía de skills alineada al CV

La sección de skills SHALL reflejar las habilidades del CV vigente, organizadas en categorías legibles,
sin eliminar las categorías propias del sitio que aportan contexto (Retail & POS, Enterprise
Integrations).

#### Scenario: Skills de IA generativa completas
- **WHEN** un visitante lee la categoría de IA del sitio
- **THEN** se incluyen como mínimo: Generative AI, Prompt Engineering, LLM Integration, AI Agents, RAG,
  Claude API, OpenAI API, Gemini API, Agentic Workflows, SDD / OpenSpec y Amazon Bedrock

#### Scenario: Cloud y bases de datos ampliadas según el CV
- **WHEN** se revisan las categorías de Cloud/Serverless y Bases de datos
- **THEN** Cloud incluye AWS Lambda, RDS, S3, Step Functions, EC2, CloudWatch, GitHub Actions y, como
  base, Azure y GCP, además de Supabase
- **AND** Bases de datos incluye PostgreSQL, MySQL, SQL Server, MongoDB, Hana SQL y DynamoDB

#### Scenario: Lenguajes y frameworks coinciden con el CV
- **WHEN** se revisan lenguajes y frameworks
- **THEN** lenguajes incluyen Python, PHP, JavaScript, TypeScript, Java y SQL
- **AND** frameworks incluyen Django, Flask, FastAPI, React y Node.js

### Requirement: Educación actualizada con formación de inglés

La sección de educación SHALL incluir la formación vigente del CV, agregando *Inglés Avanzado — Quick
Learning*.

#### Scenario: Educación lista los programas del CV
- **WHEN** un visitante lee la sección de educación
- **THEN** aparecen: Maestría en DevOps (IEU, 2024–Presente), Ingeniería en Sistemas Computacionales
  (Instituto Tecnológico de Orizaba, 2006–2011) e Inglés Avanzado (Quick Learning, en curso)

### Requirement: Certificaciones reconciliadas con el CV

La lista de certificaciones SHALL coincidir con la del CV, manteniendo coherencia con la fuente de verdad.

#### Scenario: Certificaciones del CV presentes
- **WHEN** un visitante lee certificaciones y cursos
- **THEN** aparecen: Generative AI with Amazon Bedrock (Coursera), Claude Code: SE with Gen AI Agents
  (Vanderbilt / Anthropic), Developing Applications in Python on AWS (Coursera) y GitHub Actions
  Bootcamp (Código Facilito)
- **AND** cualquier certificación adicional mostrada en el sitio que no esté en el CV se conserva solo si
  es verídica; no se inventan certificaciones
