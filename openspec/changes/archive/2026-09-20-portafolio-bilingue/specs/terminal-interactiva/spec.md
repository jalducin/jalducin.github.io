# Capability: terminal-interactiva (delta)

## ADDED Requirements

### Requirement: Comando de idioma en la terminal

La terminal SHALL aceptar los comandos `lang es`, `lang en` e `idioma es|en` para cambiar el idioma del sitio,
y `lang` sin argumento MUST responder el idioma activo. `help` lista el comando.

#### Scenario: Cambiar idioma desde la terminal
- **WHEN** el visitante escribe `lang es` y presiona Enter
- **THEN** el sitio cambia a español y la terminal confirma ("Idioma: español")
- **AND** `lang` devuelve el idioma activo y `help` incluye `lang es|en`
