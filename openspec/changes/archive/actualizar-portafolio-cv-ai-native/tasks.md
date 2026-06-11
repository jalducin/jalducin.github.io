## 0. Preparación (OBLIGATORIO — SIEMPRE PRIMERO)

- [x] 0.1 Leer `openspec/config.yaml`, `docs/base-standards.md` y `docs/frontend-standards.md`
- [x] 0.2 Crear y cambiar a la feature branch `feature/actualizar-portafolio-cv-ai-native`

## 1. Posicionamiento AI-native (capability: posicionamiento-ai-native)

- [x] 1.1 Actualizar `header h3` (tagline) a Senior Software Engineer · AI-native Development
- [x] 1.2 Reescribir el párrafo de resumen con el mensaje del CV (+10 años, IA en el SDLC, SDD, métricas)
- [x] 1.3 Actualizar `<title>`, `og:title`/`twitter:title` y `og:description`/`twitter:description`
- [x] 1.4 Confirmar email, WhatsApp (`525640800494`) y enlace de descarga del CV en el header

## 2. Experiencia (capability: experiencia-actualizada)

- [x] 2.1 Podemos: actualizar título a "Backend Support Engineer & IA Specialist", bullets (SDD −40%,
      Claude+Gemini en SDLC, RCA/postmortem con 80% autoresolución N1, AWS <15 min) y stack
- [x] 2.2 Podemos: conservar/reenmarcar Enkoth como hito serverless "shipped to production" bajo SDD
- [x] 2.3 Redsis: actualizar título a "Software Engineer → Tech Lead", bullets de liderazgo y stack
- [x] 2.4 Softtek: alinear bullets (SAP ERP/HANA, SAP BO, AMS, Scrum SLA 98%) y stack

## 3. Proyecto Fidello (capability: proyecto-fidello)

- [x] 3.1 Añadir card "Fidello — Loyalty Card System" en posición prominente reutilizando `.card`/`.tech`
- [x] 3.2 Redactar descripción (multi-negocio, roles Owner/Manager/Employee, QR mobile-first, JWT,
      WebSockets, RLS multi-tenant, QR tokens TTL 60s + fingerprint SHA-256, 100% SDD/OpenSpec)
- [x] 3.3 Listar stack (React 18, TypeScript 5.5, Vite, Tailwind, Supabase, PL/pgSQL, Edge Functions, Vitest)
- [x] 3.4 Resolver botón "View Code": enlazar si hay repo público; omitir si privado (sin enlace roto)

## 4. Skills y formación (capability: skills-y-formacion)

- [x] 4.1 Ampliar skills de IA (OpenAI/Gemini API, Agentic Workflows, Prompt Engineering, LLM Integration, Open Spec)
- [x] 4.2 Ampliar Cloud (EC2, CloudWatch, GCP base, Supabase) y Bases de datos (SQL Server, Hana SQL, DynamoDB)
- [x] 4.3 Añadir "Inglés Avanzado — Quick Learning" a educación
- [x] 4.4 Reconciliar certificaciones con el CV (sin inventar; resolver "edX" según design.md)

## 5. Hardening agentic (capability: agentic-engineering-hardening)

- [x] 5.1 Añadir sección "How I build with AI" (metodología SDD + herramientas + métricas) y su enlace en `nav`
- [x] 5.2 Añadir badges de métricas (−40% / 80% / <15 min) reutilizando estilos existentes
- [x] 5.3 Insertar JSON-LD Schema.org Person válido en `<head>` (name, jobTitle, email, url, sameAs, address, knowsAbout)
- [x] 5.4 Añadir `<meta name="description">` AI-readable coherente
- [x] 5.5 Crear `llms.txt` en la raíz, derivado de la misma fuente de verdad

## 6. Revisar y actualizar pruebas (OBLIGATORIO)

- [x] 6.1 No hay suite automatizada (sitio estático). Definir el checklist de verificación manual del
      cambio (render por sección, 3 breakpoints, enlaces, descarga CV, animaciones, validez JSON-LD)

## 7. Ejecutar verificación y reporte (OBLIGATORIO — EL AGENTE EJECUTA)

- [x] 7.1 Servir el sitio localmente (`python -m http.server` o Live Server) y abrir `index.html`
- [x] 7.2 Verificar render de cada sección modificada y los 3 breakpoints (992 / 768 / 480px)
- [x] 7.3 Validar el JSON-LD (parseo válido) y que `/llms.txt` carga y es consistente con el sitio/CV
- [x] 7.4 Verificar enlaces (email, WhatsApp, GitHub, LinkedIn), descarga del CV y animación matrix/fade-in
- [x] 7.5 Crear el reporte en `openspec/changes/actualizar-portafolio-cv-ai-native/reports/AAAA-MM-DD-step-7-verificacion.md`

## 8. Documentación (OBLIGATORIO — consistencia documental)

- [x] 8.1 Corregir datos canónicos obsoletos: WhatsApp `+52 5643540747 → 525640800494` e inglés `A2 → B1`
      en `CLAUDE.md` y `docs/frontend-standards.md`
- [x] 8.2 Actualizar `README.md` (descripción del portafolio) si cambió el posicionamiento visible
- [x] 8.3 Verificar 0 enlaces rotos y que cada dato tiene una sola fuente de verdad (CV / docs / index)

## 9. Cierre

- [x] 9.1 Commit(s) con conventional commits y PR de la feature branch
- [x] 9.2 Tras merge a `main`, verificar el sitio publicado en GitHub Pages
- [x] 9.3 Archivar el cambio (`/opsx:archive`) moviéndolo a `openspec/changes/archive/`
