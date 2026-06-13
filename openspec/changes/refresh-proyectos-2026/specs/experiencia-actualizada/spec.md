# Capability: experiencia-actualizada (delta)

## MODIFIED Requirements

### Requirement: Enkoth como mención ligera en el rol de Podemos
Enkoth DEJA de presentarse como proyecto destacado independiente. DEBE aparecer únicamente como una
**mención ligera** dentro de la experiencia actual en **Podemos Progresar**, sin la etiqueta
"shipped to production" ni card propia.

#### Scenario: Bullet de experiencia en index.html y cv.html
- **WHEN** se revisa la entrada de Podemos Progresar en `index.html` y `cv/cv.html`
- **THEN** existe un bullet que menciona, de forma ligera, tooling serverless interno
  (AWS Lambda · Step Functions · EventBridge) para procesamiento de webhooks e integraciones
  (Asana, Freshdesk, Notion, Slack)
- **AND** NO existe una card/sección dedicada llamada "Enkoth" en proyectos destacados
- **AND** NO se afirma que Enkoth fue "shipped to production"

### Requirement: Proyectos obsoletos retirados del portafolio
Inventarios (Java/Spring Boot) y socket-chat (Node/WebSocket) DEBEN retirarse de la sección de proyectos del portafolio.

#### Scenario: Cards retiradas
- **WHEN** se revisa la sección de proyectos en `index.html`
- **THEN** NO existen cards "Inventarios" ni "socket-chat"
