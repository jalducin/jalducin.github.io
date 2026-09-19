# -*- coding: utf-8 -*-
"""Aplica a cv/cv.html y cv/cv-en.html los cambios del cambio cv-portafolio-sre-automation (tasks 3.2 y 3.3)."""
import io, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TAG = "Senior Backend Engineer | Tech Lead · SRE &amp; Automation | Agentic AI"


def apply(path, reps):
    p = os.path.join(ROOT, path)
    s = io.open(p, encoding="utf-8").read()
    for o, n in reps:
        assert s.count(o) == 1, "%s: %d coincidencias -> %s" % (path, s.count(o), o[:70])
        s = s.replace(o, n)
    io.open(p, "w", encoding="utf-8", newline="").write(s)
    print(path, "OK")


def bullets(items):
    return "\n".join("            <li>%s</li>" % b for b in items)


# ============================== ES ==============================
es_current = bullets([
    "Lidero Service Support: bugs, incidentes críticos y deuda técnica end-to-end con SDD + Claude API (-40% en revisión).",
    "Sistema de post-mortems (P0–P3, blameless, tablero en vivo) y metodología de uptime mensual: 99.95% en jul 2026.",
    "Automatización con n8n (SDK): Freshdesk → Notion → Slack, alertas de atrasos y picos; pipelines spec-driven.",
    "Flujos de IA (Claude, OpenAI, Gemini, Bedrock) en el SDLC; Skill de routing de tickets con revisión humana.",
    "Trenes de liberación semanales: validación y despliegue entre core banking, originación y app de campo.",
    "AWS (Step Functions, Lambda, CloudWatch, RDS) y tooling serverless interno (Enkoth); SLA: respuesta &lt;10 min, crítica &lt;2 h.",
])
es_prev = bullets([
    "Lideré incidentes N2 con RCAs y post-mortems asistidos por IA; 80% de autoresolución N1 vía transferencia de conocimiento.",
    "ETL semanal idempotente en PostgreSQL (respaldo → limpieza → actualización → bitácora) y deduplicación de identidades.",
    "Enlace técnico central del área (Python, Django, FastAPI, PostgreSQL).",
])
apply("cv/cv.html", [
    ('<div class="tagline">Senior Backend Engineer | Tech Lead | Agentic AI Systems</div>', '<div class="tagline">%s</div>' % TAG),
    ('<p class="summary">Senior Backend Engineer y Tech Lead con +10 años en APIs, sistemas distribuidos y cloud-native (Python, FastAPI, AWS Serverless). Especializado en IA generativa: agentes, RAG y LLMs (Claude, Gemini, OpenAI) con AWS AI/ML (Bedrock, Kendra). Pipelines de datos y ETL. Tech Lead en fintech y retail; acelero la entrega con SDD: -40% en revisión y 80% de autoresolución N1.</p>',
     '<p class="summary">Senior Backend Engineer y Tech Lead con +10 años en backend y sistemas distribuidos (Python, SQL, AWS). Confiabilidad y automatización como producto: post-mortems, uptime 99.95%, runbooks y pipelines n8n/spec-driven. IA generativa (Claude, Gemini, OpenAI, Bedrock) como copiloto del SDLC con SDD: -40% en revisión y 80% de autoresolución N1.</p>'),
    ("""            <li>Lidero el equipo de Service Support: bugs, incidentes críticos y deuda técnica end-to-end con SDD + Claude API (-40% en revisión).</li>
            <li>Arquitecto flujos de IA (Claude, OpenAI, Gemini) en todo el SDLC: specs, análisis estático, debugging y documentación.</li>
            <li>Construí el tablero de post-mortems en vivo desde Asana (atrasos, escalaciones N3/N4, semáforo ITG) y reportes para dirección.</li>
            <li>Diseño tooling serverless interno (Enkoth — Lambda · Step Functions · EventBridge) y automatizaciones n8n (Asana, Freshdesk, Slack).</li>
            <li>Trenes de liberación semanales (SCI, Spore, Hipatia, Mambu Tools) y AWS: primera respuesta &lt;10 min, crítica &lt;2 h.</li>""", es_current),
    ('<div class="stack">Stack: Python · Django · FastAPI · PostgreSQL · AWS Serverless · AWS Glue · Claude API · Docker · n8n · Grafana</div>',
     '<div class="stack">Stack: Python · SQL · PostgreSQL · Django · FastAPI · AWS (Lambda, Step Functions, CloudWatch, RDS) · n8n · Grafana · Sentry · Claude API · Docker</div>'),
    ("""            <li>Lideré incidentes N2 con RCAs y postmortems técnicos asistidos por IA que previnieron fallos recurrentes.</li>
            <li>Habilité 80% de autoresolución en N1 vía transferencia de conocimiento; fui el enlace técnico central del área.</li>""", es_prev),
    ('<div class="skill"><div class="cat">Lenguajes</div><div class="val">Python, PHP, JavaScript, TypeScript, Java, SQL</div></div>',
     '<div class="skill"><div class="cat">Lenguajes</div><div class="val">Python, SQL, PHP, JavaScript, TypeScript, Java</div></div>'),
    ('<div class="skill"><div class="cat">Cloud · DevOps · Observabilidad</div><div class="val">AWS (Lambda, RDS, S3, Step Functions, EC2, CloudWatch), Serverless Framework, Kubernetes, CI/CD (GitHub Actions), Docker, n8n, Grafana, Supabase</div></div>',
     '<div class="skill"><div class="cat">Cloud &amp; Serverless</div><div class="val">AWS (Lambda, Step Functions, EventBridge, CloudWatch, RDS, S3, EC2), Serverless Framework, CI/CD (GitHub Actions), Docker, Supabase</div></div>\n'
     '        <div class="skill"><div class="cat">SRE &amp; Observabilidad</div><div class="val">Post-mortems (P0–P3, blameless), uptime/downtime, runbooks, SLAs, Grafana, Sentry, CloudWatch Logs Insights</div></div>\n'
     '        <div class="skill"><div class="cat">Automatización</div><div class="val">n8n (workflow SDK), APIs Freshdesk/Notion/Asana/Slack, webhooks serverless, pipelines spec-driven</div></div>'),
    ('<div class="skill"><div class="cat">Bases de datos</div><div class="val">PostgreSQL, MySQL, SQL Server, MongoDB, SAP HANA, DynamoDB</div></div>',
     '<div class="skill"><div class="cat">Bases de datos</div><div class="val">PostgreSQL, MySQL, SQL Server, MongoDB, SAP HANA, DynamoDB, Liquibase</div></div>'),
    ('<div class="skill"><div class="cat">IA &amp; Generative AI</div><div class="val">Claude/OpenAI/Gemini APIs, Prompt Engineering, LLM Integration, RAG, AI Agents, Agentic Workflows, Amazon Bedrock, Amazon Kendra, AWS Kiro, SDD/OpenSpec</div></div>',
     '<div class="skill"><div class="cat">IA &amp; Generative AI</div><div class="val">Claude API / Claude Code, OpenAI, Gemini, Amazon Bedrock, Prompt Engineering, LLM Integration, RAG, AI Agents/Skills, Agentic Workflows, SDD/OpenSpec</div></div>'),
    ('<div class="skill"><div class="cat">Gestión</div><div class="val">Scrum, Jira, Asana, Notion, Postman</div></div>',
     '<div class="skill"><div class="cat">Calidad &amp; Gestión</div><div class="val">pytest (mocks), Vitest, SonarQube, Merge Requests/CI, Scrum, Jira, Asana, Notion</div></div>'),
    ('<p class="pdesc">Fidelidad digital multi-negocio (roles, QR mobile-first): JWT, RLS multi-tenant, QR anti-replay, <b>passes de Google Wallet</b> (JWT RS256) y <b>feature flags</b> administrables. 100% SDD · en evolución.</p>',
     '<p class="pdesc"><b>Piloto en beta cloud</b> (cafeterías reales). Fidelidad digital multi-negocio (QR mobile-first): RLS multi-tenant, RPC PL/pgSQL, QR anti-replay, feature flags. 793 pruebas · 91 migraciones · 100% SDD.</p>'),
])

