# -*- coding: utf-8 -*-
"""Aplica a index.html los cambios del cambio cv-portafolio-sre-automation (tasks 1.x y 2.x)."""
import io, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
P = os.path.join(ROOT, "index.html")
s = io.open(P, encoding="utf-8").read()
n_before = len(s)

def rep(old, new, count=1):
    global s
    assert s.count(old) >= 1, "no encontrado: " + old[:80]
    if count == 1:
        assert s.count(old) == 1, "ambiguo (%d): %s" % (s.count(old), old[:80])
    s = s.replace(old, new)

OLD_H = "Senior Backend Engineer · Tech Lead · Agentic AI Systems"
NEW_H = "Senior Backend Engineer · Tech Lead · SRE & Automation · Agentic AI"

# ---------- 1.1 headline en head / whoami ----------
assert s.count(OLD_H) == 5, s.count(OLD_H)   # title, og:title, twitter:title, JSON-LD, whoami
s = s.replace(OLD_H, NEW_H)

# ---------- 1.2 / 1.3 descripciones y keywords ----------
rep('<meta name="description" content="Senior Software Engineer with 10+ years in backend. I integrate AI (Claude/SDD, Gemini, OpenAI) as the core of my engineering workflow. Spec-Driven Development: ~40% faster review cycles, 80% N1 incident self-resolution, sub-10-min first response. AWS Serverless · Python · CDMX, Mexico." />',
    '<meta name="description" content="Senior Backend Engineer and Tech Lead with 10+ years. Reliability and automation as a product: post-mortem system, 99.95% monthly uptime, n8n and spec-driven pipelines. AI (Claude, Gemini, OpenAI) as the SDLC copilot with Spec-Driven Development: ~40% less code review time, 80% N1 self-resolution, <10 min first response. Python · PostgreSQL · AWS · CDMX, Mexico." />')
rep('<meta name="keywords" content="AI-native engineer, agentic engineering, generative AI, Spec-Driven Development, SDD, Claude, Anthropic, Gemini, OpenAI, LLM integration, AI agents, RAG, Amazon Bedrock, Amazon Kendra, AWS Kiro, AWS AI/ML, ETL, AWS Glue, data pipelines, Python, FastAPI, Django, AWS Lambda, serverless, backend engineer, CDMX" />',
    '<meta name="keywords" content="backend engineer, tech lead, SRE, site reliability engineering, reliability, post-mortems, uptime, runbooks, automation, n8n, spec-driven pipelines, AI-native engineer, agentic engineering, generative AI, Spec-Driven Development, SDD, Claude, Anthropic, Gemini, OpenAI, LLM integration, AI agents, RAG, Amazon Bedrock, AWS AI/ML, ETL, AWS Glue, data pipelines, Python, FastAPI, Django, PostgreSQL, AWS Lambda, Step Functions, serverless, CDMX" />')
rep('<meta property="og:description" content="10+ years in backend. AI (Claude/SDD, Gemini, OpenAI) at the core of my SDLC. Spec-Driven Development: ~40% faster reviews, 80% N1 self-resolution. AWS Serverless · Python · CDMX, Mexico." />',
    '<meta property="og:description" content="10+ years in backend. Reliability &amp; automation as a product (post-mortems, 99.95% uptime, n8n) with AI (Claude, Gemini, OpenAI) as the SDLC copilot. SDD: ~40% less review time, 80% N1 self-resolution. Python · PostgreSQL · AWS · CDMX." />')
rep('<meta name="twitter:description" content="10+ years in backend. AI-native engineering with Spec-Driven Development. AWS Serverless · Python · CDMX, Mexico." />',
    '<meta name="twitter:description" content="10+ years in backend. Reliability &amp; automation (post-mortems, 99.95% uptime, n8n) with AI-native Spec-Driven Development. Python · PostgreSQL · AWS · CDMX, Mexico." />')

