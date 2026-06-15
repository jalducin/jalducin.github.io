---
description: Estándares de frontend para el portafolio estático jalducin.github.io (stack, paleta, reglas de código y responsive).
alwaysApply: true
---

# Estándares de frontend — jalducin.github.io

> Estándares específicos del portafolio personal. Complementan `base-standards.md` y
> `documentation-standards.md`. Cualquier artefacto OpenSpec que toque el sitio DEBE seguir estas reglas.

## 1. Stack (no negociable)

- **HTML5 + CSS3 + JavaScript Vanilla** — sin frameworks JS ni CSS.
- **GitHub Pages** — despliegue estático, sin build step.
- CSS embebido en `<style>` dentro del HTML (no archivos `.css` externos).
- JavaScript inline o en `<script>` al final del body (no archivos `.js` externos).
- CSS custom properties para la paleta de colores; media queries propios.

### No usar
- Frameworks JS (React, Vue, Angular, jQuery).
- Frameworks CSS (Bootstrap nuevo, Tailwind).
- Dependencias de npm o CDNs de frameworks pesados.

## 2. Paleta de colores (azul metálico profesional)

```css
/* DARK (default) */
--bg:          #0f141a   /* azul noche muy oscuro */
--fg:          #dde6ef   /* blanco azulado */
--primary:     #7fa8c9   /* azul acero claro */
--accent2:     #a9c5dd   /* azul niebla */
--card-bg:     #161d26
--border:      #2a3744
--badge-bg:    #1b232d
--badge-border:#2a3744
--container-bg:rgba(15,20,26,0.85)
--muted:       #8b949e   /* texto secundario — dark: ratio ≥6:1 */

/* LIGHT (html.light) */
--bg:          #eef2f6
--fg:          #1f2a35
--primary:     #3f6488   /* azul acero oscuro */
--accent2:     #5b80a6
--card-bg:     #ffffff
--border:      #ccd8e2
--badge-bg:    #e2eaf1
--badge-border:#ccd8e2
--container-bg:rgba(238,242,246,0.97)
--muted:       #596573   /* override para light: ratio 5.28:1 sobre #eef2f6, PASS AA */
```

El efecto **matrix** se conserva **recoloreado a azul metálico** (`#7fa8c9` sobre `#0f141a`).
Se oculta en modo claro (`html.light #matrix-bg{display:none}`).
Terminal (`#terminal .term`): fondo `#120d09` en dark; override a `#1e2730` en light.
No cambiar la paleta sin documentarlo aquí.

## 3. Responsive

Verificar siempre los tres breakpoints antes de dar un cambio por terminado: **992, 768, 480px**.
No romper el diseño responsive.

## 4. CV en PDF (self-hosted, bilingüe ES/EN)

- Fuentes editables: `cv/cv.html` (español) y `cv/cv-en.html` (inglés) — mismo diseño estilo enhancv,
  **tamaño Oficio 216×340 mm**, 1 página, ATS-friendly. La sección Idiomas vive en la columna derecha.
- Los PDFs se generan con un **build step** (Chrome/Edge headless, `cv/build.ps1`) hacia
  `cv/CV_JuanValentinAlducin.pdf` (ES) y `cv/CV_JuanValentinAlducin_EN.pdf` (EN). `build.ps1` usa un
  `--user-data-dir` único por PDF (evita el singleton de Chrome headless en llamadas seguidas).
- Las descargas usan `download` con **sufijo mes-año dinámico** (JS vanilla): el archivo se entrega como
  `CV_JuanValentinAlducin_AAAA-MM.pdf` / `..._EN_AAAA-MM.pdf`. El binario sigue siendo estático; el PDF
  **no se genera en el navegador del visitante** (no hay JS de generación en el sitio).
- El botón EN aparece donde aplique (Contact, command palette, terminal `cat cv en`).
- Para editar el CV: cambiar `cv/cv.html` y/o `cv/cv-en.html` → regenerar → commitear HTML + PDFs. No editar el binario a mano.

## 5. Datos del propietario (fuente de verdad)

```
Nombre:    Juan Valentin Alducin Vázquez
Posición:  Senior Software Engineer · AI-native Development
Email:     valentin.alducin88@gmail.com
WhatsApp:  525640800494
GitHub:    https://github.com/jalducin
LinkedIn:  https://linkedin.com/in/juanvalducinv
Ubicación: CDMX, Mexico
Inglés:    B1 (Intermedio)
```

La tabla completa de experiencia y proyectos vive en `CLAUDE.md` (sección "Datos del propietario").

## 6. Verificación manual (obligatoria por cambio)

Como no hay suite de pruebas automatizada, la verificación manual del cambio es:

1. Abrir `index.html` en el navegador (o servir con `python -m http.server` / Live Server).
2. Confirmar que la sección modificada renderiza correctamente.
3. Revisar los tres breakpoints responsive (992 / 768 / 480px).
4. Verificar que enlaces, descarga de CV y animaciones funcionan.
