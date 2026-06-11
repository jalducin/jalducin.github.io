> Migración tier 0: S3 privado + CloudFront (OAC), dominio por defecto `*.cloudfront.net`. Región us-east-2.
> Cuenta 957266312835 · IAM jalducin88. Ver design.md para el análisis de costo.

## 0. Preparación (OBLIGATORIO — PRIMERO)

- [x] 0.1 Leer `openspec/config.yaml`, `docs/base-standards.md`, `docs/frontend-standards.md` y este design.md
- [x] 0.2 Crear feature branch `feature/migrar-portafolio-aws`

## 1. Guardrails y permisos

- [x] 1.1 Budgets de alerta existen y notifican al correo del CV (alerta-free-tier $0.01; personal-tier0-alert 80%/100%)
- [x] 1.2 Validar que el IAM user puede crear S3 + CloudFront (intentar crear bucket; si falta policy, ajustarla)

## 2. S3 (origin privado)

- [x] 2.1 Crear bucket privado (p. ej. `jalducin-portfolio-site`) en us-east-2 con Block Public Access ON
- [x] 2.2 `aws s3 sync` del sitio con excludes (`openspec/`, `ai-specs/`, `docs/`, `.claude/`, `.gemini/`, `*.md` agentes, `.git`, `cv/og.html`, `cv/cv.html`→ ¿incluir? publicar solo el PDF) y content-types correctos

## 3. CloudFront + OAC

- [x] 3.1 Crear Origin Access Control (OAC) y la distribución CloudFront con el bucket como origin
- [x] 3.2 `default-root-object = index.html`; viewer-protocol-policy = redirect-to-https
- [x] 3.3 Añadir la bucket policy que permite lectura solo a la distribución (vía OAC)
- [x] 3.4 (opcional) Custom error responses 403/404

## 4. Verificación (OBLIGATORIO — EL AGENTE EJECUTA)

- [x] 4.1 `curl -I https://<dist>.cloudfront.net/` → 200 + HTTPS; `index.html` carga
- [x] 4.2 Verificar 200 en `/assets/img/og-image.png`, `/assets/img/QR.png`, `/cv/CV_JuanValentinAlducin.pdf`, `/llms.txt`, `/robots.txt`, `/sitemap.xml`
- [x] 4.3 Confirmar que la URL directa del bucket S3 NO es accesible (privado)
- [x] 4.4 Reporte en `openspec/changes/migrar-portafolio-aws/reports/AAAA-MM-DD-verificacion.md`

## 5. Deploy reproducible + documentación (OBLIGATORIO)

- [x] 5.1 Crear `scripts/deploy-aws.ps1` (sync con excludes + `cloudfront create-invalidation`)
- [x] 5.2 Actualizar `README.md` / `CLAUDE.md` / `docs/frontend-standards.md` con el flujo de deploy AWS
- [x] 5.3 `.gitignore`: ignorar credenciales/temp; nunca commitear llaves AWS

## 6. Dominio (OPCIONAL — fuera de tier 0)

- [x] 6.1 Decisión: NO dominio propio por ahora — nos quedamos en *.cloudfront.net ($0). (Reabrir si se quiere URL bonita.)
- [x] 6.2 Route53 omitido (mantener tier-0).

## 7. Cierre

- [x] 7.1 Decisión: mantener GitHub Pages en paralelo (rollback).
- [ ] 7.2 (futuro) Encarar `asistente-ia-portafolio` con Lambda (free tier) como cambio aparte
- [x] 7.3 Cambio archivado (hosting + CI/CD implementados y verificados).