# ---------- 1.4 JSON-LD ----------
rep('"description": "Senior Software Engineer with 10+ years in backend, integrating Generative AI (Claude, Gemini, OpenAI) as the central copilot of the SDLC and championing Spec-Driven Development (SDD).",',
    '"description": "Senior Backend Engineer and Tech Lead with 10+ years. Reliability and automation as a product (post-mortem system, 99.95% monthly uptime, n8n and spec-driven pipelines), integrating Generative AI (Claude, Gemini, OpenAI) as the SDLC copilot and championing Spec-Driven Development (SDD).",')
rep('''      "Spec-Driven Development", "AI-native engineering", "Agentic workflows",
      "Claude API", "Gemini API", "OpenAI API", "LLM integration", "RAG", "AI Agents",
      "Python", "FastAPI", "Django", "PHP", "JavaScript", "TypeScript",
      "AWS Lambda", "AWS Step Functions", "Serverless", "PostgreSQL", "Docker"''',
    '''      "Spec-Driven Development", "AI-native engineering", "Agentic workflows",
      "Site Reliability Engineering", "Post-mortems", "Uptime methodology", "Runbooks",
      "Automation", "n8n", "Spec-driven pipelines",
      "Claude API", "Gemini API", "OpenAI API", "Amazon Bedrock", "LLM integration", "RAG", "AI Agents",
      "Python", "SQL", "FastAPI", "Django", "PHP", "JavaScript", "TypeScript",
      "AWS Lambda", "AWS Step Functions", "CloudWatch", "Serverless", "PostgreSQL", "Docker", "Grafana", "Sentry"''')

# ---------- header ----------
rep("<h3>Senior Backend Engineer &nbsp;|&nbsp; Tech Lead &nbsp;|&nbsp; Agentic AI Systems</h3>",
    "<h3>Senior Backend Engineer &nbsp;|&nbsp; Tech Lead · SRE &amp; Automation &nbsp;|&nbsp; Agentic AI</h3>")
rep('''        Senior Backend Engineer and Tech Lead with 10+ years of experience in backend development, distributed systems and the integration of Generative AI / LLMs (Claude API, Gemini, OpenAI API) as the central copilot of the SDLC. I champion Spec-Driven Development (SDD), cutting review cycles by ~40% and enabling autonomous resolution of 80% of incidents. Specialized in Python · FastAPI · AWS Serverless and AI-native development (RAG, AI agents, agentic workflows), with technical leadership of international GK POS rollouts across Latin America.
		</p>''',
    '''        Senior Backend Engineer and Tech Lead with 10+ years in backend development and distributed systems. Today my signature is <strong>reliability and automation as a product</strong>: a blameless post-mortem system, a monthly uptime methodology (99.95% in July 2026), runbooks, and n8n / spec-driven pipelines that replace manual operations. Generative AI (Claude, Gemini, OpenAI) is the copilot of my SDLC through <strong>Spec-Driven Development</strong> — ~40% less code review time and 80% autonomous N1 resolution — on Python · PostgreSQL · AWS, with technical leadership of international GK POS rollouts across Latin America.
      </p>''')
rep('''        <span class="metric"><strong>&lt;10 min</strong> first response</span>
      </div>''',
    '''        <span class="metric"><strong>&lt;10 min</strong> first response</span>
        <span class="metric"><strong>99.95%</strong> monthly uptime</span>
      </div>''')

# ---------- 1.6 principios (después de .sdd-flow, antes de la grilla) ----------
rep('''      <div class="ai-method-grid">
        <div class="ai-card">
          <h3>Spec-Driven Development</h3>''',
    '''      <div class="now-card principles">
        <strong>How I work</strong>
        <ul>
          <li><strong>Automate &gt; operate.</strong> Rule of two: any manual report or task done more than twice becomes a spec-driven pipeline.</li>
          <li><strong>Reliability as a product.</strong> Downtime is measured by real user impact, not by ticket closure; blameless post-mortems; least-privilege runbooks.</li>
          <li><strong>State outside the code.</strong> IDs, cut-offs and thresholds live in configuration (JSON / Notion) read alike by the workflow and the dashboard — the spec is the contract.</li>
          <li><strong>Cursor over ingestion, not the clock.</strong> Designed for failure (missed runs, late data), not for the happy path.</li>
        </ul>
      </div>
      <div class="ai-method-grid">
        <div class="ai-card">
          <h3>Spec-Driven Development</h3>''')
