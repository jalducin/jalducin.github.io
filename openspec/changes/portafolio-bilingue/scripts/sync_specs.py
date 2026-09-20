# -*- coding: utf-8 -*-
"""Sincroniza los delta specs de este cambio con openspec/specs/ (equivalente manual de /opsx:sync).
ADDED  -> se agregan al final del spec principal (o se crea el archivo si la capability es nueva).
MODIFIED -> se reemplaza el bloque completo del requirement homónimo en el spec principal.
"""
import io, os, re, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
CHANGE = os.path.join(ROOT, "openspec", "changes", "portafolio-bilingue", "specs")
MAIN = os.path.join(ROOT, "openspec", "specs")

REQ_RE = re.compile(r"(### Requirement: [^\n]+\n.*?)(?=\n### Requirement: |\n## |\Z)", re.S)


def split_sections(text):
    """Devuelve {'ADDED': [(name, block)], 'MODIFIED': [...]} a partir de un delta."""
    out = {"ADDED": [], "MODIFIED": []}
    for m in re.finditer(r"## (ADDED|MODIFIED) Requirements\n(.*?)(?=\n## |\Z)", text, re.S):
        kind, body = m.group(1), m.group(2)
        for r in REQ_RE.finditer(body.strip() + "\n"):
            block = r.group(1).rstrip() + "\n"
            name = re.match(r"### Requirement: (.+)", block).group(1).strip()
            out[kind].append((name, block))
    return out


for delta_path in sorted(glob.glob(os.path.join(CHANGE, "*", "spec.md"))):
    cap = os.path.basename(os.path.dirname(delta_path))
    delta = io.open(delta_path, encoding="utf-8").read()
    secs = split_sections(delta)
    main_path = os.path.join(MAIN, cap, "spec.md")
    if not os.path.exists(main_path):
        os.makedirs(os.path.dirname(main_path), exist_ok=True)
        body = "# Capability: %s\n\n## Requirements\n\n" % cap + "\n".join(b for _, b in secs["ADDED"])
        io.open(main_path, "w", encoding="utf-8", newline="").write(body)
        print("CREADO   ", cap, "(%d requirements)" % len(secs["ADDED"]))
        continue
    main = io.open(main_path, encoding="utf-8").read()
    for name, block in secs["MODIFIED"]:
        pat = re.compile(r"### Requirement: %s\n.*?(?=\n### Requirement: |\Z)" % re.escape(name), re.S)
        assert pat.search(main), "%s: requirement no encontrado -> %s" % (cap, name)
        main = pat.sub(lambda _m: block.rstrip() + "\n", main, count=1)
    for name, block in secs["ADDED"]:
        if ("### Requirement: %s" % name) in main:
            continue
        main = main.rstrip() + "\n\n" + block
    io.open(main_path, "w", encoding="utf-8", newline="").write(main)
    print("ACTUALIZADO", cap, "(mod %d, add %d)" % (len(secs["MODIFIED"]), len(secs["ADDED"])))
