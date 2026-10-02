# jalducin.github.io — Portafolio de Proyectos

Sitio de portafolio personal publicado en [jalducin.github.io](https://jalducin.github.io).

## Descripción

Portafolio profesional de **Juan Valentin Alducin Vázquez** — Senior Software Engineer · AI-native Development, con enfoque en backend, integración de IA generativa (Claude/SDD, Gemini, OpenAI) en el SDLC y Spec-Driven Development. El sitio incluye:

- Experiencia laboral (timeline interactivo)
- Proyectos destacados con links a GitHub
- Hard skills con iconografía de tecnologías y sub-sección "Tech Stack & Tools" categorizada
- Educación y certificaciones
- Diseño estético matrix/binario: lluvia de 0s y 1s animada como fondo, tipografía monospace con glow
- Descarga directa del CV en PDF (español)

## Tecnologías

- HTML5 + CSS3 + JavaScript Vanilla (sin frameworks)
- GitHub Pages (despliegue estático)
- Diseño responsivo con media queries

## Estructura

```
jalducin.github.io/
├── index.html                         ← Portafolio principal (single page)
├── cv/                                ← CV: fuente (cv.html) + PDF generado
├── blog/                              ← Posts, caso de estudio SDD y deep dives de proyectos (HTML estático)
├── assets/img/                        ← imágenes (QR.png, og-image)
├── assets/                            ← Recursos estáticos
├── CLAUDE.md / AGENTS.md / GEMINI.md  ← Contexto por asistente de IA
├── docs/                              ← Estándares (base, frontend, documentación)
├── openspec/                          ← Flujo SDD: project.md, specs/, changes/, schemas
├── ai-specs/                          ← Fuente canónica de agentes y skills
├── .claude/  /  .gemini/              ← Comandos /opsx:*, skills, agentes, reglas
└── .gitignore
```

## Despliegue

El sitio se publica en **GitHub Pages** desde la rama `main` (estático, sin build step).

- **En vivo:** https://jalducin.github.io
- **CI/CD:** push a `main` → GitHub Pages publica automáticamente. No hay workflow de despliegue propio.
- **Historia:** entre junio y septiembre de 2026 el sitio también se sirvió desde AWS (S3 privado + CloudFront
  con OAC, desplegado por OIDC). El 2026-10-01 esos recursos se eliminaron en una limpieza de la cuenta AWS
  —junto con el backend del asistente y del formulario— y el hosting volvió a ser solo GitHub Pages, que
  siempre fue la URL canónica. Ver el cambio OpenSpec archivado `2026-10-02-migrar-backend-portafolio`.

## Asistente IA ("Ask my portfolio")

Widget de chat en `index.html` (burbuja `#ai-fab`) que responde preguntas sobre el perfil de Juan
**sin backend y sin LLM**: recuperación en el navegador sobre una base de conocimiento curada.

- **Base:** `assistant/knowledge.md` (entradas bilingües con `tags`), compilada por
  `python scripts/assistant/build_kb.py` a `<script type="application/json" id="assistant-kb">` en `index.html`.
- **Costo y privacidad:** $0, sin API key, sin peticiones de red ni rastreo; funciona offline.
- **Pruebas:** `python scripts/assistant/probe_kb.py` (18 probes) + checks en `scripts/i18n/audit_i18n.py`.
- El backend anterior en AWS (Lambda + API Gateway + DynamoDB + Bedrock) se retiró el 2026-10-01; ver el
  cambio `openspec/changes/archive/2026-10-02-migrar-backend-portafolio/`.

## 🔄 Cómo contribuir (SDD / OpenSpec)

El proyecto sigue **Spec-Driven Development**: la especificación es la fuente de verdad y cada cambio
recorre `proposal → specs → design → tasks → apply → archive` antes (y durante) la codificación.

1. Lee los estándares: `docs/base-standards.md` y `docs/frontend-standards.md`.
2. Inicia un cambio con `/opsx:new` (o `/opsx:ff` para generar todos los artefactos de un tirón).
3. Implementa con `/opsx:apply` desde una rama `feature/<change-name>`.
4. Verifica con `/opsx:verify` (verificación manual en navegador, 3 breakpoints) y archiva con `/opsx:archive`.
