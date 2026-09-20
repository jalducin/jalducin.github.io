# -*- coding: utf-8 -*-
"""Probes headless del selector de idioma (tasks 6.1, 6.2, 6.4). Imprime PASS/FAIL por check."""
import io, os, re, subprocess, tempfile, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
CH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SRC = io.open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
results = []


def check(name, ok, detail=""):
    results.append(ok); print(("PASS  " if ok else "FAIL  ") + name + ("" if ok else "  -> " + str(detail)[:300]))


def run(pre_body="", probe_js="", url_suffix=""):
    html = SRC.replace("<body>", "<body>" + pre_body, 1).replace(
        "</body>", "<script>window.addEventListener('load',function(){setTimeout(function(){try{" + probe_js +
        "}catch(e){document.title='PROBE '+JSON.stringify({error:String(e)});}},500);});</script></body>")
    tmp = os.path.join(ROOT, "_probe_i18n.html")
    io.open(tmp, "w", encoding="utf-8", newline="").write(html)
    out = subprocess.run([CH, "--headless=new", "--disable-gpu", "--virtual-time-budget=6000",
                          "--user-data-dir=" + tempfile.mkdtemp(prefix="i18n_"), "--dump-dom",
                          "file:///" + tmp.replace("\\", "/") + url_suffix],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    os.remove(tmp)
    m = re.search(r"<title>PROBE (.*?)</title>", out.stdout or "", re.S)
    if not m:
        return {"error": "sin PROBE", "stderr": (out.stderr or "")[-300:]}
    import html as h
    return json.loads(h.unescape(m.group(1)))


# --- 6.1 carga con ?lang=es ---
r = run(probe_js="""
 var r={lang:document.documentElement.lang, nav:[].map.call(document.querySelectorAll('.nav-link'),function(a){return a.textContent}),
  h2:document.querySelector('#ai-method h2').textContent, levels:[].map.call(document.querySelectorAll('.level-title'),function(h){return h.textContent.trim()}),
  btn:document.getElementById('lang-btn').textContent, current:document.querySelector('.tl-badge').textContent, title:document.title,
  placeholder:document.getElementById('cf-name').getAttribute('placeholder'), headline:document.querySelector('header h3').textContent};
 document.title='PROBE '+JSON.stringify(r);""", url_suffix="?lang=es#experience")
check("?lang=es -> html.lang=es", r.get("lang") == "es", r)
check("nav en español", r.get("nav", [None])[1] == "Experiencia", r.get("nav"))
check("h2 AI Method en español", r.get("h2") == "Cómo construyo con IA", r.get("h2"))
check("niveles Dueño/Construyo/Opero/Aprendiendo", r.get("levels") == ["Dueño", "Construyo", "Opero", "Aprendiendo"], r.get("levels"))
check("botón muestra idioma destino EN", r.get("btn") == "EN", r.get("btn"))
check("badge Current -> Actual", r.get("current") == "Actual", r.get("current"))
check("placeholder formulario en español", r.get("placeholder") == "Tu nombre", r.get("placeholder"))
check("headline invariante", "SRE & Automation" in (r.get("headline") or ""), r.get("headline"))

# --- 6.1 restauración exacta EN y handlers tras 2 alternancias, conservando la tab ---
r = run(probe_js="""
 var sel=['#ai-method h2','#experience li[data-i18n="exp.li2"]','#featured-projects h3','.level-legend','#contact p'];
 var before=sel.map(function(q){return document.querySelector(q).innerHTML});
 window.__showTab('featured-projects');
 window.__setLang('es'); var esSample=document.querySelector('#featured-projects h3').textContent; window.__setLang('en'); window.__setLang('es'); window.__setLang('en');
 var after=sel.map(function(q){return document.querySelector(q).innerHTML});
 var active=document.querySelector('.nav-link.active').getAttribute('href');
 var r={same:JSON.stringify(before)===JSON.stringify(after), esSample:esSample, active:active, lang:document.documentElement.lang,
  showTab:typeof window.__showTab, dl:typeof window.__downloadCV, cv:document.querySelectorAll('a[data-cv]').length,
  term:!!document.getElementById('term-input'), form:!!document.getElementById('contactForm'), cmdk:!!document.getElementById('cmdkList'),
  stored:(function(){try{return localStorage.getItem('lang')}catch(e){return 'err'}})()};
 document.title='PROBE '+JSON.stringify(r);""", url_suffix="?lang=en")
check("EN restaurado byte a byte tras es/en/es/en", r.get("same") is True, r)
check("muestra ES aplicada (Fidello)", r.get("esSample") == "Fidello — Sistema de tarjetas de lealtad", r.get("esSample"))
check("tab activa conservada (#featured-projects)", r.get("active") == "#featured-projects", r.get("active"))
check("handlers intactos (__showTab, __downloadCV, 4 a[data-cv], terminal, form, palette)",
      r.get("showTab") == "function" and r.get("dl") == "function" and r.get("cv") == 4 and r.get("term") and r.get("form") and r.get("cmdk"), r)
check("preferencia persistida en localStorage", r.get("stored") == "en", r.get("stored"))

# --- 6.2 detección por navigator.language ---
r = run(pre_body="<script>Object.defineProperty(navigator,'language',{get:function(){return 'es-MX'}});try{localStorage.removeItem('lang')}catch(e){}</script>",
        probe_js="document.title='PROBE '+JSON.stringify({lang:document.documentElement.lang,h2:document.querySelector('#experience h2').textContent});")
check("navigator.language es-MX sin preferencia -> ES", r.get("lang") == "es" and r.get("h2") == "Experiencia", r)
r = run(pre_body="<script>Object.defineProperty(navigator,'language',{get:function(){return 'es-MX'}});try{localStorage.setItem('lang','en')}catch(e){}</script>",
        probe_js="document.title='PROBE '+JSON.stringify({lang:document.documentElement.lang});")
check("preferencia guardada EN gana a navigator es-MX", r.get("lang") == "en", r)
r = run(pre_body="<script>Object.defineProperty(navigator,'language',{get:function(){return 'en-US'}});try{localStorage.setItem('lang','en')}catch(e){}</script>",
        probe_js="document.title='PROBE '+JSON.stringify({lang:document.documentElement.lang});", url_suffix="?lang=es")
check("?lang=es gana a preferencia EN", r.get("lang") == "es", r)
# localStorage bloqueado
r = run(pre_body="<script>(function(){var real=window.localStorage;var fake={getItem:function(k){if(k==='lang')throw new Error('blocked');return real.getItem(k)},setItem:function(k,v){if(k==='lang')throw new Error('blocked');return real.setItem(k,v)},removeItem:function(k){return real.removeItem(k)}};Object.defineProperty(window,'localStorage',{get:function(){return fake}});})();window.__errs=[];window.addEventListener('error',function(e){window.__errs.push(String(e.message))});</script>",
        probe_js="window.__setLang('es');var ok=document.documentElement.lang==='es';window.__setLang('en');document.title='PROBE '+JSON.stringify({ok:ok&&document.documentElement.lang==='en',errs:window.__errs});")
check("localStorage bloqueado: toggle funciona y sin errores de consola", r.get("ok") is True and r.get("errs") == [], r)

# --- 6.4 terminal ---
r = run(probe_js="""
 window.__showTab('terminal'); var inp=document.getElementById('term-input'), out=document.getElementById('term-out');
 function cmd(c){inp.value=c; inp.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',bubbles:true}));}
 cmd('lang es'); var l1=document.documentElement.lang; cmd('lang'); cmd('lang xx'); cmd('help'); cmd('idioma en');
 var t=out.textContent; document.title='PROBE '+JSON.stringify({l1:l1, l2:document.documentElement.lang, hasEs:t.indexOf('Idioma: español')>-1, hasCur:t.indexOf('Idioma / language')>-1, hasErr:t.indexOf('Idioma no soportado: xx')>-1, help:t.indexOf('lang es|en')>-1});""")
check("terminal: lang es / lang / lang xx / help / idioma en", r.get("l1") == "es" and r.get("l2") == "en" and r.get("hasEs") and r.get("hasCur") and r.get("hasErr") and r.get("help"), r)

print("\n%d checks · %d PASS · %d FAIL" % (len(results), sum(results), len(results) - sum(results)))
raise SystemExit(0 if all(results) else 1)
