# Capability: cicd-asistente-aws (delta)

## REMOVED Requirements

### Requirement: CI/CD del backend con flujo GitHub → AWS
**Reason**: Ya no existe Lambda del asistente que desplegar; el conocimiento se compila en `index.html` desde `assistant/knowledge.md` y viaja con el deploy estático del sitio.
**Migration**: `.github/workflows/deploy-assistant.yml` se elimina. El único despliegue de backend que queda es el de la Edge Function de contacto (`contacto-backend-supabase`).

