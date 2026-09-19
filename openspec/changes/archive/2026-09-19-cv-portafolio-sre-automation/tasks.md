# Tasks: cv-portafolio-sre-automation

Agente ejecutor: `frontend-developer` (`ai-specs/agents/`). Cada bloque ≤ 2 h. Las verificaciones las
ejecuta el agente; nunca se delegan al usuario. Orden de edición según `design.md` D8.

## 0. Preparación (OBLIGATORIO — SIEMPRE PRIMERO)

- [x] 0.1 Step 0 — Crear y cambiar a la feature branch `feature/cv-portafolio-sre-automation` desde `main`
      actualizado (`git checkout main && git pull && git checkout -b feature/cv-portafolio-sre-automation`)
- [x] 0.2 Leer `docs/base-standards.md`, `docs/frontend-standards.md`, `docs/documentation-standards.md`,
      `proposal.md`, `design.md` y las 8 specs del cambio
- [x] 0.3 Crear `openspec/changes/cv-portafolio-sre-automation/scripts/audit.py` con las comprobaciones
      automáticas reutilizables: (a) grep de nombres internos prohibidos (D2) en `index.html`, `cv/*.html`,
      `llms.txt`, `cv/CV_JuanValentinAlducin.md`; (b) headline idéntico en `header h3`, `<title>`, OG, JSON-LD,
      `whoami`, `.tagline` ES/EN; (c) fechas/títulos de los 4 roles iguales en CV ES, CV EN, `index.html`,
      `llms.txt`; (d) ausencia de "Kendra", "Kiro", "Master", "IEU"; (e) conteo de páginas y fuentes de los PDF
      (pypdf). Salida: PASS/FAIL por check

## 1. Portafolio — posicionamiento y metodología (`index.html`)

- [x] 1.1 Headline híbrido (D1) en `header h3`, `<title>`, `og:title`, `twitter:title`, JSON-LD `jobTitle`
      y comando `whoami` de la terminal
- [x] 1.2 Reescribir el resumen del header y `meta description`/`og:description`/`twitter:description`
      según spec `posicionamiento-ai-native` (confiabilidad + automatización + IA + ≥2 métricas; sin maestría)
- [x] 1.3 `meta keywords`: agregar SRE, reliability, post-mortems, n8n, automation; quitar Kendra y Kiro
- [x] 1.4 JSON-LD `knowsAbout`: agregar "Site Reliability Engineering", "Post-mortems", "n8n", "Automation";
      quitar "Amazon Kendra"/"AWS Kiro" si existen
- [x] 1.5 Badges de métricas del header y card "Measurable impact": agregar "99.95% monthly uptime"
      (spec `agentic-engineering-hardening`)
- [x] 1.6 Bloque "How I work" con los 4 principios (D5) dentro de `#ai-method`, reutilizando `.now-card`

## 2. Portafolio — experiencia, skills y Fidello (`index.html`)

- [x] 2.1 Reescribir bullets de Podemos (rol actual 7 bullets, rol anterior 3) según D3 y spec
      `experiencia-actualizada`; stack sin Kubernetes/Kendra/Kiro; reemplazar "SCI, Spore, Hipatia, Mambu
      Tools" por lenguaje genérico (D2)
- [x] 2.2 Skills por niveles (D4): CSS embebido `.level-grid`/`.level`/`.level-title`/`.level-def` con tokens de
      la paleta; leyenda de 4 niveles; reemplazar el bloque "Tech Stack & Tools" por los 4 grupos con el
      inventario de la spec `stack-por-niveles`; retirar íconos de Kubernetes y Laravel de `icons-grid`
- [x] 2.3 Card Fidello (D6): badges "★ AI-native · 100% SDD" + "🧪 Pilot · cloud beta"; descripción y
      seguridad según spec `proyecto-fidello` (sin Google Wallet como activo); fila de mini-badges con cifras
      (793 tests · 91 migrations · 22 tables · 7 Edge Functions · 5 cron · 97 OpenSpec changes · 28 journeys ·
      QAS/PROD); `.tech` ampliada; línea sobre el paquete de revisión de arquitectura
- [x] 2.4 Verificar que la card de VoltGrid conserva Kubernetes (Kustomize) en su `.tech`

## 3. Capa AI-readable y CV

- [x] 3.1 `llms.txt`: headline híbrido, sección "## How I work" (4 principios), stack por niveles, experiencia
      (ambos roles, genérico), Fidello piloto con cifras, métricas con uptime; sin Kendra/Kiro/maestría.
      Regenerar `backend/assistant/profile.txt` con `cp llms.txt backend/assistant/profile.txt`
- [x] 3.2 `cv/cv.html` (ES): `.tagline` híbrido, resumen 4 líneas, bullets Podemos (rol actual ≤ 6, anterior
      ≤ 3) compactados desde D3 en español, lenguaje genérico, Habilidades sin Kendra/Kiro/K8s y con
      Observabilidad/Automatización/Calidad, Fidello "Piloto en beta cloud · 793 pruebas · 91 migraciones"
- [x] 3.3 `cv/cv-en.html` (EN): mismos cambios en inglés
- [x] 3.4 Ejecutar `powershell -ExecutionPolicy Bypass -File cv\build.ps1`; verificar con pypdf que ambos PDF
      tienen 1 página y solo fuentes `SegoeUI*` (spec `cv-presentacion`). Si hay 2 páginas aplicar D7 y
      repetir hasta 1 página
