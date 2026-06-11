## ADDED Requirements

### Requirement: Backend proxy al LLM con credencial protegida

El asistente SHALL exponer un endpoint backend (AWS Lambda Function URL, HTTPS) que reciba la pregunta del
visitante y consulte un LLM (Claude). La credencial/permisos del LLM MUST residir solo en el backend; NUNCA
en el front ni en el repositorio.

#### Scenario: La credencial no se expone
- **WHEN** se inspecciona el front (HTML/JS/Network) y el repositorio
- **THEN** no aparece ninguna API key ni secreto del LLM
- **AND** el front solo conoce la URL del endpoint; la autenticación al modelo ocurre dentro del Lambda
  (IAM si es Bedrock, o variable de entorno cifrada si es API de Anthropic)

#### Scenario: Respuesta a una pregunta del perfil
- **WHEN** el endpoint recibe `POST` con una pregunta (ej. "¿tiene experiencia en AWS serverless?")
- **THEN** responde con texto conciso y fiel al perfil, usando `llms.txt` como base de conocimiento
- **AND** responde por HTTPS con CORS que permite solo los orígenes del sitio

### Requirement: Grounding y manejo de fuera-de-alcance

El backend SHALL fundamentar las respuestas en el perfil y NO inventar. Ante preguntas fuera de alcance,
MUST indicarlo en lugar de fabricar información.

#### Scenario: Pregunta fuera de alcance
- **WHEN** el visitante pregunta algo no contenido en el perfil
- **THEN** el asistente indica que no tiene esa información y sugiere contacto directo (email/LinkedIn)

### Requirement: Controles de costo y abuso (cerca de tier-0)

El backend SHALL limitar el gasto: cómputo dentro del free tier de Lambda y límites al consumo del LLM.

#### Scenario: Límites aplicados
- **WHEN** el Lambda procesa una solicitud
- **THEN** usa un modelo económico (Haiku) con `max_tokens` acotado
- **AND** existe `reserved concurrency` baja para acotar el gasto, y los budgets de la cuenta avisan al
  correo del CV ante consumo

#### Scenario: Degradación elegante ante fallo/límite
- **WHEN** el LLM falla o se alcanza un límite
- **THEN** el endpoint responde con un mensaje claro (sin stacktrace) y el front muestra un fallback con CTAs
  de contacto
