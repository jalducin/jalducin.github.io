# Tasks — cv-idiomas-y-descarga-en

## Step 0 — Crear feature branch (SIEMPRE PRIMERO)
- [x] Crear y cambiar a `feature/cv-idiomas-y-descarga-en`.

## Step 1 — cv.html: Idiomas a la derecha
- [x] Quitar la sección Idiomas de la columna izquierda.
- [x] Insertarla en la columna derecha (después de Habilidades) con Español (Nativo) + Inglés.

## Step 2 — CV en inglés
- [x] Crear `cv/cv-en.html` (copia con contenido traducido al inglés, mismo diseño, Idiomas a la derecha).
- [x] Actualizar `cv/build.ps1` para generar ES y EN.

## Step 3 — index.html: descarga multidioma
- [x] Botón/acción de descarga EN en Contact, command palette y terminal (`cat cv en`).
- [x] Sufijo mes-año dinámico (JS vanilla) en todas las acciones de descarga (ES y EN).

## Step 4 — Revisar pruebas existentes (OBLIGATORIO)
- [x] Sin suite automatizada; verificación manual (frontend-standards §6). N/A unitarias.

## Step 5 — Ejecutar verificación (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] Regenerar ambos PDFs y verificar **1 página** cada uno (`/Count=1`).
- [x] Verificar que el nombre de descarga lleva sufijo `AAAA-MM` (revisión del JS y atributos `download`).
- [x] Render de ambos CVs (screenshot) — Idiomas a la derecha con Español+Inglés.
- [x] Reporte en `specs/cv-idiomas-y-descarga-en/reports/AAAA-MM-DD-step-5-verificacion.md`.

## Step 6 — Verificación manual UI (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] Confirmar que los enlaces ES/EN apuntan a los PDFs correctos y la acción EN existe en Contact/palette/terminal.

## Step 7 — Documentación (OBLIGATORIO)
- [x] Actualizar `docs/frontend-standards.md` y `CLAUDE.md`: CV bilingüe + convención de nombre con sufijo.

## Step 8 — Promover specs y archivar
- [x] Merge a main, promover specs a `openspec/specs/`, archivar el cambio, push (CI/CD despliega).
