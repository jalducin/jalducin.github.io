# -*- coding: utf-8 -*-
"""Mide en Chrome headless la altura (mm) del sheet y de cada columna del CV.
Regla empírica calibrada 2026-09-19 (design.md D7): el PDF cabe en 1 página si sheet <= 340 mm
(sheet = 20 mm de padding + header + max(col)); con sheet 343.6 ya salta a 2 páginas.
Uso: python measure_cv.py cv.html cv-en.html
"""
import io, os, re, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
CHROME = next(c for c in [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                          r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                          r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"] if os.path.exists(c))
SNIP = """<script>window.addEventListener('load',function(){setTimeout(function(){
var mm=function(px){return (px/(96/25.4)).toFixed(1);};
var s=document.querySelector('.sheet'),l=document.querySelector('.col-left'),r=document.querySelector('.col-right');
document.title='MEASURE sheet='+mm(s.getBoundingClientRect().height)+'mm left='+mm(l.getBoundingClientRect().height)+'mm right='+mm(r.getBoundingClientRect().height)+'mm';
},300);});</script></body>"""
for src in sys.argv[1:]:
    path = os.path.join(ROOT, "cv", src)
    tmp = os.path.join(ROOT, "cv", "_measure_" + src)
    io.open(tmp, "w", encoding="utf-8", newline="").write(io.open(path, encoding="utf-8").read().replace("</body>", SNIP))
    udd = tempfile.mkdtemp(prefix="cvmeas_")
    out = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=3000", "--user-data-dir=" + udd,
                          "--dump-dom", "file:///" + tmp.replace("\\", "/")], capture_output=True, text=True, encoding="utf-8", errors="replace")
    os.remove(tmp)
    m = re.search(r"MEASURE[^<]*", out.stdout or "")
    print(src, "->", m.group(0) if m else "sin medida")