- [x] 3.5 Actualizar `cv/CV_JuanValentinAlducin.md` para que espeje 1:1 el contenido ES nuevo

## 4. Revisar y actualizar pruebas existentes (OBLIGATORIO)

- [x] 4.1 El proyecto no tiene suite automatizada de pruebas; las "pruebas" son las comprobaciones de
      `scripts/audit.py` (0.3) y las verificaciones headless. Extender `audit.py` con los checks nuevos que
      exijan las specs de este cambio (leyenda de niveles presente, 4 principios en `index.html` y `llms.txt`,
      badges de Fidello con las cifras, uptime en badges) y registrar en el reporte qué checks se agregaron

## 5. Ejecutar pruebas y verificar estado (OBLIGATORIO) — EL AGENTE EJECUTA

- [x] 5.1 Capturar estado previo: `git rev-parse HEAD`, tamaño y páginas de los PDF actuales, salida de
      `audit.py` antes de los cambios (se espera FAIL en los checks nuevos)
- [x] 5.2 Ejecutar `python openspec/changes/cv-portafolio-sre-automation/scripts/audit.py` tras los cambios:
      todos los checks en PASS
- [x] 5.3 Validar HTML/JSON: `python -c "import json,re;..."` parsea el JSON-LD sin error; el `index.html` no
      tiene IDs duplicados ni anclas rotas (`GROUPS` sigue apuntando a secciones existentes)
- [x] 5.4 Crear el reporte `openspec/changes/cv-portafolio-sre-automation/reports/AAAA-MM-DD-step-5-pruebas-y-verificacion.md`
      con la plantilla de `.claude/rules/openspec-tasks-mandatory-steps.md` (comandos, resultados, estado
      antes/después, restauración)
- [x] 5.5 Marcar este paso solo cuando `audit.py` esté en PASS y el reporte exista

## 6. Verificación manual UI/frontend (OBLIGATORIO) — EL AGENTE EJECUTA

- [x] 6.1 Render headless de `index.html` (Chrome `--headless=new --screenshot`) en 1280, 992, 768 y 480 px para
      las vistas `#ai-method`, `#experience`, `#featured-projects` y `#hard-skills`; revisar visualmente:
      sin desbordes horizontales, leyenda de niveles legible, principios visibles, badges de Fidello en una fila
      o envueltos sin romper la card
- [x] 6.2 Probe headless con `--dump-dom`: `window.__showTab` presente, 4 enlaces `a[data-cv]` con `download`
      dinámico `_AAAA-MM`, `whoami` devuelve el headline híbrido (ejecutar `CMDS.whoami()` vía script inyectado)
- [x] 6.3 Render headless de `cv/cv.html` y `cv/cv-en.html` a PNG (816×1330) y revisar: 1 página, dos roles de
      Podemos, sin maestría, tagline híbrido, Fidello con cifras; extraer texto del PDF con pypdf y confirmar
      que contiene nombre, teléfono, email, roles, fechas y no contiene nombres internos prohibidos
- [x] 6.4 Casos de error: abrir `index.html#seccion-inexistente` → cae en `ai-method` sin error de consola;
      `audit.py` con un nombre prohibido inyectado en un archivo temporal → FAIL detectado (luego borrar el temporal)
- [x] 6.5 Documentar comandos y resultados (con rutas de capturas) en el reporte del paso 5

## 7. Actualizar documentación técnica (OBLIGATORIO)

- [x] 7.1 `CLAUDE.md`: "Posición" del propietario → headline híbrido; nota de que las skills se listan por
      niveles y de la regla "sin nombres internos del empleador"; Fidello como piloto en la tabla de proyectos
- [x] 7.2 `docs/frontend-standards.md §5` (datos del propietario) y cualquier mención del headline anterior
      o de la maestría; `cv/README.md` si cambia el flujo
- [x] 7.3 Sincronizar specs: aplicar los deltas de este cambio a `openspec/specs/*` con `/opsx:sync` (o al
      archivar), y crear `openspec/specs/stack-por-niveles/spec.md` y `openspec/specs/principios-de-trabajo/spec.md`
- [x] 7.4 Consistencia documental: `grep` de "Agentic AI Systems", "Master's in DevOps", "Kendra", "Kiro" en
      `*.md`, `*.html`, `*.txt` (excluyendo `openspec/changes/archive`) → 0 coincidencias fuera de este cambio;
      actualizar la memoria del agente (`user_profile.md`: headline, Fidello piloto)

## 8. Cierre

- [x] 8.1 Commit(s) con conventional commits (`feat(cv+web): ...`), merge `--no-ff` a `main` y push (deploy
      automático a S3/CloudFront y Lambda del asistente)
- [x] 8.2 Verificar en vivo (`curl https://d3r3bnavnwzqaw.cloudfront.net/`): headline híbrido presente, PDF ES/EN
      HTTP 200 con el mismo tamaño en bytes que los locales, `llms.txt` con "How I work"; `gh run list` con los
      3 workflows en success
- [x] 8.3 Entregar al usuario `cv/CV_JuanValentinAlducin.md` como base para LinkedIn y ejecutar `/opsx:verify`
      antes de archivar
