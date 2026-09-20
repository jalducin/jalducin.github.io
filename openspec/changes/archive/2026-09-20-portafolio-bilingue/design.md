# Design: portafolio-bilingue

## Context

- `index.html` (main @ `a31eaea`): single-page con tabs (`GROUPS`/`__showTab`), ~40 KB de texto visible en
  inglés repartido en ~250 elementos (10 h2, 27 h3, 30 p, 120 li, badges, botones, td). Todo el JS y CSS es
  embebido; no hay build step ni dependencias.
- Ya existe un patrón de preferencia persistida (`localStorage('theme')` + botón `#theme-btn` en nav).
- El CV ya es bilingüe; el registro del español debe ser el del CV ES (`cv/cv.html`).
- Reglas: vanilla, sin archivos `.js`/`.css`/`.json` externos, paleta intacta, responsive 992/768/480,
  sin nombres internos del empleador (audit).

## Goals / Non-Goals

**Goals:** selector ES/EN instantáneo, sin recarga y sin duplicar HTML; persistencia + detección; cobertura
100 % del texto no invariante; auditable (claves huérfanas / sin traducción); sin regresiones en tabs, tema,
descarga de CV, formulario, palette ni terminal.

**Non-Goals:** traducir `blog/*.html`, la terminal (ya es bilingüe/juguetona) y los labels de la command
palette (solo se añade la acción de idioma); URLs separadas por idioma / hreflang (los crawlers siguen viendo
EN); traducir `llms.txt`.

## Decisions

### D1. Diccionario embebido, inglés en el DOM
Alternativas: (a) dos HTML (`/es/`) — descartada por drift (todo cambio se hace dos veces) y por duplicar
83 KB; (b) `i18n/es.json` externo con `fetch` — descartada: rompe en `file://` (verificación headless) y va
contra la regla de archivos embebidos; (c) **elegida**: `data-i18n` en elementos + `<script
type="application/json" id="i18n-es">` con `{clave: html}`. El inglés se captura del DOM al cargar
(`EN[key] = el.innerHTML`) → volver a EN restaura byte a byte.

### D2. Claves y marcado
- Clave = `<seccion>.<tag><n>` generada por script en orden de documento (`exp.li12`, `proj.p3`,
  `nav.a1`, `hdr.p1`…). Estables mientras no se reordene contenido; si se inserta contenido nuevo se añade
  con clave nueva (el audit avisa si falta traducción).
- Elementos marcados: `a.nav-link`, header `p`/`.tl-location`/`.metric`, `section h2`, `h3` (excepto
  `.tl-company`), `p`, `li` de contenido (timeline, ai-method, now-card, principles, ai-card, education),
  `.card-badge`, `.card-metrics .card-badge`, `.tl-date`, `.tl-badge`, `a.btn`, `button` (form/terminal),
  `td`, `label`, `.level-legend`, `.level-title`, `.level-def`, `li` de `#soft-skills` y de
  `.level-own`/`.level-learning` (frases), footer `p`.
- **No marcados (invariantes):** `header h3` (headline), `.tl-company`, `.tech`, `li` de `.level-build` /
  `.level-operate` (tecnologías), nombres de proyectos en `h3` (se marcan pero la traducción conserva el
  nombre: "Fidello — Sistema de tarjetas de lealtad").
- Atributos: `title`/`aria-label` de los iconos del header y botones (`data-i18n-title`, `data-i18n-aria`),
  `placeholder` del formulario (`data-i18n-placeholder`).
- Un script de marcado (`scripts/mark_i18n.py`) añade los atributos y extrae `{clave: EN}` a
  `scripts/en.json` para traducir; `scripts/build_dict.py` inyecta el JSON ES en `index.html`.

### D3. Runtime (≈60 líneas, al final del body, antes del script de descarga del CV)
```
const ES = JSON.parse(document.getElementById('i18n-es').textContent);
const EN = {}; document.querySelectorAll('[data-i18n]').forEach(el => EN[el.dataset.i18n] = el.innerHTML);
// idem para title/aria/placeholder
function applyLang(lang){ for each el: el.innerHTML = lang==='es' && ES[k] ? ES[k] : EN[k]; ...
  document.documentElement.lang = lang; document.title = TITLES[lang]; btn.textContent = lang==='es'?'EN':'ES';
  try{localStorage.setItem('lang',lang)}catch(e){} }
resolve: URLSearchParams lang → localStorage → navigator.language.startsWith('es') → 'en'
window.__setLang = applyLang (para palette y terminal)
```
- Se ejecuta antes del `showTab` inicial (el script de i18n va antes del script de tabs) → sin parpadeo.
- `innerHTML` solo sobre elementos hoja de contenido (D2), por eso no se pierden handlers: los elementos con
  JS (inputs, `#term-out`, enlaces `data-cv`) no llevan `data-i18n` en sí mismos; los `a.btn`/`button`
  traducidos solo cambian su texto interno.
- Nav: `<li class="nav-item nav-theme"><button id="lang-btn" …>ES</button></li>` con el mismo CSS que
  `#theme-btn`. Palette: acción "Español / English". Terminal: `lang`, `lang es|en`, `idioma …`.

### D4. Registro y contenido del español
Traducción humana (no automática) del agente, alineada al CV ES: tuteo evitado, primera persona en
experiencia ("Lidero…", "Construí…"), cifras y nombres idénticos, sin nombres internos. `Present` →
`Presente`, `Current` → `Actual`, `View Code` → `Ver código`, `Live Demo` → `Demo en vivo`, niveles →
Dueño / Construyo / Opero / Aprendiendo.

### D5. Auditoría
Se extiende `audit.py` (copiado del cambio anterior a `scripts/audit_i18n.py`): JSON parsea; 0 claves
huérfanas; lista de claves sin traducción == lista de invariantes declarada; nombres prohibidos ausentes en el
diccionario ES; conteo de elementos `data-i18n` ≥ 200.

## Risks / Trade-offs
- [Peso de `index.html` +35 KB] → aceptable para sitio estático en CDN; sigue < 130 KB sin gzip.
- [Contenido nuevo sin traducir] → audit lo reporta; regla en `docs/frontend-standards.md`: todo texto nuevo
  lleva `data-i18n` y entrada ES.
- [Parpadeo EN→ES en la primera carga] → el script corre antes de `showTab` y de los `fade-in`; el header es
  lo único visible antes y se traduce en el mismo tick.
- [SEO: crawlers ven EN] → asumido (non-goal); `llms.txt` menciona el sitio bilingüe.
- [Regresión de handlers por `innerHTML`] → D2/D3 + probe headless que verifica `__showTab`, `data-cv`,
  `__downloadCV`, formulario y terminal tras alternar idioma dos veces.

## Migration Plan
Feature branch → marcado + diccionario + runtime → audit + headless (4 breakpoints × ES/EN) → docs →
merge a `main` → deploy automático. Rollback: revert del merge.

## Open Questions
Ninguna bloqueante. Decisión tomada: idioma inicial por `navigator.language` (es → ES) cuando no hay
preferencia; el usuario puede pedir que el default sea EN fijo.
