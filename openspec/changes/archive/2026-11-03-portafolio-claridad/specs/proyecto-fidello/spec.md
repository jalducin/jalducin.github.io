# Capability: proyecto-fidello (delta)

## MODIFIED Requirements

### Requirement: Card de proyecto estrella Fidello

La sección de proyectos destacados SHALL incluir una card para **Fidello — Loyalty Card System** en **segundo
lugar** (después de platform-STALD), descrita por lo construido, con las cifras de ingeniería reales y su stack.
NO SHALL afirmar que el piloto está activo ("Pilot · cloud beta", "real coffee shops", "cafeterías reales").

#### Scenario: Fidello sin estado de piloto
- **WHEN** un visitante lee la card de Fidello, en EN o ES
- **THEN** existe la card "Fidello — Loyalty Card System" con el badge "★ AI-native · 100% SDD"
- **AND** no aparecen "Pilot", "beta", "real coffee shops" ni "cafeterías reales"

#### Scenario: Cifras de ingeniería verificables
- **WHEN** se lee la card de Fidello
- **THEN** muestra al menos 793 pruebas y 91 migraciones, coherentes con el CV y `llms.txt`

#### Scenario: CV y llms.txt sin estado de piloto
- **WHEN** se lee la entrada de Fidello en el CV (ES/EN) y en `llms.txt`
- **THEN** no se indica "piloto en beta cloud" / "cloud beta pilot" y hay al menos una cifra de ingeniería
