export const PROTOCOL_VERSION = 4;
export const TUNNEL_KIND_EPHEMERAL = "ephemeral";
export const TUNNELS_API_PATH = "/api/tunnels";
export const EPHEMERAL_TUNNELS_API_PATH = "/api/tunnels/ephemeral";
export const DEFAULT_DATA_CHANNELS = 2;
export const MAX_DATA_CHANNELS = 8;
export const DEFAULT_MAX_WEBSOCKET_MESSAGE_BYTES = 1024 * 1024;
export const DEFAULT_MAX_FRAME_BYTES = DEFAULT_MAX_WEBSOCKET_MESSAGE_BYTES;
export const DEFAULT_MAX_METADATA_BYTES = 64 * 1024;
export const DEFAULT_STREAM_CREDIT_BYTES = DEFAULT_MAX_WEBSOCKET_MESSAGE_BYTES;
export const DEFAULT_CHANNEL_CREDIT_BYTES = 4 * DEFAULT_MAX_WEBSOCKET_MESSAGE_BYTES;
export const DEFAULT_PENDING_DATA_BYTES = DEFAULT_CHANNEL_CREDIT_BYTES;
export const DEFAULT_PENDING_DATA_TIMEOUT_MS = 120_000;
export const MAX_CREDIT_BYTES = Number.MAX_SAFE_INTEGER;
export const FRAME_MAGIC_0 = 0x48; // H
export const FRAME_MAGIC_1 = 0x43; // C
export const FRAME_HEADER_BYTES = 25;
export const FRAME_CODE_REQUEST_START = 0x10;
export const FRAME_CODE_REQUEST_DATA = 0x11;
export const FRAME_CODE_REQUEST_END = 0x12;
export const FRAME_CODE_REQUEST_ABORT = 0x13;
export const FRAME_CODE_RESPONSE_START = 0x20;
export const FRAME_CODE_RESPONSE_DATA = 0x21;
export const FRAME_CODE_RESPONSE_END = 0x22;
export const FRAME_CODE_RESPONSE_ABORT = 0x23;
export const FRAME_CODE_STREAM_CREDIT = 0x30;
export const FRAME_CODE_CHANNEL_CREDIT = 0x31;
export const FRAME_TYPE_REQUEST_START = "request.start";
export const FRAME_TYPE_REQUEST_DATA = "request.data";
export const FRAME_TYPE_REQUEST_END = "request.end";
export const FRAME_TYPE_REQUEST_ABORT = "request.abort";
export const FRAME_TYPE_RESPONSE_START = "response.start";
export const FRAME_TYPE_RESPONSE_DATA = "response.data";
export const FRAME_TYPE_RESPONSE_END = "response.end";
export const FRAME_TYPE_RESPONSE_ABORT = "response.abort";
export const FRAME_TYPE_STREAM_CREDIT = "stream.credit";
export const FRAME_TYPE_CHANNEL_CREDIT = "channel.credit";
export const FRAME_FLAG_NONE = 0x00;
export const FRAME_FLAG_WS_TEXT = 0x01;
export const FRAME_FLAG_WS_BINARY = 0x02;
export const CLOSE_NORMAL = 1000;
export const CLOSE_GOING_AWAY = 1001;
export const CLOSE_UNSUPPORTED_DATA = 1003;
export const CLOSE_PROTOCOL_ERROR = 1002;
export const CLOSE_MESSAGE_TOO_BIG = 1009;
export const CLOSE_INTERNAL_ERROR = 1011;
export const CLOSE_CLIENT_CONNECTION_REPLACED = 4001;
export const MAX_TUNNEL_ID_BYTES = 128;
export const MAX_CLIENT_CONNECTION_ID_BYTES = 128;
export const MAX_CONNECT_TOKEN_BYTES = 4096;
export const MAX_URL_BYTES = 8192;
export const MAX_HEADER_COUNT = 256;
export const MAX_HEADER_NAME_BYTES = 128;
export const MAX_HEADER_VALUE_BYTES = 16 * 1024;
export const MAX_HEADERS_BYTES = 128 * 1024;
export const MAX_CLOSE_REASON_BYTES = 123;
const MAX_UINT32 = 0xffff_ffff;
const MAX_UINT64 = (1n << 64n) - 1n;
const ID_RE = /^[A-Za-z0-9](?:[A-Za-z0-9_-]{1,126}[A-Za-z0-9])?$/;
const HTTP_TOKEN_RE = /^[!#$%&'*+.^_`|~0-9A-Za-z-]+$/;
const CONNECT_TOKEN_RE = /^[A-Za-z0-9._~-]+$/;
const HOP_BY_HOP_HEADERS = new Set([
    "connection",
    "keep-alive",
    "proxy-authenticate",
    "proxy-authorization",
    "te",
    "trailer",
    "transfer-encoding",
    "upgrade",
]);
const textEncoder = new TextEncoder();
const textDecoder = new TextDecoder("utf-8", { fatal: true });
const FRAME_TYPE_TO_CODE = new Map([
    [FRAME_TYPE_REQUEST_START, FRAME_CODE_REQUEST_START],
    [FRAME_TYPE_REQUEST_DATA, FRAME_CODE_REQUEST_DATA],
    [FRAME_TYPE_REQUEST_END, FRAME_CODE_REQUEST_END],
    [FRAME_TYPE_REQUEST_ABORT, FRAME_CODE_REQUEST_ABORT],
    [FRAME_TYPE_RESPONSE_START, FRAME_CODE_RESPONSE_START],
    [FRAME_TYPE_RESPONSE_DATA, FRAME_CODE_RESPONSE_DATA],
    [FRAME_TYPE_RESPONSE_END, FRAME_CODE_RESPONSE_END],
    [FRAME_TYPE_RESPONSE_ABORT, FRAME_CODE_RESPONSE_ABORT],
    [FRAME_TYPE_STREAM_CREDIT, FRAME_CODE_STREAM_CREDIT],
    [FRAME_TYPE_CHANNEL_CREDIT, FRAME_CODE_CHANNEL_CREDIT],
]);
const FRAME_CODE_TO_TYPE = new Map([...FRAME_TYPE_TO_CODE.entries()].map(([frameType, code]) => [
    code,
    frameType,
]));
export function defaultTunnelLimits() {
    return {
        maxFrameBytes: DEFAULT_MAX_FRAME_BYTES,
        maxMetadataBytes: DEFAULT_MAX_METADATA_BYTES,
        maxWebSocketMessageBytes: DEFAULT_MAX_WEBSOCKET_MESSAGE_BYTES,
        streamCreditBytes: DEFAULT_STREAM_CREDIT_BYTES,
        channelCreditBytes: DEFAULT_CHANNEL_CREDIT_BYTES,
        pendingDataBytes: DEFAULT_PENDING_DATA_BYTES,
        pendingDataTimeoutMs: DEFAULT_PENDING_DATA_TIMEOUT_MS,
    };
}
export function isFrameType(value) {
    return (typeof value === "string" && FRAME_TYPE_TO_CODE.has(value));
}
export function getFrameTypeCode(frameType) {
    const code = FRAME_TYPE_TO_CODE.get(frameType);
    if (code === undefined) {
        throw new Error(`unknown frame type: ${String(frameType)}`);
    }
    return code;
}
export function getFrameTypeFromCode(code) {
    const frameType = FRAME_CODE_TO_TYPE.get(code);
    if (frameType === undefined) {
        throw new Error(`unknown frame type code: ${code}`);
    }
    return frameType;
}
export function isRequestFrameType(frameType) {
    return frameType.startsWith("request.");
}
export function isResponseFrameType(frameType) {
    return frameType.startsWith("response.");
}
export function isDataFrameType(frameType) {
    return (frameType === FRAME_TYPE_REQUEST_DATA ||
        frameType === FRAME_TYPE_RESPONSE_DATA);
}
export function isMetadataFrameType(frameType) {
    return !isDataFrameType(frameType);
}
export function isChannelFrameType(frameType) {
    return frameType === FRAME_TYPE_CHANNEL_CREDIT;
}
export function isStreamFrameType(frameType) {
    return !isChannelFrameType(frameType);
}
export function getFrameTypeDirection(frameType) {
    if (isRequestFrameType(frameType)) {
        return "server-to-client";
    }
    if (isResponseFrameType(frameType)) {
        return "client-to-server";
    }
    return "both";
}
export function isValidFrameForDirection(frameType, direction) {
    const frameDirection = getFrameTypeDirection(frameType);
    return (direction === "both" ||
        frameDirection === "both" ||
        frameDirection === direction);
}
export function encodeFrame(frame, options = {}) {
    const payload = frame.payload ?? new Uint8Array(0);
    if (!(payload instanceof Uint8Array)) {
        throw new Error("frame payload must be a Uint8Array");
    }
    assertValidFrameHeader({
        frameType: frame.frameType,
        streamId: frame.streamId,
        seq: frame.seq,
        flags: frame.flags ?? FRAME_FLAG_NONE,
        payloadLength: payload.byteLength,
    });
    const maxFrameBytes = options.maxFrameBytes ?? DEFAULT_MAX_FRAME_BYTES;
    if (!isPositiveSafeInteger(maxFrameBytes)) {
        throw new Error("maxFrameBytes must be a positive safe integer");
    }
    if (payload.byteLength > maxFrameBytes) {
        throw new Error("frame exceeds maxFrameBytes");
    }
    const bytes = new Uint8Array(FRAME_HEADER_BYTES + payload.byteLength);
    bytes.set(encodeFrameHeader({
        frameType: frame.frameType,
        streamId: frame.streamId,
        seq: frame.seq,
        flags: frame.flags ?? FRAME_FLAG_NONE,
        payloadLength: payload.byteLength,
    }));
    bytes.set(payload, FRAME_HEADER_BYTES);
    return bytes;
}
export function encodeFrameHeader(header, options = {}) {
    assertValidFrameHeader(header);
    const maxFrameBytes = options.maxFrameBytes ?? DEFAULT_MAX_FRAME_BYTES;
    if (!isPositiveSafeInteger(maxFrameBytes)) {
        throw new Error("maxFrameBytes must be a positive safe integer");
    }
    if (header.payloadLength > maxFrameBytes) {
        throw new Error("frame exceeds maxFrameBytes");
    }
    const bytes = new Uint8Array(FRAME_HEADER_BYTES);
    const view = new DataView(bytes.buffer);
    view.setUint8(0, FRAME_MAGIC_0);
    view.setUint8(1, FRAME_MAGIC_1);
    view.setUint8(2, PROTOCOL_VERSION);
    view.setUint8(3, getFrameTypeCode(header.frameType));
    view.setUint8(4, header.flags);
    view.setBigUint64(5, header.streamId, false);
    view.setBigUint64(13, header.seq, false);
    view.setUint32(21, header.payloadLength, false);
    return bytes;
}
export function decodeFrameHeader(input, options = {}) {
    const bytes = asUint8Array(input);
    if (bytes.byteLength < FRAME_HEADER_BYTES) {
        throw new Error("frame is shorter than header");
    }
    const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
    if (view.getUint8(0) !== FRAME_MAGIC_0 ||
        view.getUint8(1) !== FRAME_MAGIC_1) {
        throw new Error("invalid frame magic");
    }
    const version = view.getUint8(2);
    if (version !== PROTOCOL_VERSION) {
        throw new Error(`unsupported protocol version: ${version}`);
    }
    const frameType = getFrameTypeFromCode(view.getUint8(3));
    const header = {
        frameType,
        flags: view.getUint8(4),
        streamId: view.getBigUint64(5, false),
        seq: view.getBigUint64(13, false),
        payloadLength: view.getUint32(21, false),
    };
    assertValidFrameHeader(header);
    const maxFrameBytes = options.maxFrameBytes ?? DEFAULT_MAX_FRAME_BYTES;
    if (!isPositiveSafeInteger(maxFrameBytes)) {
        throw new Error("maxFrameBytes must be a positive safe integer");
    }
    if (header.payloadLength > maxFrameBytes) {
        throw new Error("frame exceeds maxFrameBytes");
    }
    return header;
}
export function decodeFrameView(input, options = {}) {
    const bytes = asUint8Array(input);
    const header = decodeFrameHeader(bytes, options);
    const expectedLength = FRAME_HEADER_BYTES + header.payloadLength;
    if (bytes.byteLength !== expectedLength) {
        throw new Error("frame payload length mismatch");
    }
    return {
        frameType: header.frameType,
        streamId: header.streamId,
        seq: header.seq,
        flags: header.flags,
        payload: bytes.subarray(FRAME_HEADER_BYTES),
    };
}
export function decodeFrame(input, options = {}) {
    const frame = decodeFrameView(input, options);
    return { ...frame, payload: frame.payload.slice() };
}
export function assertValidFrameHeader(header) {
    if (!isFrameType(header.frameType)) {
        throw new Error("invalid frame type");
    }
    if (!isValidUint8(header.flags)) {
        throw new Error("invalid frame flags");
    }
    if (!isValidStreamId(header.streamId)) {
        throw new Error("invalid stream id");
    }
    if (!isValidSeq(header.seq)) {
        throw new Error("invalid sequence number");
    }
    if (!isValidUint32(header.payloadLength)) {
        throw new Error("invalid payload length");
    }
    if (isChannelFrameType(header.frameType)) {
        if (header.streamId !== 0n) {
            throw new Error("channel-level frame must use stream id 0");
        }
        if (header.seq !== 0n) {
            throw new Error("channel-level frame must use sequence number 0");
        }
    }
    else if (header.streamId === 0n) {
        throw new Error("stream-level frame must use a non-zero stream id");
    }
    if (isMetadataFrameType(header.frameType)) {
        if (header.flags !== FRAME_FLAG_NONE) {
            throw new Error("metadata frame flags must be 0");
        }
        if (header.seq !== 0n) {
            throw new Error("metadata frame sequence number must be 0");
        }
    }
    else if (!isValidDataFrameFlags(header.flags)) {
        throw new Error("invalid data frame flags");
    }
}
export function encodeMetadata(frameType, metadata, options = {}) {
    if (!isMetadataFrameType(frameType)) {
        throw new Error(`${frameType} does not carry JSON metadata`);
    }
    if (!isMetadataForFrameType(metadata, frameType)) {
        throw new Error(`invalid metadata for ${frameType}`);
    }
    const bytes = utf8Encode(JSON.stringify(metadata));
    const maxMetadataBytes = options.maxMetadataBytes ?? DEFAULT_MAX_METADATA_BYTES;
    if (!isPositiveSafeInteger(maxMetadataBytes)) {
        throw new Error("maxMetadataBytes must be a positive safe integer");
    }
    if (bytes.byteLength > maxMetadataBytes) {
        throw new Error("metadata exceeds maxMetadataBytes");
    }
    return bytes;
}
export function decodeMetadata(frameType, payload, options = {}) {
    if (!isMetadataFrameType(frameType)) {
        throw new Error(`${frameType} does not carry JSON metadata`);
    }
    const bytes = asUint8Array(payload);
    const maxMetadataBytes = options.maxMetadataBytes ?? DEFAULT_MAX_METADATA_BYTES;
    if (!isPositiveSafeInteger(maxMetadataBytes)) {
        throw new Error("maxMetadataBytes must be a positive safe integer");
    }
    if (bytes.byteLength > maxMetadataBytes) {
        throw new Error("metadata exceeds maxMetadataBytes");
    }
    let decoded;
    try {
        decoded = JSON.parse(utf8Decode(bytes));
    }
    catch (error) {
        throw new Error(`invalid metadata JSON: ${error instanceof Error ? error.message : String(error)}`);
    }
    if (!isMetadataForFrameType(decoded, frameType)) {
        throw new Error(`invalid metadata for ${frameType}`);
    }
    return decoded;
}
export function isMetadataForFrameType(value, frameType) {
    switch (frameType) {
        case FRAME_TYPE_REQUEST_START:
            return isRequestStartMetadata(value);
        case FRAME_TYPE_REQUEST_END:
            return isRequestEndMetadata(value);
        case FRAME_TYPE_REQUEST_ABORT:
            return isRequestAbortMetadata(value);
        case FRAME_TYPE_RESPONSE_START:
            return isResponseStartMetadata(value);
        case FRAME_TYPE_RESPONSE_END:
            return isResponseEndMetadata(value);
        case FRAME_TYPE_RESPONSE_ABORT:
            return isResponseAbortMetadata(value);
        case FRAME_TYPE_STREAM_CREDIT:
            return isStreamCreditMetadata(value);
        case FRAME_TYPE_CHANNEL_CREDIT:
            return isChannelCreditMetadata(value);
        case FRAME_TYPE_REQUEST_DATA:
        case FRAME_TYPE_RESPONSE_DATA:
            return false;
    }
}
export function isRequestStartMetadata(value) {
    if (!isRecord(value)) {
        return false;
    }
    const allowedKeys = [
        "kind",
        "method",
        "target",
        "headers",
        "hasBody",
        "protocols",
    ];
    if (!hasOnlyKeys(value, allowedKeys)) {
        return false;
    }
    if (value.kind !== "http" && value.kind !== "websocket") {
        return false;
    }
    if (!isValidHttpMethod(value.method) ||
        !isValidTarget(value.target) ||
        !isValidHeaders(value.headers)) {
        return false;
    }
    if (typeof value.hasBody !== "boolean") {
        return false;
    }
    if (value.kind === "websocket" && value.hasBody) {
        return false;
    }
    if (value.protocols !== undefined && !isValidProtocolList(value.protocols)) {
        return false;
    }
    if (value.kind === "http" && value.protocols !== undefined) {
        return false;
    }
    return true;
}
export function isRequestEndMetadata(value) {
    if (!isRecord(value)) {
        return false;
    }
    const allowedKeys = ["kind", "lastSeq", "code", "reason"];
    if (!hasOnlyKeys(value, allowedKeys)) {
        return false;
    }
    if (value.kind !== "request.body" && value.kind !== "ws.client") {
        return false;
    }
    if (!isValidLastSeq(value.lastSeq)) {
        return false;
    }
    if (value.kind === "request.body" &&
        (value.code !== undefined || value.reason !== undefined)) {
        return false;
    }
    if (value.kind === "ws.client") {
        return isValidOptionalClose(value.code, value.reason);
    }
    return true;
}
export function isRequestAbortMetadata(value) {
    return isAbortMetadata(value);
}
export function isResponseStartMetadata(value) {
    if (!isRecord(value)) {
        return false;
    }
    const allowedKeys = ["status", "headers", "hasBody", "protocol"];
    if (!hasOnlyKeys(value, allowedKeys)) {
        return false;
    }
    if (!isValidStatus(value.status) || !isValidHeaders(value.headers)) {
        return false;
    }
    if (typeof value.hasBody !== "boolean") {
        return false;
    }
    if (value.protocol !== undefined && !isValidProtocol(value.protocol)) {
        return false;
    }
    return true;
}
export function isResponseEndMetadata(value) {
    if (!isRecord(value)) {
        return false;
    }
    const allowedKeys = ["kind", "lastSeq", "code", "reason"];
    if (!hasOnlyKeys(value, allowedKeys)) {
        return false;
    }
    if (value.kind !== "response.body" && value.kind !== "ws.server") {
        return false;
    }
    if (!isValidLastSeq(value.lastSeq)) {
        return false;
    }
    if (value.kind === "response.body" &&
        (value.code !== undefined || value.reason !== undefined)) {
        return false;
    }
    if (value.kind === "ws.server") {
        return isValidOptionalClose(value.code, value.reason);
    }
    return true;
}
export function isResponseAbortMetadata(value) {
    return isAbortMetadata(value);
}
export function isStreamCreditMetadata(value) {
    if (!isRecord(value)) {
        return false;
    }
    const allowedKeys = ["kind", "bytes"];
    if (!hasOnlyKeys(value, allowedKeys)) {
        return false;
    }
    return isDataKind(value.kind) && isValidCreditBytes(value.bytes);
}
export function isChannelCreditMetadata(value) {
    if (!isRecord(value)) {
        return false;
    }
    const allowedKeys = ["bytes"];
    if (!hasOnlyKeys(value, allowedKeys)) {
        return false;
    }
    return isValidCreditBytes(value.bytes);
}
export function isCreateEphemeralTunnelResponse(value) {
    if (!isRecord(value)) {
        return false;
    }
    const allowedKeys = [
        "kind",
        "protocolVersion",
        "tunnelId",
        "publicUrl",
        "clientConnectionId",
        "dataUrl",
        "connectToken",
        "dataChannels",
        "limits",
    ];
    if (!hasOnlyKeys(value, allowedKeys)) {
        return false;
    }
    return (value.kind === TUNNEL_KIND_EPHEMERAL &&
        value.protocolVersion === PROTOCOL_VERSION &&
        isValidTunnelId(value.tunnelId) &&
        isValidHttpUrl(value.publicUrl) &&
        isValidClientConnectionId(value.clientConnectionId) &&
        isValidWebSocketUrl(value.dataUrl) &&
        isValidConnectToken(value.connectToken) &&
        isValidDataChannelCount(value.dataChannels) &&
        isTunnelLimits(value.limits));
}
export function parseCreateEphemeralTunnelResponse(value) {
    if (!isCreateEphemeralTunnelResponse(value)) {
        throw new Error("create tunnel returned an invalid v4 response");
    }
    return value;
}
export function isTunnelLimits(value) {
    if (!isRecord(value)) {
        return false;
    }
    const allowedKeys = [
        "maxFrameBytes",
        "maxMetadataBytes",
        "maxWebSocketMessageBytes",
        "streamCreditBytes",
        "channelCreditBytes",
        "pendingDataBytes",
        "pendingDataTimeoutMs",
    ];
    if (!hasOnlyKeys(value, allowedKeys)) {
        return false;
    }
    return (isPositiveSafeInteger(value.maxFrameBytes) &&
        isPositiveSafeInteger(value.maxMetadataBytes) &&
        isPositiveSafeInteger(value.maxWebSocketMessageBytes) &&
        isPositiveSafeInteger(value.streamCreditBytes) &&
        isPositiveSafeInteger(value.channelCreditBytes) &&
        isPositiveSafeInteger(value.pendingDataBytes) &&
        isPositiveSafeInteger(value.pendingDataTimeoutMs) &&
        value.maxMetadataBytes <= value.maxFrameBytes &&
        value.maxWebSocketMessageBytes <= value.maxFrameBytes &&
        value.streamCreditBytes <= MAX_CREDIT_BYTES &&
        value.channelCreditBytes <= MAX_CREDIT_BYTES &&
        value.pendingDataBytes <= MAX_CREDIT_BYTES);
}
export function isValidTunnelId(value) {
    return (typeof value === "string" &&
        byteLength(value) <= MAX_TUNNEL_ID_BYTES &&
        ID_RE.test(value));
}
export function isValidClientConnectionId(value) {
    return (typeof value === "string" &&
        byteLength(value) <= MAX_CLIENT_CONNECTION_ID_BYTES &&
        ID_RE.test(value));
}
export function isValidConnectToken(value) {
    return (typeof value === "string" &&
        value.length > 0 &&
        byteLength(value) <= MAX_CONNECT_TOKEN_BYTES &&
        CONNECT_TOKEN_RE.test(value));
}
export function isValidDataChannelCount(value) {
    return (typeof value === "number" &&
        Number.isSafeInteger(value) &&
        value >= 1 &&
        value <= MAX_DATA_CHANNELS);
}
export function isValidChannelId(channelId, dataChannels) {
    return (isValidDataChannelCount(dataChannels) &&
        typeof channelId === "number" &&
        Number.isSafeInteger(channelId) &&
        channelId >= 0 &&
        channelId < dataChannels);
}
export function chooseNextDataChannel(nextChannelIndex, dataChannels) {
    if (!Number.isSafeInteger(nextChannelIndex) || nextChannelIndex < 0) {
        throw new Error("nextChannelIndex must be a non-negative safe integer");
    }
    if (!isValidDataChannelCount(dataChannels)) {
        throw new Error("invalid data channel count");
    }
    const channelId = nextChannelIndex % dataChannels;
    return { channelId, nextChannelIndex: nextChannelIndex + 1 };
}
export function buildTunnelChannelPath(tunnelId, channelId) {
    if (!isValidTunnelId(tunnelId)) {
        throw new Error("invalid tunnel id");
    }
    if (!Number.isSafeInteger(channelId) ||
        channelId < 0 ||
        channelId > MAX_DATA_CHANNELS - 1) {
        throw new Error("invalid channel id");
    }
    return `${TUNNELS_API_PATH}/${tunnelId}/channels/${channelId}`;
}
export function buildDataChannelUrl(dataUrl, channelId) {
    if (!isValidWebSocketUrl(dataUrl)) {
        throw new Error("invalid dataUrl");
    }
    if (!Number.isSafeInteger(channelId) ||
        channelId < 0 ||
        channelId > MAX_DATA_CHANNELS - 1) {
        throw new Error("invalid channel id");
    }
    const url = new URL(dataUrl);
    url.pathname = joinUrlPath(url.pathname, String(channelId));
    return url.toString();
}
export function buildPublicUrl(baseDomain, tunnelId) {
    if (!isValidTunnelId(tunnelId)) {
        throw new Error("invalid tunnel id");
    }
    const normalizedBase = baseDomain.startsWith("http://") || baseDomain.startsWith("https://")
        ? baseDomain
        : `https://${baseDomain}`;
    const url = new URL(normalizedBase);
    const host = url.hostname.startsWith(`${tunnelId}.`)
        ? url.hostname
        : `${tunnelId}.${url.hostname}`;
    url.hostname = host;
    url.pathname = "/";
    url.search = "";
    url.hash = "";
    return url.toString().replace(/\/$/, "");
}
export function isValidTarget(value) {
    return (typeof value === "string" &&
        value.length > 0 &&
        value.startsWith("/") &&
        !value.startsWith("//") &&
        !value.includes("\\") &&
        !containsControlExceptTab(value) &&
        byteLength(value) <= MAX_URL_BYTES);
}
export function isValidHeaders(value) {
    if (!Array.isArray(value) || value.length > MAX_HEADER_COUNT) {
        return false;
    }
    let totalBytes = 0;
    for (const entry of value) {
        if (!Array.isArray(entry) || entry.length !== 2) {
            return false;
        }
        const [name, headerValue] = entry;
        if (!isValidHeaderName(name) || !isValidHeaderValue(headerValue)) {
            return false;
        }
        totalBytes += byteLength(name) + byteLength(headerValue);
        if (totalBytes > MAX_HEADERS_BYTES) {
            return false;
        }
    }
    return true;
}
export function filterHopByHopHeaders(headers) {
    if (!isValidHeaders(headers)) {
        throw new Error("invalid headers");
    }
    const connectionTokens = new Set();
    for (const [name, value] of headers) {
        if (name.toLowerCase() === "connection") {
            for (const token of value.split(",")) {
                const normalized = token.trim().toLowerCase();
                if (normalized) {
                    connectionTokens.add(normalized);
                }
            }
        }
    }
    return headers.filter(([name]) => {
        const normalized = name.toLowerCase();
        return (!HOP_BY_HOP_HEADERS.has(normalized) && !connectionTokens.has(normalized));
    });
}
export function headersToEntries(headers) {
    const entries = [];
    let sawSetCookie = false;
    for (const [name, value] of headers) {
        if (name.toLowerCase() === "set-cookie") {
            sawSetCookie = true;
            continue;
        }
        entries.push([name, value]);
    }
    const setCookies = headers.getSetCookie?.() ?? [];
    for (const value of setCookies) {
        entries.push(["set-cookie", value]);
    }
    if (!sawSetCookie || setCookies.length > 0) {
        return entries;
    }
    const combined = headers.get("set-cookie");
    if (combined !== null) {
        entries.push(["set-cookie", combined]);
    }
    return entries;
}
export function filterHttpRequestHeaders(headers) {
    return filterHopByHopHeaders(headers).filter(([name]) => {
        const normalized = name.toLowerCase();
        return normalized !== "host" && normalized !== "content-length";
    });
}
export function filterWebSocketRequestHeaders(headers) {
    const websocketHeaders = new Set([
        "sec-websocket-accept",
        "sec-websocket-extensions",
        "sec-websocket-key",
        "sec-websocket-protocol",
        "sec-websocket-version",
    ]);
    return filterHttpRequestHeaders(headers).filter(([name]) => !websocketHeaders.has(name.toLowerCase()));
}
export function filterResponseHeaders(headers) {
    return filterHopByHopHeaders(headers).filter(([name]) => {
        const normalized = name.toLowerCase();
        return normalized !== "content-encoding" && normalized !== "content-length";
    });
}
export function isValidCreditBytes(value) {
    return isPositiveSafeInteger(value) && value <= MAX_CREDIT_BYTES;
}
export function addCredit(current, bytes) {
    if (!isNonNegativeSafeInteger(current) || !isValidCreditBytes(bytes)) {
        throw new Error("invalid credit value");
    }
    return Math.min(MAX_CREDIT_BYTES, current + bytes);
}
export function consumeCredit(current, bytes) {
    if (!isNonNegativeSafeInteger(current) || !isNonNegativeSafeInteger(bytes)) {
        throw new Error("invalid credit value");
    }
    if (bytes > current) {
        throw new Error("insufficient credit");
    }
    return current - bytes;
}
export function hasCredit(current, bytes) {
    return (isNonNegativeSafeInteger(current) &&
        isNonNegativeSafeInteger(bytes) &&
        current >= bytes);
}
export function isValidStreamId(value) {
    return typeof value === "bigint" && value >= 0n && value <= MAX_UINT64;
}
export function isValidSeq(value) {
    return typeof value === "bigint" && value >= 0n && value <= MAX_UINT64;
}
export function isValidLastSeq(value) {
    return value === -1 || isNonNegativeSafeInteger(value);
}
export function isValidDataFrameFlags(value) {
    return (value === FRAME_FLAG_NONE ||
        value === FRAME_FLAG_WS_TEXT ||
        value === FRAME_FLAG_WS_BINARY);
}
export function utf8Encode(value) {
    return textEncoder.encode(value);
}
export function utf8Decode(value) {
    return textDecoder.decode(asUint8Array(value));
}
export function byteLength(value) {
    return utf8Encode(value).byteLength;
}
export function normalizeCloseReason(reason) {
    if (reason === undefined || reason === null) {
        return "";
    }
    const value = String(reason).replace(/[\r\n]/g, " ");
    if (byteLength(value) <= MAX_CLOSE_REASON_BYTES) {
        return value;
    }
    let output = "";
    for (const char of value) {
        const next = output + char;
        if (byteLength(next) > MAX_CLOSE_REASON_BYTES) {
            break;
        }
        output = next;
    }
    return output;
}
export function normalizeCloseCode(code, fallback = CLOSE_NORMAL) {
    if (typeof code === "number" &&
        Number.isInteger(code) &&
        code >= 1000 &&
        code <= 4999 &&
        code !== 1004 &&
        code !== 1005 &&
        code !== 1006) {
        return code;
    }
    return fallback;
}
export const normalizeWebSocketCloseCode = normalizeCloseCode;
export const normalizeWebSocketCloseReason = normalizeCloseReason;
function isAbortMetadata(value) {
    if (!isRecord(value)) {
        return false;
    }
    const allowedKeys = ["reason"];
    return (hasOnlyKeys(value, allowedKeys) &&
        typeof value.reason === "string" &&
        byteLength(value.reason) <= MAX_CLOSE_REASON_BYTES);
}
function isDataKind(value) {
    return (value === "request.body" ||
        value === "response.body" ||
        value === "ws.client" ||
        value === "ws.server");
}
function isValidHttpMethod(value) {
    return (typeof value === "string" &&
        value.length > 0 &&
        value.length <= 64 &&
        HTTP_TOKEN_RE.test(value));
}
function isValidStatus(value) {
    return (typeof value === "number" &&
        Number.isInteger(value) &&
        value >= 100 &&
        value <= 599);
}
function isValidHeaderName(value) {
    return (typeof value === "string" &&
        value.length > 0 &&
        byteLength(value) <= MAX_HEADER_NAME_BYTES &&
        HTTP_TOKEN_RE.test(value));
}
function isValidHeaderValue(value) {
    return (typeof value === "string" &&
        byteLength(value) <= MAX_HEADER_VALUE_BYTES &&
        !containsControlExceptTab(value) &&
        !value.includes("\r") &&
        !value.includes("\n"));
}
function isValidProtocolList(value) {
    return (Array.isArray(value) && value.length <= 32 && value.every(isValidProtocol));
}
function isValidProtocol(value) {
    return (typeof value === "string" &&
        value.length > 0 &&
        value.length <= 128 &&
        HTTP_TOKEN_RE.test(value));
}
function isValidOptionalClose(code, reason) {
    if (code !== undefined && normalizeCloseCode(code, Number.NaN) !== code) {
        return false;
    }
    return (reason === undefined ||
        (typeof reason === "string" && byteLength(reason) <= MAX_CLOSE_REASON_BYTES));
}
function isValidHttpUrl(value) {
    if (typeof value !== "string" || byteLength(value) > MAX_URL_BYTES) {
        return false;
    }
    try {
        const url = new URL(value);
        return url.protocol === "https:" || url.protocol === "http:";
    }
    catch {
        return false;
    }
}
function isValidWebSocketUrl(value) {
    if (typeof value !== "string" || byteLength(value) > MAX_URL_BYTES) {
        return false;
    }
    try {
        const url = new URL(value);
        return url.protocol === "wss:" || url.protocol === "ws:";
    }
    catch {
        return false;
    }
}
function joinUrlPath(basePath, part) {
    const normalizedBase = basePath.endsWith("/")
        ? basePath.slice(0, -1)
        : basePath;
    return `${normalizedBase}/${encodeURIComponent(part)}`;
}
function asUint8Array(input) {
    return input instanceof Uint8Array ? input : new Uint8Array(input);
}
function hasOnlyKeys(value, allowedKeys) {
    return Object.keys(value).every((key) => allowedKeys.includes(key));
}
function isRecord(value) {
    return typeof value === "object" && value !== null && !Array.isArray(value);
}
function isPositiveSafeInteger(value) {
    return typeof value === "number" && Number.isSafeInteger(value) && value > 0;
}
function isNonNegativeSafeInteger(value) {
    return typeof value === "number" && Number.isSafeInteger(value) && value >= 0;
}
function isValidUint8(value) {
    return (typeof value === "number" &&
        Number.isInteger(value) &&
        value >= 0 &&
        value <= 0xff);
}
function isValidUint32(value) {
    return (typeof value === "number" &&
        Number.isInteger(value) &&
        value >= 0 &&
        value <= MAX_UINT32);
}
function containsControlExceptTab(value) {
    for (let index = 0; index < value.length; index += 1) {
        const code = value.charCodeAt(index);
        if ((code >= 0 && code < 0x20 && code !== 0x09) || code === 0x7f) {
            return true;
        }
    }
    return false;
}
