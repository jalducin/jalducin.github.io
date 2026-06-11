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

## 2. Paleta de colores

```css
--bg:        #0d1117
--fg:        #c9d1d9
--primary:   #58a6ff
--card-bg:   #161b22
--border:    #30363d
--badge-bg:  #21262d
```

No cambiar la paleta sin documentarlo aquí.

## 3. Responsive

Verificar siempre los tres breakpoints antes de dar un cambio por terminado: **992, 768, 480px**.
No romper el diseño responsive.

## 4. CV en PDF

- `CV_JuanValentinAlducin.pdf` (español) es un archivo **estático precargado** en el repo.
- El botón de descarga apunta directamente al archivo con el atributo `download`.
- El PDF **nunca se genera al vuelo** con JS/librerías. Solo se actualiza subiendo el archivo manualmente.

## 5. Datos del propietario (fuente de verdad)

```
Nombre:    Juan Valentin Alducin Vázquez
Email:     valentin.alducin88@gmail.com
WhatsApp:  +52 5643540747
GitHub:    https://github.com/jalducin
LinkedIn:  https://linkedin.com/in/juanvalducinv
Ubicación: CDMX, Mexico
Inglés:    A2 (Técnico)
```

La tabla completa de experiencia y proyectos vive en `CLAUDE.md` (sección "Datos del propietario").

## 6. Verificación manual (obligatoria por cambio)

Como no hay suite de pruebas automatizada, la verificación manual del cambio es:

1. Abrir `index.html` en el navegador (o servir con `python -m http.server` / Live Server).
2. Confirmar que la sección modificada renderiza correctamente.
3. Revisar los tres breakpoints responsive (992 / 768 / 480px).
4. Verificar que enlaces, descarga de CV y animaciones funcionan.