# ============================== EN ==============================
en_current = bullets([
    "Lead Service Support: bugs, critical incidents and technical debt end-to-end with SDD + Claude API (-40% review time).",
    "Post-mortem system (P0–P3, blameless, live dashboard) and monthly uptime methodology: 99.95% in July 2026.",
    "Automation with n8n (SDK): Freshdesk → Notion → Slack, delay and ticket-spike alerts; spec-driven pipelines.",
    "AI flows (Claude, OpenAI, Gemini, Bedrock) across the SDLC; ticket-routing AI Skill with human review.",
    "Weekly release trains: validation and deployment across core banking, origination and field-app platforms.",
    "AWS (Step Functions, Lambda, CloudWatch, RDS) and internal serverless tooling (Enkoth); SLA: response &lt;10 min, critical &lt;2 h.",
])
en_prev = bullets([
    "Led N2 incidents with RCAs and AI-assisted post-mortems; 80% autonomous N1 resolution via knowledge transfer.",
    "Weekly idempotent PostgreSQL ETL (backup → cleanup → update → audit log) and identity deduplication in production.",
    "Central technical liaison for the area (Python, Django, FastAPI, PostgreSQL).",
])
apply("cv/cv-en.html", [
    ('<div class="tagline">Senior Backend Engineer | Tech Lead | Agentic AI Systems</div>', '<div class="tagline">%s</div>' % TAG),
    ('<p class="summary">Senior Backend Engineer and Tech Lead with 10+ years in APIs, distributed systems and cloud-native solutions (Python, FastAPI, AWS Serverless). Specialized in generative AI: agents, RAG and LLMs (Claude, Gemini, OpenAI) with AWS AI/ML (Bedrock, Kendra). Data pipelines and ETL. Tech Lead in fintech and retail; accelerate delivery with SDD: -40% review cycles, 80% autonomous N1 resolution.</p>',
     '<p class="summary">Senior Backend Engineer and Tech Lead with 10+ years in backend and distributed systems (Python, SQL, AWS). Reliability and automation as a product: post-mortems, 99.95% uptime, runbooks and n8n/spec-driven pipelines. Generative AI (Claude, Gemini, OpenAI, Bedrock) as the SDLC copilot with SDD: -40% review time and 80% autonomous N1 resolution.</p>'),
    ("""            <li>Lead the Service Support team: bugs, critical incidents and technical debt end-to-end with SDD + Claude API (-40% code review time).</li>
            <li>Architect AI flows (Claude, OpenAI, Gemini) across the SDLC: specs, static analysis, debugging and documentation; adoption across engineering.</li>
            <li>Built the post-mortem governance dashboard reading live from Asana: delays, open subtasks, N3/N4 escalations and ITG traffic light vs. target.</li>
            <li>Design internal serverless tooling (Enkoth — Lambda · Step Functions · EventBridge) and n8n automations (Asana, Freshdesk, Notion, Slack).</li>
            <li>Weekly release trains (SCI, Spore, Hipatia, Mambu Tools) and AWS infra (Lambda, RDS, Step Functions): first response &lt;10 min, critical &lt;2 h.</li>""", en_current),
    ('<div class="stack">Stack: Python · Django · FastAPI · PostgreSQL · AWS Serverless · AWS Glue · Claude API · Docker · n8n · Grafana</div>',
     '<div class="stack">Stack: Python · SQL · PostgreSQL · Django · FastAPI · AWS (Lambda, Step Functions, CloudWatch, RDS) · n8n · Grafana · Sentry · Claude API · Docker</div>'),
    ("""            <li>Led N2 incident management with RCAs and AI-assisted post-mortems that prevented recurring failures.</li>
            <li>Enabled 80% autonomous N1 resolution via knowledge transfer; central technical liaison (Python, Django, FastAPI, PostgreSQL).</li>""", en_prev),
    ('<div class="skill"><div class="cat">Programming Languages</div><div class="val">Python, PHP, JavaScript, TypeScript, Java, SQL</div></div>',
     '<div class="skill"><div class="cat">Programming Languages</div><div class="val">Python, SQL, PHP, JavaScript, TypeScript, Java</div></div>'),
    ('<div class="skill"><div class="cat">Cloud · DevOps · Observability</div><div class="val">AWS (Lambda, RDS, S3, Step Functions, EC2, CloudWatch), Serverless Framework, Kubernetes, CI/CD (GitHub Actions), Docker, n8n, Grafana, Supabase</div></div>',
     '<div class="skill"><div class="cat">Cloud &amp; Serverless</div><div class="val">AWS (Lambda, Step Functions, EventBridge, CloudWatch, RDS, S3, EC2), Serverless Framework, CI/CD (GitHub Actions), Docker, Supabase</div></div>\n'
     '        <div class="skill"><div class="cat">SRE &amp; Observability</div><div class="val">Post-mortems (P0–P3, blameless), uptime/downtime, runbooks, SLAs, Grafana, Sentry, CloudWatch Logs Insights</div></div>\n'
     '        <div class="skill"><div class="cat">Automation</div><div class="val">n8n (workflow SDK), Freshdesk/Notion/Asana/Slack APIs, serverless webhooks, spec-driven pipelines</div></div>'),
    ('<div class="skill"><div class="cat">Databases</div><div class="val">PostgreSQL, MySQL, SQL Server, MongoDB, SAP HANA, DynamoDB</div></div>',
     '<div class="skill"><div class="cat">Databases</div><div class="val">PostgreSQL, MySQL, SQL Server, MongoDB, SAP HANA, DynamoDB, Liquibase</div></div>'),
    ('<div class="skill"><div class="cat">AI &amp; Generative AI</div><div class="val">Claude/OpenAI/Gemini APIs, Prompt Engineering, LLM Integration, RAG, AI Agents, Agentic Workflows, Amazon Bedrock, Amazon Kendra, AWS Kiro, SDD/OpenSpec</div></div>',
     '<div class="skill"><div class="cat">AI &amp; Generative AI</div><div class="val">Claude API / Claude Code, OpenAI, Gemini, Amazon Bedrock, Prompt Engineering, LLM Integration, RAG, AI Agents/Skills, Agentic Workflows, SDD/OpenSpec</div></div>'),
    ('<div class="skill"><div class="cat">Management</div><div class="val">Scrum, Jira, Asana, Notion, Postman</div></div>',
     '<div class="skill"><div class="cat">Quality &amp; Management</div><div class="val">pytest (mocks), Vitest, SonarQube, Merge Requests/CI, Scrum, Jira, Asana, Notion</div></div>'),
    ('<p class="pdesc">Multi-business digital loyalty (roles, mobile-first QR): JWT, multi-tenant RLS, anti-replay QR, <b>Google Wallet passes</b> (RS256 JWT) and admin-managed <b>feature flags</b>. 100% SDD · evolving.</p>',
     '<p class="pdesc"><b>Cloud beta pilot</b> (real coffee shops). Multi-business digital loyalty (mobile-first QR): multi-tenant RLS, PL/pgSQL RPC, anti-replay QR, feature flags. 793 tests · 91 migrations · 100% SDD.</p>'),
])
