/* Validate data/lesson-map.json against campus/data tracks.
   Exit 1 on any problem. */
import { createHash } from "node:crypto";
import { readFileSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const map = JSON.parse(readFileSync(join(root, "data/lesson-map.json"), "utf8"));
const schema = JSON.parse(readFileSync(join(root, "data/lesson-schema.json"), "utf8"));
const sourceFile = JSON.parse(readFileSync(join(root, "data/sources.json"), "utf8"));
const problems = [];
const sourceIds = new Set(sourceFile.sources.map((item) => item.id));
const mapped = new Map(map.lessons.map((lesson) => [lesson.key, lesson]));
const seen = new Set();
const required = schema.required;

function sourceId(url) {
  return `s${createHash("sha256").update(url).digest("hex").slice(0, 10)}`;
}

const dir = join(root, "campus/data/tracks");
for (const file of readdirSync(dir).filter((name) => name.endsWith(".json"))) {
  const track = JSON.parse(readFileSync(join(dir, file), "utf8"));
  for (const lesson of track.lessons) {
    const key = `${track.id}/${lesson.id}`;
    seen.add(key);
    const row = mapped.get(key);
    if (!row) {
      problems.push(`${key}: not in lesson-map.json`);
      continue;
    }
    for (const field of required) if (!(field in row)) problems.push(`${key}: missing field ${field}`);
    if (!Number.isInteger(row.level) || row.level < schema.levelMin || row.level > schema.levelMax) {
      problems.push(`${key}: level must be ${schema.levelMin}-${schema.levelMax}`);
    }
    if (!Array.isArray(row.outcomes) || row.outcomes.length < 1 || row.outcomes.some((item) => typeof item !== "string" || item.length < 8)) {
      problems.push(`${key}: needs at least one outcome`);
    }
    if (!Array.isArray(row.sources) || row.sources.length < 1) problems.push(`${key}: needs at least one source`);
    for (const id of row.sources || []) if (!sourceIds.has(id)) problems.push(`${key}: unknown source id ${id}`);
    const fromLesson = (lesson.cites || []).map((cite) => sourceId(cite.url));
    if (JSON.stringify(row.sources) !== JSON.stringify(fromLesson)) problems.push(`${key}: sources differ from the lesson file`);
    if (row.title !== lesson.title) problems.push(`${key}: title differs from the lesson file`);
    if (row.last_verified !== null && !/^\d{4}-\d{2}-\d{2}$/.test(row.last_verified)) {
      problems.push(`${key}: last_verified must be null or YYYY-MM-DD`);
    }
  }
}
for (const key of mapped.keys()) if (!seen.has(key)) problems.push(`${key}: in lesson-map.json but no such lesson`);

const perLevel = {};
for (const row of map.lessons) perLevel[row.level] = (perLevel[row.level] || 0) + 1;
for (const problem of problems) console.log("FAIL", problem);
console.log("lessons:", seen.size, "mapped:", mapped.size, "per level:", JSON.stringify(perLevel));
console.log("validate_lessons:", problems.length, "problems");
process.exit(problems.length ? 1 : 0);
