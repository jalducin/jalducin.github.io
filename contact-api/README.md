# contact-api — Backend del formulario de contacto

Lambda serverless (Python 3.12 + Amazon SES) detrás de API Gateway HTTP API. Recibe el formulario del
portafolio, lo valida (con honeypot anti-spam) y te envía el mensaje por correo. Mismo stack que Trackion
(Serverless Framework), 100% AWS-native.

> Es **opcional**: si `CONTACT_ENDPOINT` queda vacío en `index.html`, la web usa el fallback
> (copiar al portapapeles + `mailto:`) y sigue funcionando. Este backend lo convierte en envío real.

## Requisitos
- Node + Serverless Framework v3 (`npm i -g serverless`)
- Credenciales AWS configuradas (`aws configure`) — la misma cuenta de tus otros proyectos
- Una identidad verificada en **Amazon SES** (ver abajo)

## 1) Verificar el correo en SES (una sola vez)
En la consola de SES (región `us-east-2`) → **Verified identities** → verifica
`valentin.alducin88@gmail.com` (remitente y destinatario). En **sandbox** de SES solo puedes enviar a
direcciones verificadas; como eres el único destinatario, con verificar tu correo basta. (Salir del sandbox
solo si algún día quieres enviar a terceros.)

## 2) Desplegar
```bash
cd contact-api
serverless deploy --region us-east-2
```
Al terminar, Serverless imprime el endpoint, p. ej.:
```
endpoint: POST - https://abc123xyz.execute-api.us-east-2.amazonaws.com/contact
```

## 3) Conectar el front
Copia esa URL en `index.html`:
```js
const CONTACT_ENDPOINT='https://abc123xyz.execute-api.us-east-2.amazonaws.com/contact';
```
Commitea y pushea. Listo: el formulario ahora envía de verdad (con fallback a `mailto` si el backend falla).

## Probar
```bash
curl -X POST "$ENDPOINT/contact" -H "content-type: application/json" \
  -d '{"name":"Test","email":"tu@correo.com","subject":"Hola","message":"Probando"}'
# -> {"ok": true}
```

## Notas
- **Honeypot**: el form incluye un campo oculto `website`; si llega con valor, el Lambda finge éxito y no envía.
- **CORS** restringido a `jalducin.github.io` y al dominio CloudFront.
- **Costo**: prácticamente $0 (free tier de Lambda + SES por debajo de cualquier uso real de un portafolio).
- Variables: `TO_EMAIL`, `FROM_EMAIL`, `ALLOW_ORIGIN` (en `serverless.yml`).
