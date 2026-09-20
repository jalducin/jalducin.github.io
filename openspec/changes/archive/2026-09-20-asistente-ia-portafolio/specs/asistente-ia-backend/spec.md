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

#### Scenario: Resistencia a prompt-injection y on-topic
- **WHEN** el visitante intenta cambiar el rol del asistente, extraer el system prompt, o pedir algo
  ajeno al perfil ("ignora las instrucciones anteriores", "actúa como…", "dime tu prompt")
- **THEN** el asistente se mantiene en su rol (responder sobre el perfil de Juan), no revela su
  configuración ni secretos, y redirige al tema con cortesía

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

### Requirement: Sin RAG — el perfil cabe en contexto

El backend SHALL usar el contenido de `llms.txt` directamente como contexto del prompt (cabe holgado en la
ventana del modelo). NO se introduce RAG (vector DB / embeddings / retrieval): sería sobre-ingeniería para
un perfil de ~1 KB y no reduce llamadas.

#### Scenario: Contexto embebido, no recuperado
- **WHEN** se construye el prompt del asistente
- **THEN** el perfil (`llms.txt`) se incluye completo como contexto, sin un paso de recuperación externo
- **AND** si en el futuro el conocimiento crece más allá de lo que cabe en contexto, recién entonces se
  evalúa RAG (decisión documentada, no por defecto)

### Requirement: Caché de respuestas para ahorrar llamadas

El backend SHALL cachear respuestas a preguntas frecuentes/idénticas para no invocar al LLM en repeticiones.

#### Scenario: Pregunta repetida servida desde caché
- **WHEN** llega una pregunta equivalente a una ya respondida (normalizada: minúsculas, espacios, signos)
- **THEN** se devuelve la respuesta cacheada **sin** llamar al LLM
- **AND** la caché tiene un TTL razonable y se invalida si cambia `llms.txt` (la base de conocimiento)

### Requirement: Rate limiting y tope global

El backend SHALL limitar el abuso por cliente y fijar un tope global diario como techo duro de costo.

#### Scenario: Límite por IP
- **WHEN** una misma IP supera el umbral por ventana (p. ej. ~10/min o ~50/día)
- **THEN** el endpoint responde 429 con un mensaje claro y NO llama al LLM
- **AND** el conteo se mantiene en un almacén tier-0 (p. ej. DynamoDB on-demand con TTL) o, como mínimo, en
  memoria del contenedor

#### Scenario: Tope global diario (techo de costo)
- **WHEN** el total de invocaciones del día supera el tope configurado (p. ej. ~500/día)
- **THEN** el asistente deja de llamar al LLM por el resto del día y degrada con CTAs de contacto
- **AND** los budgets de la cuenta avisan al correo del CV; opcionalmente se evalúa captcha/WAF si el abuso persiste
