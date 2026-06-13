# Proposal — cv-idiomas-y-descarga-en

## Why

- La sección **Idiomas** queda más pulida en la **columna derecha** del CV; ahí sí cabe cómodamente
  **Español (Nativo)** además de Inglés (en la izquierda se había dejado solo Inglés por espacio).
- El CV se actualiza de forma continua. Al **descargarlo**, el archivo debe llevar un **sufijo mes-año**
  (p. ej. `CV_JuanValentinAlducin_2026-06.pdf`) para versionar la copia que se queda el reclutador.
- Hace falta una **versión del CV en inglés** descargable, con un **botón EN** donde aplique (el portafolio
  ya está en inglés y muchos reclutadores la piden).

## What changes

- **cv/cv.html**: mover la sección Idiomas a la columna derecha (Español Nativo + Inglés B1·B2).
- **cv/cv-en.html** (nuevo): CV en inglés, mismo diseño/estilo, 1 página Oficio, ATS-friendly.
- **cv/build.ps1**: generar **dos** PDFs — `CV_JuanValentinAlducin.pdf` (ES) y `CV_JuanValentinAlducin_EN.pdf` (EN).
- **index.html**:
  - Descargas con **sufijo mes-año dinámico** (JS vanilla, calculado al vuelo con la fecha actual).
  - **Botón/acción de descarga EN** donde aplique: sección Contact, command palette y terminal
    (`cat cv en`); el icono del hero descarga ES.
- **docs/frontend-standards.md** y **CLAUDE.md**: documentar el CV bilingüe y la convención de nombre con sufijo.

## Impact

- Specs: nuevas `cv-presentacion` (layout Idiomas) y `cv-descarga-multidioma` (descarga ES/EN + sufijo).
- Sin dependencias nuevas; el sufijo se calcula en cliente (no hay build del nombre). El PDF sigue siendo
  un artefacto estático versionado en el repo; **no** se genera en el navegador del visitante.
- Despliegue automático vía CI/CD (push a `main` → GitHub Actions → AWS).
