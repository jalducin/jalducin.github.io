# Capability: hosting-aws-tier0 (delta)

## REMOVED Requirements

### Requirement: Hosting estático en AWS dentro de free tier ($0)
**Reason**: Los recursos de hosting en AWS (bucket `jalducin-portfolio-957266312835`, distribución CloudFront
`EG4961CAMR9Z8` y rol OIDC `gh-actions-portfolio-deploy`) fueron eliminados el 2026-10-01 en una limpieza de la
cuenta `957266312835`. Verificado el mismo día: `GetDistribution` → `NoSuchDistribution`, `ListObjectsV2` →
`NoSuchBucket`, `GetRole` → `NoSuchEntity`, y el dominio de CloudFront ya no resuelve. El dueño decidió no
reconstruirlos: el motivo de la migración es justamente el costo y la operación de AWS.
**Migration**: El sitio se publica solo en **GitHub Pages** desde `main` (`https://jalducin.github.io`), que ya
era la URL canónica (`canonical`, `og:url`, JSON-LD, `sitemap.xml`, CV y LinkedIn). No hace falta workflow de
despliegue propio. Ver `README.md` §Despliegue.

### Requirement: Deploy reproducible
**Reason**: El despliegue reproducible describía `.github/workflows/deploy.yml` (OIDC + `aws s3 sync` +
invalidación de CloudFront) y `scripts/deploy-aws.ps1`; ambos quedaron sin destino al borrarse los recursos y
el workflow fallaba en cada push (`Not authorized to perform sts:AssumeRoleWithWebIdentity`).
**Migration**: Se eliminan el workflow y el script. La publicación la hace GitHub Pages al hacer push a `main`;
la reproducibilidad del contenido sigue garantizada por el repositorio (el sitio es estático y versionado).
