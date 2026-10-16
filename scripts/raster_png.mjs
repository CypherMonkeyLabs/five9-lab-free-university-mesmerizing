import { createRequire } from "node:module";
import { readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const require = createRequire("/tmp/raster/package.json");
const { Resvg } = require("@resvg/resvg-js");
const dir = new URL("../downloads/diagrams/", import.meta.url).pathname;
const files = readdirSync(dir).filter((name) => name.endsWith(".svg"));
let written = 0;
for (const name of files) {
  const svg = readFileSync(join(dir, name));
  const resvg = new Resvg(svg, { fitTo: { mode: "width", value: 1200 } });
  const png = resvg.render().asPng();
  writeFileSync(join(dir, name.replace(/\.svg$/, ".png")), png);
  written += 1;
}
console.log(`png ${written}`);
