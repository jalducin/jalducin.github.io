"""Lambda de contacto del portafolio: valida el formulario y envía el mensaje por SES.

Entrada (JSON, API Gateway HTTP API v2):
    {"name","email","subject","message","website"}  (website = honeypot, debe ir vacío)
Salida: {"ok": true} en éxito; error con statusCode 4xx/5xx en caso contrario.
"""
import json
import os
import re

import boto3
from botocore.exceptions import ClientError

ses = boto3.client("ses")

TO_EMAIL = os.environ.get("TO_EMAIL", "valentin.alducin88@gmail.com")
FROM_EMAIL = os.environ.get("FROM_EMAIL", TO_EMAIL)
ALLOW_ORIGIN = os.environ.get("ALLOW_ORIGIN", "*")

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
CORS = {
    "Access-Control-Allow-Origin": ALLOW_ORIGIN,
    "Access-Control-Allow-Methods": "POST,OPTIONS",
    "Access-Control-Allow-Headers": "content-type",
}


def _resp(status: int, body: dict) -> dict:
    return {
        "statusCode": status,
        "headers": {"content-type": "application/json", **CORS},
        "body": json.dumps(body),
    }


def handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "POST")
    if method == "OPTIONS":
        return _resp(200, {"ok": True})

    try:
        data = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return _resp(400, {"error": "INVALID_JSON"})

    # Honeypot anti-spam: un bot rellena el campo oculto 'website' -> fingimos éxito y no enviamos.
    if (data.get("website") or "").strip():
        return _resp(200, {"ok": True})

    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()
    subject = (data.get("subject") or "Contacto").strip()

    if not name or not message or not EMAIL_RE.match(email):
        return _resp(422, {"error": "VALIDATION", "detail": "name, valid email and message are required"})
    if len(message) > 5000 or len(name) > 200:
        return _resp(422, {"error": "TOO_LONG"})

    try:
        ses.send_email(
            Source=FROM_EMAIL,
            Destination={"ToAddresses": [TO_EMAIL]},
            ReplyToAddresses=[email],
            Message={
                "Subject": {"Data": f"[Portfolio] {subject} — {name}"},
                "Body": {"Text": {"Data": f"{message}\n\n—\n{name} · {email}"}},
            },
        )
    except ClientError as exc:  # pragma: no cover
        print("SES error:", exc)
        return _resp(502, {"error": "SEND_FAILED"})

    return _resp(200, {"ok": True})
