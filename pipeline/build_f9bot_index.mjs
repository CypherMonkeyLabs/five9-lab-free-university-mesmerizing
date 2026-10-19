/* Build the offline Five9 guide index from this lab's lesson JSON.
   Usage: node pipeline/build_f9bot_index.mjs
   Writes js/content/f9bot-index.json. Do not edit that file by hand. */
import { readdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { tokens } from "../shared/pybot-chat/engine.js";
import { SEED_RULES, SYN } from "./f9bot_seeds.mjs";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const outPath = join(root, "js/content/f9bot-index.json");

function plain(text) {
  return String(text || "").replace(/\s+/g, " ").trim();
}

function clip(text, max = 520) {
  const clean = plain(text);
  if (clean.length <= max) return clean;
  const cut = clean.slice(0, max);
  const stop = Math.max(cut.lastIndexOf(". "), cut.lastIndexOf("? "));
  if (stop > 120) return cut.slice(0, stop + 1);
  return cut.trim();
}

const rooms = readdirSync(join(root, "rooms")).filter((name) => name.endsWith(".html"));

function roomHref(trackId, lessonId) {
  const name = rooms.find((file) => file.startsWith(`${trackId}-${lessonId}-`));
  if (!name) throw new Error(`no room for ${trackId}/${lessonId}`);
  return `rooms/${name}`;
}

const trackDir = join(root, "campus/data/tracks");
const lessons = new Map();
for (const file of readdirSync(trackDir).filter((name) => name.endsWith(".json"))) {
  const track = JSON.parse(readFileSync(join(trackDir, file), "utf8"));
  for (const lesson of track.lessons) {
    lessons.set(`${track.id}/${lesson.id}`, { track, lesson });
  }
}

const docs = [];

function addLesson(track, lesson) {
  const paragraphs = (lesson.paragraphs || []).map(plain).filter(Boolean);
  const caveat = "Source check 2026-10; unconfirmed if the vendor page moved.";
  const ex = clip(`${lesson.title}. ${caveat} ${paragraphs[0] || ""}`);
  const eg = paragraphs[1] ? clip(paragraphs[1], 160) : "";
  const bodyText = [lesson.title, lesson.blurb || "", ...paragraphs, ...(lesson.objectives || [])].join("\n");
  docs.push({
    i: `lesson:${track.id}/${lesson.id}`,
    k: "lesson",
    ti: lesson.title,
    h: roomHref(track.id, lesson.id),
    s: track.id,
    ex,
    eg,
    w: tokens(bodyText, SYN, 3),
    tw: tokens(lesson.title, SYN, 2),
  });
}

for (const { track, lesson } of lessons.values()) addLesson(track, lesson);

const pages = [
  ["page:start", "start.html", "Learn", "page", "Start on the Learn page. The ten-minute path and the full course are both there."],
  ["page:downloads", "downloads.html", "Downloads", "download", "Sheets, cards, and the bundle are on the downloads page."],
  ["page:play", "play.html", "Play", "game", "Play is the port match, the daily question, and a routing desk. The routing desk is a simulation and does not call Five9."],
  ["page:listen", "listen.html", "Listen", "media", "Listen holds the study audio beside the course."],
  ["page:diagrams", "diagrams.html", "Diagrams", "diagram", "Diagrams are the drawings you can save."],
  ["page:glossary", "glossary.html", "Glossary", "glossary", "The glossary is the contract with the cited page."],
  ["page:search", "search.html", "Search", "page", "Search finds a room by its title."],
  ["page:practice", "campus/index.html", "Practice console", "page", "The practice console in this browser is a simulation. It does not call Five9."],
];

for (const [id, href, title, kind, ex] of pages) {
  docs.push({
    i: id,
    k: kind,
    ti: title,
    h: href,
    s: "",
    ex,
    eg: "",
    w: tokens(`${title} ${ex}`, SYN, 3),
    tw: tokens(title, SYN, 2),
  });
}

const seeds = SEED_RULES.map((rule) => {
  const found = lessons.get(rule.lesson);
  if (!found) throw new Error(`seed lesson missing ${rule.lesson}`);
  const { track, lesson } = found;
  const paragraphs = (lesson.paragraphs || []).map(plain).filter(Boolean);
  const caveat = "Source check 2026-10; unconfirmed if the vendor page moved.";
  const ex = clip(`${lesson.title}. ${caveat} ${paragraphs[0] || ""}`);
  return {
    i: rule.i,
    h: roomHref(track.id, lesson.id),
    ti: lesson.title,
    k: "lesson",
    topic: rule.topic,
    any: rule.any || [],
    all: rule.all || [],
    block: rule.block || [],
    allow: rule.allow || [],
    loose: Boolean(rule.loose),
    rank: rule.rank || 0,
    ex,
    eg: paragraphs[1] ? clip(paragraphs[1], 160) : "",
  };
});

const glossaryHtml = readFileSync(join(root, "glossary.html"), "utf8");
const glossary = [...glossaryHtml.matchAll(/<li><strong>([^<]+)<\/strong>/g)].map((match) => match[1].trim());
const titles = [...lessons.values()].map(({ lesson }) => lesson.title);
const index = { v: 1, lab: "five9", syn: SYN, seeds, lexicon: { titles, glossary }, docs };
writeFileSync(outPath, `${JSON.stringify(index)}\n`);
console.log(`f9bot index docs ${docs.length} seeds ${seeds.length} bytes ${Buffer.byteLength(JSON.stringify(index))}`);
