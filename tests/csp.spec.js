import { test, expect } from "@playwright/test";
import { spawn } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const REPO = "five9-lab-free-university-mesmerizing";
const PORT = 8766;
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const CSP = "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; media-src 'self' blob: data:; font-src 'self' data:; connect-src 'self'; worker-src 'self' blob:; object-src 'none'; base-uri 'self'; form-action 'self'";

let server;
let mount;

function htmlFiles(dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === "node_modules" || entry.name === ".git") continue;
    const abs = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...htmlFiles(abs));
    else if (entry.name.endsWith(".html")) out.push(abs);
  }
  return out;
}

function lessonSample() {
  const rooms = fs.readdirSync(path.join(ROOT, "rooms")).filter((name) => name.endsWith(".html")).sort();
  const step = Math.max(1, Math.floor(rooms.length / 32));
  const picked = [];
  for (let i = 0; i < rooms.length && picked.length < 32; i += step) picked.push(`rooms/${rooms[i]}`);
  return picked;
}

test.beforeAll(async () => {
  mount = fs.mkdtempSync(path.join(os.tmpdir(), "f9-csp-"));
  fs.symlinkSync(ROOT, path.join(mount, REPO));
  server = spawn("python3", ["-m", "http.server", String(PORT), "--bind", "127.0.0.1", "--directory", mount], {
    stdio: "ignore",
  });
  const deadline = Date.now() + 10000;
  while (Date.now() < deadline) {
    try {
      const origin = "http://127.0.0.1:" + PORT;
      const res = await fetch(origin + "/" + REPO + "/index.html");
      if (res.ok) return;
    } catch { /* server still starting */ }
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
  throw new Error("prefixed static server did not start");
});

test.afterAll(async () => {
  if (server) server.kill();
  if (mount) fs.rmSync(mount, { recursive: true, force: true });
});

test("every html page carries the strict CSP and no inline script", () => {
  const files = htmlFiles(ROOT);
  expect(files.length).toBeGreaterThan(1000);
  const problems = [];
  for (const file of files) {
    const text = fs.readFileSync(file, "utf8");
    const rel = path.relative(ROOT, file);
    if (!text.includes(`content="${CSP}"`)) problems.push(`${rel} missing CSP`);
    if (/<script\b(?![^>]*\bsrc=)[^>]*>/i.test(text)) problems.push(`${rel} inline script`);
    if (/\son[a-z]+\s*=/i.test(text)) problems.push(`${rel} inline handler`);
  }
  expect(problems, problems.slice(0, 12).join("\n")).toEqual([]);
});

test("mounted pages have no CSP violations and the main controls work", async ({ browser }) => {
  test.setTimeout(240000);
  const pages = [
    ...fs.readdirSync(ROOT).filter((name) => name.endsWith(".html")).sort(),
    "tracks/t01.html",
    "campus/index.html",
    "downloads/flashcards.html",
    ...lessonSample(),
  ];
  expect(pages.filter((href) => href.startsWith("rooms/")).length).toBeGreaterThanOrEqual(30);

  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  await context.addInitScript(() => {
    localStorage.setItem("f9-tour", "1");
    localStorage.setItem("f9-greeted", "1");
    localStorage.setItem("f9-offers-stop", "1");
    window.__csp = [];
    document.addEventListener("securitypolicyviolation", (event) => {
      window.__csp.push(`${event.violatedDirective} ${event.blockedURI}`);
    });
  });
  const page = await context.newPage();
  const pageErrors = [];
  const consoleErrors = [];
  let current = "";
  page.on("pageerror", (err) => pageErrors.push(`${current}: ${err}`));
  page.on("console", (msg) => {
    if (msg.type() === "error") consoleErrors.push(`${current}: ${msg.text()}`);
  });

  const violations = [];
  for (const href of pages) {
    current = href;
    const url = `http://127.0.0.1:${PORT}/${REPO}/${href}`;
    const response = await page.goto(url, { waitUntil: "domcontentloaded" });
    expect(response && response.ok(), href).toBeTruthy();
    await page.waitForLoadState("load");
    const found = await page.evaluate(() => window.__csp.splice(0));
    for (const item of found) violations.push(`${href}: ${item}`);
  }

  current = "index.html#interact";
  await page.goto(`http://127.0.0.1:${PORT}/${REPO}/index.html`, { waitUntil: "domcontentloaded" });
  await page.locator("[data-theme-toggle]").click();
  await expect(page.locator("html")).toHaveAttribute("data-theme", "midnight");
  await page.locator("#tour-menu").click();
  await expect(page.locator("#site-drawer")).toHaveAttribute("aria-hidden", "false");
  await page.locator("[data-site-search] input").fill("skill");
  await page.locator("[data-site-search]").evaluate((form) => form.requestSubmit());
  await page.waitForURL(/search\.html\?q=skill/);
  await expect(page.locator("h1")).toContainText(/search/i);

  const lesson = pages.find((href) => href.startsWith("rooms/"));
  current = `${lesson}#quiz`;
  await page.goto(`http://127.0.0.1:${PORT}/${REPO}/${lesson}`, { waitUntil: "domcontentloaded" });
  await page.locator("[data-quiz] input[type=radio]").nth(1).check();
  await page.locator("[data-quiz-check]").click();
  await expect(page.locator(".quiz-score")).toContainText(/of/);

  current = "listen.html#audio";
  await page.goto(`http://127.0.0.1:${PORT}/${REPO}/listen.html`, { waitUntil: "domcontentloaded" });
  const played = await page.locator("audio").first().evaluate(async (audio) => {
    try {
      await audio.play();
      return audio.error ? audio.error.message : "";
    } catch (err) {
      return String(err);
    }
  });
  expect(played, "audio play").not.toMatch(/Content Security Policy|Refused/i);

  current = "campus/index.html#settle";
  await page.goto(`http://127.0.0.1:${PORT}/${REPO}/campus/index.html`, { waitUntil: "load" });
  await page.waitForTimeout(500);

  const late = await page.evaluate(() => window.__csp.splice(0));
  for (const item of late) violations.push(`interaction: ${item}`);

  const cspConsole = consoleErrors.filter((line) => /Content Security Policy|Refused to/i.test(line));
  expect(violations, violations.join("\n")).toEqual([]);
  expect(cspConsole, cspConsole.join("\n")).toEqual([]);
  expect(pageErrors, pageErrors.join("\n")).toEqual([]);
  await context.close();
});
