/* Write data/lesson-map.json, data/lesson-schema.json, and data/sources.json
   from campus/data tracks. Outcomes and titles are copied from the lessons.
   last_verified stays null: this script does not claim a new source check. */
import { createHash } from "node:crypto";
import { readdirSync, readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const levelOf = { Foundation: 1, Practice: 4, Advanced: 7 };
const sources = new Map();

function sourceId(url) {
  return `s${createHash("sha256").update(url).digest("hex").slice(0, 10)}`;
}

const lessons = [];
const dir = join(root, "campus/data/tracks");
for (const file of readdirSync(dir).filter((name) => name.endsWith(".json")).sort()) {
  const track = JSON.parse(readFileSync(join(dir, file), "utf8"));
  const level = levelOf[track.level];
  if (!Number.isInteger(level)) throw new Error(`unknown level on ${track.id}`);
  for (const lesson of track.lessons) {
    const ids = [];
    for (const cite of lesson.cites || []) {
      const id = sourceId(cite.url);
      ids.push(id);
      if (!sources.has(id)) sources.set(id, { id, url: cite.url, label: cite.label || "" });
    }
    const outcomes = (lesson.objectives || []).map((item) => String(item).trim()).filter((item) => item.length >= 8);
    if (!outcomes.length) outcomes.push(`Read the lesson: ${lesson.title}`.slice(0, 180));
    lessons.push({
      key: `${track.id}/${lesson.id}`,
      title: lesson.title,
      level,
      outcomes,
      sources: ids,
      last_verified: null,
    });
  }
}

mkdirSync(join(root, "data"), { recursive: true });
writeFileSync(join(root, "data/sources.json"), `${JSON.stringify({ sources: [...sources.values()] }, null, 2)}\n`);
writeFileSync(join(root, "data/lesson-map.json"), `${JSON.stringify({ lab: "five9", lessons }, null, 2)}\n`);
writeFileSync(join(root, "data/lesson-schema.json"), `${JSON.stringify({
  required: ["key", "title", "level", "outcomes", "sources", "last_verified"],
  levelMin: 0,
  levelMax: 10,
}, null, 2)}\n`);
console.log(`lesson map ${lessons.length} sources ${sources.size}`);
