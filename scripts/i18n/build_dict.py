# -*- coding: utf-8 -*-
"""Inyecta en index.html: diccionario ES (JSON embebido), botón de idioma, runtime i18n, acción en la
command palette y comandos de terminal. Idempotente: reemplaza los bloques marcados si ya existen."""
import io, json, os, re, sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
from es import ES, INVARIANTES, TITLES  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
P = os.path.join(ROOT, "index.html")
s = io.open(P, encoding="utf-8").read()


def rep(old, new, must=True):
    global s
    if old not in s:
        assert not must, "no encontrado: " + old[:70]
        return
    assert s.count(old) == 1, "ambiguo: " + old[:70]
    s = s.replace(old, new)


# ---- 1. diccionario JSON (antes del script de descarga del CV) ----
en_keys = set(re.findall(r'data-i18n(?:-title|-aria|-placeholder)?="([^"]+)"', s))
orphans = sorted(set(ES) - en_keys)
assert not orphans, "claves ES huérfanas: %s" % orphans
untranslated = sorted(en_keys - set(ES))
unexpected = sorted(set(untranslated) - INVARIANTES)
assert not unexpected, "claves sin traducción no declaradas invariantes: %s" % unexpected
json_block = ('  <script type="application/json" id="i18n-es">' + json.dumps(ES, ensure_ascii=False, separators=(",", ":"))
              + "</script>\n")
s = re.sub(r'  <script type="application/json" id="i18n-es">.*?</script>\n', "", s, flags=re.S)
anchor = "  <script>\n    (function(){\n      const cv=document.getElementById('matrix-bg');"
assert anchor in s
s = s.replace(anchor, json_block + anchor, 1)

# ---- 2. botón de idioma en la nav + CSS ----
# hijo directo de <nav> (fuera del <ul>): así queda visible en la barra también en móvil (spec navegacion-por-secciones)
if 'id="lang-btn"' not in s: rep('    </ul>\n  </nav>',
    '    </ul>\n    <button id="lang-btn" type="button" aria-label="Cambiar idioma / Switch language" title="Español / English" lang="es">ES</button>\n  </nav>')
if '#lang-btn{' not in s: rep("    #theme-btn:hover{background:var(--border);}",
    "    #theme-btn:hover{background:var(--border);}\n"
    "    #lang-btn{background:none;border:1px solid var(--border);border-radius:6px;padding:.5rem .75rem;margin-left:.5rem;cursor:pointer;font-size:.85rem;font-weight:700;letter-spacing:.06em;color:var(--primary);font-family:'Courier New',Courier,monospace;transition:background .3s;}\n"
    "    #lang-btn:hover{background:var(--border);}")
if '#lang-btn{position:absolute' not in s: rep("      .burger{display:flex;}\n",
    "      .burger{display:flex;}\n      nav{flex-wrap:wrap;justify-content:flex-start;} #lang-btn{position:absolute;right:1rem;top:.75rem;margin:0;} /* idioma visible en la barra en móvil */\n")

