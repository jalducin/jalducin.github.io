## ADDED Requirements

### Requirement: Asistente IA sobre el perfil ("Ask my portfolio")

El sitio SHALL ofrecer un asistente conversacional que responda preguntas sobre el perfil del propietario,
usando como base de conocimiento el contenido del sitio (`llms.txt` / CV). El asistente MUST consultar un
LLM a través de un **proxy serverless**; la API key NUNCA debe quedar expuesta en el front.

#### Scenario: Respuesta fundamentada en el perfil
- **WHEN** un visitante pregunta algo respondible desde el perfil (p. ej. "¿tiene experiencia en AWS serverless?")
- **THEN** el asistente responde de forma concisa y fiel a la información del sitio/CV
- **AND** ante preguntas fuera de alcance, indica que no tiene esa información en lugar de inventar

#### Scenario: La clave del LLM no se expone
- **WHEN** se inspecciona el front (HTML/JS/Network)
- **THEN** no aparece ninguna API key; las llamadas van a un endpoint propio (AWS Lambda) que actúa de proxy

#### Scenario: Controles de costo y abuso
- **WHEN** el endpoint recibe tráfico
- **THEN** aplica rate-limiting y/o caché de preguntas frecuentes y opera bajo un tope de presupuesto
- **AND** ante fallo del proveedor/limite, el widget degrada con un mensaje claro y CTAs de contacto
