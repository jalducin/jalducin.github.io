## Context

Sitio estático (~2-3 MB: index.html, assets/, cv/, llms.txt, robots.txt, sitemap.xml) hoy en GitHub Pages.
Cuenta AWS limpia, región default us-east-2, budgets de alerta ya creados. Objetivo: hosting propio en
AWS **tier 0** con HTTPS y deploy reproducible.

## Goals / Non-Goals

**Goals:** HTTPS, costo $0, bucket privado (no público), deploy reproducible (CLI), base para Lambda IA.
**Non-Goals:** dominio propio/Route53 en esta fase (cuesta $0.50/mes); CI/CD avanzado; cambiar el stack del
sitio; backend del asistente IA (es otro cambio).

## Decisions

- **S3 privado + CloudFront con OAC** (Origin Access Control), no website-hosting público de S3.
  *Por qué:* HTTPS gratis, bucket cerrado (mejor práctica), edge global. *Alternativa descartada:* S3
  static website (solo HTTP, bucket público) — inseguro y sin TLS.
- **Dominio por defecto `*.cloudfront.net`** (TLS incluido, sin ACM ni Route53) para **mantener $0**.
  *Alternativa:* dominio propio + ACM (gratis) + Route53 ($0.50/mes) → posterior, fuera de tier 0.
- **Región del bucket: us-east-2** (default del usuario). CloudFront es global; la región del origin no
  afecta el costo. ACM (si hay dominio) DEBE ir en **us-east-1**.
- **Deploy: `aws s3 sync`** con includes/excludes (solo archivos del sitio) + `cloudfront create-invalidation`.
  Encapsulado en `scripts/deploy-aws.ps1`. *Futuro:* GitHub Actions con OIDC (sin llaves estáticas).
- **`default-root-object = index.html`**; respuestas de error: 403/404 → `index.html` (200) opcional, no
  crítico para un multipágina estático.
- **GitHub Pages**: se mantiene en paralelo hasta validar CloudFront; luego se decide apagarlo o conservarlo.

## Tier 0 — análisis de costo (objetivo $0)

| Servicio | Free tier | Uso del portafolio | Costo |
|---|---|---|---|
| S3 almacenamiento | 5 GB / 12 meses | ~2-3 MB | ~$0 (tras 12m: <$0.01/mes) |
| S3 requests | 20k GET / 2k PUT (12m) | mínimo | ~$0 |
| CloudFront egress | **1 TB/mes (always free)** | tráfico de portafolio | $0 |
| CloudFront requests | **10M/mes (always free)** | mínimo | $0 |
| ACM (TLS) | gratis | solo si dominio propio | $0 |
| Route53 | **NO free** ($0.50/mes/zona) | **se omite en tier 0** | $0 (omitido) |
| Lambda (futuro IA) | 1M req + 400k GB-s (always free) | bajo | $0 (tokens de Claude = costo aparte, no-AWS) |

Conclusión: con dominio por defecto de CloudFront, el sitio es **$0** dentro de free tier.

## Risks / Trade-offs

- **Route53 rompe tier 0** → no usar dominio propio por ahora (o aceptar $0.50/mes si se decide).
- **Free tier de S3 expira a los 12 meses** → tras eso el costo es de centavos (<$0.01/mes para 2-3 MB);
  CloudFront egress sigue always-free 1 TB → impacto despreciable.
- **Permisos del IAM user** podrían no permitir crear S3/CloudFront → se valida en Step 1; si faltan, se
  ajusta la policy del usuario antes de continuar.
- **Llaves estáticas en `~/.aws`** → para CI futuro, migrar a OIDC (sin secretos en el repo).
- **Invalidaciones de CloudFront**: 1000/mes gratis; usar paths acotados, no `/*` masivo en cada deploy.

## Migration Plan

1. Validar permisos + budgets (ya existen).
2. Crear bucket privado → `aws s3 sync` del sitio.
3. Crear CloudFront + OAC + bucket policy → probar por dominio `*.cloudfront.net` (HTTPS).
4. Verificar (curl 200, CV, og-image, llms.txt).
5. Documentar + script de deploy. Decidir sobre GitHub Pages.
Rollback: GitHub Pages sigue activo; si algo falla, no se apaga Pages hasta validar CloudFront.

## Open Questions

- ¿Dominio propio (acepta $0.50/mes de Route53) o nos quedamos en `*.cloudfront.net` ($0)? (Default: $0.)
- ¿Apagar GitHub Pages tras migrar o mantener ambos? (Default: mantener hasta validar.)
- ¿CI/CD con GitHub Actions (OIDC) ahora o deploy manual por script? (Default: script manual primero.)
