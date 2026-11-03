"""Verifica el CV contra las specs cv-contenido-claro y cv-presentacion.

Uso:  python scripts/cv/check_cv.py
Sale con código 1 si algún check falla. Sin dependencias salvo pypdf (para los PDFs).
"""
import html
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
TITULAR = "Senior Backend Engineer | Tech Lead · SRE & Automation | Agentic AI"
PROHIBIDAS = ["Pyzzeria", "IA Specialist", "beta", "cafeterías reales", "real coffee shops", "Live Demo"]
PROYECTOS = ["platform-STALD", "Fidello", "Monitoreo-Cloud"]
OTROS = ["VoltGrid", "Trackion", "dataMasterGK"]
FUENTES = {"es": ("cv/cv.html", "cv/CV_JuanValentinAlducin.pdf"),
           "en": ("cv/cv-en.html", "cv/CV_JuanValentinAlducin_EN.pdf")}

sys.stdout.reconfigure(encoding="utf-8")
fallas = []


def check(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        fallas.append(msg)


def texto(fragmento):
    return html.unescape(re.sub(r"<[^>]+>", "", fragmento)).strip()


def clase(doc, nombre):
    return [texto(m) for m in re.findall(rf'<div class="{nombre}">(.*?)</div>', doc, re.S)]


llms = (RAIZ / "llms.txt").read_text(encoding="utf-8")
m = re.search(r"^- Role: (.+)$", llms, re.M)
check(m and m.group(1).strip() == TITULAR, "llms.txt: Role = titular acordado")
for p in PROHIBIDAS:
    check(p not in llms, f"llms.txt: sin '{p}'")
check("platform-STALD" in llms, "llms.txt: incluye platform-STALD")

for idioma, (src, pdf) in FUENTES.items():
    doc = (RAIZ / src).read_text(encoding="utf-8")
    t = f"[{idioma}]"
    check(clase(doc, "tagline") == [TITULAR], f"{t} titular acordado")
    resumen = texto(re.search(r'<p class="summary">(.*?)</p>', doc, re.S).group(1))
    check(len(resumen) <= 300, f"{t} resumen ≤ 300 caracteres ({len(resumen)})")

    exp = re.search(r"<h2>(?:Experiencia|Experience)</h2>(.*?)</section>", doc, re.S).group(1)
    entradas = re.findall(r'<div class="entry">(.*?)</ul>', exp, re.S)
    limites = [4, 2, 2, 1]
    conteos = [e.count("<li>") for e in entradas]
    check(len(entradas) == 4 and all(c <= l for c, l in zip(conteos, limites)) and conteos[-1] == 1,
          f"{t} bullets por rol {conteos} dentro de {limites}")
    check('class="stack"' not in exp, f"{t} sin líneas Stack: en experiencia")
    check("Service Support Tech Lead &amp; AI Specialist" in doc, f"{t} rol 'AI Specialist'")

    check(len(clase(doc, "cat")) == 5, f"{t} 5 categorías de habilidades ({len(clase(doc, 'cat'))})")
    titulos = clase(doc, "ptitle")
    check([x.split(" — ")[0] for x in titulos] == PROYECTOS, f"{t} proyectos {PROYECTOS} en orden")
    otros = re.search(r'<p class="pother">(.*?)</p>', doc, re.S)
    check(bool(otros) and all(o in otros.group(1) for o in OTROS), f"{t} línea Otros con {OTROS}")
    for p in PROHIBIDAS:
        check(p not in doc, f"{t} sin '{p}'")
    cursos = doc.count('class="course"')
    check(cursos <= 7, f"{t} ≤ 7 cursos, uno por línea ({cursos})")
    check(re.search(r"@page\s*\{\s*size:\s*(210mm 297mm|A4)", doc) is not None, f"{t} @page A4")

    try:
        from pypdf import PdfReader
        r = PdfReader(str(RAIZ / pdf))
        check(len(r.pages) == 1, f"{t} PDF de 1 página ({len(r.pages)})")
        w, h = float(r.pages[0].mediabox.width), float(r.pages[0].mediabox.height)
        check(abs(w - 595) < 3 and abs(h - 842) < 3, f"{t} PDF A4 ({w:.0f}×{h:.0f} pt)")
        fuentes = r.pages[0]["/Resources"]["/Font"]
        tipos = {str(f.get_object()["/Subtype"]) for f in fuentes.values()}
        check("/Type3" not in tipos, f"{t} PDF sin fuentes Type3 ({sorted(tipos)})")
        txt = r.pages[0].extract_text()
        check("valentin.alducin88@gmail.com" in txt and "github.com/jalducin" in txt,
              f"{t} PDF con contacto como texto")
    except FileNotFoundError:
        check(False, f"{t} PDF existe")

print(f"\n{len(fallas)} falla(s)")
sys.exit(1 if fallas else 0)
