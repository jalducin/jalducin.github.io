## Why

El portafolio ya está en AWS (S3+CloudFront, tier-0) con CI/CD. Falta la capability estrella **agentic**:
un asistente IA "Ask my portfolio" que responda preguntas sobre el perfil de Juan. Es la prueba viva de su
posicionamiento AI-native (no lo dice, lo demuestra). Implementarlo requiere un backend (la API key/permisos
del LLM NO pueden vivir en el front estático), por eso se especifica antes de codificar (spec-driven).

## What Changes

- **Backend serverless**: AWS Lambda (Function URL, HTTPS) que actúa de proxy al LLM (Claude). La
  credencial del modelo vive solo en el backend, nunca en el front.
- **Base de conocimiento**: el contexto del asistente es el perfil del sitio (`llms.txt`), para responder
  fiel y sin inventar.
- **Widget de chat**: UI vanilla JS en `index.html` (burbuja), llama al Function URL por `fetch`.
- **CI/CD GitHub → AWS**: el despliegue del backend sigue el mismo principio que el sitio —
  **primero al repo (GitHub), después a AWS** vía GitHub Actions con OIDC (sin llaves estáticas).
- Controles de costo/abuso para mantenerse en/junto a tier-0 (concurrencia reservada, max_tokens, caché).

## Capabilities

### New Capabilities
- `asistente-ia-backend`: Lambda proxy al LLM, con la credencial solo en el backend, grounding en `llms.txt`,
  y controles de costo/abuso.
- `asistente-ia-chat-widget`: widget de chat en el sitio (vanilla, accesible, responsive) que consume el backend.
- `cicd-asistente-aws`: pipeline GitHub Actions (OIDC) que despliega el Lambda — flujo git → AWS.
- `qr-apunta-al-sitio-aws`: el QR del CV apunta al sitio en AWS (CloudFront/dominio) conservando el estilo JVAV.

### Modified Capabilities
- `asistente-ia-portafolio` (en `mejoras-portafolio-ai-native`, aún no archivada): este cambio la concreta e
  implementa. Al archivar, consolidar para que no haya duplicación de requisitos.

## Impact

- **AWS**: 1 función Lambda + Function URL (us-east-2), rol de ejecución, y (según decisión) acceso a
  **Amazon Bedrock** (Claude por IAM, sin key externa) **o** una **API key de Anthropic** en variable de
  entorno del Lambda. Rol de CI/CD extendido con permisos de deploy de Lambda.
- **Repo**: carpeta del backend (`backend/assistant/`), workflow `.github/workflows/deploy-assistant.yml`,
  widget en `index.html`, docs.
- **Costo**: Lambda dentro de free tier (~$0 de cómputo). El costo real son los **tokens del LLM**
  (Bedrock → factura AWS, cubierta por budgets; o Anthropic → factura aparte). Mitigado con Haiku + límites.
- **Seguridad**: credencial nunca en el front ni en el repo; CORS acotado a los orígenes del sitio.
