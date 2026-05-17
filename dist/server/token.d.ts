export type TokenAudience = "connect";
export type TokenPayload = {
    v: 1;
    aud: TokenAudience;
    tunnelId: string;
    clientConnectionId?: string;
    exp: number;
    nonce: string;
};
export type VerifyTokenOptions = {
    audience: TokenAudience;
    tunnelId: string;
    clientConnectionId?: string;
    now?: number;
};
export declare function signToken(secret: string, payload: TokenPayload): Promise<string>;
export declare function verifyToken(secret: string, token: string, options: VerifyTokenOptions): Promise<TokenPayload | null>;
export declare function createTokenPayload(audience: TokenAudience, tunnelId: string, ttlSeconds: number, clientConnectionId?: string, now?: number): TokenPayload;
export declare function redactToken(value: string): string;
