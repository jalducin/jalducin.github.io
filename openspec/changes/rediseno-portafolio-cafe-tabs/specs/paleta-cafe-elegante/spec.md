## ADDED Requirements

### Requirement: Paleta café elegante con matrix conservado

El sitio SHALL usar una paleta cálida (café/carbón, no negro puro) con acento café-dorado y un ámbar claro,
manteniendo el **efecto matrix** pero **recoloreado** para combinar. Los colores MUST vivir en CSS custom
properties (una sola fuente de verdad).

#### Scenario: Tokens de color aplicados
- **WHEN** se carga el sitio (tema oscuro)
- **THEN** el fondo es café muy oscuro (no `#0d1117`/negro puro), las tarjetas/superficies usan un café
  oscuro, el acento es café-dorado (~`#c8924a`) y el texto es crema legible
- **AND** los acentos azules previos (`#58a6ff`) se reemplazan por el café-dorado en toda la UI

#### Scenario: Matrix recoloreado
- **WHEN** corre la animación matrix
- **THEN** la "lluvia" usa tonos ámbar/dorados acordes a la paleta (no azul)
- **AND** respeta `prefers-reduced-motion` (no anima si está activo) y `html.light` la oculta

#### Scenario: Contraste y tema claro
- **WHEN** se evalúa el contraste del texto sobre el fondo (oscuro y claro)
- **THEN** cumple WCAG AA
- **AND** el tema claro (`html.light`) usa una variante cálida (crema), no blanco/azul frío

### Requirement: Documentación de la paleta sincronizada

La nueva paleta SHALL quedar documentada como fuente de verdad.

#### Scenario: Docs actualizados
- **WHEN** se revisa `CLAUDE.md` y `docs/frontend-standards.md` (§paleta de colores)
- **THEN** reflejan los nuevos tokens café/dorado/ámbar (sin la paleta azul anterior)
