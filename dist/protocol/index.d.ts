export declare const PROTOCOL_VERSION = 4;
export declare const TUNNEL_KIND_EPHEMERAL: "ephemeral";
export declare const TUNNELS_API_PATH = "/api/tunnels";
export declare const EPHEMERAL_TUNNELS_API_PATH = "/api/tunnels/ephemeral";
export declare const DEFAULT_DATA_CHANNELS = 2;
export declare const MAX_DATA_CHANNELS = 8;
export declare const DEFAULT_MAX_WEBSOCKET_MESSAGE_BYTES: number;
export declare const DEFAULT_MAX_FRAME_BYTES: number;
export declare const DEFAULT_MAX_METADATA_BYTES: number;
export declare const DEFAULT_STREAM_CREDIT_BYTES: number;
export declare const DEFAULT_CHANNEL_CREDIT_BYTES: number;
export declare const DEFAULT_PENDING_DATA_BYTES: number;
export declare const DEFAULT_PENDING_DATA_TIMEOUT_MS = 120000;
export declare const MAX_CREDIT_BYTES: number;
export declare const FRAME_MAGIC_0 = 72;
export declare const FRAME_MAGIC_1 = 67;
export declare const FRAME_HEADER_BYTES = 25;
export declare const FRAME_CODE_REQUEST_START = 16;
export declare const FRAME_CODE_REQUEST_DATA = 17;
export declare const FRAME_CODE_REQUEST_END = 18;
export declare const FRAME_CODE_REQUEST_ABORT = 19;
export declare const FRAME_CODE_RESPONSE_START = 32;
export declare const FRAME_CODE_RESPONSE_DATA = 33;
export declare const FRAME_CODE_RESPONSE_END = 34;
export declare const FRAME_CODE_RESPONSE_ABORT = 35;
export declare const FRAME_CODE_STREAM_CREDIT = 48;
export declare const FRAME_CODE_CHANNEL_CREDIT = 49;
export declare const FRAME_TYPE_REQUEST_START: "request.start";
export declare const FRAME_TYPE_REQUEST_DATA: "request.data";
export declare const FRAME_TYPE_REQUEST_END: "request.end";
export declare const FRAME_TYPE_REQUEST_ABORT: "request.abort";
export declare const FRAME_TYPE_RESPONSE_START: "response.start";
export declare const FRAME_TYPE_RESPONSE_DATA: "response.data";
export declare const FRAME_TYPE_RESPONSE_END: "response.end";
export declare const FRAME_TYPE_RESPONSE_ABORT: "response.abort";
export declare const FRAME_TYPE_STREAM_CREDIT: "stream.credit";
export declare const FRAME_TYPE_CHANNEL_CREDIT: "channel.credit";
export declare const FRAME_FLAG_NONE = 0;
export declare const FRAME_FLAG_WS_TEXT = 1;
export declare const FRAME_FLAG_WS_BINARY = 2;
export declare const CLOSE_NORMAL = 1000;
export declare const CLOSE_GOING_AWAY = 1001;
export declare const CLOSE_UNSUPPORTED_DATA = 1003;
export declare const CLOSE_PROTOCOL_ERROR = 1002;
export declare const CLOSE_MESSAGE_TOO_BIG = 1009;
export declare const CLOSE_INTERNAL_ERROR = 1011;
export declare const CLOSE_CLIENT_CONNECTION_REPLACED = 4001;
export declare const MAX_TUNNEL_ID_BYTES = 128;
export declare const MAX_CLIENT_CONNECTION_ID_BYTES = 128;
export declare const MAX_CONNECT_TOKEN_BYTES = 4096;
export declare const MAX_URL_BYTES = 8192;
export declare const MAX_HEADER_COUNT = 256;
export declare const MAX_HEADER_NAME_BYTES = 128;
export declare const MAX_HEADER_VALUE_BYTES: number;
export declare const MAX_HEADERS_BYTES: number;
export declare const MAX_CLOSE_REASON_BYTES = 123;
export type HeaderEntry = readonly [name: string, value: string];
export type StreamId = bigint;
export type ClientConnectionId = string;
export type FrameType = typeof FRAME_TYPE_REQUEST_START | typeof FRAME_TYPE_REQUEST_DATA | typeof FRAME_TYPE_REQUEST_END | typeof FRAME_TYPE_REQUEST_ABORT | typeof FRAME_TYPE_RESPONSE_START | typeof FRAME_TYPE_RESPONSE_DATA | typeof FRAME_TYPE_RESPONSE_END | typeof FRAME_TYPE_RESPONSE_ABORT | typeof FRAME_TYPE_STREAM_CREDIT | typeof FRAME_TYPE_CHANNEL_CREDIT;
export type FrameDirection = "server-to-client" | "client-to-server" | "both";
export type RequestKind = "http" | "websocket";
export type DataKind = "request.body" | "response.body" | "ws.client" | "ws.server";
export interface TunnelLimits {
    readonly maxFrameBytes: number;
    readonly maxMetadataBytes: number;
    readonly maxWebSocketMessageBytes: number;
    readonly streamCreditBytes: number;
    readonly channelCreditBytes: number;
    readonly pendingDataBytes: number;
    readonly pendingDataTimeoutMs: number;
}
export interface CreateEphemeralTunnelResponse {
    readonly kind: typeof TUNNEL_KIND_EPHEMERAL;
    readonly protocolVersion: typeof PROTOCOL_VERSION;
    readonly tunnelId: string;
    readonly publicUrl: string;
    readonly clientConnectionId: ClientConnectionId;
    readonly dataUrl: string;
    readonly connectToken: string;
    readonly dataChannels: number;
    readonly limits: TunnelLimits;
}
export interface RequestStartMetadata {
    readonly kind: RequestKind;
    readonly method: string;
    readonly target: string;
    readonly headers: readonly HeaderEntry[];
    readonly hasBody: boolean;
    readonly protocols?: readonly string[];
}
export interface RequestEndMetadata {
    readonly kind: "request.body" | "ws.client";
    readonly lastSeq: number;
    readonly code?: number;
    readonly reason?: string;
}
export interface RequestAbortMetadata {
    readonly reason: string;
}
export interface ResponseStartMetadata {
    readonly status: number;
    readonly headers: readonly HeaderEntry[];
    readonly hasBody: boolean;
    readonly protocol?: string;
}
export interface ResponseEndMetadata {
    readonly kind: "response.body" | "ws.server";
    readonly lastSeq: number;
    readonly code?: number;
    readonly reason?: string;
}
export interface ResponseAbortMetadata {
    readonly reason: string;
}
export interface StreamCreditMetadata {
    readonly kind: DataKind;
    readonly bytes: number;
}
export interface ChannelCreditMetadata {
    readonly bytes: number;
}
export type Metadata = RequestStartMetadata | RequestEndMetadata | RequestAbortMetadata | ResponseStartMetadata | ResponseEndMetadata | ResponseAbortMetadata | StreamCreditMetadata | ChannelCreditMetadata;
export interface Frame {
    readonly frameType: FrameType;
    readonly streamId: StreamId;
    readonly seq: bigint;
    readonly flags?: number;
    readonly payload?: Uint8Array;
}
export interface DecodedFrame {
    readonly frameType: FrameType;
    readonly streamId: StreamId;
    readonly seq: bigint;
    readonly flags: number;
    readonly payload: Uint8Array;
}
export interface FrameHeader {
    readonly frameType: FrameType;
    readonly streamId: StreamId;
    readonly seq: bigint;
    readonly flags: number;
    readonly payloadLength: number;
}
export interface FrameCodecOptions {
    readonly maxFrameBytes?: number;
}
export interface MetadataCodecOptions {
    readonly maxMetadataBytes?: number;
}
export interface ChooseDataChannelResult {
    readonly channelId: number;
    readonly nextChannelIndex: number;
}
export declare function defaultTunnelLimits(): TunnelLimits;
export declare function isFrameType(value: unknown): value is FrameType;
export declare function getFrameTypeCode(frameType: FrameType): number;
export declare function getFrameTypeFromCode(code: number): FrameType;
export declare function isRequestFrameType(frameType: FrameType): boolean;
export declare function isResponseFrameType(frameType: FrameType): boolean;
export declare function isDataFrameType(frameType: FrameType): boolean;
export declare function isMetadataFrameType(frameType: FrameType): boolean;
export declare function isChannelFrameType(frameType: FrameType): boolean;
export declare function isStreamFrameType(frameType: FrameType): boolean;
export declare function getFrameTypeDirection(frameType: FrameType): FrameDirection;
export declare function isValidFrameForDirection(frameType: FrameType, direction: FrameDirection): boolean;
export declare function encodeFrame(frame: Frame, options?: FrameCodecOptions): Uint8Array;
export declare function encodeFrameHeader(header: FrameHeader, options?: FrameCodecOptions): Uint8Array;
export declare function decodeFrameHeader(input: Uint8Array | ArrayBuffer, options?: FrameCodecOptions): FrameHeader;
export declare function decodeFrameView(input: Uint8Array | ArrayBuffer, options?: FrameCodecOptions): DecodedFrame;
export declare function decodeFrame(input: Uint8Array | ArrayBuffer, options?: FrameCodecOptions): DecodedFrame;
export declare function assertValidFrameHeader(header: FrameHeader): void;
export declare function encodeMetadata(frameType: FrameType, metadata: Metadata, options?: MetadataCodecOptions): Uint8Array;
export declare function decodeMetadata(frameType: FrameType, payload: Uint8Array | ArrayBuffer, options?: MetadataCodecOptions): Metadata;
export declare function isMetadataForFrameType(value: unknown, frameType: FrameType): value is Metadata;
export declare function isRequestStartMetadata(value: unknown): value is RequestStartMetadata;
export declare function isRequestEndMetadata(value: unknown): value is RequestEndMetadata;
export declare function isRequestAbortMetadata(value: unknown): value is RequestAbortMetadata;
export declare function isResponseStartMetadata(value: unknown): value is ResponseStartMetadata;
export declare function isResponseEndMetadata(value: unknown): value is ResponseEndMetadata;
export declare function isResponseAbortMetadata(value: unknown): value is ResponseAbortMetadata;
export declare function isStreamCreditMetadata(value: unknown): value is StreamCreditMetadata;
export declare function isChannelCreditMetadata(value: unknown): value is ChannelCreditMetadata;
export declare function isCreateEphemeralTunnelResponse(value: unknown): value is CreateEphemeralTunnelResponse;
export declare function parseCreateEphemeralTunnelResponse(value: unknown): CreateEphemeralTunnelResponse;
export declare function isTunnelLimits(value: unknown): value is TunnelLimits;
export declare function isValidTunnelId(value: unknown): value is string;
export declare function isValidClientConnectionId(value: unknown): value is ClientConnectionId;
export declare function isValidConnectToken(value: unknown): value is string;
export declare function isValidDataChannelCount(value: unknown): value is number;
export declare function isValidChannelId(channelId: unknown, dataChannels: number): channelId is number;
export declare function chooseNextDataChannel(nextChannelIndex: number, dataChannels: number): ChooseDataChannelResult;
export declare function buildTunnelChannelPath(tunnelId: string, channelId: number): string;
export declare function buildDataChannelUrl(dataUrl: string, channelId: number): string;
export declare function buildPublicUrl(baseDomain: string, tunnelId: string): string;
export declare function isValidTarget(value: unknown): value is string;
export declare function isValidHeaders(value: unknown): value is readonly HeaderEntry[];
export declare function filterHopByHopHeaders(headers: readonly HeaderEntry[]): HeaderEntry[];
export declare function headersToEntries(headers: Headers): HeaderEntry[];
export declare function filterHttpRequestHeaders(headers: readonly HeaderEntry[]): HeaderEntry[];
export declare function filterWebSocketRequestHeaders(headers: readonly HeaderEntry[]): HeaderEntry[];
export declare function filterResponseHeaders(headers: readonly HeaderEntry[]): HeaderEntry[];
export declare function isValidCreditBytes(value: unknown): value is number;
export declare function addCredit(current: number, bytes: number): number;
export declare function consumeCredit(current: number, bytes: number): number;
export declare function hasCredit(current: number, bytes: number): boolean;
export declare function isValidStreamId(value: unknown): value is StreamId;
export declare function isValidSeq(value: unknown): value is bigint;
export declare function isValidLastSeq(value: unknown): value is number;
export declare function isValidDataFrameFlags(value: unknown): value is number;
export declare function utf8Encode(value: string): Uint8Array;
export declare function utf8Decode(value: Uint8Array | ArrayBuffer): string;
export declare function byteLength(value: string): number;
export declare function normalizeCloseReason(reason: unknown): string;
export declare function normalizeCloseCode(code: unknown, fallback?: number): number;
export declare const normalizeWebSocketCloseCode: typeof normalizeCloseCode;
export declare const normalizeWebSocketCloseReason: typeof normalizeCloseReason;
