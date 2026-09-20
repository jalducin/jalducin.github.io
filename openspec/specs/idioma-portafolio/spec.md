# Capability: idioma-portafolio

## Purpose

Garantiza que el portafolio ofrezca contenido bilingüe ES/EN completo, consistente y persistente entre
visitas, sin pérdida de estado (sección activa, tema), para visitantes hispanohablantes y angloparlantes.

## Requirements

### Requirement: Selector de idioma ES/EN

El sitio SHALL ofrecer un selector de idioma español/inglés visible en la barra de navegación (junto al
toggle de tema) y como acción en la command palette. Al cambiar de idioma MUST actualizarse todo el texto
visible de `index.html` sin recargar la página y sin perder la sección activa ni el tema.

#### Scenario: Cambio de idioma desde la navegación
- **WHEN** el visitante pulsa el botón de idioma (muestra el idioma destino: "ES" en inglés, "EN" en español)
- **THEN** los textos de nav, header (resumen, ubicación, badges), secciones (títulos, párrafos, bullets,
  badges de cards, fechas de la timeline, leyenda y niveles de skills, educación, idiomas, contacto, footer)
  cambian al idioma destino
- **AND** la sección activa y el tema (claro/oscuro) se conservan
- **AND** `<html lang>` cambia a `es` o `en` y `document.title` al título del idioma activo

#### Scenario: Invariantes entre idiomas
- **WHEN** se compara la página en ES y en EN
- **THEN** el headline "Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI", los nombres
  propios (empresas, proyectos), las tecnologías, las métricas numéricas y los enlaces son idénticos
- **AND** ningún elemento con comportamiento JS (inputs del formulario, terminal, command palette, enlaces de
  descarga del CV) pierde sus handlers ni sus atributos `data-cv`/`id`

### Requirement: Mecanismo i18n vanilla y fuente de verdad

La traducción SHALL implementarse en JavaScript vanilla embebido: cada elemento traducible lleva
`data-i18n="<clave>"` (y opcionalmente `data-i18n-title`, `data-i18n-aria`, `data-i18n-placeholder`); el
inglés es el contenido del DOM (fuente de verdad) y el español vive en un diccionario embebido
`<script type="application/json" id="i18n-es">`. No se crean archivos `.js`/`.json` externos ni se duplica
el HTML.

#### Scenario: Diccionario y claves consistentes
- **WHEN** se ejecuta el audit del proyecto
- **THEN** toda clave del diccionario ES existe como `data-i18n*` en el DOM (0 claves huérfanas)
- **AND** todo elemento `data-i18n` de texto (h1–h3, p, li de contenido, badges, botones, labels, td) tiene
  entrada ES, salvo los marcados como invariantes (tecnologías/nombres propios), y el audit reporta el conteo
  de invariantes
- **AND** el JSON del diccionario parsea sin error

#### Scenario: Restauración exacta del inglés
- **WHEN** el visitante cambia a ES y vuelve a EN
- **THEN** el `innerHTML` de cada elemento traducido es idéntico al original (el inglés se captura del DOM al
  cargar, no se reescribe a mano)

### Requirement: Persistencia y detección del idioma

El idioma activo SHALL resolverse en este orden: parámetro `?lang=es|en` en la URL → preferencia guardada en
`localStorage` (`lang`) → `navigator.language` (si empieza por `es` → español) → inglés. La elección del
visitante MUST persistir entre visitas en el mismo navegador.

#### Scenario: Primera visita desde un navegador en español
- **WHEN** un visitante sin preferencia guardada abre el sitio con `navigator.language` = `es-MX`
- **THEN** la página se muestra en español antes del primer render visible (sin parpadeo apreciable)

#### Scenario: Preferencia explícita y enlace compartido
- **WHEN** el visitante eligió EN (guardado) y abre `index.html?lang=es`
- **THEN** la página se muestra en español (la URL gana) y la preferencia guardada pasa a ES

#### Scenario: Sin almacenamiento disponible
- **WHEN** `localStorage` lanza excepción (modo privado / bloqueado)
- **THEN** el selector sigue funcionando para la sesión y la página no muestra errores de consola

### Requirement: Cobertura de traducción del contenido

La traducción al español SHALL cubrir el 100 % de los textos visibles de `index.html` que no sean invariantes,
con la misma información que el inglés (misma lista de bullets, mismas cifras) y en el registro del CV en
español (`cv/cv.html`).

#### Scenario: Experiencia y proyectos en español
- **WHEN** el idioma activo es ES
- **THEN** los bullets de Podemos Progresar, Redsis y Softtek, las descripciones de las 7 cards de proyectos,
  los 4 principios, las 4 cards de metodología, la leyenda y definiciones de niveles, y la sección de
  educación/cursos se muestran en español
- **AND** la fecha "Present" se muestra como "Presente" y el badge "Current" como "Actual"
- **AND** ningún texto contiene nombres internos del empleador (misma regla que en inglés)
