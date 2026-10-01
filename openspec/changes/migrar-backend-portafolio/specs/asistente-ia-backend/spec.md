# Capability: asistente-ia-backend (delta)

## REMOVED Requirements

### Requirement: Backend proxy al LLM con credencial protegida
**Reason**: El backend en AWS (Lambda `jalducin-assistant` + API Gateway + DynamoDB) fue borrado el 2026-10-01 y el dueño decidió no reemplazarlo: el asistente pasa a ser un bot de recuperación sin LLM que corre en el navegador (costo $0, sin API key).
**Migration**: Ver la capability `asistente-local-retrieval`. El contrato HTTP desaparece; el widget ya no hace `fetch`. `backend/assistant/` se retira del repo (queda en el historial y en el archivo de este cambio).

### Requirement: Grounding y manejo de fuera-de-alcance
**Reason**: El backend en AWS (Lambda `jalducin-assistant` + API Gateway + DynamoDB) fue borrado el 2026-10-01 y el dueño decidió no reemplazarlo: el asistente pasa a ser un bot de recuperación sin LLM que corre en el navegador (costo $0, sin API key).
**Migration**: Ver la capability `asistente-local-retrieval`. El contrato HTTP desaparece; el widget ya no hace `fetch`. `backend/assistant/` se retira del repo (queda en el historial y en el archivo de este cambio).

### Requirement: Controles de costo y abuso (cerca de tier-0)
**Reason**: El backend en AWS (Lambda `jalducin-assistant` + API Gateway + DynamoDB) fue borrado el 2026-10-01 y el dueño decidió no reemplazarlo: el asistente pasa a ser un bot de recuperación sin LLM que corre en el navegador (costo $0, sin API key).
**Migration**: Ver la capability `asistente-local-retrieval`. El contrato HTTP desaparece; el widget ya no hace `fetch`. `backend/assistant/` se retira del repo (queda en el historial y en el archivo de este cambio).

### Requirement: Sin RAG — el perfil cabe en contexto
**Reason**: El backend en AWS (Lambda `jalducin-assistant` + API Gateway + DynamoDB) fue borrado el 2026-10-01 y el dueño decidió no reemplazarlo: el asistente pasa a ser un bot de recuperación sin LLM que corre en el navegador (costo $0, sin API key).
**Migration**: Ver la capability `asistente-local-retrieval`. El contrato HTTP desaparece; el widget ya no hace `fetch`. `backend/assistant/` se retira del repo (queda en el historial y en el archivo de este cambio).

### Requirement: Caché de respuestas para ahorrar llamadas
**Reason**: El backend en AWS (Lambda `jalducin-assistant` + API Gateway + DynamoDB) fue borrado el 2026-10-01 y el dueño decidió no reemplazarlo: el asistente pasa a ser un bot de recuperación sin LLM que corre en el navegador (costo $0, sin API key).
**Migration**: Ver la capability `asistente-local-retrieval`. El contrato HTTP desaparece; el widget ya no hace `fetch`. `backend/assistant/` se retira del repo (queda en el historial y en el archivo de este cambio).

### Requirement: Rate limiting y tope global
**Reason**: El backend en AWS (Lambda `jalducin-assistant` + API Gateway + DynamoDB) fue borrado el 2026-10-01 y el dueño decidió no reemplazarlo: el asistente pasa a ser un bot de recuperación sin LLM que corre en el navegador (costo $0, sin API key).
**Migration**: Ver la capability `asistente-local-retrieval`. El contrato HTTP desaparece; el widget ya no hace `fetch`. `backend/assistant/` se retira del repo (queda en el historial y en el archivo de este cambio).

