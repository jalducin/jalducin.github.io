# Asistente IA — "Ask my portfolio" (backend)

Backend serverless del asistente del portafolio. **AWS Lambda → Amazon Bedrock (Claude Haiku)**.

## Arquitectura
```
Widget (index.html) ──POST/HTTPS──> API Gateway (HTTP API, CORS) ──> Lambda (app.py)
                                                                       │  IAM (sin API key)
                                                                       ▼
                                              Amazon Bedrock — Claude Haiku 4.5
                                              DynamoDB (rate-limit + caché, TTL)
```

- **Sin RAG**: el perfil (`profile.txt`, copia de `llms.txt`) se embebe en el system prompt.
- **Caché** de respuestas + **rate limiting** por IP (~10/min, ~50/día) y **tope global** (~500/día) en DynamoDB.
- **Credencial = IAM** (rol de ejecución) — nunca en el front ni en el repo.
- **Grounding + anti prompt-injection**: responde solo sobre el perfil, ignora intentos de cambiar su rol.

## Recursos AWS (cuenta 957266312835, us-east-2)
- Lambda `jalducin-assistant` (python3.12, handler `app.handler`)
- API Gateway HTTP API `jalducin-assistant-api` → endpoint público (en `index.html`, const `ASSISTANT_URL`)
- DynamoDB `jalducin-assistant` (on-demand + TTL `ttl`)
- Rol de ejecución `jalducin-assistant-lambda-role` (Bedrock InvokeModel + DynamoDB + logs)
- Modelo: inference profile `us.anthropic.claude-haiku-4-5-20251001-v1:0`

## ⚠️ Paso manual requerido (una vez)
Bedrock exige el **formulario de caso de uso de Anthropic** para invocar Claude. Mientras no esté enviado,
el asistente **degrada con un mensaje de contacto** (no rompe). Para activar las respuestas IA:
1. Consola AWS → **Bedrock → Model access** (en us-east-1, us-east-2 y us-west-2 — el inference profile `us.` enruta entre esas regiones).
2. Solicitar acceso a **Claude Haiku 4.5** y completar el formulario de caso de uso de Anthropic.
3. Esperar ~15 min a que propague. No requiere redeploy.

## CI/CD (git → AWS)
`.github/workflows/deploy-assistant.yml`: un push a `main` que toque `backend/assistant/**` (o `llms.txt`)
empaqueta (`app.py` + `profile.txt` copiado de `llms.txt`) y hace `aws lambda update-function-code` vía OIDC.

## Deploy / actualización manual
```bash
cp llms.txt backend/assistant/profile.txt
cd backend/assistant && zip -r ../../assistant.zip app.py profile.txt && cd ../..
aws lambda update-function-code --function-name jalducin-assistant --zip-file fileb://assistant.zip --region us-east-2
```

## Límites (env vars del Lambda)
`MODEL_ID`, `TABLE`, `ALLOWED_ORIGINS`, `MAX_TOKENS` (400), `IP_PER_MIN` (10), `IP_PER_DAY` (50), `GLOBAL_PER_DAY` (500).