rep('''            <li>&lt;10 min first response · &lt;2 h resolution</li>
          </ul>''',
    '''            <li>&lt;10 min first response · &lt;2 h resolution</li>
            <li>99.95% monthly uptime (July 2026)</li>
          </ul>''')
rep("<p>Claude (Anthropic), Gemini and OpenAI across the loop: spec generation, automated debugging, RCA &amp; post-mortems, and technical documentation — driving team adoption.</p>",
    "<p>Claude (Anthropic), Gemini, OpenAI and Bedrock across the loop: spec generation, automated debugging, RCA &amp; post-mortems, technical documentation, and an AI Skill for automatic ticket routing with human review on low confidence — driving team adoption.</p>")

# ---------- 2.1 experiencia Podemos ----------
rep('''            <li>Lead the Service Support engineering team in the end-to-end resolution of bugs, critical incidents and technical debt, applying <strong>Spec-Driven Development (SDD)</strong> with the <strong>Claude API</strong>. Cut code review time by <strong>40%</strong> by redesigning the team’s diagnose-to-implement cycle.</li>
            <li>Architect AI flows (<strong>Claude, OpenAI, Gemini</strong>) integrated across the full SDLC — spec generation, static analysis, automated debugging and documentation — driving adoption across the whole engineering area.</li>
            <li>Built a <strong>post-mortem governance dashboard</strong> reading live from Asana: exposes delays, open subtasks, N3/N4 escalations and the Support <strong>ITG traffic light against target</strong>, giving leadership real-time visibility over post-incident commitments.</li>
            <li>Track and review post-mortem closure, verifying that every incident’s subtasks are completed and escalating what falls behind; prepare management status and KPI reports that translate technical detail into actionable information for decision-making.</li>
            <li>Design internal <strong>serverless tooling</strong> (Enkoth — AWS Lambda · Step Functions · EventBridge) and <strong>n8n</strong> automations connecting Asana, Freshdesk, Notion and Slack, removing manual work from the team.</li>
            <li>Take part in the weekly <strong>release trains</strong>, coordinating validation and deployment across platforms (SCI, Spore, Hipatia, Mambu Tools).</li>
            <li>Operate cloud-native AWS infrastructure (Lambda, RDS, Step Functions), sustaining SLAs with <strong>first response under 10 minutes</strong> and critical resolution under 2 hours.</li>
            <li><strong>Stack:</strong> Python · Django · FastAPI · PostgreSQL · AWS Serverless · Claude API · Docker · n8n · Grafana · Asana API</li>''',
    '''            <li>Lead the Service Support team end-to-end (bugs, critical incidents, technical debt) with <strong>Spec-Driven Development (SDD)</strong> and the <strong>Claude API</strong> — cut code review time by <strong>~40%</strong> by redesigning the diagnose-to-implement cycle.</li>
            <li>Built the <strong>post-mortem system</strong> (P0–P3 severity, 5 Whys, blameless, self-assessment rubric) with a <strong>live governance dashboard</strong> — delays, open subtasks, N3/N4 escalations and the KPI traffic light against target — plus management status reports for leadership.</li>
            <li>Defined the <strong>monthly uptime/downtime methodology</strong> (fleet × real minutes; downtime = real user impact): <strong>99.95% in July 2026</strong>. Standardized runbooks and a least-privilege access model.</li>
            <li>Automate operations with <strong>n8n (workflow SDK)</strong>: Freshdesk → Notion → Slack with an ingestion cursor, post-mortem delay watcher, ticket-spike alerts; <strong>spec-driven pipelines</strong> (n8n orchestrates, Python computes, FastAPI endpoint, Notion sink).</li>
            <li>Architect AI flows (<strong>Claude, OpenAI, Gemini, Bedrock</strong>) across the SDLC — specs, static analysis, automated debugging, documentation — and design an <strong>AI Skill for automatic ticket routing</strong> (multi-dimension classification, squad routing, human review on low confidence).</li>
            <li>Take part in the weekly <strong>release trains</strong>, coordinating validation and deployment across core banking, origination and field-app platforms; internal <strong>serverless tooling</strong> (Enkoth — AWS Lambda · Step Functions · EventBridge) for webhooks and integrations.</li>
            <li>Diagnose and operate AWS (<strong>Step Functions, Lambda, CloudWatch Logs Insights, RDS</strong>) and audit error tracking (Sentry) — SLAs: <strong>first response under 10 minutes</strong>, critical resolution under 2 hours.</li>
            <li><strong>Stack:</strong> Python · SQL · PostgreSQL · Django · FastAPI · AWS (Lambda, Step Functions, CloudWatch, RDS) · n8n · Grafana · Sentry · Claude API · Docker · Freshdesk / Notion / Asana APIs</li>''')
