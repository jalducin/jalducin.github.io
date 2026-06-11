> Migración tier 0: S3 privado + CloudFront (OAC), dominio por defecto `*.cloudfront.net`. Región us-east-2.
> Cuenta 957266312835 · IAM jalducin88. Ver design.md para el análisis de costo.

## 0. Preparación (OBLIGATORIO — PRIMERO)

- [ ] 0.1 Leer `openspec/config.yaml`, `docs/base-standards.md`, `docs/frontend-standards.md` y este design.md
- [ ] 0.2 Crear feature branch `feature/migrar-portafolio-aws`

## 1. Guardrails y permisos

- [x] 1.1 Budgets de alerta existen y notifican al correo del CV (alerta-free-tier $0.01; personal-tier0-alert 80%/100%)
- [ ] 1.2 Validar que el IAM user puede crear S3 + CloudFront (intentar crear bucket; si falta policy, ajustarla)

## 2. S3 (origin privado)

- [ ] 2.1 Crear bucket privado (p. ej. `jalducin-portfolio-site`) en us-east-2 con Block Public Access ON
- [ ] 2.2 `aws s3 sync` del sitio con excludes (`openspec/`, `ai-specs/`, `docs/`, `.claude/`, `.gemini/`, `*.md` agentes, `.git`, `cv/og.html`, `cv/cv.html`→ ¿incluir? publicar solo el PDF) y content-types correctos

## 3. CloudFront + OAC

- [ ] 3.1 Crear Origin Access Control (OAC) y la distribución CloudFront con el bucket como origin
- [ ] 3.2 `default-root-object = index.html`; viewer-protocol-policy = redirect-to-https
- [ ] 3.3 Añadir la bucket policy que permite lectura solo a la distribución (vía OAC)
- [ ] 3.4 (opcional) Custom error responses 403/404

## 4. Verificación (OBLIGATORIO — EL AGENTE EJECUTA)

- [ ] 4.1 `curl -I https://<dist>.cloudfront.net/` → 200 + HTTPS; `index.html` carga
- [ ] 4.2 Verificar 200 en `/assets/img/og-image.png`, `/assets/img/QR.png`, `/cv/CV_JuanValentinAlducin.pdf`, `/llms.txt`, `/robots.txt`, `/sitemap.xml`
- [ ] 4.3 Confirmar que la URL directa del bucket S3 NO es accesible (privado)
- [ ] 4.4 Reporte en `openspec/changes/migrar-portafolio-aws/reports/AAAA-MM-DD-verificacion.md`

## 5. Deploy reproducible + documentación (OBLIGATORIO)

- [ ] 5.1 Crear `scripts/deploy-aws.ps1` (sync con excludes + `cloudfront create-invalidation`)
- [ ] 5.2 Actualizar `README.md` / `CLAUDE.md` / `docs/frontend-standards.md` con el flujo de deploy AWS
- [ ] 5.3 `.gitignore`: ignorar credenciales/temp; nunca commitear llaves AWS

## 6. Dominio (OPCIONAL — fuera de tier 0)

- [ ] 6.1 Si se decide dominio propio: ACM cert en us-east-1 (gratis) + alias en CloudFront
- [ ] 6.2 Route53 hosted zone ($0.50/mes) + registro ALIAS → CloudFront (acepta el costo o usar DNS externo)

## 7. Cierre

- [ ] 7.1 Decidir sobre GitHub Pages (mantener en paralelo vs apagar) tras validar CloudFront
- [ ] 7.2 (futuro) Encarar `asistente-ia-portafolio` con Lambda (free tier) como cambio aparte
- [ ] 7.3 Archivar el cambio cuando el sitio quede servido y verificado desde AWS
