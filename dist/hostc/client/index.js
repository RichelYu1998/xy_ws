// ../protocol/dist/index.js
var PROTOCOL_VERSION = 4;
var TUNNEL_KIND_EPHEMERAL = "ephemeral";
var EPHEMERAL_TUNNELS_API_PATH = "/api/tunnels/ephemeral";
var DEFAULT_DATA_CHANNELS = 2;
var MAX_DATA_CHANNELS = 8;
var DEFAULT_MAX_WEBSOCKET_MESSAGE_BYTES = 1024 * 1024;
var DEFAULT_MAX_FRAME_BYTES = DEFAULT_MAX_WEBSOCKET_MESSAGE_BYTES;
var DEFAULT_MAX_METADATA_BYTES = 64 * 1024;
var DEFAULT_CHANNEL_CREDIT_BYTES = 4 * DEFAULT_MAX_WEBSOCKET_MESSAGE_BYTES;
var MAX_CREDIT_BYTES = Number.MAX_SAFE_INTEGER;
var FRAME_MAGIC_0 = 72;
var FRAME_MAGIC_1 = 67;
var FRAME_HEADER_BYTES = 25;
var FRAME_CODE_REQUEST_START = 16;
var FRAME_CODE_REQUEST_DATA = 17;
var FRAME_CODE_REQUEST_END = 18;
var FRAME_CODE_REQUEST_ABORT = 19;
var FRAME_CODE_RESPONSE_START = 32;
var FRAME_CODE_RESPONSE_DATA = 33;
var FRAME_CODE_RESPONSE_END = 34;
var FRAME_CODE_RESPONSE_ABORT = 35;
var FRAME_CODE_STREAM_CREDIT = 48;
var FRAME_CODE_CHANNEL_CREDIT = 49;
var FRAME_TYPE_REQUEST_START = "request.start";
var FRAME_TYPE_REQUEST_DATA = "request.data";
var FRAME_TYPE_REQUEST_END = "request.end";
var FRAME_TYPE_REQUEST_ABORT = "request.abort";
var FRAME_TYPE_RESPONSE_START = "response.start";
var FRAME_TYPE_RESPONSE_DATA = "response.data";
var FRAME_TYPE_RESPONSE_END = "response.end";
var FRAME_TYPE_RESPONSE_ABORT = "response.abort";
var FRAME_TYPE_STREAM_CREDIT = "stream.credit";
var FRAME_TYPE_CHANNEL_CREDIT = "channel.credit";
var FRAME_FLAG_NONE = 0;
var FRAME_FLAG_WS_TEXT = 1;
var FRAME_FLAG_WS_BINARY = 2;
var CLOSE_NORMAL = 1e3;
var CLOSE_PROTOCOL_ERROR = 1002;
var CLOSE_MESSAGE_TOO_BIG = 1009;
var CLOSE_INTERNAL_ERROR = 1011;
var MAX_TUNNEL_ID_BYTES = 128;
var MAX_CLIENT_CONNECTION_ID_BYTES = 128;
var MAX_CONNECT_TOKEN_BYTES = 4096;
var MAX_URL_BYTES = 8192;
var MAX_HEADER_COUNT = 256;
var MAX_HEADER_NAME_BYTES = 128;
var MAX_HEADER_VALUE_BYTES = 16 * 1024;
var MAX_HEADERS_BYTES = 128 * 1024;
var MAX_CLOSE_REASON_BYTES = 123;
var MAX_UINT32 = 4294967295;
var MAX_UINT64 = (1n << 64n) - 1n;
var ID_RE = /^[A-Za-z0-9](?:[A-Za-z0-9_-]{1,126}[A-Za-z0-9])?$/;
var HTTP_TOKEN_RE = /^[!#$%&'*+.^_`|~0-9A-Za-z-]+$/;
var CONNECT_TOKEN_RE = /^[A-Za-z0-9._~-]+$/;
var HOP_BY_HOP_HEADERS = /* @__PURE__ */ new Set([
  "connection",
  "keep-alive",
  "proxy-authenticate",
  "proxy-authorization",
  "te",
  "trailer",
  "transfer-encoding",
  "upgrade"
]);
var textEncoder = new TextEncoder();
var textDecoder = new TextDecoder("utf-8", { fatal: true });
var FRAME_TYPE_TO_CODE = /* @__PURE__ */ new Map([
  [FRAME_TYPE_REQUEST_START, FRAME_CODE_REQUEST_START],
  [FRAME_TYPE_REQUEST_DATA, FRAME_CODE_REQUEST_DATA],
  [FRAME_TYPE_REQUEST_END, FRAME_CODE_REQUEST_END],
  [FRAME_TYPE_REQUEST_ABORT, FRAME_CODE_REQUEST_ABORT],
  [FRAME_TYPE_RESPONSE_START, FRAME_CODE_RESPONSE_START],
  [FRAME_TYPE_RESPONSE_DATA, FRAME_CODE_RESPONSE_DATA],
  [FRAME_TYPE_RESPONSE_END, FRAME_CODE_RESPONSE_END],
  [FRAME_TYPE_RESPONSE_ABORT, FRAME_CODE_RESPONSE_ABORT],
  [FRAME_TYPE_STREAM_CREDIT, FRAME_CODE_STREAM_CREDIT],
  [FRAME_TYPE_CHANNEL_CREDIT, FRAME_CODE_CHANNEL_CREDIT]
]);
var FRAME_CODE_TO_TYPE = new Map([...FRAME_TYPE_TO_CODE.entries()].map(([frameType, code]) => [
  code,
  frameType
]));
function isFrameType(value) {
  return typeof value === "string" && FRAME_TYPE_TO_CODE.has(value);
}
function getFrameTypeCode(frameType) {
  const code = FRAME_TYPE_TO_CODE.get(frameType);
  if (code === void 0) {
    throw new Error(`unknown frame type: ${String(frameType)}`);
  }
  return code;
}
function getFrameTypeFromCode(code) {
  const frameType = FRAME_CODE_TO_TYPE.get(code);
  if (frameType === void 0) {
    throw new Error(`unknown frame type code: ${code}`);
  }
  return frameType;
}
function isRequestFrameType(frameType) {
  return frameType.startsWith("request.");
}
function isResponseFrameType(frameType) {
  return frameType.startsWith("response.");
}
function isDataFrameType(frameType) {
  return frameType === FRAME_TYPE_REQUEST_DATA || frameType === FRAME_TYPE_RESPONSE_DATA;
}
function isMetadataFrameType(frameType) {
  return !isDataFrameType(frameType);
}
function isChannelFrameType(frameType) {
  return frameType === FRAME_TYPE_CHANNEL_CREDIT;
}
function getFrameTypeDirection(frameType) {
  if (isRequestFrameType(frameType)) {
    return "server-to-client";
  }
  if (isResponseFrameType(frameType)) {
    return "client-to-server";
  }
  return "both";
}
function isValidFrameForDirection(frameType, direction) {
  const frameDirection = getFrameTypeDirection(frameType);
  return direction === "both" || frameDirection === "both" || frameDirection === direction;
}
function encodeFrame(frame, options = {}) {
  const payload = frame.payload ?? new Uint8Array(0);
  if (!(payload instanceof Uint8Array)) {
    throw new Error("frame payload must be a Uint8Array");
  }
  assertValidFrameHeader({
    frameType: frame.frameType,
    streamId: frame.streamId,
    seq: frame.seq,
    flags: frame.flags ?? FRAME_FLAG_NONE,
    payloadLength: payload.byteLength
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
    payloadLength: payload.byteLength
  }));
  bytes.set(payload, FRAME_HEADER_BYTES);
  return bytes;
}
function encodeFrameHeader(header, options = {}) {
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
function decodeFrameHeader(input, options = {}) {
  const bytes = asUint8Array(input);
  if (bytes.byteLength < FRAME_HEADER_BYTES) {
    throw new Error("frame is shorter than header");
  }
  const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  if (view.getUint8(0) !== FRAME_MAGIC_0 || view.getUint8(1) !== FRAME_MAGIC_1) {
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
    payloadLength: view.getUint32(21, false)
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
function decodeFrameView(input, options = {}) {
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
    payload: bytes.subarray(FRAME_HEADER_BYTES)
  };
}
function assertValidFrameHeader(header) {
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
  } else if (header.streamId === 0n) {
    throw new Error("stream-level frame must use a non-zero stream id");
  }
  if (isMetadataFrameType(header.frameType)) {
    if (header.flags !== FRAME_FLAG_NONE) {
      throw new Error("metadata frame flags must be 0");
    }
    if (header.seq !== 0n) {
      throw new Error("metadata frame sequence number must be 0");
    }
  } else if (!isValidDataFrameFlags(header.flags)) {
    throw new Error("invalid data frame flags");
  }
}
function encodeMetadata(frameType, metadata, options = {}) {
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
function decodeMetadata(frameType, payload, options = {}) {
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
  } catch (error) {
    throw new Error(`invalid metadata JSON: ${error instanceof Error ? error.message : String(error)}`);
  }
  if (!isMetadataForFrameType(decoded, frameType)) {
    throw new Error(`invalid metadata for ${frameType}`);
  }
  return decoded;
}
function isMetadataForFrameType(value, frameType) {
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
function isRequestStartMetadata(value) {
  if (!isRecord(value)) {
    return false;
  }
  const allowedKeys = [
    "kind",
    "method",
    "target",
    "headers",
    "hasBody",
    "protocols"
  ];
  if (!hasOnlyKeys(value, allowedKeys)) {
    return false;
  }
  if (value.kind !== "http" && value.kind !== "websocket") {
    return false;
  }
  if (!isValidHttpMethod(value.method) || !isValidTarget(value.target) || !isValidHeaders(value.headers)) {
    return false;
  }
  if (typeof value.hasBody !== "boolean") {
    return false;
  }
  if (value.kind === "websocket" && value.hasBody) {
    return false;
  }
  if (value.protocols !== void 0 && !isValidProtocolList(value.protocols)) {
    return false;
  }
  if (value.kind === "http" && value.protocols !== void 0) {
    return false;
  }
  return true;
}
function isRequestEndMetadata(value) {
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
  if (value.kind === "request.body" && (value.code !== void 0 || value.reason !== void 0)) {
    return false;
  }
  if (value.kind === "ws.client") {
    return isValidOptionalClose(value.code, value.reason);
  }
  return true;
}
function isRequestAbortMetadata(value) {
  return isAbortMetadata(value);
}
function isResponseStartMetadata(value) {
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
  if (value.protocol !== void 0 && !isValidProtocol(value.protocol)) {
    return false;
  }
  return true;
}
function isResponseEndMetadata(value) {
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
  if (value.kind === "response.body" && (value.code !== void 0 || value.reason !== void 0)) {
    return false;
  }
  if (value.kind === "ws.server") {
    return isValidOptionalClose(value.code, value.reason);
  }
  return true;
}
function isResponseAbortMetadata(value) {
  return isAbortMetadata(value);
}
function isStreamCreditMetadata(value) {
  if (!isRecord(value)) {
    return false;
  }
  const allowedKeys = ["kind", "bytes"];
  if (!hasOnlyKeys(value, allowedKeys)) {
    return false;
  }
  return isDataKind(value.kind) && isValidCreditBytes(value.bytes);
}
function isChannelCreditMetadata(value) {
  if (!isRecord(value)) {
    return false;
  }
  const allowedKeys = ["bytes"];
  if (!hasOnlyKeys(value, allowedKeys)) {
    return false;
  }
  return isValidCreditBytes(value.bytes);
}
function isCreateEphemeralTunnelResponse(value) {
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
    "limits"
  ];
  if (!hasOnlyKeys(value, allowedKeys)) {
    return false;
  }
  return value.kind === TUNNEL_KIND_EPHEMERAL && value.protocolVersion === PROTOCOL_VERSION && isValidTunnelId(value.tunnelId) && isValidHttpUrl(value.publicUrl) && isValidClientConnectionId(value.clientConnectionId) && isValidWebSocketUrl(value.dataUrl) && isValidConnectToken(value.connectToken) && isValidDataChannelCount(value.dataChannels) && isTunnelLimits(value.limits);
}
function parseCreateEphemeralTunnelResponse(value) {
  if (!isCreateEphemeralTunnelResponse(value)) {
    throw new Error("create tunnel returned an invalid v4 response");
  }
  return value;
}
function isTunnelLimits(value) {
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
    "pendingDataTimeoutMs"
  ];
  if (!hasOnlyKeys(value, allowedKeys)) {
    return false;
  }
  return isPositiveSafeInteger(value.maxFrameBytes) && isPositiveSafeInteger(value.maxMetadataBytes) && isPositiveSafeInteger(value.maxWebSocketMessageBytes) && isPositiveSafeInteger(value.streamCreditBytes) && isPositiveSafeInteger(value.channelCreditBytes) && isPositiveSafeInteger(value.pendingDataBytes) && isPositiveSafeInteger(value.pendingDataTimeoutMs) && value.maxMetadataBytes <= value.maxFrameBytes && value.maxWebSocketMessageBytes <= value.maxFrameBytes && value.streamCreditBytes <= MAX_CREDIT_BYTES && value.channelCreditBytes <= MAX_CREDIT_BYTES && value.pendingDataBytes <= MAX_CREDIT_BYTES;
}
function isValidTunnelId(value) {
  return typeof value === "string" && byteLength(value) <= MAX_TUNNEL_ID_BYTES && ID_RE.test(value);
}
function isValidClientConnectionId(value) {
  return typeof value === "string" && byteLength(value) <= MAX_CLIENT_CONNECTION_ID_BYTES && ID_RE.test(value);
}
function isValidConnectToken(value) {
  return typeof value === "string" && value.length > 0 && byteLength(value) <= MAX_CONNECT_TOKEN_BYTES && CONNECT_TOKEN_RE.test(value);
}
function isValidDataChannelCount(value) {
  return typeof value === "number" && Number.isSafeInteger(value) && value >= 1 && value <= MAX_DATA_CHANNELS;
}
function buildDataChannelUrl(dataUrl, channelId) {
  if (!isValidWebSocketUrl(dataUrl)) {
    throw new Error("invalid dataUrl");
  }
  if (!Number.isSafeInteger(channelId) || channelId < 0 || channelId > MAX_DATA_CHANNELS - 1) {
    throw new Error("invalid channel id");
  }
  const url = new URL(dataUrl);
  url.pathname = joinUrlPath(url.pathname, String(channelId));
  return url.toString();
}
function isValidTarget(value) {
  return typeof value === "string" && value.length > 0 && value.startsWith("/") && !value.startsWith("//") && !value.includes("\\") && !containsControlExceptTab(value) && byteLength(value) <= MAX_URL_BYTES;
}
function isValidHeaders(value) {
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
function filterHopByHopHeaders(headers) {
  if (!isValidHeaders(headers)) {
    throw new Error("invalid headers");
  }
  const connectionTokens = /* @__PURE__ */ new Set();
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
    return !HOP_BY_HOP_HEADERS.has(normalized) && !connectionTokens.has(normalized);
  });
}
function headersToEntries(headers) {
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
function filterHttpRequestHeaders(headers) {
  return filterHopByHopHeaders(headers).filter(([name]) => {
    const normalized = name.toLowerCase();
    return normalized !== "host" && normalized !== "content-length";
  });
}
function filterWebSocketRequestHeaders(headers) {
  const websocketHeaders = /* @__PURE__ */ new Set([
    "sec-websocket-accept",
    "sec-websocket-extensions",
    "sec-websocket-key",
    "sec-websocket-protocol",
    "sec-websocket-version"
  ]);
  return filterHttpRequestHeaders(headers).filter(([name]) => !websocketHeaders.has(name.toLowerCase()));
}
function filterResponseHeaders(headers) {
  return filterHopByHopHeaders(headers).filter(([name]) => {
    const normalized = name.toLowerCase();
    return normalized !== "content-encoding" && normalized !== "content-length";
  });
}
function isValidCreditBytes(value) {
  return isPositiveSafeInteger(value) && value <= MAX_CREDIT_BYTES;
}
function addCredit(current, bytes) {
  if (!isNonNegativeSafeInteger(current) || !isValidCreditBytes(bytes)) {
    throw new Error("invalid credit value");
  }
  return Math.min(MAX_CREDIT_BYTES, current + bytes);
}
function consumeCredit(current, bytes) {
  if (!isNonNegativeSafeInteger(current) || !isNonNegativeSafeInteger(bytes)) {
    throw new Error("invalid credit value");
  }
  if (bytes > current) {
    throw new Error("insufficient credit");
  }
  return current - bytes;
}
function isValidStreamId(value) {
  return typeof value === "bigint" && value >= 0n && value <= MAX_UINT64;
}
function isValidSeq(value) {
  return typeof value === "bigint" && value >= 0n && value <= MAX_UINT64;
}
function isValidLastSeq(value) {
  return value === -1 || isNonNegativeSafeInteger(value);
}
function isValidDataFrameFlags(value) {
  return value === FRAME_FLAG_NONE || value === FRAME_FLAG_WS_TEXT || value === FRAME_FLAG_WS_BINARY;
}
function utf8Encode(value) {
  return textEncoder.encode(value);
}
function utf8Decode(value) {
  return textDecoder.decode(asUint8Array(value));
}
function byteLength(value) {
  return utf8Encode(value).byteLength;
}
function normalizeCloseReason(reason) {
  if (reason === void 0 || reason === null) {
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
function normalizeCloseCode(code, fallback = CLOSE_NORMAL) {
  if (typeof code === "number" && Number.isInteger(code) && code >= 1e3 && code <= 4999 && code !== 1004 && code !== 1005 && code !== 1006) {
    return code;
  }
  return fallback;
}
var normalizeWebSocketCloseCode = normalizeCloseCode;
var normalizeWebSocketCloseReason = normalizeCloseReason;
function isAbortMetadata(value) {
  if (!isRecord(value)) {
    return false;
  }
  const allowedKeys = ["reason"];
  return hasOnlyKeys(value, allowedKeys) && typeof value.reason === "string" && byteLength(value.reason) <= MAX_CLOSE_REASON_BYTES;
}
function isDataKind(value) {
  return value === "request.body" || value === "response.body" || value === "ws.client" || value === "ws.server";
}
function isValidHttpMethod(value) {
  return typeof value === "string" && value.length > 0 && value.length <= 64 && HTTP_TOKEN_RE.test(value);
}
function isValidStatus(value) {
  return typeof value === "number" && Number.isInteger(value) && value >= 100 && value <= 599;
}
function isValidHeaderName(value) {
  return typeof value === "string" && value.length > 0 && byteLength(value) <= MAX_HEADER_NAME_BYTES && HTTP_TOKEN_RE.test(value);
}
function isValidHeaderValue(value) {
  return typeof value === "string" && byteLength(value) <= MAX_HEADER_VALUE_BYTES && !containsControlExceptTab(value) && !value.includes("\r") && !value.includes("\n");
}
function isValidProtocolList(value) {
  return Array.isArray(value) && value.length <= 32 && value.every(isValidProtocol);
}
function isValidProtocol(value) {
  return typeof value === "string" && value.length > 0 && value.length <= 128 && HTTP_TOKEN_RE.test(value);
}
function isValidOptionalClose(code, reason) {
  if (code !== void 0 && normalizeCloseCode(code, Number.NaN) !== code) {
    return false;
  }
  return reason === void 0 || typeof reason === "string" && byteLength(reason) <= MAX_CLOSE_REASON_BYTES;
}
function isValidHttpUrl(value) {
  if (typeof value !== "string" || byteLength(value) > MAX_URL_BYTES) {
    return false;
  }
  try {
    const url = new URL(value);
    return url.protocol === "https:" || url.protocol === "http:";
  } catch {
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
  } catch {
    return false;
  }
}
function joinUrlPath(basePath, part) {
  const normalizedBase = basePath.endsWith("/") ? basePath.slice(0, -1) : basePath;
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
  return typeof value === "number" && Number.isInteger(value) && value >= 0 && value <= 255;
}
function isValidUint32(value) {
  return typeof value === "number" && Number.isInteger(value) && value >= 0 && value <= MAX_UINT32;
}
function containsControlExceptTab(value) {
  for (let index = 0; index < value.length; index += 1) {
    const code = value.charCodeAt(index);
    if (code >= 0 && code < 32 && code !== 9 || code === 127) {
      return true;
    }
  }
  return false;
}

// src/adapters/local-origin.ts
import WebSocket from "ws";
function localOriginAdapter(options) {
  const origin = new URL(options.origin);
  const fetchImpl = options.fetch ?? fetch;
  return {
    async handleHttp(request) {
      const publicOrigin = request.publicUrl ? new URL(request.publicUrl).origin : options.publicUrl ? new URL(options.publicUrl).origin : null;
      const response = await fetchImpl(new URL(request.target, origin), {
        method: request.method,
        headers: entriesToHeaders(
          filterHttpRequestHeaders(
            rewriteLocalRequestHeaders(request.headers, publicOrigin, origin)
          )
        ),
        body: request.body,
        duplex: request.body ? "half" : void 0,
        redirect: "manual",
        signal: request.signal
      });
      return {
        status: response.status,
        headers: filterResponseHeaders(headersToEntries(response.headers)),
        body: response.body
      };
    },
    async handleWebSocket(request) {
      const publicOrigin = request.publicUrl ? new URL(request.publicUrl).origin : options.publicUrl ? new URL(options.publicUrl).origin : null;
      const url = new URL(request.target, origin);
      url.protocol = url.protocol === "https:" ? "wss:" : "ws:";
      const socket = new WebSocket(url, request.protocols, {
        headers: Object.fromEntries(
          filterWebSocketRequestHeaders(
            rewriteLocalRequestHeaders(request.headers, publicOrigin, origin)
          )
        )
      });
      request.signal?.addEventListener(
        "abort",
        () => safeCloseWebSocket(socket, 1011, "aborted"),
        { once: true }
      );
      await waitForOpen(socket);
      return new LocalUpstreamWebSocket(socket);
    }
  };
}
var LocalUpstreamWebSocket = class {
  constructor(socket) {
    this.socket = socket;
    this.socket.on("message", (data, isBinary) => {
      const payload = rawDataToUint8Array(data);
      const message = {
        data: isBinary ? payload : Buffer.from(payload).toString("utf8"),
        binary: isBinary
      };
      for (const listener of this.messageListeners) {
        listener(message);
      }
    });
    this.socket.on("close", (code, reason) => {
      const event = { code, reason: reason.toString() };
      for (const listener of this.closeListeners) {
        listener(event);
      }
    });
  }
  socket;
  messageListeners = /* @__PURE__ */ new Set();
  closeListeners = /* @__PURE__ */ new Set();
  get protocol() {
    return this.socket.protocol || void 0;
  }
  accept() {
  }
  send(message) {
    this.socket.send(
      typeof message === "string" ? message : Buffer.from(message)
    );
  }
  close(code, reason) {
    safeCloseWebSocket(this.socket, code, reason);
  }
  onMessage(listener) {
    this.messageListeners.add(listener);
  }
  onClose(listener) {
    this.closeListeners.add(listener);
  }
};
function entriesToHeaders(entries) {
  const headers = new Headers();
  for (const [name, value] of entries) {
    headers.append(name, value);
  }
  return headers;
}
function rewriteLocalRequestHeaders(headers, publicOrigin, localOrigin) {
  let sawAcceptEncoding = false;
  const rewritten = [];
  for (const [name, value] of headers) {
    const lowerName = name.toLowerCase();
    if (lowerName === "accept-encoding") {
      sawAcceptEncoding = true;
      rewritten.push([name, "identity"]);
      continue;
    }
    if (publicOrigin && lowerName === "origin" && value === publicOrigin) {
      rewritten.push([name, localOrigin.origin]);
      continue;
    }
    if (publicOrigin && lowerName === "referer") {
      rewritten.push([
        name,
        rewriteSameOriginUrl(value, publicOrigin, localOrigin)
      ]);
      continue;
    }
    rewritten.push([name, value]);
  }
  if (!sawAcceptEncoding) {
    rewritten.push(["accept-encoding", "identity"]);
  }
  return rewritten;
}
function rewriteSameOriginUrl(value, publicOrigin, localOrigin) {
  try {
    const url = new URL(value);
    if (url.origin !== publicOrigin) {
      return value;
    }
    return new URL(`${url.pathname}${url.search}${url.hash}`, localOrigin).href;
  } catch {
    return value;
  }
}
function waitForOpen(socket, timeoutMs = 15e3) {
  if (socket.readyState === WebSocket.OPEN) {
    return Promise.resolve();
  }
  return new Promise((resolve, reject) => {
    const timeout = setTimeout(() => {
      cleanup();
      reject(new Error("local websocket unavailable"));
    }, timeoutMs);
    const cleanup = () => {
      clearTimeout(timeout);
      socket.off("open", onOpen);
      socket.off("error", onError);
      socket.off("close", onClose);
    };
    const onOpen = () => {
      cleanup();
      resolve();
    };
    const onError = (error) => {
      cleanup();
      reject(error);
    };
    const onClose = () => {
      cleanup();
      reject(new Error("local websocket unavailable"));
    };
    socket.once("open", onOpen);
    socket.once("error", onError);
    socket.once("close", onClose);
  });
}
function rawDataToUint8Array(data) {
  if (typeof data === "string") {
    return utf8Encode(data);
  }
  if (Array.isArray(data)) {
    return new Uint8Array(Buffer.concat(data));
  }
  if (data instanceof ArrayBuffer) {
    return new Uint8Array(data);
  }
  return new Uint8Array(data);
}
function safeCloseWebSocket(socket, code, reason) {
  try {
    socket.close(
      normalizeWebSocketCloseCode(code),
      normalizeWebSocketCloseReason(reason)
    );
  } catch {
    socket.terminate();
  }
}

// src/hostc-client.ts
import { EventEmitter } from "events";

// src/client-connection.ts
import WebSocket3 from "ws";

// src/credit.ts
var ClientCreditController = class {
  constructor(limits) {
    this.limits = limits;
  }
  limits;
  outboundStreamCredit = /* @__PURE__ */ new Map();
  inboundStreamCredit = /* @__PURE__ */ new Map();
  outboundChannelCredit = /* @__PURE__ */ new Map();
  inboundChannelCredit = /* @__PURE__ */ new Map();
  waiters = /* @__PURE__ */ new Set();
  reset(dataChannels) {
    this.outboundStreamCredit.clear();
    this.inboundStreamCredit.clear();
    this.outboundChannelCredit.clear();
    this.inboundChannelCredit.clear();
    for (let channelId = 0; channelId < dataChannels; channelId += 1) {
      this.outboundChannelCredit.set(
        channelId,
        this.limits().channelCreditBytes
      );
      this.inboundChannelCredit.set(
        channelId,
        this.limits().channelCreditBytes
      );
    }
    this.wakeWaiters();
  }
  seedStream(streamId) {
    for (const kind of dataKinds()) {
      this.outboundStreamCredit.set(
        creditKey(streamId, kind),
        this.limits().streamCreditBytes
      );
      this.inboundStreamCredit.set(
        creditKey(streamId, kind),
        this.limits().streamCreditBytes
      );
    }
  }
  deleteStream(streamId) {
    for (const kind of dataKinds()) {
      this.outboundStreamCredit.delete(creditKey(streamId, kind));
      this.inboundStreamCredit.delete(creditKey(streamId, kind));
    }
    this.wakeWaiters();
  }
  applyStreamCredit(streamId, metadata) {
    const key = creditKey(streamId, metadata.kind);
    this.outboundStreamCredit.set(
      key,
      addCredit(this.outboundStreamCredit.get(key) ?? 0, metadata.bytes)
    );
    this.wakeWaiters();
  }
  applyChannelCredit(channelId, metadata) {
    this.outboundChannelCredit.set(
      channelId,
      addCredit(this.outboundChannelCredit.get(channelId) ?? 0, metadata.bytes)
    );
    this.wakeWaiters();
  }
  async waitForOutbound(streamId, channelId, kind, bytes, canWait) {
    if (!canWait()) {
      throw new Error("stream unavailable");
    }
    while (!this.hasOutbound(streamId, channelId, kind, bytes)) {
      await new Promise((resolve) => this.waiters.add(resolve));
      if (!canWait()) {
        throw new Error("stream unavailable");
      }
    }
  }
  decrementOutbound(streamId, channelId, kind, bytes) {
    const key = creditKey(streamId, kind);
    this.outboundStreamCredit.set(
      key,
      consumeCredit(this.outboundStreamCredit.get(key) ?? 0, bytes)
    );
    this.outboundChannelCredit.set(
      channelId,
      consumeCredit(this.outboundChannelCredit.get(channelId) ?? 0, bytes)
    );
  }
  consumeInbound(streamId, channelId, kind, bytes) {
    const key = creditKey(streamId, kind);
    const streamCredit = this.inboundStreamCredit.get(key) ?? 0;
    const channelCredit = this.inboundChannelCredit.get(channelId) ?? 0;
    if (streamCredit < bytes || channelCredit < bytes) {
      return false;
    }
    this.inboundStreamCredit.set(key, streamCredit - bytes);
    this.inboundChannelCredit.set(channelId, channelCredit - bytes);
    return true;
  }
  grantInbound(streamId, channelId, kind, bytes) {
    if (bytes <= 0) {
      return;
    }
    const key = creditKey(streamId, kind);
    this.inboundStreamCredit.set(
      key,
      addCredit(this.inboundStreamCredit.get(key) ?? 0, bytes)
    );
    this.inboundChannelCredit.set(
      channelId,
      addCredit(this.inboundChannelCredit.get(channelId) ?? 0, bytes)
    );
  }
  wakeWaiters() {
    for (const waiter of this.waiters) {
      waiter();
    }
    this.waiters.clear();
  }
  hasOutbound(streamId, channelId, kind, bytes) {
    return (this.outboundStreamCredit.get(creditKey(streamId, kind)) ?? 0) >= bytes && (this.outboundChannelCredit.get(channelId) ?? 0) >= bytes;
  }
};
function dataKinds() {
  return ["request.body", "response.body", "ws.client", "ws.server"];
}
function creditKey(streamId, kind) {
  return `${streamId.toString()}:${kind}`;
}

// src/queue.ts
var DataChannelQueue = class {
  chains = /* @__PURE__ */ new Map();
  enqueue(channelId, task) {
    const previous = this.chains.get(channelId) ?? Promise.resolve();
    const next = previous.catch(() => void 0).then(task);
    this.chains.set(
      channelId,
      next.catch(() => void 0)
    );
    return next;
  }
  clear() {
    this.chains.clear();
  }
};

// src/socket.ts
import WebSocket2 from "ws";
var DATA_SOCKET_BACKPRESSURE_HIGH_WATERMARK = 512 * 1024;
var DATA_SOCKET_BACKPRESSURE_LOW_WATERMARK = 128 * 1024;
var DATA_SOCKET_BACKPRESSURE_POLL_MS = 4;
var WEBSOCKET_CONNECT_TIMEOUT_MS = 15e3;
function openWebSocket(url, token) {
  return new Promise((resolve, reject) => {
    const socket = new WebSocket2(url, {
      headers: { authorization: `Bearer ${token}` }
    });
    const timeout = setTimeout(() => {
      cleanup();
      safeCloseWebSocket2(socket, CLOSE_INTERNAL_ERROR, "connect timeout");
      reject(new Error("WebSocket connect timed out"));
    }, WEBSOCKET_CONNECT_TIMEOUT_MS);
    timeout.unref?.();
    const cleanup = () => {
      clearTimeout(timeout);
      socket.off("open", onOpen);
      socket.off("error", onError);
      socket.off("close", onClose);
    };
    const onOpen = () => {
      cleanup();
      resolve(socket);
    };
    const onError = (error) => {
      cleanup();
      reject(error);
    };
    const onClose = (code, reason) => {
      cleanup();
      reject(
        new Error(`WebSocket closed before open: ${code} ${reason.toString()}`)
      );
    };
    socket.once("open", onOpen);
    socket.once("error", onError);
    socket.once("close", onClose);
  });
}
function rawDataToUint8Array2(data) {
  if (typeof data === "string") {
    return utf8Encode(data);
  }
  if (Array.isArray(data)) {
    return new Uint8Array(Buffer.concat(data));
  }
  if (data instanceof ArrayBuffer) {
    return new Uint8Array(data);
  }
  return new Uint8Array(data);
}
async function waitForSocketCapacity(socket) {
  if (socket.bufferedAmount <= DATA_SOCKET_BACKPRESSURE_HIGH_WATERMARK) {
    return;
  }
  while (socket.readyState === WebSocket2.OPEN && socket.bufferedAmount > DATA_SOCKET_BACKPRESSURE_LOW_WATERMARK) {
    await sleep(DATA_SOCKET_BACKPRESSURE_POLL_MS);
  }
}
function safeCloseWebSocket2(socket, code, reason) {
  if (!socket) {
    return;
  }
  try {
    socket.close(
      normalizeWebSocketCloseCode(code),
      normalizeWebSocketCloseReason(reason)
    );
  } catch {
    socket.terminate();
  }
}
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// src/stream-registry.ts
var MAX_REMEMBERED_CLOSED_STREAMS = 4096;
var StreamRegistry = class {
  streams = /* @__PURE__ */ new Map();
  closedStreamIds = /* @__PURE__ */ new Set();
  resetForNewTunnel() {
    this.streams.clear();
    this.closedStreamIds.clear();
  }
  set(stream) {
    this.streams.set(stream.id, stream);
    this.closedStreamIds.delete(stream.id.toString());
  }
  get(streamId) {
    return this.streams.get(streamId);
  }
  has(streamId) {
    return this.streams.has(streamId);
  }
  isClosed(streamId) {
    return this.closedStreamIds.has(streamId.toString());
  }
  isCurrent(stream) {
    return this.streams.get(stream.id) === stream;
  }
  delete(streamId) {
    const stream = this.streams.get(streamId);
    if (!stream) {
      return void 0;
    }
    this.streams.delete(streamId);
    this.rememberClosedStream(streamId);
    return stream;
  }
  values() {
    return [...this.streams.values()];
  }
  rememberClosedStream(streamId) {
    const key = streamId.toString();
    this.closedStreamIds.delete(key);
    this.closedStreamIds.add(key);
    if (this.closedStreamIds.size <= MAX_REMEMBERED_CLOSED_STREAMS) {
      return;
    }
    const oldest = this.closedStreamIds.values().next().value;
    if (oldest !== void 0) {
      this.closedStreamIds.delete(oldest);
    }
  }
};

// src/client-connection.ts
var ClientConnection = class {
  sockets = /* @__PURE__ */ new Map();
  queue = new DataChannelQueue();
  streams = new StreamRegistry();
  credit = new ClientCreditController(
    () => this.tunnel.limits
  );
  disconnected;
  resolveDisconnected;
  closed = false;
  tunnel;
  upstream;
  emitLog;
  constructor(options) {
    this.tunnel = options.tunnel;
    this.upstream = options.upstream;
    this.emitLog = options.emitLog;
    this.disconnected = new Promise((resolve) => {
      this.resolveDisconnected = resolve;
    });
  }
  async connect() {
    this.streams.resetForNewTunnel();
    this.credit.reset(this.tunnel.dataChannels);
    await Promise.all(
      Array.from({ length: this.tunnel.dataChannels }, async (_, channelId) => {
        const url = new URL(
          buildDataChannelUrl(this.tunnel.dataUrl, channelId)
        );
        url.searchParams.set(
          "clientConnectionId",
          this.tunnel.clientConnectionId
        );
        const socket = await openWebSocket(
          url.toString(),
          this.tunnel.connectToken
        );
        if (this.closed) {
          safeCloseWebSocket2(socket, CLOSE_NORMAL, "closed");
          throw new Error("client connection closed while connecting");
        }
        socket.on("message", (data, isBinary) => {
          this.enqueueDataMessage(
            channelId,
            () => this.handleDataMessage(channelId, data, isBinary)
          );
        });
        socket.on("close", (code, reason) => {
          if (this.closed || this.sockets.get(channelId) !== socket) {
            return;
          }
          this.failConnection(
            `data channel ${channelId} closed ${code} ${reason.toString()}`
          );
        });
        socket.on("error", (error) => {
          if (this.closed || this.sockets.get(channelId) !== socket) {
            return;
          }
          this.failConnection(
            `data channel ${channelId} error ${error.message}`
          );
        });
        this.sockets.set(channelId, socket);
      })
    );
  }
  waitForDisconnect() {
    return this.disconnected;
  }
  close(code, reason) {
    if (this.closed) {
      return;
    }
    this.closed = true;
    this.closeSockets(code, reason);
    this.abortAllStreams(reason);
    this.queue.clear();
    this.credit.wakeWaiters();
    this.resolveDisconnected(reason);
  }
  async handleDataMessage(channelId, data, isBinary) {
    if (!isBinary) {
      throw new Error("text data channel message");
    }
    let frame;
    try {
      frame = decodeFrameView(rawDataToUint8Array2(data), {
        maxFrameBytes: this.tunnel.limits.maxFrameBytes
      });
    } catch (error) {
      throw new Error(`invalid data frame: ${errorMessage(error)}`);
    }
    if (!isValidFrameForDirection(frame.frameType, "server-to-client")) {
      throw new Error("wrong frame direction");
    }
    if (frame.frameType === FRAME_TYPE_CHANNEL_CREDIT) {
      const metadata = decodeMetadata(
        FRAME_TYPE_CHANNEL_CREDIT,
        frame.payload
      );
      this.credit.applyChannelCredit(channelId, metadata);
      return;
    }
    if (frame.frameType === FRAME_TYPE_STREAM_CREDIT) {
      const metadata = decodeMetadata(
        FRAME_TYPE_STREAM_CREDIT,
        frame.payload
      );
      this.credit.applyStreamCredit(frame.streamId, metadata);
      return;
    }
    if (this.streams.isClosed(frame.streamId)) {
      return;
    }
    if (frame.frameType === FRAME_TYPE_REQUEST_START) {
      await this.handleRequestStart(channelId, frame);
      return;
    }
    const stream = this.streams.get(frame.streamId);
    if (!stream) {
      throw new Error("unknown stream");
    }
    if (stream.channelId !== channelId) {
      throw new Error("stream frame on wrong channel");
    }
    await this.dispatchStreamFrame(stream, frame);
  }
  async handleRequestStart(channelId, frame) {
    const metadata = decodeMetadata(
      FRAME_TYPE_REQUEST_START,
      frame.payload
    );
    if (this.streams.has(frame.streamId)) {
      throw new Error("duplicate stream start");
    }
    const stream = {
      id: frame.streamId,
      kind: metadata.kind,
      channelId,
      target: metadata.target,
      requestWriter: null,
      requestEndSeq: null,
      localAbortController: new AbortController(),
      upstreamWebSocket: null,
      pendingInboundFrames: [],
      pendingInboundBytes: 0,
      receiveNextSeq: /* @__PURE__ */ new Map(),
      sendNextSeq: /* @__PURE__ */ new Map(),
      sendChains: /* @__PURE__ */ new Map(),
      aborted: false
    };
    this.streams.set(stream);
    this.credit.seedStream(stream.id);
    this.emitLog({
      level: "debug",
      message: "stream.request.start",
      fields: { streamId: stream.id.toString(), channelId, kind: stream.kind }
    });
    if (metadata.kind === "http") {
      void this.startHttpProxy(stream, metadata).catch((error) => {
        void this.abortResponseStream(stream, errorMessage(error));
      });
      return;
    }
    void this.startWebSocketProxy(stream, metadata).catch((error) => {
      void this.abortResponseStream(stream, errorMessage(error));
    });
  }
  async startHttpProxy(stream, metadata) {
    let body = null;
    if (metadata.hasBody) {
      const bodyStream = new TransformStream();
      stream.requestWriter = bodyStream.writable.getWriter();
      body = bodyStream.readable;
    }
    const response = await this.upstream.handleHttp({
      method: metadata.method,
      target: metadata.target,
      headers: [...metadata.headers],
      body,
      publicUrl: this.tunnel.publicUrl,
      signal: stream.localAbortController.signal
    });
    if (!this.canSendForStream(stream)) {
      return;
    }
    await this.sendMetadataFrame(stream, FRAME_TYPE_RESPONSE_START, {
      status: response.status,
      headers: response.headers ?? [],
      hasBody: response.body !== null && response.body !== void 0
    });
    await this.sendHttpResponseBody(stream, response);
    if (!this.canSendForStream(stream)) {
      return;
    }
    await this.sendMetadataFrame(stream, FRAME_TYPE_RESPONSE_END, {
      kind: "response.body",
      lastSeq: this.lastSentSeq(stream, "response.body")
    });
    this.cleanupStream(stream.id);
  }
  async sendHttpResponseBody(stream, response) {
    const body = response.body;
    if (!body) {
      return;
    }
    if (typeof body === "string") {
      await this.sendDataPayload(stream, "response.body", utf8Encode(body));
      return;
    }
    if (body instanceof Uint8Array) {
      await this.sendDataPayload(stream, "response.body", body);
      return;
    }
    const reader = body.getReader();
    for (; ; ) {
      const { done, value } = await reader.read();
      if (done) {
        break;
      }
      await this.sendDataPayload(stream, "response.body", value);
    }
  }
  async startWebSocketProxy(stream, metadata) {
    if (!this.upstream.handleWebSocket) {
      throw new Error("local websocket unavailable");
    }
    const upstreamWebSocket = await this.upstream.handleWebSocket({
      method: metadata.method,
      target: metadata.target,
      headers: [...metadata.headers],
      protocols: [...metadata.protocols ?? []],
      publicUrl: this.tunnel.publicUrl,
      signal: stream.localAbortController.signal
    });
    stream.upstreamWebSocket = upstreamWebSocket;
    await this.sendMetadataFrame(stream, FRAME_TYPE_RESPONSE_START, {
      status: 101,
      headers: [],
      hasBody: false,
      protocol: upstreamWebSocket.protocol
    });
    upstreamWebSocket.onMessage((message) => {
      const payload = typeof message.data === "string" ? utf8Encode(message.data) : message.data;
      if (payload.byteLength > this.tunnel.limits.maxWebSocketMessageBytes) {
        upstreamWebSocket.close(
          CLOSE_MESSAGE_TOO_BIG,
          "WebSocket message too big"
        );
        return;
      }
      void this.enqueueStreamSend(
        stream,
        "ws.server",
        () => this.sendDataPayload(
          stream,
          "ws.server",
          payload,
          message.binary ? FRAME_FLAG_WS_BINARY : FRAME_FLAG_WS_TEXT
        )
      ).catch(
        (error) => void this.abortResponseStream(stream, errorMessage(error))
      );
    });
    upstreamWebSocket.onClose((event) => {
      if (!this.canSendForStream(stream)) {
        return;
      }
      void this.sendMetadataFrame(stream, FRAME_TYPE_RESPONSE_END, {
        kind: "ws.server",
        lastSeq: this.lastSentSeq(stream, "ws.server"),
        code: normalizeWebSocketCloseCode(event.code),
        reason: normalizeWebSocketCloseReason(event.reason)
      }).finally(
        () => this.cleanupStream(stream.id)
      );
    });
    await this.flushPendingInboundFrames(stream);
  }
  async dispatchStreamFrame(stream, frame) {
    switch (frame.frameType) {
      case FRAME_TYPE_REQUEST_DATA: {
        const kind = stream.kind === "http" ? "request.body" : "ws.client";
        if (stream.kind === "http" && frame.flags !== FRAME_FLAG_NONE) {
          throw new Error("HTTP request data must not have WebSocket flags");
        }
        if (stream.kind === "websocket" && frame.flags !== FRAME_FLAG_WS_TEXT && frame.flags !== FRAME_FLAG_WS_BINARY) {
          throw new Error("WebSocket request data missing type flag");
        }
        if (!this.credit.consumeInbound(
          stream.id,
          stream.channelId,
          kind,
          frame.payload.byteLength
        )) {
          throw new Error("credit violation");
        }
        if (!this.checkReceiveSeq(stream, kind, frame.seq)) {
          throw new Error("seq discontinuity");
        }
        try {
          await this.deliverInboundFrame(stream, {
            kind,
            seq: frame.seq,
            flags: frame.flags,
            payload: frame.payload
          });
        } catch (error) {
          await this.abortResponseStream(stream, errorMessage(error));
        }
        return;
      }
      case FRAME_TYPE_REQUEST_END: {
        const metadata = decodeMetadata(
          FRAME_TYPE_REQUEST_END,
          frame.payload
        );
        const kind = stream.kind === "http" ? "request.body" : "ws.client";
        if (metadata.kind !== kind) {
          throw new Error("request end kind mismatch");
        }
        if (!this.checkReceiveEndSeq(stream, kind, metadata.lastSeq)) {
          throw new Error("request end lastSeq mismatch");
        }
        stream.requestEndSeq = metadata.lastSeq;
        try {
          await this.finishIncomingDirection(stream, metadata);
        } catch (error) {
          await this.abortResponseStream(stream, errorMessage(error));
        }
        return;
      }
      case FRAME_TYPE_REQUEST_ABORT: {
        const metadata = decodeMetadata(
          FRAME_TYPE_REQUEST_ABORT,
          frame.payload
        );
        this.abortLocalStream(stream, metadata.reason);
        return;
      }
      default:
        throw new Error("unexpected stream frame");
    }
  }
  async deliverInboundFrame(stream, frame) {
    if (frame.kind === "request.body") {
      if (!stream.requestWriter) {
        throw new Error("request body writer unavailable");
      }
      await stream.requestWriter.write(frame.payload);
      await this.grantInboundCredit(
        stream,
        frame.kind,
        frame.payload.byteLength
      );
      return;
    }
    if (!stream.upstreamWebSocket) {
      this.enqueuePendingInboundFrame(stream, frame);
      return;
    }
    stream.upstreamWebSocket.send(
      frame.flags === FRAME_FLAG_WS_TEXT ? utf8Decode(frame.payload) : frame.payload
    );
    await this.grantInboundCredit(stream, frame.kind, frame.payload.byteLength);
  }
  enqueuePendingInboundFrame(stream, frame) {
    if (stream.pendingInboundBytes + frame.payload.byteLength > this.tunnel.limits.pendingDataBytes) {
      void this.abortResponseStream(stream, "pending data limit exceeded");
      return;
    }
    stream.pendingInboundFrames.push(frame);
    stream.pendingInboundBytes += frame.payload.byteLength;
  }
  async flushPendingInboundFrames(stream) {
    for (; ; ) {
      const frame = stream.pendingInboundFrames.shift();
      if (!frame) {
        return;
      }
      stream.pendingInboundBytes -= frame.payload.byteLength;
      await this.deliverInboundFrame(stream, frame);
    }
  }
  async finishIncomingDirection(stream, metadata) {
    if (metadata.kind === "request.body") {
      await stream.requestWriter?.close();
      return;
    }
    stream.upstreamWebSocket?.close(
      metadata.code ?? CLOSE_NORMAL,
      metadata.reason ?? ""
    );
  }
  async sendDataPayload(stream, kind, payload, flags = FRAME_FLAG_NONE) {
    const limits = this.tunnel.limits;
    if (kind === "ws.server" && payload.byteLength > limits.maxWebSocketMessageBytes) {
      throw new Error("websocket message exceeds max message size");
    }
    for (let offset = 0; offset < payload.byteLength || offset === 0; ) {
      if (!this.canSendForStream(stream)) {
        throw new Error("stream unavailable");
      }
      const chunk = payload.byteLength === 0 ? payload : payload.subarray(offset, offset + limits.maxFrameBytes);
      await this.credit.waitForOutbound(
        stream.id,
        stream.channelId,
        kind,
        chunk.byteLength,
        () => this.canSendForStream(stream)
      );
      const socket = this.sockets.get(stream.channelId);
      if (!socket || socket.readyState !== WebSocket3.OPEN) {
        throw new Error("data channel unavailable");
      }
      await waitForSocketCapacity(socket);
      const seq = stream.sendNextSeq.get(kind) ?? 0n;
      socket.send(
        encodeFrame(
          {
            frameType: FRAME_TYPE_RESPONSE_DATA,
            streamId: stream.id,
            seq,
            flags,
            payload: chunk
          },
          { maxFrameBytes: limits.maxFrameBytes }
        )
      );
      stream.sendNextSeq.set(kind, seq + 1n);
      this.credit.decrementOutbound(
        stream.id,
        stream.channelId,
        kind,
        chunk.byteLength
      );
      if (payload.byteLength === 0) {
        break;
      }
      offset += chunk.byteLength;
    }
  }
  async sendMetadataFrame(stream, frameType, metadata) {
    return this.sendMetadataFrameByChannel(
      stream.channelId,
      frameType,
      stream.id,
      metadata
    );
  }
  async sendMetadataFrameByChannel(channelId, frameType, streamId, metadata) {
    const socket = this.sockets.get(channelId);
    if (!socket || socket.readyState !== WebSocket3.OPEN) {
      throw new Error("data channel unavailable");
    }
    const payload = encodeMetadata(frameType, metadata, {
      maxMetadataBytes: this.tunnel.limits.maxMetadataBytes
    });
    await waitForSocketCapacity(socket);
    socket.send(
      encodeFrame(
        { frameType, streamId, seq: 0n, payload },
        { maxFrameBytes: this.tunnel.limits.maxFrameBytes }
      )
    );
  }
  enqueueStreamSend(stream, kind, task) {
    const previous = stream.sendChains.get(kind) ?? Promise.resolve();
    const next = previous.catch(() => void 0).then(task);
    const current = next.finally(() => {
      if (stream.sendChains.get(kind) === current) {
        stream.sendChains.delete(kind);
      }
    });
    stream.sendChains.set(kind, current);
    return next;
  }
  async grantInboundCredit(stream, kind, bytes) {
    this.credit.grantInbound(stream.id, stream.channelId, kind, bytes);
    await this.sendMetadataFrameByChannel(
      stream.channelId,
      FRAME_TYPE_STREAM_CREDIT,
      stream.id,
      { kind, bytes }
    );
    await this.sendMetadataFrameByChannel(
      stream.channelId,
      FRAME_TYPE_CHANNEL_CREDIT,
      0n,
      { bytes }
    );
  }
  canSendForStream(stream) {
    return !stream.aborted && this.streams.isCurrent(stream) && this.sockets.get(stream.channelId)?.readyState === WebSocket3.OPEN;
  }
  checkReceiveSeq(stream, kind, seq) {
    const expected = stream.receiveNextSeq.get(kind) ?? 0n;
    if (seq !== expected) {
      return false;
    }
    stream.receiveNextSeq.set(kind, expected + 1n);
    return true;
  }
  checkReceiveEndSeq(stream, kind, lastSeq) {
    const nextSeq = stream.receiveNextSeq.get(kind) ?? 0n;
    return BigInt(lastSeq) === nextSeq - 1n;
  }
  lastSentSeq(stream, kind) {
    return Number((stream.sendNextSeq.get(kind) ?? 0n) - 1n);
  }
  async abortResponseStream(stream, reason) {
    const shouldNotifyServer = this.canSendForStream(stream);
    this.abortLocalStream(stream, reason);
    if (shouldNotifyServer) {
      await this.sendMetadataFrameByChannel(
        stream.channelId,
        FRAME_TYPE_RESPONSE_ABORT,
        stream.id,
        { reason }
      ).catch(() => void 0);
    }
  }
  abortLocalStream(stream, reason) {
    stream.aborted = true;
    stream.localAbortController.abort(new Error(reason));
    stream.upstreamWebSocket?.close(CLOSE_INTERNAL_ERROR, reason);
    void stream.requestWriter?.abort(new Error(reason));
    this.cleanupStream(stream.id);
  }
  cleanupStream(streamId) {
    const stream = this.streams.delete(streamId);
    if (!stream) {
      return;
    }
    this.credit.deleteStream(streamId);
    this.emitLog({
      level: "debug",
      message: "stream.end",
      fields: { streamId: streamId.toString() }
    });
  }
  abortAllStreams(reason) {
    for (const stream of this.streams.values()) {
      this.abortLocalStream(stream, reason);
    }
  }
  failConnection(reason) {
    this.emitLog({ level: "debug", message: reason });
    this.close(CLOSE_PROTOCOL_ERROR, reason);
  }
  closeSockets(code, reason) {
    for (const socket of this.sockets.values()) {
      safeCloseWebSocket2(socket, code, reason);
    }
    this.sockets.clear();
  }
  enqueueDataMessage(channelId, task) {
    const next = this.queue.enqueue(channelId, task);
    void next.catch((error) => this.failConnection(errorMessage(error)));
    return next;
  }
};
function errorMessage(error) {
  return error instanceof Error ? error.message : String(error);
}

// src/tunnel-api.ts
var HostcProtocolUpgradeError = class extends Error {
  constructor(detail) {
    super(createProtocolUpgradeMessage(detail));
    this.name = "HostcProtocolUpgradeError";
  }
};
async function createEphemeralTunnel(options) {
  const fetcher = options.fetcher ?? fetch;
  const controller = new AbortController();
  const timeout = setTimeout(
    () => controller.abort(),
    options.timeoutMs ?? 15e3
  );
  timeout.unref?.();
  const abortFromParent = () => controller.abort();
  options.signal?.addEventListener("abort", abortFromParent, { once: true });
  try {
    const response = await fetcher(
      new URL(EPHEMERAL_TUNNELS_API_PATH, options.serverUrl),
      {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
          dataChannels: options.dataChannels ?? DEFAULT_DATA_CHANNELS
        }),
        signal: controller.signal
      }
    );
    const text = await response.text();
    if (response.status === 426) {
      throw new HostcProtocolUpgradeError(text || "server requires upgrade");
    }
    if (!response.ok) {
      throw new Error(`create tunnel failed (${response.status}): ${text}`);
    }
    let json;
    try {
      json = JSON.parse(text);
    } catch {
      throw new Error("create tunnel returned invalid JSON");
    }
    let parsed;
    try {
      parsed = parseCreateEphemeralTunnelResponse(json);
    } catch {
      throw new HostcProtocolUpgradeError(describeProtocolMismatch(json));
    }
    return rewriteLocalDataUrl(parsed, options.serverUrl);
  } finally {
    clearTimeout(timeout);
    options.signal?.removeEventListener("abort", abortFromParent);
  }
}
function withJitter(delayMs, jitterRatio = 0.2) {
  const spread = delayMs * jitterRatio;
  return Math.max(0, Math.round(delayMs - spread + Math.random() * spread * 2));
}
function rewriteLocalDataUrl(response, serverUrl) {
  const server = new URL(serverUrl);
  if (!isLocalServer(server.hostname)) {
    return response;
  }
  const dataUrl = new URL(response.dataUrl);
  dataUrl.hostname = server.hostname;
  dataUrl.port = server.port;
  dataUrl.protocol = server.protocol === "https:" ? "wss:" : "ws:";
  return { ...response, dataUrl: dataUrl.toString() };
}
function describeProtocolMismatch(value) {
  if (!isRecord2(value)) {
    return `server did not return a v${PROTOCOL_VERSION} create tunnel response`;
  }
  if ("protocolVersion" in value) {
    return `server protocolVersion is ${String(value.protocolVersion)}, CLI expects ${PROTOCOL_VERSION}`;
  }
  return `server did not return a v${PROTOCOL_VERSION} create tunnel response`;
}
function createProtocolUpgradeMessage(detail) {
  const lines = [
    "This hostc CLI is incompatible with the tunnel server protocol."
  ];
  if (detail) {
    lines.push(`Reason: ${detail}`);
  }
  lines.push("Please upgrade hostc CLI:", "npm i -g hostc@latest");
  return lines.join("\n");
}
function isRecord2(value) {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}
function isLocalServer(hostname) {
  return hostname === "localhost" || hostname === "127.0.0.1" || hostname === "::1" || hostname === "[::1]";
}

// src/hostc-client.ts
var HostcClient = class {
  constructor(options) {
    this.options = options;
    this.fetchImpl = options.fetch ?? fetch;
    this.snapshot = {
      state: this.state,
      tunnelId: null,
      clientConnectionId: null,
      publicUrl: null,
      dataChannels: options.dataChannels ?? DEFAULT_DATA_CHANNELS,
      limits: null
    };
  }
  options;
  emitter = new EventEmitter();
  fetchImpl;
  state = "idle";
  snapshot;
  connection = null;
  closed = false;
  forcedReconnectReason = null;
  on(event, listener) {
    this.emitter.on(event, listener);
    return this;
  }
  off(event, listener) {
    this.emitter.off(event, listener);
    return this;
  }
  getSnapshot() {
    return { ...this.snapshot };
  }
  async start() {
    let reconnectAttempt = 0;
    let delayMs = 500;
    let hasReadyConnection = false;
    let reconnectReason = "data channel disconnected";
    while (!this.closed) {
      let connection = null;
      try {
        const isReconnect = hasReadyConnection || reconnectAttempt > 0;
        this.setState(isReconnect ? "reconnecting" : "creatingTunnel");
        if (isReconnect) {
          this.emit("reconnecting", {
            attempt: reconnectAttempt,
            delayMs,
            reason: this.forcedReconnectReason ?? reconnectReason
          });
          await sleep2(withJitter(delayMs));
          delayMs = Math.min(delayMs * 2, 1e4);
        }
        const tunnel = await createEphemeralTunnel({
          serverUrl: this.options.serverUrl,
          dataChannels: this.options.dataChannels ?? DEFAULT_DATA_CHANNELS,
          fetcher: this.fetchImpl
        });
        this.snapshot = {
          ...this.snapshot,
          tunnelId: tunnel.tunnelId,
          clientConnectionId: tunnel.clientConnectionId,
          publicUrl: tunnel.publicUrl,
          dataChannels: tunnel.dataChannels,
          limits: tunnel.limits
        };
        connection = new ClientConnection({
          tunnel,
          upstream: this.options.upstream,
          emitLog: (event) => this.emit("log", event)
        });
        this.connection = connection;
        this.setState("connecting");
        await connection.connect();
        if (this.closed || this.connection !== connection) {
          connection.close(CLOSE_INTERNAL_ERROR, "superseded");
          continue;
        }
        this.setReady(
          {
            tunnelId: tunnel.tunnelId,
            clientConnectionId: tunnel.clientConnectionId,
            publicUrl: tunnel.publicUrl
          },
          tunnel.limits
        );
        hasReadyConnection = true;
        reconnectAttempt = 0;
        delayMs = 500;
        this.forcedReconnectReason = null;
        reconnectReason = await connection.waitForDisconnect();
      } catch (error) {
        reconnectReason = toError(error).message;
        if (!this.closed) {
          this.emit("error", toError(error));
        }
        if (!hasReadyConnection && reconnectAttempt === 0) {
          throw error;
        }
      } finally {
        if (connection && this.connection === connection) {
          connection.close(CLOSE_INTERNAL_ERROR, "reconnect");
          this.connection = null;
        }
      }
      if (!this.closed) {
        reconnectAttempt += 1;
      }
    }
  }
  async stop() {
    if (this.closed) {
      return;
    }
    this.closed = true;
    this.connection?.close(CLOSE_NORMAL, "closed");
    this.connection = null;
    this.setState("closed");
    this.emit("closed", { reason: "stopped" });
  }
  forceReconnect(reason = "forced reconnect") {
    if (this.closed) {
      return;
    }
    this.forcedReconnectReason = reason;
    this.connection?.close(CLOSE_INTERNAL_ERROR, reason);
  }
  setReady(event, limits) {
    this.snapshot = {
      ...this.snapshot,
      state: "ready",
      tunnelId: event.tunnelId,
      clientConnectionId: event.clientConnectionId,
      publicUrl: event.publicUrl,
      limits
    };
    this.state = "ready";
    this.emit("state", "ready");
    this.emit("ready", event);
  }
  setState(state) {
    if (this.state === state) {
      return;
    }
    this.state = state;
    this.snapshot = { ...this.snapshot, state };
    this.emit("state", state);
  }
  emit(event, ...args) {
    this.emitter.emit(event, ...args);
  }
};
function sleep2(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
function toError(error) {
  return error instanceof Error ? error : new Error(String(error));
}
export {
  HostcClient,
  HostcProtocolUpgradeError,
  createEphemeralTunnel,
  localOriginAdapter
};
