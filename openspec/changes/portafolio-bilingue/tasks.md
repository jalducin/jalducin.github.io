# Tasks: portafolio-bilingue

Agente ejecutor: `frontend-developer`. Bloques ≤ 2 h. El agente ejecuta todas las verificaciones.

## 0. Preparación (OBLIGATORIO — SIEMPRE PRIMERO)

- [x] 0.1 Step 0 — Crear la feature branch `feature/portafolio-bilingue` desde `main` actualizado
- [x] 0.2 Leer `docs/*-standards.md`, `proposal.md`, `design.md` y las 4 specs del cambio
- [x] 0.3 Crear `scripts/mark_i18n.py`: añade `data-i18n`/`data-i18n-title|aria|placeholder` según D2 y
      extrae `scripts/en.json` (clave → HTML EN); idempotente (no duplica atributos)

## 1. Marcado y diccionario

- [x] 1.1 Ejecutar `mark_i18n.py` sobre `index.html`; revisar que ningún elemento con JS (inputs, `#term-out`,
      `a[data-cv]`, palette) quede marcado
- [x] 1.2 Escribir la traducción ES completa (`scripts/es.py` → dict) en el registro del CV ES (D4); declarar
      la lista de claves invariantes (tecnologías/nombres)
- [x] 1.3 `scripts/build_dict.py`: inyecta/reemplaza `<script type="application/json" id="i18n-es">` en
      `index.html` (idempotente)

## 2. Runtime y UI

- [x] 2.1 Botón `#lang-btn` en la nav (junto a `#theme-btn`), CSS reutilizado, `aria-label` bilingüe
- [x] 2.2 Script i18n (D3) antes del script de tabs: captura EN, `applyLang`, resolución
      URL → localStorage → navigator.language → en, `window.__setLang`, `<html lang>`, `document.title`
- [x] 2.3 Command palette: acción "Español / English" (`window.__setLang`)
- [x] 2.4 Terminal: comandos `lang`, `lang es|en`, `idioma es|en`; `help` los lista

## 3. Documentación de apoyo

- [x] 3.1 `llms.txt` + `profile.txt`: nota "site available in ES/EN (language switch)"
- [x] 3.2 `docs/frontend-standards.md`: regla i18n para contenido nuevo (`data-i18n` + entrada ES); `CLAUDE.md`:
      referencia rápida

## 4. Revisar y actualizar pruebas existentes (OBLIGATORIO)

- [x] 4.1 Copiar `audit.py` del cambio archivado a `scripts/audit_i18n.py` y extender con los checks D5
      (JSON parsea, 0 huérfanas, sin traducción == invariantes, sin nombres prohibidos en ES, ≥200 elementos)

## 5. Ejecutar pruebas y verificar estado (OBLIGATORIO) — EL AGENTE EJECUTA

- [x] 5.1 Estado previo: `git rev-parse HEAD`, tamaño de `index.html`, conteo de `data-i18n` (0)
- [x] 5.2 `python scripts/audit_i18n.py` → todos los checks PASS (incluye los 47 heredados)
- [x] 5.3 Estado posterior: tamaño de `index.html`, conteo de claves ES y de invariantes
- [x] 5.4 Reporte `reports/AAAA-MM-DD-step-5-pruebas-y-verificacion.md` (plantilla de la regla)
- [x] 5.5 Marcar solo con audit en PASS y reporte creado

## 6. Verificación manual UI/frontend (OBLIGATORIO) — EL AGENTE EJECUTA

- [x] 6.1 Probe headless: cargar con `?lang=es` → `html.lang=es`, nav en español, h2 de la sección activa en
      español; alternar `__setLang('en')` → innerHTML de 5 elementos muestreados idéntico al original;
      `__showTab`, `a[data-cv]`, `__downloadCV`, `#term-input`, formulario intactos tras 2 alternancias
- [x] 6.2 Probe: sin `?lang`, con `navigator.language` simulado `es-MX` (override en script) → ES; con
      `localStorage.lang=en` → EN; con `localStorage` bloqueado (stub que lanza) → sin errores y toggle funciona
- [x] 6.3 Capturas ES en 1280/768/480 de `#ai-method`, `#experience`, `#featured-projects`, `#hard-skills`,
      `#contact`; sin overflow horizontal; botón de idioma visible en barra y en menú móvil
- [x] 6.4 Terminal: `lang es`, `lang`, `lang xx` (error amable), `help` incluye el comando (probe DOM)
- [x] 6.5 Documentar comandos, resultados y rutas de capturas en el reporte

## 7. Actualizar documentación técnica (OBLIGATORIO)

- [x] 7.1 Sincronizar specs (`scripts/sync_specs.py` reutilizado) → `openspec/specs/idioma-portafolio/spec.md`
      nuevo + deltas en stack-por-niveles, navegacion-por-secciones, terminal-interactiva
- [x] 7.2 Consistencia: `CLAUDE.md`, `docs/frontend-standards.md`, `llms.txt`, memoria del agente; 0 referencias
      rotas

## 8. Cierre

- [ ] 8.1 Commit(s) conventional, merge `--no-ff` a `main`, push; workflows en success
- [ ] 8.2 Verificar en vivo: `curl` de `index.html` contiene `id="i18n-es"` y `id="lang-btn"`; render headless
      de la URL de CloudFront con `?lang=es` muestra "Experiencia"
- [ ] 8.3 `/opsx:verify` y archivar
