import { addCredit, consumeCredit, FRAME_TYPE_CHANNEL_CREDIT, FRAME_TYPE_STREAM_CREDIT, MAX_CREDIT_BYTES, } from "@hostc/protocol";
const CREDIT_KINDS = [
    "request.body",
    "response.body",
    "ws.client",
    "ws.server",
];
export class TunnelCreditController {
    limits;
    sendCredit;
    waitUntil;
    onCreditError;
    outboundStreamCredit = new Map();
    inboundStreamCredit = new Map();
    outboundChannelCredit = new Map();
    inboundChannelCredit = new Map();
    waiters = new Set();
    constructor(limits, sendCredit, waitUntil, onCreditError) {
        this.limits = limits;
        this.sendCredit = sendCredit;
        this.waitUntil = waitUntil;
        this.onCreditError = onCreditError;
    }
    reset(dataChannels) {
        this.outboundStreamCredit.clear();
        this.inboundStreamCredit.clear();
        this.outboundChannelCredit.clear();
        this.inboundChannelCredit.clear();
        for (let channelId = 0; channelId < dataChannels; channelId += 1) {
            this.outboundChannelCredit.set(channelId, this.limits().channelCreditBytes);
            this.inboundChannelCredit.set(channelId, this.limits().channelCreditBytes);
        }
        this.wakeWaiters();
    }
    seedStream(streamId) {
        for (const kind of CREDIT_KINDS) {
            this.outboundStreamCredit.set(creditKey(streamId, kind), this.limits().streamCreditBytes);
            this.inboundStreamCredit.set(creditKey(streamId, kind), this.limits().streamCreditBytes);
        }
    }
    deleteStream(streamId) {
        for (const kind of CREDIT_KINDS) {
            this.outboundStreamCredit.delete(creditKey(streamId, kind));
            this.inboundStreamCredit.delete(creditKey(streamId, kind));
        }
        this.wakeWaiters();
    }
    applyStreamCredit(streamId, metadata) {
        const key = creditKey(streamId, metadata.kind);
        this.outboundStreamCredit.set(key, Math.min(MAX_CREDIT_BYTES, (this.outboundStreamCredit.get(key) ?? 0) + metadata.bytes));
        this.wakeWaiters();
    }
    applyChannelCredit(channelId, metadata) {
        this.outboundChannelCredit.set(channelId, Math.min(MAX_CREDIT_BYTES, (this.outboundChannelCredit.get(channelId) ?? 0) + metadata.bytes));
        this.wakeWaiters();
    }
    async waitForOutbound(streamId, channelId, kind, bytes, canWait) {
        if (!canWait()) {
            throw new Error("Stream unavailable");
        }
        while (!this.hasOutbound(streamId, channelId, kind, bytes)) {
            await new Promise((resolve) => this.waiters.add(resolve));
            if (!canWait()) {
                throw new Error("Stream unavailable");
            }
        }
    }
    decrementOutbound(streamId, channelId, kind, bytes) {
        const streamKey = creditKey(streamId, kind);
        this.outboundStreamCredit.set(streamKey, consumeCredit(this.outboundStreamCredit.get(streamKey) ?? 0, bytes));
        this.outboundChannelCredit.set(channelId, consumeCredit(this.outboundChannelCredit.get(channelId) ?? 0, bytes));
    }
    consumeInbound(streamId, channelId, kind, bytes) {
        const streamKey = creditKey(streamId, kind);
        const streamCredit = this.inboundStreamCredit.get(streamKey) ?? 0;
        const channelCredit = this.inboundChannelCredit.get(channelId) ?? 0;
        if (streamCredit < bytes || channelCredit < bytes) {
            return false;
        }
        this.inboundStreamCredit.set(streamKey, streamCredit - bytes);
        this.inboundChannelCredit.set(channelId, channelCredit - bytes);
        return true;
    }
    grantInbound(streamId, channelId, kind, bytes) {
        if (bytes <= 0) {
            return;
        }
        const streamKey = creditKey(streamId, kind);
        this.inboundStreamCredit.set(streamKey, addCredit(this.inboundStreamCredit.get(streamKey) ?? 0, bytes));
        this.inboundChannelCredit.set(channelId, addCredit(this.inboundChannelCredit.get(channelId) ?? 0, bytes));
        this.waitUntil(this.sendCredit(channelId, FRAME_TYPE_STREAM_CREDIT, streamId, {
            kind,
            bytes,
        })
            .then(() => this.sendCredit(channelId, FRAME_TYPE_CHANNEL_CREDIT, 0n, { bytes }))
            .catch((error) => this.onCreditError(error)));
    }
    wakeWaiters() {
        for (const waiter of this.waiters) {
            waiter();
        }
        this.waiters.clear();
    }
    hasOutbound(streamId, channelId, kind, bytes) {
        return ((this.outboundStreamCredit.get(creditKey(streamId, kind)) ?? 0) >=
            bytes && (this.outboundChannelCredit.get(channelId) ?? 0) >= bytes);
    }
}
function creditKey(streamId, kind) {
    return `${streamId.toString()}:${kind}`;
}
