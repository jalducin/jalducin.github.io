# -*- coding: utf-8 -*-
"""Probes headless del bot local: preguntas conocidas (ES/EN), fuera de alcance y ausencia de red.
Uso: python scripts/assistant/probe_kb.py
"""
import io, json, os, re, subprocess, tempfile, html as H

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(ROOT)
CH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SRC = io.open("index.html", encoding="utf-8").read()
results = []


def check(name, ok, detail=""):
    results.append(ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("" if ok else "  -> " + str(detail)[:260]))


def run(probe_js, pre_body="", url_suffix="", mutate=None):
    base = mutate(SRC) if mutate else SRC
    html = base.replace("<body>", "<body>" + pre_body, 1).replace(
        "</body>", "<script>window.addEventListener('load',function(){setTimeout(function(){try{" + probe_js +
        "}catch(e){document.title='PROBE '+JSON.stringify({error:String(e)});}},400);});</script></body>")
    tmp = os.path.join(ROOT, "_probe_kb.html")
    io.open(tmp, "w", encoding="utf-8", newline="").write(html)
    out = subprocess.run([CH, "--headless=new", "--disable-gpu", "--virtual-time-budget=5000",
                          "--user-data-dir=" + tempfile.mkdtemp(prefix="kb_"), "--dump-dom",
                          "file:///" + tmp.replace("\\", "/") + url_suffix],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    os.remove(tmp)
    m = re.search(r"<title>PROBE (.*?)</title>", out.stdout or "", re.S)
    return json.loads(H.unescape(m.group(1))) if m else {"error": "sin PROBE"}


# preguntas esperadas -> id de la entrada (el probe compara contra el texto de la entrada)
CASES_EN = [("What is your AWS and serverless experience?", "aws-cloud"),
            ("Tell me about Fidello", "proyecto-fidello"),
            ("What is SDD?", "ia-sdd"),
            ("How can I contact Juan?", "contacto"),
            ("What is his current role?", "rol-actual"),
            ("Where does he live?", "ubicacion")]
CASES_ES = [("¿Qué experiencia tienes en AWS?", "aws-cloud"),
            ("Cuéntame de Fidello", "proyecto-fidello"),
            ("¿Qué es SDD?", "ia-sdd"),
            ("¿Cómo contacto a Juan?", "contacto"),
            ("¿Cuál es su rol actual?", "rol-actual"),
            ("¿Dónde vive?", "ubicacion")]

js = """
 var KB=JSON.parse(document.getElementById('assistant-kb').textContent);
 var byId={}; KB.forEach(function(e){byId[e.id]=e;});
 var cases=%s, lang='%s';
 if(window.__setLang)window.__setLang(lang);
 var res=cases.map(function(c){var a=window.__askPortfolio(c[0]); var exp=byId[c[1]][lang];
   return {q:c[0], ok:a===exp, got:(a||'(null)').slice(0,40)};});
 document.title='PROBE '+JSON.stringify({res:res, kb:KB.length});"""

for lang, cases in (("en", CASES_EN), ("es", CASES_ES)):
    r = run(js % (json.dumps(cases, ensure_ascii=False), lang))
    for item in r.get("res", []):
        check("%s | %s" % (lang.upper(), item["q"]), item["ok"], item.get("got"))
    check("%s | KB cargada (21 entradas)" % lang.upper(), r.get("kb") == 21, r.get("kb"))

# fuera de alcance
r = run("""var out=['cual es tu color favorito','what is the weather tomorrow','dame la receta de tacos'].map(function(q){return window.__askPortfolio(q)===null;});
 document.title='PROBE '+JSON.stringify({out:out});""")
check("fuera de alcance -> sin match (3 casos)", r.get("out") == [True, True, True], r)

# sin peticiones de red del asistente + sin restos de AWS
r = run("""var calls=[]; var of=window.fetch; window.fetch=function(u){calls.push(String(u));return of.apply(this,arguments);};
 document.getElementById('ai-fab').click(); window.__askPortfolio('tell me about fidello');
 document.title='PROBE '+JSON.stringify({calls:calls, src:(document.documentElement.innerHTML.indexOf('vd4c00'+'py15')>-1)});""")
check("el asistente no hace fetch", r.get("calls") == [], r.get("calls"))
check("sin la URL del backend borrado (vd4c00py15) en el DOM", r.get("src") is False, r.get("src"))

# KB rota -> mensaje de contacto, sin excepción
r = run("""document.getElementById('ai-fab').click();
 var txt=document.getElementById('ai-msgs').textContent;
 document.title='PROBE '+JSON.stringify({greet:txt.indexOf('valentin.alducin88')>-1, err:window.__kbError||null});""",
        mutate=lambda t: re.sub(r'(<script type="application/json" id="assistant-kb">).*?(</script>)', r'[]', t, flags=re.S))
check("KB inválida -> CTA de contacto sin romper", r.get("greet") is True, r)

print("\n%d checks · %d PASS · %d FAIL" % (len(results), sum(results), len(results) - sum(results)))
raise SystemExit(0 if all(results) else 1)
