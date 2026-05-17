import { EPHEMERAL_TUNNELS_API_PATH, isValidChannelId, isValidClientConnectionId, isValidTunnelId, MAX_DATA_CHANNELS, } from "@hostc/protocol";
export function classifyHost(hostname, baseDomain) {
    const rawHost = stripHostnamePort(hostname).replace(/\.$/, "");
    const host = rawHost.toLowerCase();
    const base = normalizeHostname(baseDomain);
    if (isLocalAppHost(host) || host === base) {
        return { kind: "app" };
    }
    const suffix = `.${base}`;
    if (host.endsWith(suffix)) {
        const label = host.slice(0, -suffix.length);
        const rawLabel = rawHost.slice(0, rawHost.length - suffix.length);
        if (!label || label.includes(".") || rawLabel !== rawLabel.toLowerCase()) {
            return { kind: "unknown" };
        }
        if (label === "api" || label === "www") {
            return { kind: "unknown" };
        }
        if (!isValidTunnelId(label)) {
            return { kind: "unknown" };
        }
        return { kind: "tunnel", tunnelId: label };
    }
    return { kind: "unknown" };
}
export function parseApiRoute(method, url) {
    const pathname = stripTrailingSlash(url.pathname);
    if (pathname === "/health") {
        return method === "GET"
            ? { kind: "health" }
            : { kind: "method-not-allowed", allow: "GET" };
    }
    if (pathname === EPHEMERAL_TUNNELS_API_PATH) {
        return method === "POST"
            ? { kind: "create" }
            : { kind: "method-not-allowed", allow: "POST" };
    }
    const parts = pathname.split("/").filter(Boolean);
    if (parts.length !== 5 ||
        parts[0] !== "api" ||
        parts[1] !== "tunnels" ||
        parts[3] !== "channels") {
        return { kind: "not-found" };
    }
    const tunnelId = decodeURIComponent(parts[2] ?? "");
    if (!isValidTunnelId(tunnelId)) {
        return { kind: "invalid", status: 400, message: "Invalid tunnel id" };
    }
    if (method !== "GET") {
        return { kind: "method-not-allowed", allow: "GET" };
    }
    const channelId = Number(parts[4]);
    if (!isValidChannelId(channelId, MAX_DATA_CHANNELS)) {
        return { kind: "invalid", status: 400, message: "Invalid channel" };
    }
    const clientConnectionId = url.searchParams.get("clientConnectionId");
    if (clientConnectionId !== null &&
        !isValidClientConnectionId(clientConnectionId)) {
        return {
            kind: "invalid",
            status: 400,
            message: "Invalid client connection id",
        };
    }
    return { kind: "channel", tunnelId, channelId, clientConnectionId };
}
export function isWebSocketUpgrade(request) {
    const upgrade = request.headers.get("upgrade")?.toLowerCase();
    const connection = request.headers.get("connection") ?? "";
    return (upgrade === "websocket" &&
        connection
            .split(",")
            .some((token) => token.trim().toLowerCase() === "upgrade"));
}
export function normalizeHostname(hostname) {
    return stripHostnamePort(hostname).replace(/\.$/, "").toLowerCase();
}
function stripHostnamePort(hostname) {
    return hostname.startsWith("[")
        ? hostname
        : (hostname.split(":")[0] ?? hostname);
}
function stripTrailingSlash(pathname) {
    return pathname.length > 1 ? pathname.replace(/\/+$/, "") : pathname;
}
function isLocalAppHost(host) {
    return (host === "localhost" ||
        host.endsWith(".localhost") ||
        host === "127.0.0.1" ||
        host === "::1" ||
        host === "[::1]");
}
