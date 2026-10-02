# Reporte Fase 1 — Asistente local (pruebas y verificación)

- Fecha: 2026-10-01 · Cambio: migrar-backend-portafolio · Agente: frontend-developer (Claude Code)
- Rama: `feature/migrar-backend-portafolio` (desde `main` @ `19bc4c2`)

## Comandos ejecutados
- `curl` a `https://vd4c00py15…` y `https://tekik4wm8e…` → **exit 6 (no resuelven)**: confirma el borrado del backend
- `mcp Supabase list_projects` → `Fidello` y `Fidello QAS` ACTIVE_HEALTHY, `IMMEX` INACTIVE (org `gbjvahsnbkecstsiyffb`)
- `python scripts/assistant/build_kb.py` (×2, idempotente) → 21 entradas, 262 tags, 17 653 bytes
- `python openspec/changes/migrar-backend-portafolio/scripts/patch_widget.py` → widget local
- `python scripts/assistant/probe_kb.py` → **18 checks · 18 PASS**
- `python scripts/i18n/audit_i18n.py` → **64 checks · 64 PASS** (7 nuevos del asistente; se retiró el de `profile.txt`)
- `python scripts/i18n/probe_i18n.py` → **18/18 PASS**
- Capturas headless EN/ES en 1280 y 480 con el panel abierto y dos preguntas reales

## Resultados
| Check | Resultado |
|---|---|
| 12 preguntas conocidas (6 EN + 6 ES) | devuelven la entrada esperada en el idioma activo |
| 3 preguntas fuera de alcance | sin match → mensaje honesto + sugerencias + contacto |
| `fetch` del asistente | **0 peticiones** (resolución local) |
| URL del backend borrado en el DOM | ausente (`ASSISTANT_URL` eliminado) |
| KB inválida (`[]`) | el widget muestra el CTA de contacto, sin excepción |
| Responsive EN/ES 1280/768/480 | sin overflow, panel dentro del viewport, foco al input |

## Verificación de estado
- Antes: `index.html` 111 235 bytes, widget con `fetch` a API Gateway (siempre error), `backend/assistant/` y
  `deploy-assistant.yml` presentes.
- Después: `index.html` ~131 KB (incluye la base de conocimiento), widget local, `backend/assistant/` y
  `.github/workflows/deploy-assistant.yml` eliminados del repo.
- Estado restaurado: temporales `_probe_kb.html` y `_shot_kb.html` borrados.

## Incidencias resueltas durante la implementación
1. `build_kb.py`: el lookahead `(?!.*—)` con `re.S` consumía todo el archivo → 0 entradas. Simplificado el patrón.
2. Widget: faltaba `]` al cerrar el `Set` de stopwords → `window.__askPortfolio` no se definía. Corregido.
3. `probe_kb.py`: el check de "sin URL del backend" se detectaba a sí mismo (el literal viajaba en el script
   inyectado) → se construye la aguja en runtime. El caso de KB rota ahora muta el archivo, no el DOM.

## Resultado
- Fase 1: **PASS**. Bloqueos: ninguno.
- Pendiente externo para la Fase 2: organización + proyecto de Supabase (`project ref`) y API key de Resend.

## Addendum — alcance real de la limpieza de AWS (descubierto al desplegar)

Al hacer push de la Fase 1, el workflow `Deploy to AWS (S3 + CloudFront)` falló con
`Not authorized to perform sts:AssumeRoleWithWebIdentity`. Verificación con la CLI (solo lectura):

| Recurso | Comando | Resultado |
|---|---|---|
| Rol OIDC `gh-actions-portfolio-deploy` | `aws iam get-role` | `NoSuchEntity` |
| Bucket `jalducin-portfolio-957266312835` | `aws s3 ls` | `NoSuchBucket` |
| Distribución `EG4961CAMR9Z8` | `aws cloudfront get-distribution` | `NoSuchDistribution` |
| `https://d3r3bnavnwzqaw.cloudfront.net` | `curl` | no resuelve (000) |
| `https://jalducin.github.io` | `curl` | **200 y ya sirve la Fase 1** (KB + `__askPortfolio`) |

Es decir, la limpieza no solo borró el backend: también el **hosting** del sitio en AWS. La nota de traspaso
solo documentaba el backend. Acciones tomadas en consecuencia (mismo cambio):

- Eliminados `.github/workflows/deploy.yml`, `deploy-contact-api.yml`, `scripts/deploy-aws.ps1` y `contact-api/`.
- **QR del CV regenerado**: apuntaba a la distribución borrada; ahora codifica `https://jalducin.github.io`,
  con corrección de errores **H** y el logo "JVAV" central preservado (verificado con `cv2.QRCodeDetector`).
  PDFs ES/EN regenerados (1 página cada uno).
- `README.md` §Despliegue reescrito (GitHub Pages como único hosting), `assistant/knowledge.md` y `cv/README.md`
  actualizados.
- Specs: `hosting-aws-tier0` retirada (REMOVED, 2 requirements) y `qr-apunta-al-sitio-aws` modificada.
