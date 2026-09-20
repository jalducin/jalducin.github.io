# -*- coding: utf-8 -*-
"""Auditoría de consistencia (heredada de cv-portafolio-sre-automation) + checks i18n del cambio portafolio-bilingue.

Uso: python openspec/changes/cv-portafolio-sre-automation/scripts/audit.py  (desde la raíz del repo)
Salida: una línea PASS/FAIL por check y código de salida 1 si algo falla.
"""
import io, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(ROOT)

HEADLINE_SITE = "Senior Backend Engineer · Tech Lead · SRE & Automation · Agentic AI"
HEADLINE_CV = "Senior Backend Engineer | Tech Lead · SRE &amp; Automation | Agentic AI"
PUBLIC_FILES = ["index.html", "cv/cv.html", "cv/cv-en.html", "llms.txt", "cv/CV_JuanValentinAlducin.md"]
# Nombres internos del empleador y datos privados (design.md D2)
FORBIDDEN = [r"\bSCI\b", r"\bSpore\b", r"\bHipatia\b", r"Mambu", r"\bLUCI\b", r"\bAleph\b", r"\bDANIEL\b",
             r"\bStrauss\b", r"Alejandr[ií]a", r"\bWatson\b", r"\bSherlock\b", r"INC-20\d\d-", r"podemos_clientes",
             r"freshdeskdb", r"BBVA", r"Ban ?Baj[ií]o", r"24,?965", r"Pichardo"]
STALE = [r"Kendra", r"\bKiro\b", r"Master'?s in DevOps", r"Maestr[ií]a en DevOps", r"\bIEU\b", r"Agentic AI Systems"]
ROLES = [  # (fecha ES, fecha EN, fecha sitio, título ES, título EN/sitio)
    ("07/2026 - Presente", "07/2026 - Present", "Jul 2026 – Present",
     "Service Support Tech Lead &amp; IA Specialist", "Service Support Tech Lead &amp; AI Specialist"),
    ("09/2025 - 06/2026", "09/2025 - 06/2026", "Sept 2025 – Jun 2026", "Backend Support Specialist", "Backend Support Specialist"),
    ("01/2022 - 09/2025", "01/2022 - 09/2025", "Jan 2022 – Sept 2025", "Software Engineer > Tech Lead", "Software Engineer → Tech Lead"),
    ("03/2017 - 01/2022", "03/2017 - 01/2022", "Mar 2017 – Jan 2022", "Software Engineer", "Software Engineer"),
]

results = []


def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(("PASS  " if ok else "FAIL  ") + name + (("  -> " + detail) if detail and not ok else ""))


def read(p):
    return io.open(p, encoding="utf-8").read()


files = {p: read(p) for p in PUBLIC_FILES if os.path.exists(p)}
idx, es, en, llm = files["index.html"], files["cv/cv.html"], files["cv/cv-en.html"], files["llms.txt"]

# (a) nombres internos prohibidos
for p, s in files.items():
    hits = [pat for pat in FORBIDDEN if re.search(pat, s)]
    check("sin nombres internos: " + p, not hits, ", ".join(hits))

# (d) contenido obsoleto
for p, s in files.items():
    hits = [pat for pat in STALE if re.search(pat, s)]
    check("sin contenido obsoleto (Kendra/Kiro/maestría/headline viejo): " + p, not hits, ", ".join(hits))

# (b) headline idéntico en todas las superficies
h3 = re.search(r"<header[^>]*>.*?<h3>(.*?)</h3>", idx, re.S)
h3txt = re.sub(r"\s+", " ", h3.group(1).replace("&nbsp;", " ")).strip() if h3 else ""
check("header h3 = headline híbrido", h3txt == "Senior Backend Engineer | Tech Lead · SRE &amp; Automation | Agentic AI", h3txt)
title = re.search(r"<title>(.*?)</title>", idx, re.S).group(1)
check("<title> contiene headline", HEADLINE_SITE in title, title)
for meta in ("og:title", "twitter:title"):
    m = re.search(r'property="%s" content="([^"]+)"|name="%s" content="([^"]+)"' % (meta, meta), idx)
    val = (m.group(1) or m.group(2)) if m else ""
    check("%s contiene headline" % meta, HEADLINE_SITE in val, val)
ld = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', idx, re.S)
try:
    ldj = json.loads(ld.group(1))
    check("JSON-LD válido y jobTitle híbrido", ldj.get("jobTitle") == HEADLINE_SITE, str(ldj.get("jobTitle")))
    ka = " ".join(ldj.get("knowsAbout", []))
    check("JSON-LD knowsAbout incluye SRE/n8n y excluye Kendra/Kiro",
          all(k in ka for k in ("Site Reliability Engineering", "n8n")) and not re.search(r"Kendra|Kiro", ka), ka[:120])
except Exception as e:  # noqa
    check("JSON-LD válido", False, str(e))
who = re.search(r"whoami:\(\)=>\"([^\"]+)\"", idx)
check("terminal whoami usa headline", bool(who) and HEADLINE_SITE in who.group(1), who.group(1) if who else "")
for p, s in (("cv/cv.html", es), ("cv/cv-en.html", en)):
    tg = re.search(r'class="tagline">(.*?)</div>', s)
    check("tagline CV " + p, bool(tg) and tg.group(1).strip() == HEADLINE_CV, tg.group(1) if tg else "")
