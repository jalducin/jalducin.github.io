# -*- coding: utf-8 -*-
"""Retira las cifras (~40%, 80%, 99.95%) de index.html (EN) y de scripts/i18n/es.py (ES). Idempotente."""
import io, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
os.chdir(ROOT)


def rw(p, reps):
    s = io.open(p, encoding="utf-8").read()
    for o, n in reps:
        if o in s:
            assert s.count(o) == 1, (p, o[:50], s.count(o)); s = s.replace(o, n)
        else:
            assert n in s, (p, "ni viejo ni nuevo: " + o[:50])
    io.open(p, "w", encoding="utf-8", newline="").write(s); print(p, "OK")


rw("index.html", [
    # head
    ('post-mortem system, 99.95% monthly uptime, n8n and spec-driven pipelines. AI (Claude, Gemini, OpenAI) as the SDLC copilot with Spec-Driven Development: ~40% less code review time, 80% N1 self-resolution, <10 min first response.',
     'post-mortem system, monthly uptime methodology, n8n and spec-driven pipelines. AI (Claude, Gemini, OpenAI) as the SDLC copilot with Spec-Driven Development; SLAs: <10 min first response, <2 h critical resolution.'),
    ('(post-mortems, 99.95% uptime, n8n) with AI (Claude, Gemini, OpenAI) as the SDLC copilot. SDD: ~40% less review time, 80% N1 self-resolution.',
     '(post-mortems, uptime methodology, n8n) with AI (Claude, Gemini, OpenAI) as the SDLC copilot and Spec-Driven Development.'),
    ('(post-mortems, 99.95% uptime, n8n) with AI-native Spec-Driven Development.',
     '(post-mortems, uptime methodology, n8n) with AI-native Spec-Driven Development.'),
    ('(post-mortem system, 99.95% monthly uptime, n8n and spec-driven pipelines), integrating',
     '(post-mortem system, monthly uptime methodology, n8n and spec-driven pipelines), integrating'),
    # header
    ('a monthly uptime methodology (99.95% in July 2026), runbooks, and n8n / spec-driven pipelines that replace manual operations. Generative AI (Claude, Gemini, OpenAI) is the copilot of my SDLC through <strong>Spec-Driven Development</strong> — ~40% less code review time and 80% autonomous N1 resolution — on Python · PostgreSQL · AWS,',
     'a monthly uptime methodology, runbooks, and n8n / spec-driven pipelines that replace manual operations. Generative AI (Claude, Gemini, OpenAI) is the copilot of my SDLC through <strong>Spec-Driven Development</strong> on Python · PostgreSQL · AWS,'),
    ('        <span class="metric" data-i18n="hdr.span1"><strong>~40%</strong> less code review time</span>\n        <span class="metric" data-i18n="hdr.span2"><strong>80%</strong> N1 self-resolution</span>\n        <span class="metric" data-i18n="hdr.span3"><strong>&lt;10 min</strong> first response</span>\n        <span class="metric" data-i18n="hdr.span4"><strong>99.95%</strong> monthly uptime</span>',
     '        <span class="metric" data-i18n="hdr.span1"><strong>&lt;10 min</strong> first response</span>\n        <span class="metric" data-i18n="hdr.span2"><strong>&lt;2 h</strong> critical resolution</span>\n        <span class="metric" data-i18n="hdr.span3"><strong>Blameless</strong> post-mortems</span>\n        <span class="metric" data-i18n="hdr.span4"><strong>Spec-driven</strong> pipelines</span>'),
    # ai-method
    ('proposes implementations against the contract — cutting review cycles by ~40%.</p>',
     'proposes implementations against the contract — shortening review cycles.</p>'),
    ('          <h3 data-i18n="aim.h33">Measurable impact</h3>\n          <ul>\n            <li data-i18n="aim.li8">~40% less code review time</li>\n            <li data-i18n="aim.li9">80% autonomous N1 incident resolution</li>\n            <li data-i18n="aim.li10">&lt;10 min first response · &lt;2 h resolution</li>\n            <li data-i18n="aim.li11">99.95% monthly uptime (July 2026)</li>\n          </ul>',
     '          <h3 data-i18n="aim.h33">Operational SLAs &amp; practices</h3>\n          <ul>\n            <li data-i18n="aim.li8">&lt;10 min first response · &lt;2 h critical resolution</li>\n            <li data-i18n="aim.li9">Blameless post-mortems with a live governance dashboard</li>\n            <li data-i18n="aim.li10">Monthly uptime/downtime methodology by real user impact</li>\n            <li data-i18n="aim.li11">Spec-driven pipelines instead of manual reports</li>\n          </ul>'),
    # experience
    ('with <strong>Spec-Driven Development (SDD)</strong> and the <strong>Claude API</strong> — cut code review time by <strong>~40%</strong> by redesigning the diagnose-to-implement cycle.</li>',
     'with <strong>Spec-Driven Development (SDD)</strong> and the <strong>Claude API</strong> — shortened the review cycle by redesigning the diagnose-to-implement flow.</li>'),
    ('(fleet × real minutes; downtime = real user impact): <strong>99.95% in July 2026</strong>. Standardized runbooks',
     '(fleet × real minutes; downtime = real user impact). Standardized runbooks'),
    ('that prevented recurring failures; enabled <strong>80% autonomous resolution</strong> in the N1 team through knowledge transfer.</li>',
     'that prevented recurring failures; enabled <strong>autonomous resolution</strong> in the N1 team through knowledge transfer.</li>'),
    # writing card + terminal
    ('and why it cut my review cycles ~40%.</p>', 'and why it shortened my review cycles.</p>'),
    ('(~40% menos ciclo de revisión, 80% autoresolución N1, <10 min primera respuesta).', '(<10 min primera respuesta, <2 h resolución crítica).'),
])

