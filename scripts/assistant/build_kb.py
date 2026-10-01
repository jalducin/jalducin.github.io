# -*- coding: utf-8 -*-
"""Compila assistant/knowledge.md -> <script type="application/json" id="assistant-kb"> en index.html.

Uso: python scripts/assistant/build_kb.py   (idempotente; falla si una entrada no tiene en/es)
Formato de knowledge.md:  ## <id> / tags: a, b, c / en: ... / es: ...
"""
import io, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(ROOT)
SRC = "assistant/knowledge.md"
P = "index.html"

md = io.open(SRC, encoding="utf-8").read()
entries, errors = [], []
for m in re.finditer(r"^## ([a-z0-9-]+)[ \t]*\n(.*?)(?=\n## |\Z)", md, re.S | re.M):
    eid, body = m.group(1), m.group(2)
    tags = re.search(r"^tags:\s*(.+)$", body, re.M)
    en = re.search(r"^en:\s*(.+)$", body, re.M)
    es = re.search(r"^es:\s*(.+)$", body, re.M)
    if not (tags and en and es):
        errors.append("%s: falta %s" % (eid, ", ".join(k for k, v in (("tags", tags), ("en", en), ("es", es)) if not v)))
        continue
    entries.append({
        "id": eid,
        "t": [t.strip().lower() for t in tags.group(1).split(",") if t.strip()],
        "en": en.group(1).strip(),
        "es": es.group(1).strip(),
    })

if errors:
    print("ERROR en %s:" % SRC); [print("  -", e) for e in errors]; sys.exit(1)
assert len(entries) >= 18, "se esperaban >= 18 entradas, hay %d" % len(entries)
ids = [e["id"] for e in entries]
assert len(ids) == len(set(ids)), "ids duplicados: %s" % [i for i in ids if ids.count(i) > 1]

block = '  <script type="application/json" id="assistant-kb">' + json.dumps(entries, ensure_ascii=False, separators=(",", ":")) + "</script>\n"
s = io.open(P, encoding="utf-8").read()
if re.search(r'  <script type="application/json" id="assistant-kb">.*?</script>\n', s, re.S):
    s = re.sub(r'  <script type="application/json" id="assistant-kb">.*?</script>\n', block, s, flags=re.S)
else:
    anchor = '  <script type="application/json" id="i18n-es">'
    assert anchor in s, "no se encontró el ancla del diccionario i18n"
    s = s.replace(anchor, block + anchor, 1)
io.open(P, "w", encoding="utf-8", newline="").write(s)
print("index.html OK | entradas: %d | tags: %d | bytes KB: %d" % (len(entries), sum(len(e["t"]) for e in entries), len(block)))
