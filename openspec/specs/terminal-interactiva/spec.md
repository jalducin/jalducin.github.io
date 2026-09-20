# Capability: terminal-interactiva

## Purpose

Garantiza que la terminal interactiva del portafolio responda a comandos básicos (incluido el cambio de
idioma) de forma accesible y on-brand, como vía complementaria de navegación para visitantes técnicos.

## Requirements

### Requirement: Sección Terminal interactiva

El sitio SHALL incluir una sección "Terminal" donde el visitante escribe comandos y obtiene respuestas,
en JavaScript vanilla, on-brand con la estética matrix/monospace.

#### Scenario: Comandos básicos
- **WHEN** el visitante escribe un comando soportado y presiona Enter
- **THEN** el terminal responde adecuadamente para al menos: `help`, `whoami`, `ls projects`, `cat cv`
  (enlaza/abre el CV), `skills`, `contact`, `sdd`, `clear`
- **AND** un comando desconocido muestra un mensaje tipo "command not found" con sugerencia de `help`

#### Scenario: Easter egg
- **WHEN** el visitante escribe un comando "secreto" (p. ej. `sudo hire-me` o `matrix`)
- **THEN** se muestra una respuesta divertida/única (easter egg)

#### Scenario: Accesible y on-brand
- **WHEN** se usa el terminal
- **THEN** el input es navegable por teclado, hay historial básico (↑/↓) y autoscroll de salida
- **AND** respeta la paleta café/ámbar, es responsive (992/768/480) y no expone datos sensibles

### Requirement: Comando de idioma en la terminal

La terminal SHALL aceptar los comandos `lang es`, `lang en` e `idioma es|en` para cambiar el idioma del sitio,
y `lang` sin argumento MUST responder el idioma activo. `help` lista el comando.

#### Scenario: Cambiar idioma desde la terminal
- **WHEN** el visitante escribe `lang es` y presiona Enter
- **THEN** el sitio cambia a español y la terminal confirma ("Idioma: español")
- **AND** `lang` devuelve el idioma activo y `help` incluye `lang es|en`
