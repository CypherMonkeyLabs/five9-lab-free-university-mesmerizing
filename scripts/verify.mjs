import { readFileSync, statSync, readdirSync } from "node:fs";
import { diagram, diagramIds, flowIds } from "../campus/js/diagrams.js";
import { chartIds, chartStrip } from "../campus/js/charts.js";
import { join } from "node:path";

const root = new URL("..", import.meta.url).pathname;
const read = (path) => JSON.parse(readFileSync(join(root, path), "utf8"));
const catalog = read("campus/data/catalog.json");
let lessons = 0;
let quiz = 0;
let cards = 0;
let labs = 0;
let faults = 0;
let cites = 0;
const problems = [];

for (const meta of catalog.tracks) {
  const track = read(`campus/data/${meta.file}`);
  if (track.id !== meta.id) problems.push(`id ${meta.id}`);
  for (const lesson of track.lessons) {
    lessons += 1;
    quiz += lesson.quiz.length;
    cards += lesson.cards.length;
    if (lesson.lab) labs += 1;
    if (lesson.fault) faults += 1;
    if (!lesson.cites?.length) problems.push(`${track.id}/${lesson.id} cites`);
    if (!lesson.figure || !lesson.flow?.steps?.length) problems.push(`${track.id}/${lesson.id} figure or flow`);
    for (const cite of lesson.cites || []) {
      cites += 1;
      if (!String(cite.url).startsWith("https://")) problems.push(`${track.id}/${lesson.id} url`);
    }
  }
}

const interview = read("campus/data/interview.json");
const bosses = read("campus/data/boss.json");
const eco = read("campus/data/ecosystem.json");
if (interview.items.length < 36) problems.push("interview");
if (bosses.items.length < 8) problems.push("boss");
if (eco.glossary.length < 30) problems.push("glossary");
const uni = read("campus/data/university.json");
if (!uni.ports || uni.ports.length < 10) problems.push("ports");
if (!uni.playbooks || uni.playbooks.length < 8) problems.push("playbooks");
if (diagramIds.length < 30) problems.push("diagrams");
if (diagramIds.length < 25) problems.push("diagrams25");
if (flowIds.length < 12) problems.push("flows");
for (const id of flowIds) {
  if (!diagram(id).includes("flow-line")) problems.push(`flow-anim ${id}`);
}
if (chartIds.length < 6) problems.push("chartIds");
const chartHtml = chartStrip(catalog, uni);
const chartSvgs = chartHtml.split("<svg").length - 1;
if (chartSvgs < 6) problems.push("chartSvg");
const sheets = read("campus/downloads/manifest.json");
const htmlSheets = sheets.files.filter((file) => file.href.endsWith(".html"));
const pdfSheets = sheets.files.filter((file) => file.href.endsWith(".pdf"));
const pngSheets = sheets.files.filter((file) => file.href.endsWith(".png"));
if (htmlSheets.length < 10) problems.push("html-sheets");
if (pdfSheets.length < 10) problems.push("pdf-sheets");
if (pngSheets.length < 10) problems.push("png-sheets");
for (const file of htmlSheets) {
  const text = readFileSync(join(root, "campus", file.href), "utf8");
  if (!text.includes("https://cyphermonkeylabs.com")) problems.push(`sheet-labs ${file.href}`);
  if (!text.includes("https://linktr.ee/cyphermonkey")) problems.push(`sheet-tree ${file.href}`);
  if (!text.includes("https://github.com/cipher0x9/five9-lab-free-university-mesmerizing")) problems.push(`sheet-repo ${file.href}`);
  if (!text.includes("CC BY-NC-SA")) problems.push(`sheet-license ${file.href}`);
  if (/linkedin/i.test(text)) problems.push(`sheet-linkedin ${file.href}`);
  if (/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i.test(text)) problems.push(`sheet-email ${file.href}`);
}
const page = readFileSync(join(root, "campus/index.html"), "utf8");
const license = readFileSync(join(root, "LICENSE"), "utf8");
const rootPage = readFileSync(join(root, "index.html"), "utf8");
const uniJs = readFileSync(join(root, "campus/js/university.js"), "utf8");
for (const label of ["Diagrams", "Flows", "Charts", "Cheat Codes", "Play", "Ecosystem", "Downloads", "Careers"]) {
  if (!page.includes(`>${label}<`)) problems.push(`menu ${label}`);
}
if (!page.includes('id="primary-menu"') || !page.includes('id="crumbs"')) problems.push("chrome");
if (!uniJs.includes('id="fold"') || !uniJs.includes("track-band")) problems.push("surfaces");
for (const href of [
  "https://cipher0x9.github.io/webex-lab-free-university-mesmerizing/",
  "https://cipher0x9.github.io/uc-lab-free-university-mesmerizing/",
  "https://cipher0x9.github.io/ai-lab-free-university-mesmerizing/",
  "https://cipher0x9.github.io/five9-lab-free-university-mesmerizing/"
]) {
  if (!page.includes(href) || !rootPage.includes(href)) problems.push(`sibling ${href}`);
}
if (!license.includes("MIT") || !license.includes("CC BY-NC-SA")) problems.push("license");
if (!page.includes("MIT code, CC BY-NC-SA content")) problems.push("footer-license");
const vendorOk = ["anime", "rough", "d3", "confetti", "markmap", "three"].every((name) => (
  readdirSync(join(root, "campus/vendor", name)).some((file) => file.toLowerCase().startsWith("license"))
));
if (!vendorOk) problems.push("vendor-license");

const shellFiles = [
  "campus/index.html",
  "campus/css/app.css",
  "campus/js/app.js",
  "campus/js/loaders.js"
];
const shell = shellFiles.reduce((sum, file) => sum + statSync(join(root, file)).size, 0);
const gates = [
  [catalog.tracks.length >= 15, "tracks"],
  [lessons >= 100, "lessons"],
  [quiz >= 600, "quiz"],
  [labs >= 20, "labs"],
  [faults >= 30, "faults"],
  [shell < 500000, "shell"],
  [problems.length === 0, "problems"]
];

const report = {
  tracks: catalog.tracks.length,
  lessons,
  quiz,
  cards,
  labs,
  faults,
  cites,
  interview: interview.items.length,
  bosses: bosses.items.length,
  glossary: eco.glossary.length,
  diagrams: diagramIds.length,
  flows: flowIds.length,
  charts: chartIds.length,
  chartSvgs,
  htmlSheets: htmlSheets.length,
  pdfSheets: pdfSheets.length,
  pngSheets: pngSheets.length,
  shellBytes: shell,
  problems
};
console.log(JSON.stringify(report, null, 2));
if (gates.some(([ok]) => !ok)) process.exit(1);
