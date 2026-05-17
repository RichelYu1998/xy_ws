type HeaderEntry = readonly [name: string, value: string];
type HostcHttpRequest = {
    method: string;
    target: string;
    headers: HeaderEntry[];
    body: ReadableStream<Uint8Array> | null;
    publicUrl?: string;
    signal?: AbortSignal;
};
type HostcHttpResponse = {
    status: number;
    headers?: HeaderEntry[];
    body?: ReadableStream<Uint8Array> | Uint8Array | string | null;
};
type HostcWebSocketMessage = {
    data: Uint8Array | string;
    binary: boolean;
};
type HostcUpstreamWebSocket = {
    readonly protocol?: string;
    accept(options?: {
        protocol?: string;
    }): void;
    send(message: Uint8Array | string): void;
    close(code?: number, reason?: string): void;
    onMessage(listener: (message: HostcWebSocketMessage) => void): void;
    onClose(listener: (event: {
        code: number;
        reason: string;
    }) => void): void;
};
type HostcWebSocketRequest = {
    method: string;
    target: string;
    headers: HeaderEntry[];
    protocols: string[];
    publicUrl?: string;
    signal?: AbortSignal;
};
type UpstreamAdapter = {
    handleHttp(request: HostcHttpRequest): Promise<HostcHttpResponse>;
    handleWebSocket?(request: HostcWebSocketRequest): Promise<HostcUpstreamWebSocket>;
};

type LocalOriginAdapterOptions = {
    origin: string | URL;
    publicUrl?: string | URL;
    fetch?: typeof fetch;
};
declare function localOriginAdapter(options: LocalOriginAdapterOptions): UpstreamAdapter;

type HostcClientState = "idle" | "creatingTunnel" | "connecting" | "ready" | "reconnecting" | "closed";
type HostcReadyEvent = {
    tunnelId: string;
    clientConnectionId: string;
    publicUrl: string;
};
type HostcReconnectEvent = {
    attempt: number;
    delayMs: number;
    reason: string;
};
type HostcClosedEvent = {
    reason: string;
};
type HostcLogEvent = {
    level: "debug" | "info" | "warn" | "error";
    message: string;
    fields?: Record<string, unknown>;
};
type HostcClientEvents = {
    state: [state: HostcClientState];
    ready: [event: HostcReadyEvent];
    reconnecting: [event: HostcReconnectEvent];
    closed: [event: HostcClosedEvent];
    error: [error: Error];
    log: [event: HostcLogEvent];
};

type HostcTunnelLimits = {
    readonly maxFrameBytes: number;
    readonly maxMetadataBytes: number;
    readonly maxWebSocketMessageBytes: number;
    readonly streamCreditBytes: number;
    readonly channelCreditBytes: number;
    readonly pendingDataBytes: number;
    readonly pendingDataTimeoutMs: number;
};
type HostcClientOptions = {
    serverUrl: string;
    upstream: UpstreamAdapter;
    dataChannels?: number;
    debug?: boolean;
    fetch?: typeof fetch;
};
type HostcClientSnapshot = {
    state: HostcClientState;
    tunnelId: string | null;
    clientConnectionId: string | null;
    publicUrl: string | null;
    dataChannels: number;
    limits: HostcTunnelLimits | null;
};

type HostcEphemeralTunnel = {
    readonly kind: "ephemeral";
    readonly protocolVersion: 4;
    readonly tunnelId: string;
    readonly publicUrl: string;
    readonly clientConnectionId: string;
    readonly dataUrl: string;
    readonly connectToken: string;
    readonly dataChannels: number;
    readonly limits: HostcTunnelLimits;
};
declare class HostcProtocolUpgradeError extends Error {
    constructor(detail?: string);
}
declare function createEphemeralTunnel(options: {
    serverUrl: string;
    dataChannels?: number;
    fetcher?: typeof fetch;
    signal?: AbortSignal;
    timeoutMs?: number;
}): Promise<HostcEphemeralTunnel>;

type Listener<T extends keyof HostcClientEvents> = (...args: HostcClientEvents[T]) => void;
declare class HostcClient {
    private readonly options;
    private readonly emitter;
    private readonly fetchImpl;
    private state;
    private snapshot;
    private connection;
    private closed;
    private forcedReconnectReason;
    constructor(options: HostcClientOptions);
    on<T extends keyof HostcClientEvents>(event: T, listener: Listener<T>): this;
    off<T extends keyof HostcClientEvents>(event: T, listener: Listener<T>): this;
    getSnapshot(): HostcClientSnapshot;
    start(): Promise<void>;
    stop(): Promise<void>;
    forceReconnect(reason?: string): void;
    protected setReady(event: HostcReadyEvent, limits: HostcTunnelLimits): void;
    private setState;
    private emit;
}

export { type HeaderEntry, HostcClient, type HostcClientEvents, type HostcClientOptions, type HostcClientSnapshot, type HostcClientState, type HostcClosedEvent, type HostcEphemeralTunnel, type HostcHttpRequest, type HostcHttpResponse, type HostcLogEvent, HostcProtocolUpgradeError, type HostcReadyEvent, type HostcReconnectEvent, type HostcTunnelLimits, type HostcUpstreamWebSocket, type HostcWebSocketMessage, type HostcWebSocketRequest, type LocalOriginAdapterOptions, type UpstreamAdapter, createEphemeralTunnel, localOriginAdapter };
