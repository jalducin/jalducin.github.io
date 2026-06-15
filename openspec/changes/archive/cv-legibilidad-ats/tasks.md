# Tasks — cv-legibilidad-ats

## Step 0 — Feature branch (PRIMERO)
- [x] `feature/cv-legibilidad-ats`.

## Step 1 — Tipografía y 1 página
- [x] Escala 8.5/9/10pt (cuerpo 11.3px, headings 14px, role 13px, nombre completo 22px).
- [x] Acortar descripciones de proyectos a 1 línea; Idiomas a la derecha; QR Portafolio al header; quitar edX y un bullet de Redsis.
- [x] Header `align-items:flex-start` (QR + caption alineados).

## Step 2 — ATS
- [x] Contacto como texto (tel, email, portafolio, LinkedIn, GitHub); `aria-hidden` en los QR.

## Step 3 — Fix crítico
- [x] Reescribir el bullet 4 de Podemos (cv/cv.html) corrompido por sed (`&` en reemplazo) → texto limpio.

## Step 4 — Verificación (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] Regenerar PDFs (`cv/build.ps1`, `--headless=new`) y verificar **1 página** por conteo real del árbol de páginas (ES=1, EN=1).
- [x] Render de ambos CVs.
- [x] Reporte en `specs/cv-legibilidad-ats/reports/2026-06-15-verificacion.md` con resultados de los 3 agentes.

## Step 5 — Revisión por agentes (OBLIGATORIO)
- [x] **design-specialist**: 7.5/10 APTO CON OBSERVACIONES (detectó el bullet corrupto → corregido).
- [x] **ats-reviewer**: 7.5/10 APTO CON OBSERVACIONES (detectó el bullet corrupto → corregido; sugirió aria-hidden → aplicado).
- [x] **compliance-reviewer**: agente no disponible en sesión (registry); validación manual = APTO (sin secretos/PII/claims problemáticos; sin cambios de contenido legal).

## Step 6 — Promover spec y archivar
- [x] Merge a main, promover delta a `openspec/specs/cv-presentacion/`, archivar el cambio, push (CI/CD).