rw("scripts/i18n/es.py", [
    ('una metodología de uptime mensual (99.95 % en julio 2026), runbooks y pipelines n8n / spec-driven que sustituyen operación manual. La IA generativa (Claude, Gemini, OpenAI) es el copiloto de mi SDLC mediante <strong>Spec-Driven Development</strong> — ~40 % menos tiempo de revisión de código y 80 % de autoresolución N1 — sobre Python · PostgreSQL · AWS,',
     'una metodología de uptime mensual, runbooks y pipelines n8n / spec-driven que sustituyen operación manual. La IA generativa (Claude, Gemini, OpenAI) es el copiloto de mi SDLC mediante <strong>Spec-Driven Development</strong> sobre Python · PostgreSQL · AWS,'),
    ('    "hdr.span1": "<strong>~40%</strong> menos tiempo de revisión",\n    "hdr.span2": "<strong>80%</strong> autoresolución N1",\n    "hdr.span3": "<strong>&lt;10 min</strong> primera respuesta",\n    "hdr.span4": "<strong>99.95%</strong> uptime mensual",',
     '    "hdr.span1": "<strong>&lt;10 min</strong> primera respuesta",\n    "hdr.span2": "<strong>&lt;2 h</strong> resolución crítica",\n    "hdr.span3": "Post-mortems <strong>blameless</strong>",\n    "hdr.span4": "Pipelines <strong>spec-driven</strong>",'),
    ('propone implementaciones contra el contrato — recortando los ciclos de revisión ~40 %.', 'propone implementaciones contra el contrato — acortando los ciclos de revisión.'),
    ('    "aim.h33": "Impacto medible",\n    "aim.li8": "~40 % menos tiempo de revisión de código",\n    "aim.li9": "80 % de resolución autónoma de incidentes N1",\n    "aim.li10": "&lt;10 min primera respuesta · &lt;2 h resolución",\n    "aim.li11": "99.95 % de uptime mensual (julio 2026)",',
     '    "aim.h33": "SLAs y prácticas operativas",\n    "aim.li8": "&lt;10 min primera respuesta · &lt;2 h resolución crítica",\n    "aim.li9": "Post-mortems blameless con tablero de gobierno en vivo",\n    "aim.li10": "Metodología mensual de uptime/downtime por impacto real al usuario",\n    "aim.li11": "Pipelines spec-driven en lugar de reportes manuales",'),
    ('y <strong>Claude API</strong> — reduje el tiempo de revisión de código <strong>~40 %</strong> al rediseñar el ciclo diagnóstico → implementación.',
     'y <strong>Claude API</strong> — acorté el ciclo de revisión al rediseñar el flujo diagnóstico → implementación.'),
    ('(flota × minutos reales; downtime = impacto real al usuario): <strong>99.95 % en julio 2026</strong>. Estandaricé',
     '(flota × minutos reales; downtime = impacto real al usuario). Estandaricé'),
    ('que previnieron fallos recurrentes; habilité <strong>80 % de resolución autónoma</strong> en el equipo N1 mediante transferencia de conocimiento.',
     'que previnieron fallos recurrentes; habilité la <strong>resolución autónoma</strong> en el equipo N1 mediante transferencia de conocimiento.'),
    ('y por qué recortó mis ciclos de revisión ~40 %.', 'y por qué acortó mis ciclos de revisión.'),
])

for p in ("index.html", "scripts/i18n/es.py"):
    t = io.open(p, encoding="utf-8").read()
    t = re.sub(r'<script type="application/json" id="i18n-es">.*?</script>', "", t, flags=re.S)
    left = [m.group(0) for m in re.finditer(r".{25}(?:~?40 ?%|80 ?%|99\.95).{25}", t)]
    assert not left, (p, left)
print("sin cifras en index.html (fuera del JSON) y es.py")
