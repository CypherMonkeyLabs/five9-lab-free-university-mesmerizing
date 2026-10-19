import { test, expect } from "@playwright/test";
import fs from "node:fs";
import path from "node:path";

const shot = path.join("docs", "screenshots", "wave");
fs.mkdirSync(shot, { recursive: true });

function quiet(page) {
  const errors = [];
  page.on("pageerror", (err) => errors.push(String(err)));
  return errors;
}

async function ready(page) {
  await page.addInitScript(() => {
    localStorage.setItem("f9-tour", "1");
    localStorage.setItem("f9-greeted", "1");
    localStorage.setItem("f9-offers-stop", "1");
  });
}

test("home, guide, and lesson at both sizes", async ({ browser }) => {
  for (const viewport of [
    { width: 1440, height: 900, name: "1440" },
    { width: 390, height: 844, name: "390" },
  ]) {
    const context = await browser.newContext({
      viewport: { width: viewport.width, height: viewport.height },
      hasTouch: viewport.width < 500,
      serviceWorkers: "allow",
      reducedMotion: "reduce",
    });
    const page = await context.newPage();
    await ready(page);
    const errors = quiet(page);
    await page.goto("/index.html");
    await expect(page.locator(".hero-title")).toContainText("Learn the floor");
    await page.screenshot({ path: path.join(shot, `home-${viewport.name}.png`) });
    await page.locator(".cg-monkey").click();
    await expect(page.locator("#cg-panel")).toBeVisible();
    await page.waitForFunction(() => window.__f9botReady === true);
    await expect(page.locator("#py-chat-input")).toBeVisible();
    await page.locator("#py-chat-input").fill("What is a skill group?");
    await page.locator("#py-chat-input").press("Enter");
    await expect(page.locator(".py-msg-bot").last()).toContainText(/skill/i);
    await expect(page.locator(".py-msg-bot").last().locator("a")).toHaveCount(1);
    await page.screenshot({ path: path.join(shot, `bot-${viewport.name}.png`) });
    await page.goto("/rooms/t05-l01-preview-lets-the-agent-read-first.html");
    await expect(page.locator("h1")).toBeVisible();
    await page.screenshot({ path: path.join(shot, `lesson-${viewport.name}.png`) });
    expect(errors, errors.join("\n")).toEqual([]);
    await context.close();
  }
});

test("short phone shows the chat input and Send", async ({ browser }) => {
  const context = await browser.newContext({
    viewport: { width: 390, height: 430 },
    hasTouch: true,
    reducedMotion: "reduce",
  });
  const page = await context.newPage();
  await ready(page);
  await page.goto("/index.html");
  await page.locator(".cg-monkey").click();
  await page.waitForFunction(() => window.__f9botReady === true);
  const input = page.locator("#py-chat-input");
  const send = page.locator(".py-chat-form button[type='submit']");
  await expect(input).toBeVisible();
  await expect(send).toBeVisible();
  const inputBox = await input.boundingBox();
  const sendBox = await send.boundingBox();
  expect(inputBox).toBeTruthy();
  expect(sendBox).toBeTruthy();
  expect(inputBox.y).toBeGreaterThanOrEqual(0);
  expect(inputBox.y + inputBox.height).toBeLessThanOrEqual(430);
  expect(sendBox.y).toBeGreaterThanOrEqual(0);
  expect(sendBox.y + sendBox.height).toBeLessThanOrEqual(430);
  const uncovered = await page.evaluate(() => {
    function hit(el) {
      const box = el.getBoundingClientRect();
      const x = box.left + box.width / 2;
      const y = box.top + box.height / 2;
      const top = document.elementFromPoint(x, y);
      return Boolean(top && (top === el || el.contains(top)));
    }
    return {
      input: hit(document.querySelector("#py-chat-input")),
      send: hit(document.querySelector(".py-chat-form button[type='submit']")),
    };
  });
  expect(uncovered.input).toBe(true);
  expect(uncovered.send).toBe(true);
  await page.screenshot({ path: path.join(shot, "bot-390x430.png") });
  await context.close();
});

