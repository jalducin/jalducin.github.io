# Capability: asistente-local-retrieval

## Purpose

Asistente "Ask my portfolio" que responde preguntas sobre el perfil desde una base de conocimiento curada,
recuperada en el navegador: sin LLM, sin backend, sin credenciales y sin peticiones de red.

## Requirements

### Requirement: Base de conocimiento curada y editable

El asistente SHALL responder desde una base de conocimiento curada por el dueño, cuya fuente editable es
`assistant/knowledge.md` (Markdown, bilingüe) y cuyo artefacto de runtime es un bloque
`<script type="application/json" id="assistant-kb">` embebido en `index.html`, generado por
`scripts/assistant/build_kb.py` (mismo patrón que el diccionario i18n). NO se usa ningún LLM, API key ni
servicio externo en tiempo de ejecución.

#### Scenario: Entradas con tema, alias y respuesta bilingüe
- **WHEN** se revisa `assistant/knowledge.md`
- **THEN** cada entrada declara: `id`, `tags` (palabras clave y alias de búsqueda, ES y EN), `answer.en` y
  `answer.es`
- **AND** la base cubre al menos: rol actual, experiencia previa, confiabilidad/SRE, automatización/n8n,
  IA y SDD, stack por niveles, AWS, Fidello, Pyzzeria, VoltGrid, Trackion, Monitoreo-Cloud, dataMasterGK,
  educación/cursos, idiomas, contacto, descarga del CV y disponibilidad laboral
- **AND** ninguna respuesta contiene nombres internos del empleador, personas, bases de datos ni IDs
  (misma regla que el resto del sitio)

#### Scenario: Compilación determinista
- **WHEN** se ejecuta `python scripts/assistant/build_kb.py`
- **THEN** el bloque `#assistant-kb` de `index.html` se reemplaza con el JSON derivado de `knowledge.md`
- **AND** el script es idempotente y falla con error claro si una entrada no tiene respuesta en ambos idiomas

### Requirement: Recuperación en el navegador sin servicios externos

El widget SHALL resolver cada pregunta en el cliente: normaliza el texto (minúsculas, sin acentos ni
puntuación), puntúa cada entrada por coincidencia de `tags` y palabras del contenido, y devuelve la respuesta
de la entrada con mayor puntaje por encima de un umbral, en el idioma activo del sitio.

#### Scenario: Pregunta cubierta por la base
- **WHEN** el visitante pregunta "What's your AWS experience?" con el sitio en inglés
- **THEN** el widget responde con la entrada de AWS en inglés, sin peticiones de red
- **AND** la misma pregunta en español ("¿Qué experiencia tienes en AWS?") responde la misma entrada en español

#### Scenario: Sin coincidencia suficiente
- **WHEN** la pregunta no supera el umbral (p. ej. "¿cuál es tu color favorito?")
- **THEN** el widget responde honestamente que solo puede hablar del perfil, ofrece 2–3 temas sugeridos y los
  CTAs de contacto (email/LinkedIn)
- **AND** NO inventa información ni afirma datos que no estén en la base

#### Scenario: Sin red y sin secretos
- **WHEN** se inspecciona el JS del widget o se abre la página sin conexión
- **THEN** no hay `fetch` a ningún endpoint del asistente, ni API keys, ni URLs de backend
- **AND** el asistente sigue respondiendo con normalidad

#### Scenario: Latencia y límites
- **WHEN** el visitante envía varias preguntas seguidas
- **THEN** cada respuesta aparece en menos de 100 ms y no hay límites de uso ni mensajes de cuota
- **AND** se conserva el tope de turnos del widget (CTA de contacto tras el máximo) como guía conversacional
