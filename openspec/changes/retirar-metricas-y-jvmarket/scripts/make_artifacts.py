# -*- coding: utf-8 -*-
"""Genera proposal/design/tasks y los delta specs (MODIFIED copiando el bloque completo del spec principal)."""
import io, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
os.chdir(ROOT)
CH = "openspec/changes/retirar-metricas-y-jvmarket"


def block(cap, name):
    s = io.open("openspec/specs/%s/spec.md" % cap, encoding="utf-8").read()
    m = re.search(r"(### Requirement: %s\n.*?)(?=\n### Requirement: |\Z)" % re.escape(name), s, re.S)
    assert m, (cap, name)
    return m.group(1).rstrip() + "\n"


def delta(cap, mods, removed=None):
    os.makedirs("%s/specs/%s" % (CH, cap), exist_ok=True)
    out = "# Capability: %s (delta)\n\n" % cap
    if mods:
        out += "## MODIFIED Requirements\n\n"
        for name, reps in mods:
            b = block(cap, name)
            for o, n in reps:
                assert o in b, (cap, name, o[:40])
                b = b.replace(o, n)
            out += b + "\n"
    if removed:
        out += "## REMOVED Requirements\n\n" + removed
    io.open("%s/specs/%s/spec.md" % (CH, cap), "w", encoding="utf-8", newline="").write(out)
    print("delta", cap)


delta("agentic-engineering-hardening", [
    ('Sección "How I build with AI" (metodología agentic)', [
        ("candidato, demostrando el *cómo* con métricas verificables, no solo declarando herramientas.",
         "candidato, demostrando el *cómo* con prácticas y resultados operativos, no solo declarando herramientas."),
        ("- **AND** se muestran las métricas de impacto: ~40% de reducción del ciclo de revisión, 80% de\n  autoresolución de incidentes N1, primera respuesta <10 min y resolución de incidentes <2 h",
         "- **AND** se muestran los SLAs operativos: primera respuesta <10 min y resolución de incidentes críticos <2 h\n- **AND** NO se publican porcentajes de mejora (reducción de revisión, autoresolución N1, uptime): retirados por\n  decisión del propietario el 2026-09-20")]),
    ("Badges de métricas", [
        ("El sitio SHALL destacar visualmente las métricas de impacto del CV mediante badges, reutilizando el\nsistema de diseño existente.",
         "El sitio SHALL destacar visualmente los SLAs operativos del CV mediante badges, reutilizando el sistema de\ndiseño existente, sin porcentajes de mejora."),
        ('- **THEN** se muestran badges con "−40% code review time", "80% N1 self-resolution", "<10 min first\n  response" y "99.95% monthly uptime"\n- **AND** la tarjeta "Measurable impact" de la sección de metodología lista las mismas cuatro métricas',
         '- **THEN** se muestran badges con "<10 min first response" y "<2 h critical resolution" (y opcionalmente\n  prácticas como "blameless post-mortems" / "spec-driven pipelines"), sin "40%", "80%" ni "99.95%"\n- **AND** la tarjeta "Measurable impact" pasa a "Operational SLAs & practices" y lista los mismos SLAs y prácticas')]),
])
delta("experiencia-actualizada", [
    ("Rol Podemos Progresar alineado al CV", [
        ("críticos y deuda técnica end-to-end con SDD + Claude API, con ~40 % menos tiempo de revisión de código",
         "críticos y deuda técnica end-to-end con SDD + Claude API, acortando el ciclo de revisión (sin porcentaje)"),
        ("reales; downtime = impacto real al usuario) con el resultado 99.95 % en julio 2026",
         "reales; downtime = impacto real al usuario), sin publicar la cifra de uptime"),
        ("- **AND** sus bullets incluyen: gestión de incidentes N2 con RCA/post-mortems asistidos por IA; 80 % de\n  autoresolución N1 vía transferencia de conocimiento;",
         "- **AND** sus bullets incluyen: gestión de incidentes N2 con RCA/post-mortems asistidos por IA; autoresolución\n  N1 habilitada vía transferencia de conocimiento (sin porcentaje);")]),
])
delta("posicionamiento-ai-native", [
    ("Resumen profesional alineado al CV", [
        ("spec-driven); IA generativa (Claude, Gemini, OpenAI) como copiloto del SDLC con Spec-Driven Development; y\nmétricas de impacto verificables.",
         "spec-driven); IA generativa (Claude, Gemini, OpenAI) como copiloto del SDLC con Spec-Driven Development; sin\nporcentajes de mejora."),
        ("- **AND** incluye al menos dos métricas de impacto entre: ~40 % menos tiempo de revisión, 80 % de\n  autoresolución N1, primera respuesta <10 min, uptime mensual 99.95 %",
         "- **AND** NO incluye porcentajes de mejora (~40 %, 80 %, 99.95 %); puede citar los SLAs (<10 min / <2 h)")]),
])
delta("proyecto-jvmarket", [], removed="""### Requirement: Proyecto JV Market (desplegado en AWS) en portafolio y CV
**Reason**: El propietario retiró JV Market del portafolio el 2026-09-20 (la demo destacada es Pyzzeria; el e-commerce
no aporta a la narrativa SRE/automatización/IA y duplicaba stack con Pyzzeria).
**Migration**: Se elimina la card de `index.html`, la entrada en `llms.txt`, la fila en `CLAUDE.md`, las claves
`proj.div7/h36/p7/a6` del diccionario ES y el nombre en `ls projects` de la terminal. El repositorio
`jalducin/EcommerceJVAV` sigue público; no se enlaza desde el sitio.
""")

