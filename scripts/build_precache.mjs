/* Fill SHELL_ASSETS in sw.js. Required chat files must fit under 3.5 MB. */
import fs from "node:fs";
import path from "node:path";

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const budget = 3_500_000;
const required = [
  "index.html",
  "offline.html",
  "start.html",
  "play.html",
  "manifest.webmanifest",
  "favicon.svg",
  "assets/icons/icon-192.png",
  "assets/icons/icon-512.png",
  "assets/icons/icon-maskable-512.png",
  "assets/css/frame.css",
  "assets/css/wow.css",
  "assets/css/footer.css",
  "assets/js/frame.js",
  "assets/js/university.js",
  "assets/js/route-sim.js",
  "guide/guide.js",
  "guide/guide.css",
  "shared/pybot-chat/engine.js",
  "shared/pybot-chat/ui.js",
  "shared/pybot-chat/chat.css",
  "js/content/f9bot-index.json",
  "rooms/t05-l01-preview-lets-the-agent-read-first.html",
];

const chosen = [];
let total = 0;
const missing = [];
for (const rel of required) {
  const abs = path.join(root, rel);
  if (!fs.existsSync(abs)) {
    missing.push(rel);
    continue;
  }
  const size = fs.statSync(abs).size;
  if (total + size > budget) {
    console.error(`precache over budget at ${rel}`);
    process.exit(1);
  }
  chosen.push(rel);
  total += size;
}
if (missing.length) {
  console.error("missing precache files", missing.join(", "));
  process.exit(1);
}
const body = ["  \"./\",", ...chosen.map((rel) => `  "./${rel}",`)].join("\n");
const swPath = path.join(root, "sw.js");
let sw = fs.readFileSync(swPath, "utf8");
if (!sw.includes("five9-university-r9")) {
  console.error("cache name was not bumped");
  process.exit(1);
}
sw = sw.replace(/const SHELL_ASSETS = \[[\s\S]*?\];/, `const SHELL_ASSETS = [\n${body}\n];`);
fs.writeFileSync(swPath, sw);
console.log(`precache ${chosen.length + 1} files, ${total} bytes, budget ${budget}`);
