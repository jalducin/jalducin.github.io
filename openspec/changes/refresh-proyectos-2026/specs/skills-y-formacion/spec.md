# Capability: skills-y-formacion (delta)

## MODIFIED Requirements

### Requirement: Skills ampliadas por los proyectos nuevos
La sección de Hard Skills del portafolio y la de Habilidades del CV DEBEN incluir las tecnologías que
demuestran los proyectos nuevos, sin inventar competencias.

#### Scenario: Hard Skills del portafolio (index.html)
- **WHEN** se revisa la sección Hard Skills
- **THEN** la grilla de íconos incluye **Next.js**, **Kubernetes** y **Grafana**
- **AND** el bloque "Tech Stack & Tools" incluye **Next.js 14**, **Kubernetes (Kustomize)**,
  **Grafana (observabilidad)** y **SSO / OIDC**

#### Scenario: Habilidades del CV (cv.html)
- **WHEN** se revisa la sección Habilidades del CV
- **THEN** se listan visiblemente **n8n**, **Grafana**, **Kubernetes** y **Next.js**
- **AND** la categoría Cloud/DevOps incluye observabilidad (Grafana) y orquestación de contenedores (Kubernetes/Kustomize)
