# Reporte — Migración a AWS (tier 0) + CI/CD

- Fecha: 2026-06-11
- Cambio: migrar-portafolio-aws
- Agente: Claude (Opus 4.8)

## Recursos creados (cuenta 957266312835, us-east-2)
- **S3 bucket**: `jalducin-portfolio-957266312835` (privado, Block Public Access ON)
- **CloudFront OAC**: `EMNWM8LIJNM9D` (jalducin-portfolio-oac)
- **CloudFront distribución**: `EG4961CAMR9Z8` → `d3r3bnavnwzqaw.cloudfront.net` (PriceClass_100, redirect-to-https, default-root-object index.html, 403/404→/index.html 200)
- **Bucket policy**: lectura solo para CloudFront vía OAC (condición AWS:SourceArn = distribución)
- **OIDC provider**: `token.actions.githubusercontent.com`
- **IAM role CI/CD**: `gh-actions-portfolio-deploy` (trust: repo `jalducin/jalducin.github.io` ref main; policy mínima: s3 put/delete/list en el bucket + cloudfront:CreateInvalidation en la distribución)

## Comandos de verificación
- `aws cloudfront get-distribution` → Status **Deployed**
- `curl -I https://d3r3bnavnwzqaw.cloudfront.net/...`
- `curl` directo al endpoint S3

## Resultados
- `/` → 200 · `/cv/CV_JuanValentinAlducin.pdf` → 200 · `/assets/img/og-image.png` → 200 ·
  `/assets/img/QR.png` → 200 · `/llms.txt` → 200 · `/robots.txt` → 200 · `/sitemap.xml` → 200 (todo HTTPS)
- Acceso directo a S3 (`...s3.us-east-2.amazonaws.com/index.html`) → **403** (bucket privado, correcto)

## Costo / tier 0
- S3 (~0.5 MB) + CloudFront (free 1 TB egress + 10M req) + sin Route53 = dentro de free tier (~$0).
- Budgets de alerta (`alerta-free-tier` $0.01; `personal-tier0-alert` 80%/100%) notifican al correo del CV.

## CI/CD
- `.github/workflows/deploy.yml`: push a `main` → OIDC assume-role → `aws s3 sync` + invalidación CloudFront.
- Deploy manual alterno: `scripts/deploy-aws.ps1`.

## Resultado
- Estado: **PASS** — sitio en vivo en https://d3r3bnavnwzqaw.cloudfront.net
- Pendiente/decisión: dominio propio (Route53 = $0.50/mes, fuera de tier 0); apagar GitHub Pages; URLs
  absolutas (og:image/JSON-LD apuntan a jalducin.github.io — válidas mientras Pages siga activo).
