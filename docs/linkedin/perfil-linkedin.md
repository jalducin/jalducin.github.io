# Perfil de LinkedIn: textos listos para pegar

> Derivado de `llms.txt` y `cv/cv.html` (cambio `cv-claridad`, 2026-11-02). Si cambia el CV, se actualiza
> esto también. Regla de privacidad del empleador: lenguaje genérico, sin nombres de sistemas internos ni cifras
> de clientes. Usa el texto tal cual o ajústalo, pero **no le agregues métricas que no puedas demostrar**.

## 0. Qué cambiar respecto a hoy (checklist)

- [ ] Título del puesto: **"IA Specialist" → "AI Specialist"** (así aparece en el CV y el portafolio).
- [ ] Fechas de *Backend Support Specialist*: hoy dice **sept 2025 – jul 2026** y el puesto actual empieza en
      jul 2026. Cámbialo a **jun 2026** (como en el CV).
- [ ] Quita **"80 % de resolución autónoma"**: esa métrica se retiró del CV y del sitio el 2026-09-20.
- [ ] Recorta cada puesto a 3–4 bullets (textos en §3).
- [ ] Agrega **platform-STALD** en *Proyectos* y en *Destacado*. Pyzzeria ya no va (su demo está caída).
- [ ] Sustituye el titular y el *Acerca de* (§1 y §2).

## 1. Titular (máx. 220 caracteres)

```
Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI · Python · AWS · Claude Code · Spec-Driven Development
```

## 2. Acerca de

**Español:**

```
Senior Backend Engineer y Tech Lead con +10 años en Python, SQL y AWS.

Hoy coordino Service Support en una fintech: trabajo en la confiabilidad y automatización de la operación con post-mortems, control de uptime, runbooks y flujos de n8n.

Construyo software con Spec-Driven Development (OpenSpec) y agentes de IA. En la práctica: la spec es el contrato, y los agentes (Claude Code con subagentes, skills y hooks) implementan, prueban y revisan con controles que yo defino. Como pasatiempo hice platform-STALD, una plataforma educativa con la que practico este flujo.

Stack: Python (FastAPI, Django), PostgreSQL, AWS serverless, Supabase, n8n, Grafana, Claude Code / Claude API.

Portafolio: jalducin.github.io · GitHub: github.com/jalducin
```

**English (perfil secundario):**

```
Senior Backend Engineer and Tech Lead with 10+ years in Python, SQL and AWS.

I coordinate Service Support at a fintech, working on operational reliability and automation: post-mortems, uptime tracking, runbooks and n8n workflows.

I build software with Spec-Driven Development (OpenSpec) and AI agents: the spec is the contract, and agents (Claude Code with subagents, skills and hooks) implement, test and review under guardrails I define. As a hobby I built platform-STALD, an educational platform where I practice this workflow.

Stack: Python (FastAPI, Django), PostgreSQL, AWS serverless, Supabase, n8n, Grafana, Claude Code / Claude API.

Portfolio: jalducin.github.io · GitHub: github.com/jalducin
```

## 3. Experiencia

### Service Support Tech Lead & AI Specialist · Podemos Progresar · jul 2026 – actualidad

```
• Coordino el equipo de Service Support (bugs, incidentes críticos y deuda técnica) y apliqué Spec-Driven Development con Claude API al flujo diagnóstico → implementación para agilizar las revisiones.
• Participo en la construcción del proceso de post-mortems (P0–P3, 5 Whys, blameless) con un tablero de seguimiento de atrasos, escalaciones y avance contra la meta.
• Calculo y llevo el control mensual de uptime/downtime (downtime = impacto real al usuario) con la metodología definida por el liderazgo, y estandarizo runbooks y accesos de mínimo privilegio.
• Automatizo parte de la operación con n8n (Freshdesk → Notion → Slack, vigilancia de atrasos y alertas por picos de tickets) y desarrollo un Skill de IA para clasificar y rutear tickets con revisión humana.
• Participo en los trenes de liberación semanales coordinados por Ingeniería, validando despliegues desde Service Support; diagnostico y opero AWS (CloudWatch Logs Insights, RDS) y Sentry. Meta de SLA: primera respuesta <10 min, crítica <2 h.
```
Aptitudes (5): Spec-Driven Development · Anthropic Claude · n8n · Amazon Web Services (AWS) · Site Reliability Engineering

