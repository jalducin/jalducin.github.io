## ADDED Requirements

### Requirement: CI/CD del backend con flujo GitHub → AWS

El backend del asistente SHALL desplegarse mediante CI/CD siguiendo el principio **primero al repo
(GitHub), después a AWS**: un push a `main` dispara GitHub Actions, que despliega el Lambda. NO se sube
nada a AWS sin pasar antes por el repositorio.

#### Scenario: Deploy automático al hacer push
- **WHEN** se hace push a `main` con cambios en el código del backend (`backend/assistant/**`)
- **THEN** GitHub Actions empaqueta el código y actualiza la función Lambda (`update-function-code`)
- **AND** el orden es git → AWS (el commit existe en el repo antes de desplegarse)

#### Scenario: Autenticación sin llaves estáticas (OIDC)
- **WHEN** el workflow se autentica con AWS
- **THEN** usa OIDC (assume-role) con un rol de permisos mínimos (deploy del Lambda), sin llaves estáticas
  en GitHub
- **AND** la credencial del LLM (si aplica, Opción B) NO viaja por CI; se configura una sola vez en el Lambda

#### Scenario: Permiso mínimo del rol de CI
- **WHEN** se revisa la policy del rol de deploy
- **THEN** concede solo lo necesario (p. ej. `lambda:UpdateFunctionCode` sobre la función del asistente),
  sin permisos amplios