io.open(CH + "/proposal.md", "w", encoding="utf-8", newline="").write("""# Proposal: retirar-metricas-y-jvmarket

## Why
El propietario decidió (2026-09-20) no publicar porcentajes de mejora en CV ni portafolio (~40 % menos tiempo de
revisión, 80 % de autoresolución N1, 99.95 % de uptime en julio 2026) y retirar el proyecto JV Market del
portafolio. Las specs vigentes exigen ambas cosas, así que el cambio debe formalizarse.

## What Changes
- Se retiran las tres cifras de: header y badges de `index.html`, tarjeta "Measurable impact", bullets de
  Podemos, meta/OG/JSON-LD, `llms.txt`, diccionario ES, CV ES/EN (PDFs regenerados). Se conservan los SLAs
  (<10 min primera respuesta, <2 h resolución crítica) y la redacción cualitativa.
- Se elimina la card de JV Market (`index.html`), su entrada en `llms.txt`, su fila en `CLAUDE.md`, sus claves
  ES y su mención en la terminal (`ls projects`).
- Audit i18n actualizado (checks de cifras / JV Market).

## Capabilities
### New Capabilities
(ninguna)
### Modified Capabilities
- `agentic-engineering-hardening`: badges y tarjeta de impacto sin porcentajes.
- `experiencia-actualizada`: bullets de Podemos sin cifras.
- `posicionamiento-ai-native`: resumen sin porcentajes.
- `proyecto-jvmarket`: requirement REMOVED.

## Impact
`index.html`, `scripts/i18n/es.py` (+ `build_dict.py`), `llms.txt`/`profile.txt`, `cv/cv.html`, `cv/cv-en.html`,
PDFs, `CLAUDE.md`, `scripts/i18n/audit_i18n.py`, specs. Deploy automático al mergear.
""")
io.open(CH + "/design.md", "w", encoding="utf-8", newline="").write("""# Design: retirar-metricas-y-jvmarket

## Context
Cambio de contenido dirigido por el propietario; no hay decisión técnica nueva. Se aplica sobre `main` tras
mergear `feature/case-study-y-deep-dives` para evitar conflictos en `index.html`/`es.py`.

## Decisions
- D1. Las cifras se sustituyen por redacción cualitativa equivalente ("acortando el ciclo de revisión",
  "habilité la autoresolución en N1", "metodología de uptime/downtime por impacto real"); no se dejan huecos.
- D2. Se conservan los SLAs (<10 min / <2 h): el propietario no los mencionó y son compromisos, no porcentajes
  de mejora.
- D3. La tarjeta "Measurable impact" se renombra "Operational SLAs & practices" (EN) / "SLAs y prácticas
  operativas" (ES) y lista SLAs + 2 prácticas para no quedar con 2 líneas.
- D4. JV Market se elimina por completo (no se oculta); las claves i18n se retiran de `es.py` para que
  `build_dict.py` no reporte huérfanas.
- D5. `audit_i18n.py`: el check "uptime en badges/impacto" pasa a "sin cifras 40%/80%/99.95 en index, llms,
  CV y diccionario" y se añade "sin JV Market".

## Risks / Trade-offs
- [Perder gancho cuantitativo en el header] → los SLAs y las prácticas (post-mortems, uptime methodology,
  n8n) mantienen el mensaje; decisión del propietario.
""")
io.open(CH + "/tasks.md", "w", encoding="utf-8", newline="").write("""# Tasks: retirar-metricas-y-jvmarket

## 0. Preparación (OBLIGATORIO — SIEMPRE PRIMERO)
- [x] 0.1 Step 0 — Rama `feature/retirar-metricas-y-jvmarket` desde `main` tras mergear las ramas paralelas

## 1. Contenido
- [x] 1.1 CV ES/EN sin 40 %/80 %/99.95 %; PDFs regenerados (1 página)
- [x] 1.2 `llms.txt`/`profile.txt` sin cifras y sin JV Market; `CLAUDE.md` sin la fila de JV Market y con la nota
- [ ] 1.3 `index.html`: header, badges, tarjeta de impacto, bullets, meta/OG/JSON-LD sin cifras; card JV Market
      eliminada; `ls projects` sin JV-Market
- [ ] 1.4 `scripts/i18n/es.py`: traducciones sin cifras; claves de JV Market retiradas; `build_dict.py`

## 2. Revisar y actualizar pruebas existentes (OBLIGATORIO)
- [ ] 2.1 `scripts/i18n/audit_i18n.py`: check de uptime → check "sin cifras" + "sin JV Market"

## 3. Ejecutar pruebas y verificar estado (OBLIGATORIO) — EL AGENTE EJECUTA
- [ ] 3.1 `audit_i18n.py` 0 FAIL; `probe_i18n.py` 18/18; PDFs 1 página sin cifras; reporte en `reports/`

## 4. Verificación manual (OBLIGATORIO) — EL AGENTE EJECUTA
- [ ] 4.1 Render headless de header/AI Method/Projects (1280/480) en EN y ES: sin cifras, sin JV Market, grilla de
      proyectos sin hueco

## 5. Documentación (OBLIGATORIO)
- [ ] 5.1 Specs sincronizadas (3 deltas + REMOVED de `proyecto-jvmarket`), `openspec validate --specs` verde

## 6. Cierre
- [ ] 6.1 Push a `main`, workflows en success, verificación en vivo, archivar
""")
print("artefactos OK")
