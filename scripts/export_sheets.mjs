import { spawn } from "node:child_process";
import { readdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { setTimeout as delay } from "node:timers/promises";

const root = new URL("..", import.meta.url).pathname;
const port = 9335;
const targets = [];
for (const dir of ["downloads/sheets", "downloads/templates"]) {
  for (const name of readdirSync(join(root, dir))) {
    if (name.endsWith(".html")) targets.push(join(dir, name));
  }
}
targets.push("downloads/flashcards.html");

const chrome = spawn("google-chrome", [
  "--headless=new",
  "--disable-gpu",
  "--no-sandbox",
  "--disable-dev-shm-usage",
  `--user-data-dir=/tmp/chrome-export-${port}`,
  `--remote-debugging-port=${port}`,
  "about:blank"
], { stdio: "ignore" });

async function waitJson(url) {
  for (let i = 0; i < 50; i += 1) {
    try {
      const res = await fetch(url);
      if (res.ok) return await res.json();
    } catch {
      /* chrome still starting */
    }
    await delay(200);
  }
  throw new Error(`cdp timeout ${url}`);
}

const version = await waitJson(`http://127.0.0.1:${port}/json/version`);
const ws = new WebSocket(version.webSocketDebuggerUrl);
let seq = 0;
const pending = new Map();
const waits = [];
ws.addEventListener("message", (event) => {
  const msg = JSON.parse(event.data);
  if (msg.id && pending.has(msg.id)) {
    pending.get(msg.id)(msg);
    pending.delete(msg.id);
  }
  for (const wait of waits) wait(msg);
});
await new Promise((resolve) => ws.addEventListener("open", resolve, { once: true }));

function send(method, params = {}, sessionId) {
  return new Promise((resolve) => {
    const id = ++seq;
    pending.set(id, resolve);
    const payload = { id, method, params };
    if (sessionId) payload.sessionId = sessionId;
    ws.send(JSON.stringify(payload));
  });
}

function loadFired(sessionId) {
  return new Promise((resolve) => {
    const timer = setTimeout(() => resolve("timeout"), 8000);
    const onMsg = (msg) => {
      if (msg.method === "Page.loadEventFired" && msg.sessionId === sessionId) {
        clearTimeout(timer);
        waits.splice(waits.indexOf(onMsg), 1);
        resolve("load");
      }
    };
    waits.push(onMsg);
  });
}

const created = await send("Target.createTarget", { url: "about:blank" });
const attached = await send("Target.attachToTarget", { targetId: created.result.targetId, flatten: true });
const sessionId = attached.result.sessionId;
await send("Page.enable", {}, sessionId);

let done = 0;
for (const rel of targets) {
  const url = `file://${join(root, rel)}`;
  const loaded = loadFired(sessionId);
  await send("Page.navigate", { url }, sessionId);
  await loaded;
  await delay(150);
  const pdf = await send("Page.printToPDF", { printBackground: true, preferCSSPageSize: true }, sessionId);
  writeFileSync(join(root, rel.replace(/\.html$/, ".pdf")), Buffer.from(pdf.result.data, "base64"));
  if (rel.startsWith("downloads/sheets/")) {
    const metrics = await send("Page.getLayoutMetrics", {}, sessionId);
    const width = Math.ceil(metrics.result.cssContentSize.width);
    const height = Math.min(4000, Math.ceil(metrics.result.cssContentSize.height));
    await send("Emulation.setDeviceMetricsOverride", {
      width: Math.max(800, width),
      height,
      deviceScaleFactor: 1,
      mobile: false
    }, sessionId);
    const shot = await send("Page.captureScreenshot", {
      format: "png",
      captureBeyondViewport: true,
      clip: { x: 0, y: 0, width: Math.max(800, width), height, scale: 1 }
    }, sessionId);
    writeFileSync(join(root, rel.replace(/\.html$/, ".png")), Buffer.from(shot.result.data, "base64"));
  }
  done += 1;
  if (done % 10 === 0) console.log(`exported ${done}/${targets.length}`);
}
console.log(`exported ${done}`);
ws.close();
chrome.kill();
process.exit(0);
