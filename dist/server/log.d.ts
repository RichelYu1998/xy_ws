export type JsonLog = Record<string, unknown>;
export declare function log(fields: JsonLog): void;
export declare function redactLogFields(fields: JsonLog): JsonLog;