rep('''            <li>Led N2 incident management, producing <strong>RCAs</strong> and AI-assisted technical post-mortems that prevented recurring failures.</li>
            <li>Enabled <strong>80% autonomous resolution</strong> in the N1 team through knowledge-transfer strategies, sharply reducing escalation to senior engineering.</li>
            <li>Acted as the central technical liaison in operational coordination, accelerating incident resolution across <strong>Python, Django, FastAPI and PostgreSQL</strong> systems.</li>
            <li><strong>Stack:</strong> Python · Django · FastAPI · PostgreSQL · AWS Serverless · Docker · n8n · Grafana</li>''',
    '''            <li>Led N2 incident management, producing <strong>RCAs</strong> and AI-assisted technical post-mortems that prevented recurring failures; enabled <strong>80% autonomous resolution</strong> in the N1 team through knowledge transfer.</li>
            <li>Own the <strong>weekly idempotent cleanup ETL on PostgreSQL</strong> (backup → delete → update → audit log, pre-validated against expected counts) and identity deduplication in production; schema changes versioned with Liquibase.</li>
            <li>Central technical liaison in operational coordination, accelerating incident resolution across <strong>Python, Django, FastAPI and PostgreSQL</strong> systems.</li>
            <li><strong>Stack:</strong> Python · SQL · PostgreSQL · MySQL · Liquibase · Django · FastAPI · AWS · Docker · Grafana</li>''')

# ---------- 2.3 Fidello ----------
rep('''          <div class="card-badge">★ AI-native · 100% SDD</div>
          <div class="card-badge">🚧 In active development</div>
          <h3>Fidello — Loyalty Card System</h3>''',
    '''          <div class="card-badge">★ AI-native · 100% SDD</div>
          <div class="card-badge">🧪 Pilot · cloud beta</div>
          <h3>Fidello — Loyalty Card System</h3>''')
old_fid = re.search(r'(<h3>Fidello — Loyalty Card System</h3>\n)(\s*<p>.*?</p>\n)(\s*<div class="tech">.*?</div>\n)', s, re.S)
assert old_fid, "card Fidello"
new_fid = old_fid.group(1) + '''          <p>Multi-business digital loyalty platform: customers collect stamps via QR with nothing to install. Five actors (guest, registered customer, cashier, owner/manager, platform admin), multi-business wallet, tiers and redemptions, self-service business onboarding, KPIs/analytics, satisfaction surveys and a scheduled monthly platform report (<strong>pg_cron</strong>). All business rules live in PostgreSQL: <strong>multi-tenant RLS</strong>, RPC in <strong>PL/pgSQL <code>SECURITY DEFINER</code></strong>, QR tokens with TTL + SHA-256 fingerprint against replay, rate limiting on anonymous functions, PII-free audit log and <strong>feature flags</strong> (global + per-business override). Core journeys validated by product in real coffee shops. Ships with an architecture review package (pieces, where each rule lives, deployment, scale limits) for external reviewers. <strong>100% SDD/OpenSpec</strong> with 5 specialized AI agents and 28 journeys with twin runbooks.</p>
          <div class="card-metrics">
            <span class="card-badge">793 tests · 337 DB + 456 UI</span>
            <span class="card-badge">91 migrations · 22 tables</span>
            <span class="card-badge">7 Edge Functions · 5 cron jobs</span>
            <span class="card-badge">97 OpenSpec changes</span>
            <span class="card-badge">28 journeys + runbooks</span>
            <span class="card-badge">CI: 2 blocking jobs · QAS/PROD</span>
          </div>
          <div class="tech">React 18 · TypeScript · Vite 5 · Tailwind 3 · React Router 7 · PWA (Workbox, code-splitting) · WCAG AA · html5-qrcode · Supabase (PostgreSQL 15 + Auth + PostgREST + Realtime) · RLS · PL/pgSQL SECURITY DEFINER · Edge Functions (Deno) · pg_cron · Vitest + Testing Library + msw + pg harness · ESLint · GitHub Actions · Vercel (QAS/PROD) · Supabase CLI + Docker</div>
'''
s = s.replace(old_fid.group(0), new_fid)

