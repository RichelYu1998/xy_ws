const SENSITIVE_KEY_PATTERN = /authorization|token|secret/i;
const SIGNED_TOKEN_PATTERN = /[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}/g;
export function log(fields) {
    console.log(JSON.stringify(redactLogFields(fields)));
}
export function redactLogFields(fields) {
    const redacted = {};
    for (const [key, value] of Object.entries(fields)) {
        redacted[key] = redactLogValue(key, value);
    }
    return redacted;
}
function redactLogValue(key, value) {
    if (SENSITIVE_KEY_PATTERN.test(key)) {
        return "[redacted]";
    }
    if (typeof value === "string") {
        return value
            .replace(SIGNED_TOKEN_PATTERN, "[redacted-token]")
            .replace(/Bearer\s+\S+/gi, "Bearer [redacted-token]");
    }
    if (Array.isArray(value)) {
        return value.map((item) => redactLogValue(key, item));
    }
    if (typeof value === "object" && value !== null) {
        return redactLogFields(value);
    }
    return value;
}
