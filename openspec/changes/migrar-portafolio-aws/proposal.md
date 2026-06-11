## Why

Juan quiere práctica hands-on de AWS y hospedar su propio portafolio en su infra (coherente con el
posicionamiento AWS/AI-native), migrándolo desde GitHub Pages. Requisito duro: **costo cero (tier 0)**.

Estado de la cuenta (verificado por CLI el 2026-06-11): cuenta `957266312835`, usuario IAM `jalducin88`,
región por defecto `us-east-2`. **Sin** S3, CloudFront, Route53, ACM ni Lambda (lienzo limpio). Ya existen
2 budgets de alerta (`alerta-free-tier`, `personal-tier0-alert`) → guardrail de costo presente.

## What Changes

- Servir el sitio estático desde **S3 privado + CloudFront** (HTTPS) en lugar de (o además de) GitHub Pages.
- Usar el **dominio por defecto de CloudFront** (`*.cloudfront.net`) para mantener **$0** (sin Route53).
  Dominio propio = opcional y posterior (Route53 cuesta $0.50/mes, deja de ser tier 0).
- Deploy reproducible con `aws s3 sync` + invalidación de CloudFront; solo se publican los archivos del
  sitio (no `openspec/`, `ai-specs/`, `docs/`, `.claude/`, `.gemini/`, `*.md` de agentes).
- Mantener el build del CV (`cv/build.ps1`) sin cambios; el PDF se publica como artefacto estático.
- Dejar preparado el terreno para el futuro asistente IA (AWS Lambda, free tier).

## Capabilities

### New Capabilities
- `hosting-aws-tier0`: el sitio se sirve por HTTPS desde S3+CloudFront manteniéndose en free tier ($0),
  con bucket privado (sin acceso público) y deploy reproducible.

### Modified Capabilities
(ninguna)

## Impact

- **AWS**: 1 bucket S3 privado (us-east-2), 1 distribución CloudFront con OAC, política de bucket para OAC.
  ACM solo si se añade dominio propio (us-east-1, gratis).
- **Repo**: script de deploy (`scripts/deploy-aws.ps1`), docs (`README`, `CLAUDE.md`, `docs/`), `.gitignore`.
- **Costo**: dentro de free tier → ~$0 (ver design.md). Budgets ya configurados.
- **Permisos**: el usuario IAM `jalducin88` debe poder crear S3/CloudFront; se valida al ejecutar.
- **Restricciones**: no exponer el bucket públicamente; mantener el sitio estático (sin cambios de stack).
