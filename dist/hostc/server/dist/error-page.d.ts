export type TunnelErrorPageOptions = {
    status: number;
    title: string;
    eyebrow: string;
    message: string;
    hint?: string;
};
export declare function tunnelErrorResponse(request: Request, options: TunnelErrorPageOptions): Response;
