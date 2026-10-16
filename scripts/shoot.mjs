import { spawn } from "node:child_process";
import { mkdirSync, writeFileSync } from "node:fs";
import { setTimeout as delay } from "node:timers/promises";

const root = new URL("..", import.meta.url).pathname;
const out = `${root}docs/screenshots/round2`;
mkdirSync(out, { recursive: true });
const port = 9341;
const httpPort = 8766;

const chrome = spawn("google-chrome", [
  "--headless=new",
  "--disable-gpu",
  "--no-sandbox",
  "--disable-dev-shm-usage",
  `--user-data-dir=/tmp/chrome-shoot-${port}`,
  `--remote-debugging-port=${port}`,
  "about:blank"
], { stdio: "ignore" });

async function waitOk(url, asJson) {
  for (let i = 0; i < 50; i += 1) {
    try {
      const res = await fetch(url);
      if (res.ok) return asJson ? await res.json() : true;
    } catch {
      /* starting */
    }
    await delay(200);
  }
  throw new Error(`timeout ${url}`);
}

await waitOk(`http://127.0.0.1:${httpPort}/index.html`, false);
const version = await waitOk(`http://127.0.0.1:${port}/json/version`, true);
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
    const timer = setTimeout(resolve, 8000);
    const onMsg = (msg) => {
      if (msg.method === "Page.loadEventFired" && msg.sessionId === sessionId) {
        clearTimeout(timer);
        waits.splice(waits.indexOf(onMsg), 1);
        resolve();
      }
    };
    waits.push(onMsg);
  });
}

const created = await send("Target.createTarget", { url: "about:blank" });
const attached = await send("Target.attachToTarget", { targetId: created.result.targetId, flatten: true });
const sessionId = attached.result.sessionId;
await send("Page.enable", {}, sessionId);
await send("Runtime.enable", {}, sessionId);
await send("Network.enable", {}, sessionId);
await send("Network.setCacheDisabled", { cacheDisabled: true }, sessionId);
await send("Page.addScriptToEvaluateOnNewDocument", {
  source: "try{localStorage.setItem('f9-tour','1');localStorage.setItem('f9-greeted','1');localStorage.setItem('f9-offers-stop','1');}catch(e){}"
}, sessionId);

const shots = [];
async function shoot(name, width, height, path, expression) {
  await send("Emulation.setDeviceMetricsOverride", {
    width, height, deviceScaleFactor: 1, mobile: width < 500
  }, sessionId);
  const loaded = loadFired(sessionId);
  await send("Page.navigate", { url: `http://127.0.0.1:${httpPort}/${path}` }, sessionId);
  await loaded;
  await delay(500);
  if (expression) {
    const result = await send("Runtime.evaluate", { expression, awaitPromise: true, returnByValue: true }, sessionId);
    if (result.result && result.result.exceptionDetails) {
      console.log(name, JSON.stringify(result.result.exceptionDetails));
    }
    await delay(400);
  }
  const shot = await send("Page.captureScreenshot", { format: "png" }, sessionId);
  const file = `${out}/${name}.png`;
  writeFileSync(file, Buffer.from(shot.result.data, "base64"));
  const measure = await send("Runtime.evaluate", {
    expression: `(() => {
      const panel = document.querySelector('.cg-panel');
      const dock = document.querySelector('.phone-dock');
      const banner = document.querySelector('.canon-banner');
      const head = document.querySelector('.chrome-stack');
      const greet = document.querySelector('.cg-greet');
      const pr = panel && !panel.hidden ? panel.getBoundingClientRect() : null;
      const dr = dock ? dock.getBoundingClientRect() : null;
      return {
        panel: pr && { top: pr.top, bottom: pr.bottom, height: pr.height },
        dockTop: dr && dr.top,
        bannerH: banner && banner.getBoundingClientRect().height,
        headH: head && head.getBoundingClientRect().height,
        greetHidden: greet ? greet.hidden : null,
        innerH: window.innerHeight
      };
    })()`,
    returnByValue: true
  }, sessionId);
  shots.push({ name, measure: measure.result && measure.result.result && measure.result.result.value });
  console.log(name, JSON.stringify(shots[shots.length - 1].measure));
}

await shoot("home-desktop", 1440, 900, "index.html");
await shoot("home-1280", 1280, 800, "index.html");
await shoot("home-scrolled", 1440, 900, "index.html", "window.scrollTo(0, 900);");
await shoot("menu-desktop", 1440, 900, "index.html", "document.querySelector('[data-open-menu]').click();");
await shoot("room-desktop", 1440, 900, "rooms/t01-l01-a-contact-center-is-not-a-phone-system.html");
await shoot("downloads-desktop", 1440, 900, "downloads.html");
await shoot("bot-desktop", 1440, 900, "index.html", "document.querySelector('.cg-monkey').click();");
await shoot("greet-desktop", 1440, 900, "index.html", "document.querySelector('.cg-root').classList.add('is-greet'); document.querySelector('.cg-greet').hidden=false;");
await shoot("home-phone", 390, 844, "index.html");
await shoot("menu-phone", 390, 844, "index.html", "document.querySelector('[data-open-menu]').click();");
await shoot("room-phone", 390, 844, "rooms/t01-l01-a-contact-center-is-not-a-phone-system.html");
await shoot("bot-phone", 390, 844, "index.html", "document.querySelector('.cg-monkey').click();");
await shoot("downloads-phone", 390, 844, "downloads.html");
await shoot("footer-desktop", 1440, 900, "index.html", "window.scrollTo(0, document.body.scrollHeight);");
await shoot("footer-1280", 1280, 800, "index.html", "window.scrollTo(0, document.body.scrollHeight);");
await shoot("footer-phone", 390, 844, "index.html", "window.scrollTo(0, document.body.scrollHeight);");

writeFileSync(`${out}/measures.json`, JSON.stringify(shots, null, 2));
ws.close();
chrome.kill();
process.exit(0);
