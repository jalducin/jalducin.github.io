# Capability: hosting-aws-tier0

## Requirements

### Requirement: Hosting estático en AWS dentro de free tier ($0)

El portafolio SHALL servirse desde AWS por HTTPS usando S3 + CloudFront, manteniéndose dentro del free
tier (costo objetivo ~$0). El bucket S3 MUST ser privado (sin acceso público); CloudFront accede vía OAC.

#### Scenario: Sitio servido por HTTPS desde CloudFront
- **WHEN** un visitante abre el dominio de CloudFront (`*.cloudfront.net`)
- **THEN** el sitio carga por HTTPS y `index.html` es el documento raíz
- **AND** `assets/`, `cv/CV_JuanValentinAlducin.pdf`, `llms.txt`, `robots.txt` y `sitemap.xml` responden 200

#### Scenario: Bucket privado (no público)
- **WHEN** se intenta acceder al bucket S3 directamente por su URL
- **THEN** el acceso está bloqueado (Block Public Access activo); solo CloudFront (OAC) puede leer

#### Scenario: Permanece en tier 0
- **WHEN** se revisa la arquitectura y el consumo
- **THEN** no se usan servicios de pago recurrente (sin Route53 salvo decisión explícita); el uso cabe en
  S3/CloudFront free tier
- **AND** existen budgets de alerta que notifican al correo del CV (valentin.alducin88@gmail.com)

### Requirement: Deploy reproducible

El despliegue SHALL ser reproducible mediante un script versionado que sincroniza solo los archivos del
sitio e invalida la caché de CloudFront.

#### Scenario: Publicar una actualización
- **WHEN** se ejecuta el script de deploy
- **THEN** `aws s3 sync` sube solo los archivos del sitio (excluye `openspec/`, `ai-specs/`, `docs/`,
  `.claude/`, `.gemini/`, `*.md` de agentes, `.git`)
- **AND** se crea una invalidación de CloudFront acotada para reflejar los cambios