# ---------- 2.2 skills por niveles ----------
rep('        <img loading="lazy" decoding="async" width="38" height="38" src="assets/img/icons/laravel-original.svg" alt="Laravel" title="Laravel" />\n', "")
rep('        <img loading="lazy" decoding="async" width="38" height="38" src="assets/img/icons/kubernetes-plain.svg" alt="Kubernetes" title="Kubernetes" />\n', "")
start = s.index('      <div style="margin-top:2rem;">\n        <h3 style="color:var(--primary);font-size:1.05rem;margin-bottom:.9rem;font-family:\'Courier New\',monospace;letter-spacing:.05em;">Tech Stack &amp; Tools</h3>')
end = s.index("    </section>\n\n    <!-- SOFT SKILLS -->")
levels = '''      <div style="margin-top:2rem;">
        <h3 style="color:var(--primary);font-size:1.05rem;margin-bottom:.5rem;font-family:'Courier New',monospace;letter-spacing:.05em;">Tech Stack by level of mastery</h3>
        <p class="level-legend">An honest inventory, not a keyword list. <strong>Own</strong> = built end-to-end and operationally owned · <strong>Build</strong> = solutions I assemble recurrently · <strong>Operate</strong> = fluent for diagnosis and operations, not building the platform · <strong>Learning</strong> = directed study, no operational depth yet.</p>
        <div class="level-grid">
          <div class="level level-own">
            <h3 class="level-title"><span class="level-dot" aria-hidden="true"></span>Own</h3>
            <p class="level-def">Built it end-to-end; if it breaks, they call me.</p>
            <ul class="soft-list">
              <li>PostgreSQL &amp; advanced SQL</li><li>Idempotent production ETL</li><li>Post-mortem system (P0–P3, blameless)</li><li>Uptime / downtime methodology</li><li>Runbooks &amp; least-privilege access</li><li>Notion as knowledge system</li><li>Spec-Driven Development (OpenSpec)</li>
            </ul>
          </div>
          <div class="level level-build">
            <h3 class="level-title"><span class="level-dot" aria-hidden="true"></span>Build</h3>
            <p class="level-def">I assemble solutions with these on a recurring basis.</p>
            <ul class="soft-list">
              <li>Python</li><li>FastAPI</li><li>Django</li><li>Flask</li><li>pytest (mocks)</li><li>SQL</li><li>Liquibase</li><li>n8n (workflow SDK)</li><li>Freshdesk / Notion / Asana / Slack APIs</li><li>Webhooks · serverless tooling</li><li>Spec-driven pipelines</li><li>Grafana dashboards &amp; alerting</li><li>Chart.js dashboards</li><li>Claude API / Claude Code</li><li>OpenAI API</li><li>Gemini API</li><li>Amazon Bedrock</li><li>Prompt Engineering</li><li>LLM Integration</li><li>AI Agents / Skills</li><li>Agentic Workflows</li><li>RAG</li><li>SonarQube</li><li>GitHub Actions (CI/CD)</li><li>Docker</li><li>Serverless Framework</li><li>Supabase (PL/pgSQL, RLS, Edge Functions)</li><li>React</li><li>TypeScript</li><li>Next.js</li><li>Node.js</li><li>Vitest / Jest</li><li>SQLAlchemy 2.0 async · Alembic · Pydantic v2</li><li>Pandas · openpyxl · SFTP / Paramiko</li><li>OpenAPI · REST · WebSocket · SSO / OIDC</li>
            </ul>
          </div>
          <div class="level level-operate">
            <h3 class="level-title"><span class="level-dot" aria-hidden="true"></span>Operate</h3>
            <p class="level-def">Fluent for diagnosis and operations; I don't build the platform.</p>
            <ul class="soft-list">
              <li>AWS Lambda</li><li>Step Functions</li><li>CloudWatch Logs Insights</li><li>RDS</li><li>S3</li><li>EventBridge</li><li>EC2</li><li>AWS SSO / Identity Center</li><li>Sentry</li><li>MySQL</li><li>SQL Server</li><li>MongoDB</li><li>DynamoDB</li><li>SAP ERP / HANA · SAP BO · SAP CAR</li><li>GK POS · GK OmniPOS</li><li>Core banking / credit-bureau integrations</li><li>Scrum · Jira · Asana · Postman</li><li>Azure (base)</li><li>GCP (base)</li>
            </ul>
          </div>
          <div class="level level-learning">
            <h3 class="level-title"><span class="level-dot" aria-hidden="true"></span>Learning</h3>
            <p class="level-def">Directed study; no operational depth yet.</p>
            <ul class="soft-list">
              <li>IaC: Terraform / AWS CDK</li><li>Amazon QuickSight</li><li>Synthetic checks &amp; proactive observability</li><li>AWS Glue at scale</li>
            </ul>
          </div>
        </div>
      </div>
'''
s = s[:start] + levels + s[end:]

