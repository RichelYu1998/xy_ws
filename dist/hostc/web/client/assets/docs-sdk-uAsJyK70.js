import{k as e,t}from"./jsx-runtime-BAhgWS5N.js";import{a as n,i as r,n as i,o as a}from"./docs-layout-C_Zo4PfI.js";import{n as o,r as s,t as c}from"./alert-ClCN6BPj.js";var l=t(),u=[{title:`Install`,href:`#install`},{title:`Node.js integration`,href:`#example`},{title:`Protocol boundary`,href:`#protocol-boundary`}],d=`npm install @hostc/client`,f=`import { HostcClient, localOriginAdapter } from "@hostc/client";

const client = new HostcClient({
  serverUrl: "https://hostc.example.com",
  upstream: localOriginAdapter({
    origin: "http://127.0.0.1:3000",
  }),
});

client.on("ready", ({ publicUrl }) => {
  console.log(\`Tunnel ready: \${publicUrl}\`);
});

client.on("reconnecting", ({ reason }) => {
  console.log(\`Reconnecting: \${reason}\`);
});

await client.start();`;function p(e){return[{title:`Client SDK | hostc Docs`},{name:`description`,content:`Embed hostc tunnels with the @hostc/client SDK.`}]}var m=e(function(){return(0,l.jsxs)(r,{eyebrow:`Client SDK`,title:`Embed hostc in your own product.`,description:`Use @hostc/client when tunnels need to live inside a desktop app, daemon, custom CLI, or Node.js runtime.`,toc:u,children:[(0,l.jsx)(n,{id:`install`,title:`Install`,description:`The SDK is the public integration boundary. Application code only needs @hostc/client.`,children:(0,l.jsx)(i,{label:`npm`,code:d})}),(0,l.jsx)(n,{id:`example`,title:`Node.js integration`,description:`Create a client, point it at your hostc server, and forward traffic to a local origin.`,children:(0,l.jsx)(i,{label:`Example`,code:f,language:`ts`})}),(0,l.jsx)(n,{id:`protocol-boundary`,title:`Protocol boundary`,description:`The SDK uses the v4 protocol internally, but protocol frames and stream internals are not public SDK API.`,children:(0,l.jsxs)(c,{children:[(0,l.jsx)(s,{children:`Use the SDK, not the protocol package.`}),(0,l.jsxs)(o,{children:[(0,l.jsx)(a,{children:`@hostc/protocol`}),` is the internal wire-contract source of truth. It is bundled into`,` `,(0,l.jsx)(a,{children:`@hostc/client`}),` so your app only needs one public dependency.`]})]})})]})});export{m as default,p as meta};