### Backend Support Specialist · Podemos Progresar · sept 2025 – jun 2026

```
• Gestioné incidentes N2 con RCAs y post-mortems asistidos por IA para prevenir fallos recurrentes.
• Transferí conocimiento al primer nivel para que resolviera más casos sin escalar a ingeniería.
• Dueño del ETL semanal idempotente en PostgreSQL (respaldo → limpieza → actualización → bitácora) y de la deduplicación de identidades en producción.
```
Aptitudes (4): Python · PostgreSQL · Django · FastAPI

### Software Engineer → Tech Lead · Redsis · ene 2022 – sept 2025

```
• Desarrollé APIs REST (Python, Java, PHP) que integran GK POS con ERPs/CRMs vía XML/SFTP en 3 países de LATAM.
• Lideré el Go-Live cloud de GK POS (Perú, Colombia, Bolivia): cronogramas, stakeholders de negocio/TI y capacitación local.
• Dirigí al equipo funcional-técnico: estrategia de pruebas y calidad por release.
```

### Software Engineer · Softtek · mar 2017 – ene 2022

```
• Facturación, portales de cliente y ETLs con SAP ERP/HANA, y dashboards ejecutivos en SAP BO.
• Soporte AMS a retail (GK) bajo Scrum, con SLA al 98 %.
```

## 4. Proyectos (sección *Proyectos* del perfil)

**platform-STALD: proyecto personal**, asociado a "Proyecto personal" · 2026 – actualidad

```
Plataforma educativa que hice como pasatiempo y uso para practicar tecnologías e IA: Spec-Driven Development con Claude Code (subagentes, skills y hooks), juegos multijugador en tiempo real y pruebas en CI.
Stack: Deno · TypeScript · Supabase (Postgres RLS, Auth, Realtime) · GitHub Actions.
github.com/jalducin/platform-STALD
```

**Fidello: Loyalty Card System** · 2026

```
Fidelidad digital multi-negocio (QR mobile-first) con toda la lógica en PostgreSQL: RLS multi-tenant, RPC en PL/pgSQL, QR anti-replay y feature flags. 793 pruebas · 91 migraciones · 100 % SDD.
Stack: React · TypeScript · Supabase. Caso técnico: jalducin.github.io/blog/deep-dive-fidello.html
```

**Monitoreo-Cloud: observabilidad multi-fuente**

```
Observabilidad self-hosted (Grafana + Docker) sobre 3 fuentes: CloudWatch, contenedores Docker y tickets/SLA, con recolección en n8n.
github.com/jalducin/monitoreo-cloud
```

## 5. Destacado (máx. 3, en este orden)

1. Repo **platform-STALD**: github.com/jalducin/platform-STALD
2. **Portafolio**: jalducin.github.io
3. **CV en PDF** (ES o EN): jalducin.github.io/cv/CV_JuanValentinAlducin.pdf

## 6. Aptitudes principales (fija estas 5 arriba)

Python · PostgreSQL · Amazon Web Services (AWS) · Spec-Driven Development (SDD) · Anthropic Claude

Las demás pueden quedarse, pero quita las que no tengan evidencia en el CV (p. ej. RAG, MongoDB, AWS Glue).

## 7. Licencias y certificaciones

**Orden sugerido** (de más relevante a menos):

1. Claude Code in Action (Anthropic, oct 2026)
2. Introduction to Model Context Protocol (Anthropic, nov 2026)
3. Introduction to agent skills (Anthropic, nov 2026)
4. Introduction to subagents (Anthropic, oct 2026)
5. Claude Code: Software Engineering with Generative AI Agents (Vanderbilt University, mar 2026)
6. Generative AI Applications with Amazon Bedrock (AWS, abr 2026)
7. Claude Code 101 (Anthropic, oct 2026): puede quedarse en LinkedIn, pero en el CV no se lista porque lo cubre *in Action*.
8. Bootcamp de GitHub Actions (Código Facilito)

**Cursos que conviene tomar después** (confirma que sigan en Anthropic Academy):

- **Building with the Claude API**: respalda lo de "Claude API" en el CV con algo verificable. Es el más útil.
- **MCP: Advanced Topics**: complementa *Intro to MCP* y encaja con el tooling de agentes.
- **Claude with Amazon Bedrock** (opcional): une tu perfil AWS con Claude.

Los de *AI Fluency* los dejaría fuera: son menos técnicos y no suman a tu perfil.