# CSS embebido para los niveles (tokens de la paleta, sin colores nuevos)
rep("    .ai-method-grid{display:grid;",
    "    .level-legend{font-size:.9rem;color:var(--muted);margin-bottom:1rem;}\n"
    "    .level-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1.2rem;}\n"
    "    .level{background:var(--card-bg);border:1px solid var(--border);border-left:3px solid var(--border);border-radius:12px;padding:1rem 1.1rem;}\n"
    "    .level-own{border-left-color:var(--primary);} .level-build{border-left-color:var(--accent2);} .level-operate{border-left-color:var(--muted);} .level-learning{border-left-style:dashed;}\n"
    "    .level-title{color:var(--primary);font-size:1rem;margin-bottom:.2rem;font-family:'Courier New',Courier,monospace;letter-spacing:.05em;display:flex;align-items:center;gap:.5rem;}\n"
    "    .level-dot{width:.6rem;height:.6rem;border-radius:50%;background:var(--primary);display:inline-block;}\n"
    "    .level-build .level-dot{background:var(--accent2);} .level-operate .level-dot{background:var(--muted);} .level-learning .level-dot{background:transparent;border:1px dashed var(--muted);}\n"
    "    .level-def{font-size:.85rem;color:var(--muted);margin-bottom:.7rem;}\n"
    "    .level .soft-list li{font-size:.85rem;padding:.3rem .65rem;}\n"
    "    .card-metrics{display:flex;flex-wrap:wrap;gap:.4rem;margin:.2rem 0 .7rem;} .card-metrics .card-badge{margin-bottom:0;}\n"
    "    .principles ul{margin-left:1.1rem;} .principles li{margin:.4rem 0;font-size:.92rem;}\n"
    "    .ai-method-grid{display:grid;")
rep("    @media(max-width:768px){", "    @media(max-width:768px){.level-grid{grid-template-columns:1fr;}")

io.open(P, "w", encoding="utf-8", newline="").write(s)
print("index.html OK  (%d -> %d bytes)" % (n_before, len(s)))
