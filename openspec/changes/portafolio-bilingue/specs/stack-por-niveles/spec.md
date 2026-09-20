# Capability: stack-por-niveles (delta)

## ADDED Requirements

### Requirement: Etiquetas de nivel bilingües

Las etiquetas y definiciones de los niveles SHALL mostrarse en el idioma activo del sitio: Own / Build /
Operate / Learning en inglés y **Dueño / Construyo / Opero / Aprendiendo** en español, con la misma
semántica y marca visual.

#### Scenario: Niveles en español
- **WHEN** el idioma activo es ES
- **THEN** los `h3.level-title` muestran Dueño, Construyo, Opero, Aprendiendo y la leyenda/definiciones están
  en español
- **AND** los ítems que son tecnologías o nombres propios (p. ej. "PostgreSQL", "n8n (workflow SDK)")
  permanecen iguales; los ítems descriptivos (p. ej. "Idempotent production ETL") se traducen
