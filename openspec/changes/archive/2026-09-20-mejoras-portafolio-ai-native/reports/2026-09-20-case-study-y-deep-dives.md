# Reporte Step 9 — Pruebas, verificación de estado y verificación manual UI (case-study-sdd + project-deep-dives)

- Fecha: 2026-09-20
- Cambio: mejoras-portafolio-ai-native (capabilities `case-study-sdd` y `project-deep-dives`; tareas 7.x, 8.x, 9.x, 10.x)
- Agente: frontend-developer (Claude Code)
- Rama: `feature/case-study-y-deep-dives` (desde `main` @ `2170aa9`)

## Comandos ejecutados

- `python scripts/i18n/build_dict.py` — regenera el JSON `#i18n-es` en `index.html` (198 claves ES, 22 invariantes)
- `python scripts/i18n/audit_i18n.py` — 57 checks de consistencia (nombres internos, headline, fechas, PDFs, i18n)
- `python scripts/i18n/probe_i18n.py` — 18 probes headless del selector de idioma
- `cp llms.txt backend/assistant/profile.txt` — regenera el artefacto local (gitignored) que exige el check `profile.txt == llms.txt`
- `python <scratchpad>/verify_pages.py <root> blog/anatomia-de-un-cambio.html blog/deep-dive-fidello.html blog/deep-dive-pyzzeria.html index.html`
  — script ad hoc (fuente incluida al final): `href`/`src` relativos existen en disco, enlaces a GitHub con patrón
  `https://github.com/jalducin[/<repo>[/(blob|tree)/main/...]]`, conteo balanceado de `<section>/<div>/<svg>/<article>/<a>/<p>/<ul>/<li>/<pre>/<code>/<table>/<tr>/<td>`,
  `html.parser` sin tags mal anidados, sin nombres internos/personas, sin CDN/scripts externos, tokens de paleta, sin imágenes externas
- `python <scratchpad>/probe_dom.py blog/... index.html?lang=en index.html?lang=es` — Chrome `--headless=new --dump-dom`
  con script inyectado en copia temporal (`_probe_*.html`, borrada al terminar): `scrollWidth <= innerWidth` en 480/768/1280,
  presencia de botones "Deep dive", card del caso de estudio y `<svg>` de arquitectura, título traducido en ES
- `python <scratchpad>/shot.py <out> anatomia=... fidello=... pyzzeria=... index-writing=index.html?lang=en#writing index-projects=index.html?lang=en#featured-projects index-writing-es=index.html?lang=es#writing`
  (la máquina tiene `navigator.language` es-MX: sin `?lang=en` las capturas de `index.html` salen en ES — primera tanda repetida con `?lang=en`)
  — Chrome `--headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=5000 --user-data-dir=<tmp único> --window-size=W,H --screenshot=<png>` en 1280/768/480
- `python -c "import xml.dom.minidom; xml.dom.minidom.parse('sitemap.xml')"` — sitemap válido tras añadir las 6 páginas del blog
- `Get-Command lighthouse; npx --no-install lighthouse --version` — **no hay CLI de Lighthouse** en la máquina

## Resultados de pruebas (no hay suite unitaria; las "pruebas" son los scripts de auditoría del proyecto)

- `audit_i18n.py`: **57 checks · 57 PASS · 0 FAIL**. Primera corrida dio 1 FAIL (`profile.txt == llms.txt`) porque el worktree
  nuevo no tenía el artefacto gitignored; se regeneró con `cp llms.txt backend/assistant/profile.txt` (mismo comando del workflow CI).
- `probe_i18n.py`: **18 checks · 18 PASS · 0 FAIL**.
- `verify_pages.py` (4 archivos): **66 checks · 66 PASS · 0 FAIL** — 0 enlaces relativos rotos (15 + 7 + 7 + 55 `href/src` revisados),
  enlaces a GitHub correctos, tags balanceados (`index.html`: `<section>` 10/10, `<svg>` 7/7; deep dives: `<svg>` 1/1), sin nombres internos.
  Dos falsos positivos iniciales del script (el `<link rel="canonical">` contaba como CDN y la URL de perfil `github.com/jalducin`)
  se corrigieron en el script, no en las páginas.
- `probe_dom.py`: **15 probes · 15 PASS · 0 FAIL** (5 páginas/idiomas × 3 anchos). Nota: la primera corrida reportó FAIL por un
  error de mi condición (`scrollW == innerW`; `innerWidth` incluye los 15 px de scrollbar) — corregido a `scrollW <= innerW`.
- Lighthouse (tareas 4.3 / 9.2): **omitido** — no existe `lighthouse` CLI ni `npx lighthouse` instalado y el proyecto prohíbe
  añadir dependencias npm; queda como pendiente documentado en `tasks.md`.
