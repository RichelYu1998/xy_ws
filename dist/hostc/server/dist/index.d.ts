import { HostcTunnel } from "./durable/tunnel";
import type { HostcEnv } from "./env";
export { HostcTunnel };
declare const _default: {
    fetch(request: Request<unknown, IncomingRequestCfProperties<unknown>>, env: HostcEnv): Promise<Response>;
};
export default _default;
export declare function handleRequest(request: Request, env: HostcEnv): Promise<Response>;
