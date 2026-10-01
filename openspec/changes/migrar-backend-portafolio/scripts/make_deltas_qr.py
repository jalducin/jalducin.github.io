# -*- coding: utf-8 -*-
"""Delta de qr-apunta-al-sitio-aws: el QR pasa de CloudFront (borrado) a GitHub Pages."""
import io, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
os.chdir(ROOT)
CAP = "qr-apunta-al-sitio-aws"
s = io.open("openspec/specs/%s/spec.md" % CAP, encoding="utf-8").read()


def block(name):
    m = re.search(r"(### Requirement: %s\n.*?)(?=\n### Requirement: |\Z)" % re.escape(name), s, re.S)
    assert m, name
    return m.group(1).rstrip() + "\n"


b = block("El QR apunta al sitio en AWS conservando el estilo")
reps = [
    ("El código QR del CV (`assets/img/QR.png`) SHALL codificar la URL del **sitio en AWS** (la distribución\nCloudFront, p. ej. `https://d3r3bnavnwzqaw.cloudfront.net`, o el dominio canónico vigente), en lugar del\nrepositorio.",
     "El código QR del CV (`assets/img/QR.png`) SHALL codificar la **URL canónica del sitio**,\n`https://jalducin.github.io` (GitHub Pages), en lugar del repositorio o de un hosting dado de baja. Si en el\nfuturo hay dominio propio, el QR se regenera para apuntar a ese dominio."),
    ("#### Scenario: Escanear el QR abre el sitio en AWS\n- **WHEN** alguien escanea el QR del CV\n- **THEN** se abre la URL del sitio en AWS (CloudFront / dominio canónico), no la del repositorio de GitHub",
     "#### Scenario: Escanear el QR abre el sitio publicado\n- **WHEN** alguien escanea el QR del CV\n- **THEN** se abre `https://jalducin.github.io`, no el repositorio de GitHub ni una URL dada de baja\n- **AND** la URL codificada se verifica decodificando la imagen (p. ej. `cv2.QRCodeDetector`) tras cada regeneración"),
]
for o, n in reps:
    assert o in b, o[:60]
    b = b.replace(o, n)

body = "# Capability: %s (delta)\n\n## MODIFIED Requirements\n\n%s\n" % (CAP, b)
out = "openspec/changes/migrar-backend-portafolio/specs/%s" % CAP
os.makedirs(out, exist_ok=True)
io.open(out + "/spec.md", "w", encoding="utf-8", newline="").write(body)
print("delta", CAP)
