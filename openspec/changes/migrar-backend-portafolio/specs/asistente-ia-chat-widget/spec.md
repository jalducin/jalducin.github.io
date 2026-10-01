# Capability: asistente-ia-chat-widget (delta)

## MODIFIED Requirements

### Requirement: Widget de chat "Ask my portfolio" en el sitio

El sitio SHALL incluir un widget de chat (vanilla JS, sin frameworks) que permita preguntar sobre el perfil
y muestre las respuestas resueltas **localmente** por `asistente-local-retrieval` (sin backend ni LLM).
MUST respetar la paleta, ser responsive (992/768/480px) y accesible.

#### Scenario: Conversación básica
- **WHEN** el visitante abre el widget y escribe una pregunta
- **THEN** el front resuelve la respuesta contra la base de conocimiento embebida y la muestra en el hilo del chat
- **AND** muestra un estado breve de “escribiendo…” y permite enviar con Enter

#### Scenario: Accesible y no intrusivo
- **WHEN** el widget está cerrado
- **THEN** no interfiere con el sitio; al abrirlo es navegable por teclado, con foco manejado y `Esc` cierra
- **AND** respeta `prefers-reduced-motion` y la paleta de colores

#### Scenario: Degradación cuando no hay respuesta en la base
- **WHEN** la pregunta no tiene coincidencia suficiente en la base de conocimiento
- **THEN** el widget lo dice con honestidad, sugiere temas y muestra CTAs de contacto (email/LinkedIn), sin romper la página
- **AND** si el bloque `#assistant-kb` faltara o fuese inválido, el widget muestra el mensaje de contacto en vez de fallar

#### Scenario: Sin credenciales ni endpoints en el front
- **WHEN** se inspecciona el JS del widget
- **THEN** no contiene API keys, secretos ni URL de backend del asistente (la resolución es local)
