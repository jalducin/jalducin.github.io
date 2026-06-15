# Capability: paleta-azul-metalico

> Sustituye a la anterior `paleta-cafe-elegante`. La identidad pasó de café/dorado a **azul metálico profesional**.

## Requirements

### Requirement: Paleta azul metálico con matrix conservado

El sitio SHALL usar una paleta **azul metálico profesional** (azul noche, no negro puro) con acento azul acero
y un azul niebla claro, manteniendo el **efecto matrix** pero **recoloreado** para combinar. Los colores MUST
vivir en CSS custom properties (una sola fuente de verdad).

#### Scenario: Tokens de color aplicados
- **WHEN** se carga el sitio (tema oscuro)
- **THEN** el fondo es azul noche muy oscuro (`#0f141a`, no `#0d1117`/negro puro), las superficies usan azul
  oscuro (`#161d26`), el acento es azul acero (`#7fa8c9`) y el texto es blanco azulado legible (`#dde6ef`)
- **AND** no quedan acentos café/dorado (`#c8924a`) ni el azul eléctrico previo (`#58a6ff`)

#### Scenario: Matrix recoloreado
- **WHEN** corre la animación matrix
- **THEN** la "lluvia" usa azul metálico (`#7fa8c9`) acorde a la paleta (no ámbar ni azul eléctrico)
- **AND** respeta `prefers-reduced-motion` (no anima si está activo) y `html.light` la oculta

#### Scenario: Contraste y tema claro
- **WHEN** se evalúa el contraste del texto sobre el fondo (oscuro y claro)
- **THEN** cumple WCAG AA (incl. `--muted` con override `#596573` en `html.light`)
- **AND** el tema claro (`html.light`) usa una variante fría (`--bg:#eef2f6`, `--primary:#3f6488`), no crema cálida

#### Scenario: Armonía con el CV
- **WHEN** se compara el portafolio con el CV (`cv/cv.html`, `cv/cv-en.html`)
- **THEN** el CV usa el mismo azul acero como acento (`--gold:#3f6488`) sobre navy `#2b3947`, manteniendo 1 página

### Requirement: Documentación de la paleta sincronizada

La nueva paleta SHALL quedar documentada como fuente de verdad.

#### Scenario: Docs actualizados
- **WHEN** se revisa `CLAUDE.md` y `docs/frontend-standards.md` (§2 paleta de colores)
- **THEN** reflejan los tokens azul metálico (dark + light, incl. `--muted`) sin la paleta café anterior