- Duración: ~30 s por script de auditoría; ~2 min por tanda de capturas.

## Verificación de estado

- Antes: `main` @ `2170aa9`; `blog/` con 3 posts; `llms.txt` sin Pyzzeria ni deep dives; sitemap con 2 URLs; `index.html` 198−7 claves i18n.
- Después: `blog/` con 6 páginas; `index.html` con card "Anatomy of a change" (`wri.div4/h34/p5/span4`), botones "Deep dive ↗"
  (`proj.a8`, `proj.a9`) y enlaces a los deep dives en la intro de Writing; `llms.txt` con Pyzzeria, deep dives y el caso de estudio;
  `sitemap.xml` con 8 URLs; `es.py` con 7 claves nuevas; JSON `#i18n-es` regenerado (112 578 bytes en `index.html`).
- Estado restaurado: Sí — copias temporales `_probe_*.html` eliminadas; `scripts/i18n/__pycache__/es.cpython-312.pyc` (rastreado en git)
  restaurado con `git checkout --` tras importar `es.py`; `git status` solo muestra archivos del cambio.

## Verificación manual UI/frontend (EL AGENTE EJECUTÓ)

Capturas en `reports/shots/`: `{anatomia,fidello,pyzzeria,index-writing,index-projects,index-writing-es}_{1280,768,480}.png`.

| Check | Resultado |
|---|---|
| Caso de estudio (`anatomia_*.png`) | Flujo de 7 etapas en chips, 4 KPIs (4 col → 2 col ≤768), 7 bloques `.stage` con fragmento real + enlace GitHub; `pre` con scroll interno; sin overflow de página |
| Deep dive Fidello (`fidello_*.png`) | Diagrama SVG: 5 actores → PWA → Supabase (Auth/PostgREST/Realtime/7 Edge Functions) → PostgreSQL (RLS, RPC SECURITY DEFINER, pg_cron) + CI; franja "built, flag off" (Wallet/OAuth/Resend/WhatsApp) — no se presentan como activos; sin botón de código, CTA "Request a demo" |
| Deep dive Pyzzeria (`pyzzeria_*.png`) | Primera versión del SVG tenía etiquetas solapadas y ruta WS recortada → rediseñado por filas (request path sólido, push WS punteado); 0 cruces de etiquetas; CTAs Live demo + View code |
| Diagramas a 480 px | `.diagram{overflow-x:auto}` + `svg{min-width:600px}`: se desplaza el diagrama, no la página (`scrollW 489 <= innerW 504`) |
| `index.html?lang=en#writing` / `?lang=es#writing` (`index-writing*.png`, `index-writing-es*.png`) | Card nueva en primera posición con badge, meta y botón; ES: "Anatomía de un cambio…", "★ Caso de estudio", "Leer ↗"; intro con enlaces Fidello · Pyzzeria |
| `index.html#featured-projects` (`index-projects_*.png`) | Fidello: botón "Deep dive ↗" tras `.tech` (sin "View Code"); Pyzzeria: Live Demo · View Code · Deep dive en fila con wrap; grilla intacta en 1280/768/480 |
| Responsive 992/768/480 | Sin overflow horizontal en las 15 combinaciones probadas (probe DOM); paleta y CSS embebido sin cambios; 0 CDN |
| Casos de error | Enlace a una página inexistente inyectado en copia temporal → `verify_pages.py` reporta FAIL (luego se borró la copia); `index.html#seccion-inexistente` sigue cayendo en `ai-method` (comportamiento previo, sin cambios) |

## Resultado

- Estado Step 9 (pruebas + verificación manual) y Step 10 (documentación): **PASS**
- Bloqueos: ninguno. Pendientes fuera de este cambio: Lighthouse (sin CLI) y merge/archivo (11.x, lo hace el propietario).

## Anexo — `verify_pages.py` (fuente del script ad hoc, ejecutado desde el scratchpad)

```python
GH = re.compile(r"^https://github\.com/jalducin(/[A-Za-z0-9_.-]+(/(blob|tree)/main/[^\s\"']+)?)?/?$")
for f in FILES:
    hrefs = re.findall(r'(?:href|src)="([^"]+)"', s)
    # relativos -> os.path.exists(join(dirname(f), target sin #/?)); GitHub -> GH.match
    for tag in ("section","div","svg","article","a","p","ul","li","pre","code","table","tr","td"):
        o = len(re.findall(r"<%s\b[^>]*(?<!/)>" % tag, s)); c = len(re.findall(r"</%s>" % tag, s)); check(..., o == c)
    HTMLParser subclass -> pila de tags (void: meta/link/img/br/hr/input/path/rect/...) vacía y sin cierres fuera de orden
    FORBIDDEN (nombres internos + personas) -> 0 hits; sin <script src="http..."> ni <link rel="stylesheet" href="http...">
```
