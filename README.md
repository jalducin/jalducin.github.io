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

El sitio se publica automáticamente vía GitHub Pages desde la rama `main`.

## 🔄 Cómo contribuir (SDD / OpenSpec)

El proyecto sigue **Spec-Driven Development**: la especificación es la fuente de verdad y cada cambio
recorre `proposal → specs → design → tasks → apply → archive` antes (y durante) la codificación.

1. Lee los estándares: `docs/base-standards.md` y `docs/frontend-standards.md`.
2. Inicia un cambio con `/opsx:new` (o `/opsx:ff` para generar todos los artefactos de un tirón).
3. Implementa con `/opsx:apply` desde una rama `feature/<change-name>`.
4. Verifica con `/opsx:verify` (verificación manual en navegador, 3 breakpoints) y archiva con `/opsx:archive`.
