# -*- coding: utf-8 -*-
"""Marca los elementos traducibles de index.html con data-i18n="<seccion>.<tag><n>" (design.md D2) y
extrae scripts/en.json con {clave: innerHTML EN}. Idempotente: si un elemento ya tiene data-i18n, lo respeta.
Uso: python mark_i18n.py            (desde cualquier cwd)
"""
import io, json, os, re
from html.parser import HTMLParser

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
P = os.path.join(ROOT, "index.html")
OUT = os.path.join(os.path.dirname(__file__), "en.json")
VOID = {"img", "input", "br", "hr", "meta", "link", "source", "wbr", "area", "base", "col", "embed", "param", "track"}
SECTION_CODES = {"ai-method": "aim", "experience": "exp", "featured-projects": "proj", "writing": "wri",
                 "hard-skills": "skl", "soft-skills": "soft", "languages": "lang", "education": "edu",
                 "contact": "con", "terminal": "term"}
# atributos traducibles: (tag, id) -> lista de atributos
ATTR_TARGETS = {"title", "aria-label", "placeholder"}


def classes(attrs):
    return set((dict(attrs).get("class") or "").split())


class Marker(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src
        self.line_starts = [0]
        for i, ch in enumerate(src):
            if ch == "\n":
                self.line_starts.append(i + 1)
        self.stack = []          # [tag, attrs, start_off, start_len, targeted(bool), key]
        self.sec = "top"
        self.counters = {}
        self.found = []          # (start_off, start_len, end_off, key, tag)
        self.attr_found = []     # (start_off, start_len, key, attrs_to_mark)
        self.in_script = 0

    def off(self):
        l, c = self.getpos()
        return self.line_starts[l - 1] + c

    def key_for(self, tag):
        k = (self.sec, tag)
        self.counters[k] = self.counters.get(k, 0) + 1
        return "%s.%s%d" % (self.sec, tag, self.counters[k])

    def parent_has(self, cls):
        return any(cls in classes(a) for _, a, *_ in self.stack)

    def parent_tag(self, tag):
        return any(t == tag for t, *_ in self.stack)

    def targeted(self, tag, attrs):
        a = dict(attrs); cl = classes(attrs); id_ = a.get("id", "")
        if "data-i18n" in a or self.in_script:
            return False
        if tag == "h2":
            return True
        if tag == "h3":
            return self.sec != "top"                      # excluye el headline del header
        if tag == "p":
            return True
        if tag == "li":
            if self.parent_has("nav-list"):
                return False
            if self.parent_has("level-build") or self.parent_has("level-operate"):
                return False                               # tecnologías: invariantes
            return True
        if tag == "span":
            return bool(cl & {"metric", "tl-date", "tl-badge", "card-badge", "btn"})
        if tag == "div":
            return bool(cl & {"card-badge", "form-success", "cmdk-hint"})
        if tag == "a":
            return "nav-link" in cl or "btn" in cl
        if tag == "button":
            return id_ in {"copyEmail", "ai-fab"} or a.get("type") == "submit"
        if tag == "td":
            return True
        if tag == "footer":
            return True
        if tag == "b":
            return self.parent_has("ai-head")
        if tag == "strong":
            # solo los títulos sueltos de las now-cards ("Now", "How I work"): strong hijo directo de .now-card
            return bool(self.stack) and "now-card" in classes(self.stack[-1][1])
        return False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.in_script += 1
        a = dict(attrs)
        if tag == "section" and a.get("id") in SECTION_CODES:
            self.sec = SECTION_CODES[a["id"]]
        elif tag == "nav":
            self.sec = "nav"
        elif tag == "header":
            self.sec = "hdr"
        elif tag == "footer":
            self.sec = "ftr"
        elif tag == "div" and a.get("id") in ("ai-panel",):
            self.sec = "ai"
        elif tag == "button" and a.get("id") == "ai-fab":
            self.sec = "ai"
        elif tag == "div" and "cmdk-overlay" in classes(attrs):
            self.sec = "cmdk"
        start = self.off(); raw = self.get_starttag_text(); n = len(raw)
        # atributos traducibles (title/aria-label/placeholder) en cualquier elemento, salvo enlaces al CV (ya bilingües)
        attrs_to_mark = [k for k in ATTR_TARGETS if k in a and not a.get("data-cv") and not self.in_script and tag != "script"]
        if attrs_to_mark:
            self.attr_found.append((start, n, self.key_for(tag), attrs_to_mark))
        if tag in VOID:
            return
        t = self.targeted(tag, attrs)
        self.stack.append([tag, attrs, start, n, t, self.key_for(tag) if t else None])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.in_script -= 1
        # cerrar hasta el tag correspondiente (tolerante a etiquetas sin cerrar)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                el = self.stack[i]
                if el[4]:
                    self.found.append((el[2], el[3], self.off(), el[5], tag))
                del self.stack[i:]
                break
        if tag == "nav" or tag == "header" or tag == "footer" or tag == "section":
            self.sec = "top"
        if tag == "div" and self.sec in ("ai", "cmdk") and not any(t == "div" for t, *_ in self.stack):
            self.sec = "top"


src = io.open(P, encoding="utf-8").read()
m = Marker(src); m.feed(src)
en = {}
edits = []   # (offset_before_gt, text_to_insert)
for start, n, end, key, tag in m.found:
    en[key] = src[start + n:end]
    edits.append((start + n - 1, ' data-i18n="%s"' % key))
for start, n, key, attrs_to_mark in m.attr_found:
    raw = src[start:start + n]; a = dict(re.findall(r'([a-zA-Z-]+)="([^"]*)"', raw))
    ins = ""
    for at in attrs_to_mark:
        short = {"title": "title", "aria-label": "aria", "placeholder": "placeholder"}[at]
        en["%s@%s" % (key, short)] = a[at]
        ins += ' data-i18n-%s="%s@%s"' % (short, key, short)
    edits.append((start + n - 1, ins))
# aplicar de atrás hacia adelante
out = src
for pos, text in sorted(edits, key=lambda e: e[0], reverse=True):
    # tolerar "/>": insertar antes de la barra
    p = pos
    if out[p - 1] == "/":
        p -= 1
    out = out[:p] + text + out[p:]
io.open(P, "w", encoding="utf-8", newline="").write(out)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(json.dumps(en, ensure_ascii=False, indent=1))
print("elementos marcados:", len(m.found), "| atributos:", sum(len(x[3]) for x in m.attr_found), "| claves:", len(en))