check("llms.txt contiene headline", HEADLINE_SITE.replace(" · ", " · ") in llm or "SRE & Automation" in llm)

# (c) roles y fechas iguales en las 4 fuentes
for fes, fen, fsite, tes, ten in ROLES:
    check("rol ES: %s | %s" % (tes, fes), tes in es and fes in es)
    ten_cv = ten.replace("→", ">")  # el CV usa ">" en ambos idiomas; el sitio usa la flecha
    check("rol EN: %s | %s" % (ten_cv, fen), ten_cv in en and fen in en)
    check("rol sitio: %s | %s" % (ten, fsite), ten in idx and fsite in idx)
check("llms.txt roles Podemos", "Jul 2026 – present" in llm and "Sep 2025 – Jun 2026" in llm)

# (f) specs nuevas de este cambio
check("4 principios en index.html", all(k in idx for k in ("Automate", "Reliability as a product", "State outside the code", "Cursor over ingestion")))
check("4 principios en llms.txt", all(k in llm for k in ("Automate", "Reliability as a product", "State outside the code", "Cursor over ingestion")))
check("leyenda de niveles en index.html", all(k in idx for k in ("level-grid", "Own", "Build", "Operate", "Learning")))
check("Kubernetes solo en VoltGrid", idx.count("Kubernetes") >= 1 and "kubernetes-plain.svg" not in idx and
      all("VoltGrid" in idx[max(0, m.start() - 1500):m.start()] for m in re.finditer("Kubernetes", idx)))
check("badges Fidello con cifras", all(k in idx for k in ("793", "91 migrations", "Pilot")))
check("uptime en badges/impacto", idx.count("99.95%") >= 2)
check("Fidello piloto en CV ES/EN y llms", "piloto" in es.lower() and "pilot" in en.lower() and "pilot" in llm.lower())
check("profile.txt == llms.txt", os.path.exists("backend/assistant/profile.txt") and read("backend/assistant/profile.txt") == llm)

# (e) PDFs: 1 página y fuentes Segoe UI (TrueType)
try:
    from pypdf import PdfReader
    for f in ("cv/CV_JuanValentinAlducin.pdf", "cv/CV_JuanValentinAlducin_EN.pdf"):
        r = PdfReader(f)
        fonts = set()
        for pg in r.pages:
            for k, v in pg.get("/Resources", {}).get("/Font", {}).items():
                o = v.get_object()
                bf = o.get("/BaseFont") or o["/DescendantFonts"][0].get_object().get("/BaseFont")
                fonts.add(str(bf))
        ok = len(r.pages) == 1 and fonts and all("SegoeUI" in x for x in fonts)
        check("PDF 1 página + Segoe UI: " + f, ok, "paginas=%d fuentes=%s" % (len(r.pages), sorted(fonts)))
        txt = " ".join((pg.extract_text() or "") for pg in r.pages)
        hits = [pat for pat in FORBIDDEN if re.search(pat, txt)]
        check("PDF sin nombres internos: " + f, not hits, ", ".join(hits))
        check("PDF contiene contacto y roles: " + f, all(k in txt for k in ("valentin.alducin88", "525640800494", "Service Support", "Backend Support Specialist", "Redsis", "Softtek")))
except ImportError:
    check("pypdf disponible", False, "pip install pypdf")

# ---------- i18n (portafolio-bilingue, design.md D5) ----------
import importlib.util
spec = importlib.util.spec_from_file_location("es", os.path.join(os.path.dirname(os.path.abspath(__file__)), "es.py"))
esmod = importlib.util.module_from_spec(spec); spec.loader.exec_module(esmod)
m = re.search(r'<script type="application/json" id="i18n-es">(.*?)</script>', idx, re.S)
try:
    ES = json.loads(m.group(1)); check("diccionario ES embebido parsea", True)
except Exception as e:
    ES = {}; check("diccionario ES embebido parsea", False, str(e))
dom_keys = set(re.findall(r'data-i18n(?:-title|-aria|-placeholder)?="([^"]+)"', idx))
check("0 claves ES huérfanas (sin elemento en el DOM)", not (set(ES) - dom_keys), sorted(set(ES) - dom_keys)[:10])
untr = set(dom_keys) - set(ES)
check("claves sin traducción == invariantes declaradas", untr == set(esmod.INVARIANTES) & dom_keys, sorted(untr ^ (set(esmod.INVARIANTES) & dom_keys))[:10])
check("elementos data-i18n >= 200", len(dom_keys) >= 200, len(dom_keys))
check("diccionario ES == es.py (build al día)", ES == esmod.ES)
hits = [pat for pat in FORBIDDEN if any(re.search(pat, v) for v in ES.values())]
check("sin nombres internos en el diccionario ES", not hits, hits)
check("botón #lang-btn en nav y runtime presente", 'id="lang-btn"' in idx and "window.__setLang=applyLang" in idx and 'id="i18n-es"' in idx)
check("terminal: comandos lang", "'lang es':()=>" in idx and "lang es|en" in idx)
check("palette: acción de idioma", "Español / English" in idx)
check("html lang por defecto en", '<html lang="en">' in idx)

fails = [n for n, ok, _ in results if not ok]
print("\n%d checks · %d PASS · %d FAIL" % (len(results), len(results) - len(fails), len(fails)))
sys.exit(1 if fails else 0)
