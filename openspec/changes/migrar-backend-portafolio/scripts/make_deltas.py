# -*- coding: utf-8 -*-
"""Genera los delta specs MODIFIED/REMOVED copiando los bloques completos de openspec/specs."""
import io, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
os.chdir(ROOT)
CH = "openspec/changes/migrar-backend-portafolio"


def block(cap, name):
    s = io.open("openspec/specs/%s/spec.md" % cap, encoding="utf-8").read()
    m = re.search(r"(### Requirement: %s\n.*?)(?=\n### Requirement: |\Z)" % re.escape(name), s, re.S)
    assert m, (cap, name)
    return m.group(1).rstrip() + "\n"


def names(cap):
    s = io.open("openspec/specs/%s/spec.md" % cap, encoding="utf-8").read()
    return re.findall(r"### Requirement: (.+)", s)


def write(cap, body):
    os.makedirs("%s/specs/%s" % (CH, cap), exist_ok=True)
    io.open("%s/specs/%s/spec.md" % (CH, cap), "w", encoding="utf-8", newline="").write(body)
    print("delta", cap)


# --- MODIFIED: el widget ya no llama a un backend ---
b = block("asistente-ia-chat-widget", 'Widget de chat "Ask my portfolio" en el sitio')
reps = [
    ("El sitio SHALL incluir un widget de chat (vanilla JS, sin frameworks) que permita preguntar sobre el perfil\ny muestre las respuestas del backend. MUST respetar la paleta, ser responsive (992/768/480px) y accesible.",
     "El sitio SHALL incluir un widget de chat (vanilla JS, sin frameworks) que permita preguntar sobre el perfil\ny muestre las respuestas resueltas **localmente** por `asistente-local-retrieval` (sin backend ni LLM).\nMUST respetar la paleta, ser responsive (992/768/480px) y accesible."),
    ("- **THEN** el front hace `fetch` al endpoint del backend y muestra la respuesta en el hilo del chat\n- **AND** muestra estado de carga mientras espera y permite enviar con Enter",
     "- **THEN** el front resuelve la respuesta contra la base de conocimiento embebida y la muestra en el hilo del chat\n- **AND** muestra un estado breve de “escribiendo…” y permite enviar con Enter"),
    ("#### Scenario: Degradación si el backend no responde\n- **WHEN** el endpoint falla o no está disponible\n- **THEN** el widget muestra un mensaje claro y CTAs de contacto (email/LinkedIn), sin romper la página",
     "#### Scenario: Degradación cuando no hay respuesta en la base\n- **WHEN** la pregunta no tiene coincidencia suficiente en la base de conocimiento\n- **THEN** el widget lo dice con honestidad, sugiere temas y muestra CTAs de contacto (email/LinkedIn), sin romper la página\n- **AND** si el bloque `#assistant-kb` faltara o fuese inválido, el widget muestra el mensaje de contacto en vez de fallar"),
    ("#### Scenario: La credencial nunca está en el front\n- **WHEN** se inspecciona el JS del widget\n- **THEN** solo contiene la URL del endpoint; ninguna API key ni secreto",
     "#### Scenario: Sin credenciales ni endpoints en el front\n- **WHEN** se inspecciona el JS del widget\n- **THEN** no contiene API keys, secretos ni URL de backend del asistente (la resolución es local)"),
]
for o, n in reps:
    assert o in b, o[:50]
    b = b.replace(o, n)
write("asistente-ia-chat-widget", "# Capability: asistente-ia-chat-widget (delta)\n\n## MODIFIED Requirements\n\n" + b)

# --- REMOVED: backend del asistente y su CI ---
REASON_BK = ("**Reason**: El backend en AWS (Lambda `jalducin-assistant` + API Gateway + DynamoDB) fue borrado el "
             "2026-10-01 y el dueño decidió no reemplazarlo: el asistente pasa a ser un bot de recuperación sin LLM "
             "que corre en el navegador (costo $0, sin API key).\n"
             "**Migration**: Ver la capability `asistente-local-retrieval`. El contrato HTTP desaparece; el widget ya no "
             "hace `fetch`. `backend/assistant/` se retira del repo (queda en el historial y en el archivo de este cambio).\n")
REASON_CI = ("**Reason**: Ya no existe Lambda del asistente que desplegar; el conocimiento se compila en `index.html` "
             "desde `assistant/knowledge.md` y viaja con el deploy estático del sitio.\n"
             "**Migration**: `.github/workflows/deploy-assistant.yml` se elimina. El único despliegue de backend que queda "
             "es el de la Edge Function de contacto (`contacto-backend-supabase`).\n")
for cap, reason in (("asistente-ia-backend", REASON_BK), ("cicd-asistente-aws", REASON_CI)):
    body = "# Capability: %s (delta)\n\n## REMOVED Requirements\n\n" % cap
    for n in names(cap):
        body += "### Requirement: %s\n%s\n" % (n, reason)
    write(cap, body)