# ---- 3. runtime i18n (antes de las tabs, para evitar parpadeo) ----
runtime = """    /* i18n ES/EN — el inglés vive en el DOM (fuente de verdad); el español en #i18n-es (design.md D3) */
    (function(){
      var ES={}; try{ES=JSON.parse(document.getElementById('i18n-es').textContent);}catch(e){}
      var TITLES=%s;
      var ATTRS={title:'title',aria:'aria-label',placeholder:'placeholder'};
      var EN={}; document.querySelectorAll('[data-i18n]').forEach(function(el){EN[el.dataset.i18n]=el.innerHTML;});
      Object.keys(ATTRS).forEach(function(k){document.querySelectorAll('[data-i18n-'+k+']').forEach(function(el){EN[el.getAttribute('data-i18n-'+k)]=el.getAttribute(ATTRS[k])||'';});});
      var store={get:function(){try{return localStorage.getItem('lang');}catch(e){return null;}},set:function(v){try{localStorage.setItem('lang',v);}catch(e){}}};
      var current='en';
      function applyLang(lang){
        lang=(lang==='es')?'es':'en'; current=lang;
        document.querySelectorAll('[data-i18n]').forEach(function(el){var k=el.dataset.i18n; var v=(lang==='es'&&ES[k]!==undefined)?ES[k]:EN[k]; if(v!==undefined&&el.innerHTML!==v)el.innerHTML=v;});
        Object.keys(ATTRS).forEach(function(k){document.querySelectorAll('[data-i18n-'+k+']').forEach(function(el){var key=el.getAttribute('data-i18n-'+k); var v=(lang==='es'&&ES[key]!==undefined)?ES[key]:EN[key]; if(v!==undefined)el.setAttribute(ATTRS[k],v);});});
        document.documentElement.lang=lang; document.title=TITLES[lang]||document.title;
        var b=document.getElementById('lang-btn'); if(b){b.textContent=lang==='es'?'EN':'ES'; b.setAttribute('lang',lang==='es'?'en':'es');}
        store.set(lang);
      }
      var q=null; try{q=new URLSearchParams(location.search).get('lang');}catch(e){}
      var initial=(q==='es'||q==='en')?q:(store.get()||((navigator.language||'').toLowerCase().indexOf('es')===0?'es':'en'));
      applyLang(initial);
      window.__setLang=applyLang; window.__getLang=function(){return current;};
      var btn=document.getElementById('lang-btn'); if(btn)btn.addEventListener('click',function(){applyLang(current==='es'?'en':'es');});
    })();
""" % json.dumps(TITLES, ensure_ascii=False)
s = re.sub(r"    /\* i18n ES/EN — .*?\n    \}\)\(\);\n", "", s, flags=re.S)
rep("    /* Tabs (una sección a la vez) + Terminal interactiva */\n    (function(){",
    runtime + "    /* Tabs (una sección a la vez) + Terminal interactiva */\n    (function(){")

# ---- 4. command palette ----
rep("        {label:'Toggle theme',tag:'action',run:()=>{const l=document.documentElement.classList.toggle('light');localStorage.setItem('theme',l?'light':'dark');}}\n      ];",
    "        {label:'Toggle theme',tag:'action',run:()=>{const l=document.documentElement.classList.toggle('light');localStorage.setItem('theme',l?'light':'dark');}},\n"
    "        {label:'Español / English',tag:'action',run:()=>window.__setLang&&window.__setLang(window.__getLang()==='es'?'en':'es')}\n      ];", must=False)

# ---- 5. terminal: lang / idioma ----
rep('''          help:()=>"Comandos: whoami · ls projects · writing · cat cv · skills · contact · sdd · clear · help\\nTip: hay un par de secretos por ahí… (prueba 'mundial')",''',
    '''          help:()=>"Comandos: whoami · ls projects · writing · cat cv · skills · contact · sdd · lang es|en · clear · help\\nTip: hay un par de secretos por ahí… (prueba 'mundial')",
          lang:()=>"Idioma / language: "+(window.__getLang&&window.__getLang()==='es'?'español':'english')+"   (usa 'lang es' o 'lang en')",
          'lang es':()=>{window.__setLang&&window.__setLang('es'); return "Idioma: español 🇲🇽";},
          'lang en':()=>{window.__setLang&&window.__setLang('en'); return "Language: english 🇺🇸";},
          idioma:()=>CMDS.lang(), 'idioma es':()=>CMDS['lang es'](), 'idioma en':()=>CMDS['lang en'](),''', must=False)
if 'Idioma no soportado' not in s: rep('''          else line("command not found: "+cmd+"   (prueba 'help')",'resp');''',
    '''          else if(/^(lang|idioma)\\s/.test(cmd.toLowerCase())) line("Idioma no soportado: "+cmd.split(/\\s+/)[1]+"   (usa 'lang es' o 'lang en')",'resp');
          else line("command not found: "+cmd+"   (prueba 'help')",'resp');''', must=False)

io.open(P, "w", encoding="utf-8", newline="").write(s)
print("index.html OK | claves ES:", len(ES), "| invariantes (sin traducción):", len(untranslated), "| bytes:", len(s.encode("utf-8")))
