export type HostRoute = {
    kind: "app";
} | {
    kind: "tunnel";
    tunnelId: string;
} | {
    kind: "unknown";
};
export type ApiRoute = {
    kind: "health";
} | {
    kind: "create";
} | {
    kind: "channel";
    tunnelId: string;
    channelId: number;
    clientConnectionId: string | null;
} | {
    kind: "not-found";
} | {
    kind: "invalid";
    status: number;
    message: string;
} | {
    kind: "method-not-allowed";
    allow: string;
};
export declare function classifyHost(hostname: string, baseDomain: string): HostRoute;
export declare function parseApiRoute(method: string, url: URL): ApiRoute;
export declare function isWebSocketUpgrade(request: Request): boolean;
export declare function normalizeHostname(hostname: string): string;
