## ADDED Requirements

### Requirement: El contacto funciona de extremo a extremo

El sitio SHALL permitir que un visitante contacte al propietario sin enlaces ni endpoints rotos. El
formulario MUST dejar de apuntar al placeholder `formspree.io/f/YOUR_FORM_ID`.

#### Scenario: Envío de formulario operativo
- **WHEN** un visitante completa y envía el formulario de contacto
- **THEN** el mensaje se entrega por un endpoint real configurado (p. ej. Formspree con ID válido u otro
  servicio) y se muestra el estado de éxito
- **AND** ante error de red se muestra un estado de error y el visitante puede reintentar

#### Scenario: Alternativas de contacto siempre disponibles
- **WHEN** el visitante prefiere no usar el formulario
- **THEN** existen CTAs operativos: enviar email (con opción de copiar la dirección), WhatsApp y LinkedIn
- **AND** ninguno apunta a un placeholder ni a una URL inválida

#### Scenario: Sin placeholders en producción
- **WHEN** se inspecciona el HTML publicado
- **THEN** no existe ningún `YOUR_FORM_ID` ni marcador equivalente sin reemplazar