test("chat input fills the phone sheet", async ({ browser }) => {
  for (const viewport of [
    { width: 390, height: 844 },
    { width: 390, height: 430 },
  ]) {
    const context = await browser.newContext({
      viewport,
      hasTouch: true,
      reducedMotion: "reduce",
    });
    const page = await context.newPage();
    await ready(page);
    await page.goto("/index.html");
    await page.locator(".cg-monkey").click();
    await page.waitForFunction(() => window.__f9botReady === true);
    const input = page.locator("#py-chat-input");
    await expect(input).toBeVisible();
    const box = await input.boundingBox();
    expect(box, `${viewport.width}x${viewport.height}`).toBeTruthy();
    expect(box.width, `${viewport.width}x${viewport.height} input width`).toBeGreaterThanOrEqual(180);
    expect(box.y, `${viewport.width}x${viewport.height} input top`).toBeGreaterThanOrEqual(0);
    expect(box.y + box.height, `${viewport.width}x${viewport.height} input bottom`).toBeLessThanOrEqual(viewport.height);
    await context.close();
  }
});

test("answer log stays readable on both phones", async ({ browser }) => {
  for (const viewport of [
    { width: 390, height: 844 },
    { width: 390, height: 430 },
  ]) {
    const context = await browser.newContext({
      viewport,
      hasTouch: true,
      reducedMotion: "reduce",
    });
    const page = await context.newPage();
    await ready(page);
    await page.goto("/index.html");
    await page.locator(".cg-monkey").click();
    await page.waitForFunction(() => window.__f9botReady === true);
    if (viewport.height === 430) {
      await expect(page.locator(".chrome-stack")).toBeHidden();
      await expect(page.locator(".phone-dock")).toBeHidden();
    }
    await page.locator("#py-chat-input").fill("What is a skill group?");
    await page.locator("#py-chat-input").press("Enter");
    const log = page.locator(".py-chat-log");
    await expect(log).toBeVisible();
    await expect(log.locator(".py-msg-bot").last()).toContainText(/skill/i);
    const visible = await log.evaluate((el) => {
      const box = el.getBoundingClientRect();
      const panel = document.querySelector("#cg-panel").getBoundingClientRect();
      const top = Math.max(box.top, panel.top, 0);
      const bottom = Math.min(box.bottom, panel.bottom, window.innerHeight);
      return { height: box.height, visible: Math.max(0, bottom - top) };
    });
    expect(visible.height, `${viewport.width}x${viewport.height} log height`).toBeGreaterThanOrEqual(120);
    expect(visible.visible, `${viewport.width}x${viewport.height} visible log`).toBeGreaterThanOrEqual(120);
    await context.close();
  }
});

test("routing desk is a labelled simulation", async ({ page }) => {
  await ready(page);
  await page.goto("/play.html");
  await page.locator("[data-skill]").fill("Billing");
  await page.locator("[data-mode]").selectOption("preview");
  await page.locator("[data-route-run]").click();
  const out = page.locator("[data-route-out]");
  await expect(out).toContainText("Simulation");
  await expect(out).toContainText("Billing");
  await expect(out).toContainText("does not call Five9");
  await expect(out).toContainText("Preview");
});

test("offline shell reloads a lesson and the guide", async ({ browser }) => {
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    serviceWorkers: "allow",
    reducedMotion: "reduce",
  });
  const page = await context.newPage();
  await ready(page);
  await page.goto("/index.html");
  await page.waitForFunction(async () => {
    const reg = await navigator.serviceWorker.ready;
    return Boolean(reg && reg.active);
  });
  await page.reload();
  await expect(page.locator(".hero-title")).toBeVisible();
  await context.setOffline(true);
  await page.reload();
  await expect(page.locator(".hero-title")).toContainText("Learn the floor");
  await page.goto("/rooms/t05-l01-preview-lets-the-agent-read-first.html");
  await expect(page.locator("h1")).toContainText(/preview/i);
  await page.locator(".cg-monkey").click();
  await page.waitForFunction(() => window.__f9botReady === true);
  await page.locator("#py-chat-input").fill("What is preview dialing?");
  await page.locator("#py-chat-input").press("Enter");
  const bot = page.locator(".py-msg-bot").last();
  await expect(bot).toContainText(/preview/i);
  await expect(bot).not.toContainText("I don't have that yet");
  await context.close();
});
