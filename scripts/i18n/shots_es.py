# -*- coding: utf-8 -*-
"""Capturas en español (1280/768/480) de 5 vistas + probe de overflow y visibilidad del botón (task 6.3)."""
import io, os, re, subprocess, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "scripts", "i18n", "shots")
os.makedirs(OUT, exist_ok=True)
CH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROBE = ("<style>.fade-in{opacity:1!important;transform:none!important;}</style><script>window.addEventListener('load',function(){setTimeout(function(){"
         "var b=document.getElementById('lang-btn').getBoundingClientRect();"
         "document.title='PROBE ow='+(document.documentElement.scrollWidth>window.innerWidth)+' btnVisible='+(b.width>0&&b.right<=window.innerWidth)+' lang='+document.documentElement.lang;},400);});</script></body>")
src = io.open(os.path.join(ROOT, "index.html"), encoding="utf-8").read().replace("</body>", PROBE)
tmp = os.path.join(ROOT, "_shot_es.html"); io.open(tmp, "w", encoding="utf-8", newline="").write(src)
url = "file:///" + tmp.replace("\\", "/") + "?lang=es#"
ok = True
for view in ("ai-method", "experience", "featured-projects", "hard-skills", "contact"):
    for w in (1280, 768, 480):
        png = os.path.join(OUT, "es_%s_%d.png" % (view, w))
        subprocess.run([CH, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=5000",
                        "--user-data-dir=" + tempfile.mkdtemp(), "--window-size=%d,%d" % (w, 4200 if w > 700 else 6000),
                        "--screenshot=" + png, url + view], capture_output=True)
        out = subprocess.run([CH, "--headless=new", "--disable-gpu", "--virtual-time-budget=5000", "--user-data-dir=" + tempfile.mkdtemp(),
                              "--window-size=%d,900" % w, "--dump-dom", url + view], capture_output=True, text=True, encoding="utf-8", errors="replace")
        m = re.search(r"PROBE[^<]*", out.stdout or ""); res = m.group(0) if m else "?"
        good = "ow=false" in res and "btnVisible=true" in res and "lang=es" in res
        ok &= good
        print("%-4s %-18s %4d  %s  %s" % ("PASS" if good else "FAIL", view, w, res, os.path.relpath(png, ROOT) if os.path.exists(png) else "(sin captura)"))
os.remove(tmp)
raise SystemExit(0 if ok else 1)
