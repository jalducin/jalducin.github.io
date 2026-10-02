// Formulario de contacto de jalducin.github.io
// Cambio OpenSpec: migrar-backend-portafolio (capability contacto-backend-supabase).
//
// Flujo: CORS -> validación -> honeypot -> rate limit por ip_hash -> INSERT -> Resend -> UPDATE sent.
// Se guarda ANTES de enviar: si Resend falla, el mensaje no se pierde y el visitante recibe ok:true,queued:true.
// Secretos (Edge Function secrets): RESEND_API_KEY (opcional), TO_EMAIL, FROM_EMAIL, IP_SALT.
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "jsr:@supabase/supabase-js@2";

const ALLOWED_ORIGINS = [
  "https://jalducin.github.io",
  "http://localhost:5500",
  "http://127.0.0.1:5500",
];
const TO_EMAIL = Deno.env.get("TO_EMAIL") ?? "valentin.alducin88@gmail.com";
const FROM_EMAIL = Deno.env.get("FROM_EMAIL") ?? "onboarding@resend.dev";
const RESEND_API_KEY = Deno.env.get("RESEND_API_KEY") ?? "";
const IP_SALT = Deno.env.get("IP_SALT") ?? "jalducin-portfolio";
const RATE_LIMIT = 5; // mensajes por hora y por IP
const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;

function cors(origin: string | null) {
  const allow = origin && ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    "Access-Control-Allow-Origin": allow,
    "Access-Control-Allow-Methods": "POST,OPTIONS",
    "Access-Control-Allow-Headers": "content-type,authorization,apikey",
    "Vary": "Origin",
  };
}

function json(status: number, body: unknown, origin: string | null) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json", ...cors(origin) },
  });
}

async function sha256(text: string) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text));
  return Array.from(new Uint8Array(buf)).map((b) => b.toString(16).padStart(2, "0")).join("");
}

const clean = (v: unknown, max: number) => String(v ?? "").trim().slice(0, max);
const esc = (s: string) =>
  s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]!));

Deno.serve(async (req: Request) => {
  const origin = req.headers.get("origin");
  if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: cors(origin) });
  if (req.method !== "POST") return json(405, { error: "method not allowed" }, origin);

  let body: Record<string, unknown>;
  try {
    body = await req.json();
  } catch {
    return json(400, { error: "invalid json" }, origin);
  }

  // Honeypot: un bot rellena el campo oculto. Se responde ok para no darle señal.
  if (clean(body.website, 200)) return json(200, { ok: true }, origin);

  const name = clean(body.name, 120);
  const email = clean(body.email, 200);
  const subject = clean(body.subject, 200) || "Contacto desde el portafolio";
  const message = clean(body.message, 5000);
  if (!name || !email || !message) return json(400, { error: "missing fields" }, origin);
  if (!EMAIL_RE.test(email)) return json(400, { error: "invalid email" }, origin);

  const ip = (req.headers.get("x-forwarded-for") ?? "").split(",")[0].trim() || "unknown";
  const ipHash = await sha256(ip + IP_SALT);

  const db = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
    { auth: { persistSession: false } },
  );

  // Rate limit: 5 por hora y por IP
  const since = new Date(Date.now() - 3600_000).toISOString();
  const { count } = await db
    .from("contact_messages")
    .select("id", { count: "exact", head: true })
    .eq("ip_hash", ipHash)
    .gte("created_at", since);
  if ((count ?? 0) >= RATE_LIMIT) {
    return json(429, { error: "too many messages", answer: "Has enviado varios mensajes; inténtalo más tarde o escribe a " + TO_EMAIL }, origin);
  }

  // Guardar primero: ningún mensaje se pierde aunque falle el correo
  const { data: row, error: dbError } = await db
    .from("contact_messages")
    .insert({ name, email, subject, message, ip_hash: ipHash })
    .select("id")
    .single();
  if (dbError) {
    console.error("db insert failed", dbError.message);
    return json(500, { error: "could not store message" }, origin);
  }

  if (!RESEND_API_KEY) {
    await db.from("contact_messages").update({ error: "RESEND_API_KEY no configurada" }).eq("id", row.id);
    return json(200, { ok: true, queued: true }, origin);
  }

  try {
    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { authorization: `Bearer ${RESEND_API_KEY}`, "content-type": "application/json" },
      body: JSON.stringify({
        from: `Portafolio <${FROM_EMAIL}>`,
        to: [TO_EMAIL],
        reply_to: email,
        subject: `[Portafolio] ${subject} — ${name}`,
        html: `<p><strong>${esc(name)}</strong> &lt;${esc(email)}&gt;</p>`
          + `<p><em>${esc(subject)}</em></p>`
          + `<pre style="white-space:pre-wrap;font-family:inherit">${esc(message)}</pre>`,
      }),
    });
    if (!r.ok) {
      const detail = (await r.text()).slice(0, 300);
      await db.from("contact_messages").update({ error: `resend ${r.status}: ${detail}` }).eq("id", row.id);
      return json(200, { ok: true, queued: true }, origin);
    }
    await db.from("contact_messages").update({ sent: true }).eq("id", row.id);
    return json(200, { ok: true }, origin);
  } catch (e) {
    await db.from("contact_messages").update({ error: String(e).slice(0, 300) }).eq("id", row.id);
    return json(200, { ok: true, queued: true }, origin);
  }
});
