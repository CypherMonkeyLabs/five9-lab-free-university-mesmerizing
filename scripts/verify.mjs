import { readFileSync, statSync } from "node:fs";
import { diagramIds } from "../campus/js/diagrams.js";
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
const sheets = read("campus/downloads/manifest.json");
if (!sheets.files.some((file) => file.href.endsWith(".pdf"))) problems.push("pdf");
if (!sheets.files.some((file) => file.href.endsWith(".png"))) problems.push("png");

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
  shellBytes: shell,
  problems
};
console.log(JSON.stringify(report, null, 2));
if (gates.some(([ok]) => !ok)) process.exit(1);
