const keyCache = new Map();
const encoder = new TextEncoder();
const decoder = new TextDecoder();
export async function signToken(secret, payload) {
    assertUsableSecret(secret);
    const encodedPayload = base64UrlEncodeBytes(encoder.encode(JSON.stringify(payload)));
    const signature = await hmac(secret, encodedPayload);
    return `${encodedPayload}.${base64UrlEncodeBytes(signature)}`;
}
export async function verifyToken(secret, token, options) {
    assertUsableSecret(secret);
    const [encodedPayload, encodedSignature, ...extra] = token.split(".");
    if (!encodedPayload || !encodedSignature || extra.length > 0) {
        return null;
    }
    const signature = base64UrlDecodeBytes(encodedSignature);
    if (!signature) {
        return null;
    }
    const key = await importKey(secret);
    const verified = await crypto.subtle.verify("HMAC", key, toArrayBuffer(signature), toArrayBuffer(encoder.encode(encodedPayload)));
    if (!verified) {
        return null;
    }
    const payloadBytes = base64UrlDecodeBytes(encodedPayload);
    if (!payloadBytes) {
        return null;
    }
    let payload;
    try {
        payload = JSON.parse(decoder.decode(payloadBytes));
    }
    catch {
        return null;
    }
    if (!isTokenPayload(payload)) {
        return null;
    }
    const now = options.now ?? Math.floor(Date.now() / 1000);
    if (payload.aud !== options.audience ||
        payload.tunnelId !== options.tunnelId ||
        payload.exp < now) {
        return null;
    }
    if (options.clientConnectionId !== undefined &&
        payload.clientConnectionId !== options.clientConnectionId) {
        return null;
    }
    return payload;
}
export function createTokenPayload(audience, tunnelId, ttlSeconds, clientConnectionId, now = Math.floor(Date.now() / 1000)) {
    return {
        v: 1,
        aud: audience,
        tunnelId,
        clientConnectionId,
        exp: now + ttlSeconds,
        nonce: crypto.randomUUID(),
    };
}
export function redactToken(value) {
    return value.replace(/[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+/g, "[redacted-token]");
}
function assertUsableSecret(secret) {
    if (typeof secret !== "string" || encoder.encode(secret).byteLength < 32) {
        throw new Error("TOKEN_SECRET must be at least 32 bytes");
    }
}
async function hmac(secret, payload) {
    const key = await importKey(secret);
    const signature = await crypto.subtle.sign("HMAC", key, toArrayBuffer(encoder.encode(payload)));
    return new Uint8Array(signature);
}
function importKey(secret) {
    let cached = keyCache.get(secret);
    if (!cached) {
        cached = crypto.subtle.importKey("raw", toArrayBuffer(encoder.encode(secret)), { name: "HMAC", hash: "SHA-256" }, false, ["sign", "verify"]);
        keyCache.set(secret, cached);
    }
    return cached;
}
function toArrayBuffer(bytes) {
    return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
}
function isTokenPayload(value) {
    if (typeof value !== "object" || value === null || Array.isArray(value)) {
        return false;
    }
    const record = value;
    return (record.v === 1 &&
        record.aud === "connect" &&
        typeof record.tunnelId === "string" &&
        (record.clientConnectionId === undefined ||
            typeof record.clientConnectionId === "string") &&
        Number.isInteger(record.exp) &&
        typeof record.nonce === "string");
}
function base64UrlEncodeBytes(bytes) {
    let binary = "";
    for (const byte of bytes) {
        binary += String.fromCharCode(byte);
    }
    return btoa(binary)
        .replaceAll("+", "-")
        .replaceAll("/", "_")
        .replace(/=+$/, "");
}
function base64UrlDecodeBytes(value) {
    try {
        const padded = value.replaceAll("-", "+").replaceAll("_", "/");
        const base64 = padded.padEnd(padded.length + ((4 - (padded.length % 4)) % 4), "=");
        const binary = atob(base64);
        const bytes = new Uint8Array(binary.length);
        for (let index = 0; index < binary.length; index += 1) {
            bytes[index] = binary.charCodeAt(index);
        }
        return bytes;
    }
    catch {
        return null;
    }
}
