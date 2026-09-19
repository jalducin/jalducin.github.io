# Capability: principios-de-trabajo

## Requirements

### Requirement: Bloque de principios de ingeniería

La sección de metodología (`#ai-method`, "How I Build with AI") SHALL incluir un bloque **"How I work"**
con los principios de ingeniería del candidato, cada uno con título corto y una línea de explicación:

1. **Automate > operate** — regla de las 2 veces: todo reporte o tarea manual hecha más de dos veces se
   convierte en un pipeline spec-driven.
2. **Reliability as a product** — el downtime se mide por impacto real al usuario, no por cierre de
   ticket; post-mortems blameless; runbooks con mínimo privilegio.
3. **State outside the code** — IDs, cortes y umbrales viven en configuración (JSON/Notion) que leen por
   igual el workflow y el tablero; la spec es el contrato.
4. **Cursor over ingestion, not the clock** — diseñado para el fallo (corridas caídas, datos tardíos), no
   para el camino feliz.

#### Scenario: Principios visibles y coherentes con el diseño
- **WHEN** un visitante abre la sección "How I Build with AI"
- **THEN** ve el bloque "How I work" con los 4 principios (título + explicación) después del flujo SDD y
  antes o dentro de la grilla `.ai-method-grid`
- **AND** el bloque reutiliza `.card`/`.ai-method-grid` o `.now-card` y la paleta vigente, sin CSS ad hoc
  que rompa 992/768/480px

#### Scenario: Principios reflejados en las fuentes AI-readable
- **WHEN** un agente lee `llms.txt`
- **THEN** existe una subsección "How I work" con los 4 principios en una línea cada uno
- **AND** el texto es consistente con `index.html` (misma lista, mismo orden)

### Requirement: Contenido sin información interna del empleador

Todo contenido de principios, metodología y experiencia SHALL describir prácticas en lenguaje genérico y
NO incluir nombres de personas, nombres propios de sistemas internos del empleador, nombres de bases de
datos, identificadores de incidentes/workflows/organizaciones, ni conteos de registros de clientes.

#### Scenario: Auditoría de nombres internos
- **WHEN** se buscan en `index.html`, `cv/*.html`, `llms.txt` y `cv/CV_JuanValentinAlducin.md` las cadenas
  de sistemas internos conocidos (p. ej. "SCI", "Spore", "Hipatia", "Mambu Tools", "LUCI", "Aleph",
  "DANIEL", "Strauss", "Alejandría", "Watson", "Sherlock") e identificadores tipo `INC-2026-`
- **THEN** no hay coincidencias
- **AND** las referencias al empleador se limitan al nombre de la empresa, el sector (fintech /
  microfinanzas) y descripciones genéricas ("core banking", "app de campo", "buró de crédito", "sistema
  de tickets")
