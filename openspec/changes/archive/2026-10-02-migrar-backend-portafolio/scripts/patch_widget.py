# -*- coding: utf-8 -*-
"""Reemplaza el widget del asistente: de fetch a un backend -> recuperación local sobre #assistant-kb (D1)."""
import io, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
os.chdir(ROOT)
P = "index.html"
s = io.open(P, encoding="utf-8").read()

OLD_START = '    /* Ask my portfolio — AI assistant widget */\n    (function(){\n      const ASSISTANT_URL='
assert OLD_START in s, "no se encontró el widget"
start = s.index(OLD_START)
end = s.index("    })();\n", s.index("document.addEventListener('keydown',(e)=>{if(e.key==='Escape'&&panel.classList.contains('open'))closePanel();});", start)) + len("    })();\n")

NEW = r'''    /* Ask my portfolio — bot de recuperación local (sin LLM ni backend; base en #assistant-kb) */
    (function(){
      const fab=document.getElementById('ai-fab');
      const panel=document.getElementById('ai-panel');
      const closeBtn=document.getElementById('ai-x');
      const msgs=document.getElementById('ai-msgs');
      const chipsEl=document.getElementById('ai-chips');
      const form=document.getElementById('ai-form');
      const input=document.getElementById('ai-input');
      const sendBtn=document.getElementById('ai-send');
      if(!fab||!panel)return;
      var KB=[]; try{KB=JSON.parse(document.getElementById('assistant-kb').textContent)||[];}catch(e){KB=[];}
      const L=()=>(window.__getLang&&window.__getLang()==='es')?'es':'en';
      const T={
        greet:{en:"Hi! I'm Juan's assistant. Ask me about his experience, stack or projects.",
               es:"¡Hola! Soy el asistente de Juan. Pregúntame sobre su experiencia, stack o proyectos."},
        none:{en:"I can only answer about Juan's profile — experience, stack, projects, education or contact. Try one of the suggestions, or write to him: valentin.alducin88@gmail.com",
              es:"Solo puedo responder sobre el perfil de Juan: experiencia, stack, proyectos, educación o contacto. Prueba una de las sugerencias, o escríbele: valentin.alducin88@gmail.com"},
        broken:{en:"The assistant isn't available right now. Write to Juan: valentin.alducin88@gmail.com or LinkedIn.",
                es:"El asistente no está disponible ahora. Escríbele a Juan: valentin.alducin88@gmail.com o LinkedIn."},
        limit:{en:"That's a good start — to keep going, write to him: valentin.alducin88@gmail.com or LinkedIn.",
               es:"Buen comienzo — para seguir, escríbele directo: valentin.alducin88@gmail.com o LinkedIn."},
        chips:{en:["AWS & serverless experience?","Tell me about Fidello","Backend stack?","What is SDD?"],
               es:["¿Experiencia en AWS y serverless?","Cuéntame de Fidello","¿Stack de backend?","¿Qué es SDD?"]}
      };
      const norm=t=>(t||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9ñ\s]/g,' ').replace(/\s+/g,' ').trim();
      const STOP=new Set(['que','cual','cuales','como','donde','cuando','quien','para','por','con','una','uno','los','las','del','sus','sobre','tiene','tienes','su','el','la','de','en','y','o','a','is','are','the','what','which','how','where','who','does','do','his','her','your','you','about','tell','me','and','or','of','in','on','for','to','with','can']);
      function tokens(t){return norm(t).split(' ').filter(w=>w.length>2&&!STOP.has(w));}
      function best(q){
        const nq=' '+norm(q)+' ', toks=tokens(q); if(!toks.length||!KB.length)return null;
        let top=null, topScore=0;
        KB.forEach(function(e){
          let sc=0;
          (e.t||[]).forEach(function(tag){ if(tag&&nq.indexOf(' '+norm(tag)+' ')>-1) sc+=3*Math.min(norm(tag).split(' ').length,3); });
          const body=' '+norm((e.en||'')+' '+(e.es||''))+' ';
          toks.forEach(function(w){ if(body.indexOf(' '+w)>-1) sc+=1; });
          if(sc>topScore){topScore=sc;top=e;}
        });
        return topScore>=3?top:null;
      }
      const MAX_TURNS=10; let turns=0, greeted=false;
      function add(text,cls){const d=document.createElement('div');d.className='ai-msg '+cls;d.textContent=text;msgs.appendChild(d);msgs.scrollTop=msgs.scrollHeight;return d;}
      function renderChips(){chipsEl.innerHTML='';T.chips[L()].forEach(function(q){const b=document.createElement('button');b.className='ai-chip';b.type='button';b.textContent=q;b.addEventListener('click',function(){ask(q);});chipsEl.appendChild(b);});}
      function openPanel(){panel.classList.add('open');if(!greeted){add(KB.length?T.greet[L()]:T.broken[L()],'a');renderChips();greeted=true;}setTimeout(function(){input.focus();},60);}
      function closePanel(){panel.classList.remove('open');}
      function ask(q){
        q=(q||'').trim(); if(!q)return;
        input.value=''; add(q,'u');
        if(!KB.length){add(T.broken[L()],'a');return;}
        if(turns>=MAX_TURNS){add(T.limit[L()],'sys');return;}
        const t=add('…','a typing');
        setTimeout(function(){
          const hit=best(q); t.remove();
          add(hit?(hit[L()]||hit.en):T.none[L()],'a');
          if(!hit)renderChips();
          turns++; input.focus();
        },120);
      }
      window.__askPortfolio=function(q){return (function(h){return h?h[L()]:null;})(best(q));};
      fab.addEventListener('click',function(){panel.classList.contains('open')?closePanel():openPanel();});
      closeBtn.addEventListener('click',closePanel);
      form.addEventListener('submit',function(e){e.preventDefault();ask(input.value);});
      document.addEventListener('keydown',function(e){if(e.key==='Escape'&&panel.classList.contains('open'))closePanel();});
    })();
'''
s = s[:start] + NEW + s[end:]
io.open(P, "w", encoding="utf-8", newline="").write(s)
assert "ASSISTANT_URL" not in s and "vd4c00py15" not in s
print("widget local OK | bytes:", len(s.encode("utf-8")))
