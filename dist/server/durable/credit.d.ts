import { type ChannelCreditMetadata, type DataKind, FRAME_TYPE_CHANNEL_CREDIT, FRAME_TYPE_STREAM_CREDIT, type StreamCreditMetadata, type TunnelLimits } from "@hostc/protocol";
type SendCredit = (channelId: number, frameType: typeof FRAME_TYPE_STREAM_CREDIT | typeof FRAME_TYPE_CHANNEL_CREDIT, streamId: bigint, metadata: StreamCreditMetadata | ChannelCreditMetadata) => Promise<void>;
export declare class TunnelCreditController {
    private readonly limits;
    private readonly sendCredit;
    private readonly waitUntil;
    private readonly onCreditError;
    private readonly outboundStreamCredit;
    private readonly inboundStreamCredit;
    private readonly outboundChannelCredit;
    private readonly inboundChannelCredit;
    private readonly waiters;
    constructor(limits: () => TunnelLimits, sendCredit: SendCredit, waitUntil: (promise: Promise<unknown>) => void, onCreditError: (error: unknown) => void);
    reset(dataChannels: number): void;
    seedStream(streamId: bigint): void;
    deleteStream(streamId: bigint): void;
    applyStreamCredit(streamId: bigint, metadata: StreamCreditMetadata): void;
    applyChannelCredit(channelId: number, metadata: ChannelCreditMetadata): void;
    waitForOutbound(streamId: bigint, channelId: number, kind: DataKind, bytes: number, canWait: () => boolean): Promise<void>;
    decrementOutbound(streamId: bigint, channelId: number, kind: DataKind, bytes: number): void;
    consumeInbound(streamId: bigint, channelId: number, kind: DataKind, bytes: number): boolean;
    grantInbound(streamId: bigint, channelId: number, kind: DataKind, bytes: number): void;
    wakeWaiters(): void;
    private hasOutbound;
}
export {};
