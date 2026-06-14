# Tasks — cv-icono-resume

## Step 0 — Crear feature branch (SIEMPRE PRIMERO)
- [x] Crear y cambiar a `feature/cv-icono-resume`.

## Step 1 — Reemplazar el glifo del ícono de CV (hero)
- [x] En `index.html`, dentro de `.header-links`, reemplazar el `path` SVG de los **dos** botones `a.cv-link`
      (ES y EN) por el ícono résumé (hoja + busto de persona + líneas). Conservar `viewBox="0 0 24 24"`,
      `fill="currentColor"`, las etiquetas `<span>ES</span>` / `<span>EN</span>`, `data-cv`, `download`,
      `title`/`aria-label` y la clase `cv-link`.
- [x] Glifo candidato (un solo `<path>` para mantener el patrón actual):

      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor"
      d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-6-6zm-1 1.5L18.5 9H14a1 1 0 01-1-1V3.5zM9.5 13.2a1.7 1.7 0 110-3.4 1.7 1.7 0 010 3.4zM6.4 18c0-1.9 1.4-3.1 3.1-3.1S12.6 16.1 12.6 18zM14.5 11h3.2v1.2h-3.2zM14.5 14h2.6v1.2h-2.6z"/></svg>

      (página con esquina doblada + cabeza + hombros + 2 líneas de texto; ajustar coordenadas si hace falta
      para que el busto y las líneas se vean balanceados a 22×22 px).

## Step 2 — Revisar pruebas existentes (OBLIGATORIO)
- [x] Sin suite automatizada; verificación manual (frontend-standards §6). N/A unitarias.

## Step 3 — Ejecutar verificación (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] Render del hero (screenshot) y confirmar que el ícono se lee como CV/résumé en dorado, con ES/EN.
- [x] Confirmar que la descarga sigue funcionando (atributos `download` con sufijo `AAAA-MM` vía `--dump-dom`).
- [x] Reporte en `specs/cv-icono-resume/reports/AAAA-MM-DD-step-3-verificacion.md`.

## Step 4 — Verificación manual UI (OBLIGATORIO) — EL AGENTE EJECUTA
- [x] Revisar los tres breakpoints (992 / 768 / 480px): el ícono y las etiquetas ES/EN no se rompen.

## Step 5 — Documentación (OBLIGATORIO)
- [x] Si cambia algo del contrato visual, sincronizar `docs/frontend-standards.md` (sección CV). (Probable: sin cambios.)

## Step 6 — Promover specs y archivar
- [x] Merge a main, promover el delta a `openspec/specs/cv-descarga-multidioma/`, archivar el cambio, push (CI/CD).
