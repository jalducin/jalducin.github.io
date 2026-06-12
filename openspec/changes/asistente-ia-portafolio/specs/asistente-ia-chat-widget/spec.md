## ADDED Requirements

### Requirement: Widget de chat "Ask my portfolio" en el sitio

El sitio SHALL incluir un widget de chat (vanilla JS, sin frameworks) que permita preguntar sobre el perfil
y muestre las respuestas del backend. MUST respetar la paleta, ser responsive (992/768/480px) y accesible.

#### Scenario: Conversación básica
- **WHEN** el visitante abre el widget y escribe una pregunta
- **THEN** el front hace `fetch` al endpoint del backend y muestra la respuesta en el hilo del chat
- **AND** muestra estado de carga mientras espera y permite enviar con Enter

#### Scenario: Accesible y no intrusivo
- **WHEN** el widget está cerrado
- **THEN** no interfiere con el sitio; al abrirlo es navegable por teclado, con foco manejado y `Esc` cierra
- **AND** respeta `prefers-reduced-motion` y la paleta de colores

#### Scenario: Degradación si el backend no responde
- **WHEN** el endpoint falla o no está disponible
- **THEN** el widget muestra un mensaje claro y CTAs de contacto (email/LinkedIn), sin romper la página

#### Scenario: La credencial nunca está en el front
- **WHEN** se inspecciona el JS del widget
- **THEN** solo contiene la URL del endpoint; ninguna API key ni secreto

### Requirement: Preguntas sugeridas

El widget SHALL ofrecer preguntas sugeridas (chips) para guiar al visitante y aumentar los aciertos de caché.

#### Scenario: Chips de preguntas frecuentes
- **WHEN** el visitante abre el widget
- **THEN** ve 3-4 chips (p. ej. "¿Experiencia en AWS?", "Cuéntame de Fidello", "¿Stack de backend?")
- **AND** al pulsar uno, se envía esa pregunta como si la hubiera escrito

### Requirement: Tope de turnos por sesión

El widget SHALL acotar la longitud de la conversación para limitar costo y abuso.

#### Scenario: Límite de turnos
- **WHEN** la conversación alcanza el tope de turnos por sesión (p. ej. ~8)
- **THEN** el widget invita a contactar directamente (email/LinkedIn) en lugar de seguir consultando al LLM
