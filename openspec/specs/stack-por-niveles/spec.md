# Capability: stack-por-niveles

## Requirements

### Requirement: Skills organizadas por nivel de dominio

La sección de skills del portafolio (`#hard-skills`) SHALL presentar las tecnologías agrupadas por **nivel de
dominio** con la rúbrica del candidato, en este orden y con esta semántica:

| Nivel | Etiqueta (EN, sitio) | Significado |
|---|---|---|
| 1 | **Own** | Lo construyó de punta a punta y es el dueño operativo |
| 2 | **Build** | Arma soluciones con ello de forma recurrente |
| 3 | **Operate** | Lo usa con soltura para diagnosticar y operar; no construye la plataforma |
| 4 | **Learning** | Estudio dirigido; sin profundidad operativa todavía |

Cada nivel MUST tener una leyenda visible (nombre + definición corta) y una marca visual reutilizable
(clase CSS por nivel) que use únicamente tokens de la paleta vigente (`--primary`, `--accent2`, `--muted`,
`--border`), sin colores nuevos.

#### Scenario: Inventario por nivel con evidencia
- **WHEN** un visitante lee la sección de skills
- **THEN** **Own** incluye al menos: PostgreSQL & SQL avanzado, ETL idempotente en producción, sistema de
  post-mortems y uptime (SRE), runbooks, Notion como sistema de conocimiento
- **AND** **Build** incluye al menos: Python (FastAPI, Django, Flask, pytest), n8n (workflow SDK), APIs
  Freshdesk/Notion/Asana/Slack, pipelines spec-driven, Grafana dashboards/alertas, Chart.js, Claude Code /
  Claude API, Gemini, Amazon Bedrock, SDD/OpenSpec, GitHub Actions, Docker, Supabase (PL/pgSQL, RLS, Edge
  Functions), React/TypeScript, Liquibase, SonarQube
- **AND** **Operate** incluye al menos: AWS (Lambda, Step Functions, CloudWatch Logs Insights, RDS, S3,
  EventBridge, SSO/Identity Center), Sentry, MySQL, SAP ERP/HANA, GK POS
- **AND** **Learning** incluye al menos: IaC (Terraform / AWS CDK), QuickSight, synthetic checks /
  observabilidad proactiva
- **AND** NO aparecen Amazon Kendra ni AWS Kiro en ninguna categoría
- **AND** Kubernetes no aparece en la sección de skills (permanece únicamente en la card de VoltGrid)

#### Scenario: Leyenda y accesibilidad
- **WHEN** se renderiza la sección
- **THEN** existe una leyenda con los 4 niveles y su definición antes del inventario
- **AND** cada grupo es un bloque con encabezado de nivel (`h3`) y lista (`ul`), navegable por teclado, sin
  depender solo del color para distinguir niveles (el nombre del nivel siempre es texto)

#### Scenario: Responsive y sistema de diseño
- **WHEN** se ve la sección en 992px, 768px y 480px
- **THEN** los grupos se apilan sin desbordes horizontales y las listas conservan legibilidad
- **AND** el CSS es embebido en `<style>` de `index.html`, reutiliza `.soft-list`/badges existentes donde aplique
  y no introduce dependencias externas

### Requirement: Coherencia del inventario con CV y llms.txt

El inventario por niveles SHALL ser la fuente de verdad de skills del sitio; `llms.txt` y la sección
Habilidades del CV MUST derivar de él (subconjunto compacto), sin listar tecnologías ausentes del inventario.

#### Scenario: Sin tecnologías huérfanas
- **WHEN** se comparan las tecnologías de `llms.txt` y de la sección Habilidades del CV contra el inventario
- **THEN** toda tecnología del CV/llms.txt existe en algún nivel del inventario del sitio
- **AND** el CV puede omitir niveles (por espacio) pero no contradecirlos
