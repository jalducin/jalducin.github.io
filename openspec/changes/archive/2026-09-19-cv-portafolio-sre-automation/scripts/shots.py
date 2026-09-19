# -*- coding: utf-8 -*-
"""Capturas headless de index.html (4 vistas × 4 anchos) y del CV, más probes de DOM/JS (tasks 6.1–6.3)."""
import io, os, re, subprocess, sys, tempfile, time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
OUT = os.path.join(ROOT, "openspec", "changes", "cv-portafolio-sre-automation", "reports", "shots")
os.makedirs(OUT, exist_ok=True)
CH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def chrome(args):
    return subprocess.run([CH, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=5000",
                           "--user-data-dir=" + tempfile.mkdtemp(prefix="shot_")] + args,
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


src = io.open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
# fade-in visible de inmediato + probe: mide overflow horizontal y evalua whoami/enlaces de descarga
PROBE = """<style>.fade-in{opacity:1!important;transform:none!important;}</style>
<script>window.addEventListener('load',function(){setTimeout(function(){
 var r=[]; r.push('scrollW='+document.documentElement.scrollWidth+'/innerW='+window.innerWidth);
 r.push('overflowX='+(document.documentElement.scrollWidth>window.innerWidth));
 document.querySelectorAll('a[data-cv]').forEach(function(a){r.push(a.getAttribute('data-cv')+'|'+a.getAttribute('href')+'|'+a.getAttribute('download'));});
 r.push('showTab='+(typeof window.__showTab));
 r.push('levels='+document.querySelectorAll('.level').length+' principles='+document.querySelectorAll('.principles li').length+' fidelloMetrics='+document.querySelectorAll('.card-metrics .card-badge').length);
 var ids=['ai-method','experience','featured-projects','writing','hard-skills','soft-skills','languages','education','contact','terminal'];
 r.push('missingSections='+ids.filter(function(i){return !document.getElementById(i);}).join(','));
 var dup=[]; var seen={}; document.querySelectorAll('[id]').forEach(function(e){if(seen[e.id])dup.push(e.id);seen[e.id]=1;}); r.push('dupIds='+dup.join(','));
 document.title='PROBE '+r.join(' ;; ');
},400);});</script></body>"""
tmp = os.path.join(ROOT, "_shot_index.html")
io.open(tmp, "w", encoding="utf-8", newline="").write(src.replace("</body>", PROBE))
url = "file:///" + tmp.replace("\\", "/")

for view in ("ai-method", "experience", "featured-projects", "hard-skills"):
    for w in (1280, 992, 768, 480):
        png = os.path.join(OUT, "%s_%d.png" % (view, w))
        chrome(["--window-size=%d,%d" % (w, 4200 if w > 700 else 6000), "--screenshot=" + png, url + "#" + view])
        print("captura", os.path.relpath(png, ROOT))
    out = chrome(["--window-size=480,900", "--dump-dom", url + "#" + view])
    m = re.search(r"PROBE[^<]*", out.stdout or "")
    print("probe 480px #%s: %s" % (view, m.group(0)[6:] if m else "sin resultado"))
# caso de error: hash inexistente cae en ai-method
out = chrome(["--window-size=1280,900", "--dump-dom", url + "#seccion-inexistente"])
active = re.search(r'class="nav-link active"[^>]*href="#([^"]+)"|href="#([^"]+)"[^>]*class="nav-link active"', out.stdout or "")
print("hash inexistente -> tab activa:", (active.group(1) or active.group(2)) if active else "?")
os.remove(tmp)

# CV a PNG
for f in ("cv.html", "cv-en.html"):
    png = os.path.join(OUT, f.replace(".html", ".png"))
    chrome(["--window-size=816,1330", "--screenshot=" + png, "file:///" + os.path.join(ROOT, "cv", f).replace("\\", "/")])
    print("captura", os.path.relpath(png, ROOT))
