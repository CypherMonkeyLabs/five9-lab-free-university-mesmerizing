import { diagram, diagramIds, diagramMeta, flowIds } from "./diagrams.js";
import { chartStrip } from "./charts.js";
import { buildZip } from "./zipstore.js";
import { applyI18n } from "./i18n.js";
import { glyphImg, warmGlyphs } from "./glyphs.js";

const UNI_KEY = "f9lab-university";
const REPO = "https://github.com/cipher0x9/five9-lab-free-university-mesmerizing";
const LABS = "https://cyphermonkeylabs.com";

const NAV = [
  ["#/atlas", "Atlas"],
  ["#/explorer", "Flow map"],
  ["#/ports", "Ports game"],
  ["#/deploy", "Deployment"],
  ["#/sip", "SIP and PSTN"],
  ["#/migrate", "Migration"],
  ["#/config", "Configure"],
  ["#/trouble", "Playbooks"],
  ["#/wfm", "WFM"],
  ["#/record", "Recording"],
  ["#/e911", "E911"],
  ["#/analytics", "Reporting"],
  ["#/integrations", "CRM and APIs"],
  ["#/ai", "AI agents"],
  ["#/security", "Security"],
  ["#/roadmap", "2026 notes"],
  ["#/career", "Career"],
  ["#/downloads", "Cheat codes"],
  ["#/daily", "Daily"],
  ["#/badges", "Badges"],
  ["#/sandbox", "Call-flow sandbox"]
];

let pack = null;
const sky = { raf: 0, pointer: { x: 0.5, y: 0.2 } };

function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, (ch) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[ch]));
}

function loadState() {
  const base = { checks: {}, portsBest: 0, daily: {}, egg: false, downloads: 0, share: "" };
  try {
    return Object.assign(base, JSON.parse(localStorage.getItem(UNI_KEY) || "{}"));
  } catch (err) {
    return base;
  }
}

function saveState(state) {
  localStorage.setItem(UNI_KEY, JSON.stringify(state));
  if (state.egg) document.documentElement.dataset.egg = "1";
}

async function loadUni() {
  if (pack) return pack;
  const response = await fetch("data/university.json");
  if (!response.ok) throw new Error("university");
  pack = await response.json();
  return pack;
}

function lookFor(hash) {
  const state = loadState();
  if (state.egg) return "egg";
  if (hash.startsWith("#/ivr") || hash.startsWith("#/sandbox")) return "ivr";
  if (hash.startsWith("#/pacing") || hash.startsWith("#/ports")) return "dial";
  if (hash.startsWith("#/boss") || hash.startsWith("#/trouble")) return "boss";
  const cycle = ["dawn", "day", "dusk", "night"];
  return cycle[Math.floor(Date.now() / 180000) % cycle.length];
}

function updateMascot() {
  document.documentElement.dataset.look = lookFor(location.hash || "#/");
}

function toast(text) {
  document.querySelectorAll(".toast").forEach((node) => node.remove());
  const node = document.createElement("p");
  node.className = "toast";
  node.setAttribute("role", "status");
  node.textContent = text;
  document.body.appendChild(node);
  setTimeout(() => node.remove(), 3200);
}

function citesHtml(items) {
  if (!items || !items.length) return "";
  return `<ol class="cites">${items.map((item) => `<li><a href="${esc(item.url)}" rel="noopener" target="_blank">${esc(item.label)}</a></li>`).join("")}</ol>`;
}

function figure(id, caption) {
  const svg = diagram(id);
  if (!svg) return "";
  return `<figure class="figure">${svg}<figcaption>${esc(caption || id)}</figcaption></figure>`;
}

function renderBlocks(section, data, ctx) {
  const state = loadState();
  return section.blocks.map((block) => {
    if (block.kind === "prose") {
      return `<section class="panel"><h2>${esc(block.h)}</h2>${block.p.map((p) => `<p>${esc(p)}</p>`).join("")}</section>`;
    }
    if (block.kind === "steps") {
      return `<section class="panel"><h2>${esc(block.h)}</h2><ol>${block.items.map((item) => `<li>${esc(item)}</li>`).join("")}</ol></section>`;
    }
    if (block.kind === "checks") {
      const picked = state.checks[block.id] || [];
      return `<section class="panel"><h2>${esc(block.h)}</h2><p class="note">${picked.length} of ${block.items.length} checked on this browser.</p><ul class="checks" data-check-list="${esc(block.id)}">${block.items.map((item, i) => `<li><label><input type="checkbox" data-check="${i}" ${picked.includes(i) ? "checked" : ""}> ${esc(item)}</label></li>`).join("")}</ul></section>`;
    }
    if (block.kind === "cites") return `<section><h2>Sources</h2>${citesHtml(block.items)}</section>`;
    if (block.kind === "widget" && block.id === "erlang") return erlangHtml();
    if (block.kind === "customers") return customersHtml(data);
    if (block.kind === "roadmap") return roadmapHtml(data);
    return `<p class="uncertain">Unknown block.</p>`;
  }).join("");
}

function bindChecks(ctx) {
  ctx.view.querySelectorAll("[data-check-list]").forEach((list) => {
    list.querySelectorAll("[data-check]").forEach((box) => {
      ctx.on(box, "change", () => {
        const state = loadState();
        const id = list.dataset.checkList;
        state.checks[id] = [...list.querySelectorAll("[data-check]:checked")].map((node) => Number(node.dataset.check));
        saveState(state);
        const note = list.parentElement.querySelector(".note");
        if (note) note.textContent = `${state.checks[id].length} of ${list.querySelectorAll("[data-check]").length} checked on this browser.`;
      });
    });
  });
  const form = ctx.view.querySelector("#erlang-form");
  if (form) ctx.on(form, "submit", (event) => { event.preventDefault(); runErlang(ctx.view); });
}

function erlangHtml() {
  return `<section class="panel"><h2>Classroom Erlang C</h2><p>Enter your own interval. The result is textbook traffic theory. It is not the Five9 WFM engine.</p>
    <form id="erlang-form">
      <div class="field"><label for="er-calls">Calls in the interval</label><input id="er-calls" type="number" min="1" max="5000" value="120"></div>
      <div class="field"><label for="er-min">Interval minutes</label><input id="er-min" type="number" min="5" max="60" value="30"></div>
      <div class="field"><label for="er-aht">Average handle seconds, including after-call work</label><input id="er-aht" type="number" min="30" max="3600" value="300"></div>
      <div class="field"><label for="er-wait">Target probability of waiting</label><input id="er-wait" type="number" min="0.01" max="0.5" step="0.01" value="0.2"></div>
      <button class="btn primary" type="submit">Calculate</button>
    </form>
    <p id="erlang-out" class="note">Waiting for your numbers.</p></section>`;
}

function erlangB(load, agents) {
  let inverse = 1;
  for (let k = 1; k <= agents; k += 1) inverse = 1 + inverse * k / load;
  return 1 / inverse;
}

function erlangC(load, agents) {
  if (agents <= load) return 1;
  const b = erlangB(load, agents);
  return (agents * b) / (agents - load * (1 - b));
}

function runErlang(root) {
  const calls = Number(root.querySelector("#er-calls").value);
  const minutes = Number(root.querySelector("#er-min").value);
  const aht = Number(root.querySelector("#er-aht").value);
  const target = Number(root.querySelector("#er-wait").value);
  const out = root.querySelector("#erlang-out");
  if (!(calls > 0 && minutes > 0 && aht > 0 && target > 0 && target < 1)) {
    out.textContent = "Use positive numbers. The wait target stays below 1.";
    return;
  }
  const load = (calls * aht) / (minutes * 60);
  let agents = Math.floor(load) + 1;
  let guard = 0;
  while (erlangC(load, agents) > target && guard < 500) {
    agents += 1;
    guard += 1;
  }
  out.textContent = `Offered load is ${load.toFixed(2)} erlangs. ${agents} agents keep the wait probability at or under ${target}. Occupancy would be about ${Math.min(99, (load / agents) * 100).toFixed(0)} percent if every agent takes only this work. Five9 has not published this formula as WEM.`;
}

function customersHtml(data) {
  return `<section><h2>Public case studies</h2><p class="note">Figures are the headlines on Five9's own pages as retrieved in October 2026. This lab did not audit them.</p><div class="grid">${data.customers.map((row) => `<article class="panel"><h3><a href="${esc(row.href)}" rel="noopener" target="_blank">${esc(row.name)}</a></h3><ul>${row.claims.map((claim) => `<li>${esc(claim)}</li>`).join("")}</ul></article>`).join("")}</div></section>`;
}

function roadmapHtml(data) {
  return `<ol class="checks">${data.roadmap.map((row) => `<li><strong>${esc(row.when)}</strong> <span class="tag">${esc(row.status)}</span><p>${esc(row.what)}</p><p><a href="${esc(row.url)}" rel="noopener" target="_blank">${esc(row.source)}</a></p></li>`).join("")}</ol>`;
}

async function renderSection(ctx, key) {
  const data = await loadUni();
  const section = data.sections[key];
  ctx.setTitle(section.title, section.lede);
  const extra = key === "career" ? `<p><a class="btn" href="#/interview">Interview deck</a> <a class="btn" href="#/certs">Credentials</a> <a class="btn" href="#/tracks">All tracks</a></p>` : "";
  ctx.view.innerHTML = `<p class="note">${esc(data.banner)}</p>${figure(section.diagram, section.title)}${renderBlocks(section, data, ctx)}${extra}<p><a class="btn" href="#/downloads">Cheat sheets</a></p>`;
  bindChecks(ctx);
}

function renderTrouble(ctx, data) {
  ctx.setTitle("Troubleshooting playbooks", "Ten symptoms. Each one names the object that actually failed.");
  ctx.view.innerHTML = `<p class="note">${esc(data.banner)}</p>${figure("nat-path", "Signaling up does not prove media")}<div class="grid">${data.playbooks.map((book) => `<article class="panel"><h2>${esc(book.symptom)}</h2><ol>${book.tree.map((step) => `<li>${esc(step)}</li>`).join("")}</ol><p>${esc(book.meaning)}</p><p><a href="${esc(book.lesson)}">Open the lesson</a> · <a href="${esc(book.url)}" rel="noopener" target="_blank">${esc(book.source)}</a></p></article>`).join("")}</div>`;
}

function figureBlock(id, title, source) {
  return `<figure class="figure float-card">${diagram(id)}<figcaption><strong>${esc(title)}</strong><br>${esc(source)}</figcaption><button type="button" class="btn enlarge" data-open-diagram="${esc(id)}">Enlarge</button></figure>`;
}

function renderAtlas(ctx) {
  ctx.setTitle("Diagrams", "Teaching drawings. The caption names the public page. None of these are captured Five9 traces.");
  ctx.view.innerHTML = `<p class="note">${diagramIds.length} diagrams in this atlas. ${flowIds.length} of them are animated flows. Open <a href="#/flows">Flows</a> for the moving ones. Enlarge a drawing to pause, step, and read why it matters.</p><div class="atlas-grid">${diagramMeta.map(([id, title, source]) => figureBlock(id, title, source)).join("")}</div>`;
}

function renderFlows(ctx) {
  ctx.setTitle("Flows", `${flowIds.length} animated call, signal, and data flows. The dashes move until reduced motion is on.`);
  const known = new Map(diagramMeta);
  ctx.view.innerHTML = `<p class="note">Hand-built SVG. The SIP ladder is an RFC 3261 teaching drawing, not a capture. The forecast loop is textbook Erlang, not the Five9 WEM engine. Mermaid is not bundled.</p><div class="atlas-grid">${flowIds.map((id) => {
    const row = known.get(id) ? diagramMeta.find((item) => item[0] === id) : null;
    const title = row ? row[1] : id;
    const source = row ? row[2] : "This lab";
    return figureBlock(id, title, source);
  }).join("")}</div>`;
}

async function renderCharts(ctx) {
  const catalog = await ctx.getCatalog();
  const data = await loadUni();
  ctx.setTitle("Charts", "Six charts from this lab's catalog and the cited bandwidth and port tables.");
  ctx.view.innerHTML = `${counterRow(catalog)}<div class="chart-grid">${chartStrip(catalog, data)}</div><h2>Study map</h2><svg id="study-map" width="720" height="360"></svg><p class="note">The mind map is a study outline for this lab. It is not a Five9 organization chart. It is drawn by the vendored markmap build and does not fetch a stylesheet.</p>`;
  import("./effects.js").then((mod) => mod.mountMindmap(ctx.view.querySelector("#study-map"))).catch(() => {});
}

function renderRegions(ctx) {
  ctx.setTitle("Regions", "Only the places a public Five9 page actually names. Anything else is marked as an example.");
  ctx.view.innerHTML = `
    <p class="note">Flags below the cited cards are symbols for the switcher. They are not a coverage map and not a carrier list.</p>
    <div class="grid">
      <article class="panel region-card">
        <h2>United States, Canada, Europe</h2>
        <p class="flag-row" aria-hidden="true">🇺🇸 🇨🇦 🇪🇺</p>
        <p>The July 2026 technical-requirements change log says domains were added for US, Canadian, and European centers. This lab does not copy the IP lists. They move.</p>
        <p><a href="https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf" rel="noopener" target="_blank">Technical requirements PDF</a></p>
      </article>
      <article class="panel region-card">
        <h2>Studio portals</h2>
        <p>3 names in the March 2026 change log: GCP, CHI, VIR. That line clarifies Studio 7 network text. It is not a promise that those three strings are the only portals.</p>
        <p>The Studio 7 article says you copy a task key from the regional Studio portal into VCC. A key from the wrong portal is a different bot.</p>
        <p><a href="https://community.five9.com/s/article/Studio-7-Integrate-Digital-IVA-in-Studio-with-VCC?language=en_US" rel="noopener" target="_blank">Studio digital IVA with VCC</a></p>
      </article>
      <article class="panel region-card">
        <h2>Example symbols</h2>
        <p class="flag-row" aria-label="Example flags, not coverage">🇮🇳 🇫🇷 🇩🇪 🇯🇵 🇲🇽 🇧🇷</p>
        <p>Example only. This lab has no public page that lists PSTN coverage, carriers, or a regulation pack for these countries. Do not brief a customer from this row.</p>
      </article>
    </div>`;
}

function renderPlay(ctx) {
  ctx.setTitle("Play", "Benches that use the same public facts as the lessons.");
  const tiles = [
    ["#/ivr", "Call-flow sandbox", "IVR modules named in the administrator guide."],
    ["#/pacing", "Dialer clock", "Preview through predictive, labeled as a teaching clock."],
    ["#/topology", "3D floor", "Vendored Three.js. Reduced motion uses the flat map."],
    ["#/ports", "Ports game", "The same rows as the firewall matrix."],
    ["#/daily", "Daily challenge", "One real quiz item from the lesson bank."],
    ["#/explorer", "Flow map", "Click a box. The note cites the page."]
  ];
  ctx.view.innerHTML = `<div class="grid">${tiles.map(([href, title, text]) => `<a class="card" href="${href}">${glyphImg(href.includes("topology") ? "t17" : href.includes("ivr") ? "t07" : href.includes("pacing") ? "t05" : href.includes("ports") ? "t13" : href.includes("daily") ? "t18" : "t14")}<div class="card-copy"><h2>${esc(title)}</h2><p>${esc(text)}</p></div></a>`).join("")}</div>`;
}

function renderPorts(ctx, data) {
  ctx.setTitle("Ports and protocols", "The table is the community softphone list plus the WEM supervisor ports. The game uses those same rows.");
  const state = { index: 0, score: 0, order: shuffle(data.ports.map((_, i) => i)), locked: false };
  const paint = () => {
    const row = data.ports[state.order[state.index]];
    const choices = decoys(data.ports, row);
    ctx.view.innerHTML = `
      <p class="note">${esc(data.banner)}</p>
      ${figure("firewall", "A few of the softphone rows, drawn")}
      <section class="panel" id="port-game">
        <h2>Port mastery</h2>
        <p class="game-score">Correct ${state.score} · answered ${state.index} · best ${loadState().portsBest}</p>
        <p>Question ${state.index + 1} of ${data.ports.length}</p>
        <p><strong>${esc(row.use)}</strong></p>
        <div class="choice-grid">${choices.map((choice) => `<button type="button" class="btn" data-port="${esc(choice.port)}">${esc(choice.port)} ${esc(choice.proto)}</button>`).join("")}</div>
        <p class="why" id="port-why" role="status"></p>
      </section>
      <h2>Bandwidth, G.711 table</h2>
      <p class="note">Copied as figures from the technical requirements PDF read in October 2026. <a href="${esc(data.bandwidthSource.url)}" rel="noopener" target="_blank">${esc(data.bandwidthSource.label)}</a></p>
      <div class="table-wrap"><table><thead><tr><th>Use</th><th>Minimum</th><th>Recommended</th><th>Note</th></tr></thead><tbody>
        ${data.bandwidth.map((row) => `<tr><td>${esc(row.use)}</td><td>${esc(row.min)}</td><td>${esc(row.rec)}</td><td>${esc(row.note)}</td></tr>`).join("")}
      </tbody></table></div>
      <h2>Firewall matrix</h2>
      <div class="table-wrap"><table><thead><tr><th>Port</th><th>Proto</th><th>Direction</th><th>Who</th><th>Purpose</th><th>Source</th></tr></thead><tbody>
        ${data.ports.map((item) => `<tr><td>${esc(item.port)}</td><td>${esc(item.proto)}</td><td>${esc(item.dir)}</td><td>${esc(item.who)}</td><td>${esc(item.use)}</td><td><a href="${esc(item.url)}" rel="noopener" target="_blank">${esc(item.source)}</a></td></tr>`).join("")}
      </tbody></table></div>
      <p><button type="button" class="btn" id="share-ports">Share this score</button></p><div id="share-host"></div>`;
    ctx.view.querySelectorAll("[data-port]").forEach((button) => {
      ctx.on(button, "click", () => {
        if (state.locked) return;
        state.locked = true;
        const why = ctx.view.querySelector("#port-why");
        const right = button.dataset.port === row.port;
        if (right) {
          state.score += 1;
          why.textContent = `Yes. ${row.port}/${row.proto}. ${row.source}.`;
          why.className = "why ok";
          ctx.audio.ok();
        } else {
          why.textContent = `That port is a different row. This purpose is ${row.port}/${row.proto}.`;
          why.className = "why bad";
          ctx.audio.bad();
        }
        setTimeout(() => {
          if (!ctx.view.isConnected) return;
          state.index += 1;
          state.locked = false;
          if (state.index >= data.ports.length) {
            finish();
            return;
          }
          paint();
        }, 700);
      });
    });
    const share = ctx.view.querySelector("#share-ports");
    if (share) ctx.on(share, "click", () => shareCard(ctx.view.querySelector("#share-host"), `Ports ${state.score}/${state.index}`));
  };
  const finish = () => {
    const saved = loadState();
    saved.portsBest = Math.max(saved.portsBest || 0, state.score);
    saveState(saved);
    toast(`Round complete. ${state.score} of ${data.ports.length}.`);
    const game = ctx.view.querySelector("#port-game");
    if (game) {
      game.innerHTML = `<h2>Round complete</h2><p class="game-score">${state.score} of ${data.ports.length}</p><button type="button" class="btn primary" id="port-again">Play again</button> <button type="button" class="btn" id="share-ports">Share this score</button><div id="share-host"></div>`;
      ctx.on(game.querySelector("#port-again"), "click", () => renderPorts(ctx, data));
      ctx.on(game.querySelector("#share-ports"), "click", () => shareCard(game.querySelector("#share-host"), `Ports ${state.score}/${data.ports.length}`));
    }
  };
  paint();
}

function shuffle(list) {
  const copy = list.slice();
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

function decoys(ports, row) {
  const others = shuffle(ports.filter((item) => item.port !== row.port)).slice(0, 3);
  return shuffle([row, ...others]);
}

const MAP_NODES = [
  { id: "pstn", x: 40, y: 40, w: 140, h: 48, label: "PSTN / ITSP", text: "Five9 as the carrier, your carrier into Five9, or your own gateway.", href: "#/sip", url: "https://documentation.five9.com/bundle/technical-reqs/page/technical-reqs/SIP-trunk-options/_ch-five9-sip-trunk-options.htm" },
  { id: "sbc", x: 250, y: 40, w: 150, h: 48, label: "SIP edge", text: "DNS SRV is preferred. Pinning IPs means you watch the domains.", href: "#/ports", url: "https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf" },
  { id: "vcc", x: 470, y: 120, w: 160, h: 56, label: "VCC domain", text: "Skills, lists, campaigns, and IVR live in the tenant.", href: "#/track/t01", url: "https://documentation.five9.com/bundle/basic-admin/page/basic-admin/intro/planning-your-implementation.htm" },
  { id: "ivr", x: 250, y: 210, w: 140, h: 48, label: "IVR", text: "Modules, then a Skill Transfer that names a skill.", href: "#/ivr", url: "https://documentation.five9.com/bundle/ivr-admin/page/ivr-admin/modules/_ch-modules.htm" },
  { id: "agent", x: 40, y: 300, w: 150, h: 48, label: "Agent station", text: "Softphone, WebRTC, gateway, or PSTN station.", href: "#/deploy", url: "https://community.five9.com/s/article/VCC-Five9-WebRTC" },
  { id: "crm", x: 250, y: 300, w: 150, h: 48, label: "CRM adapter", text: "HTTPS and Secure WebSocket. Voice can be up while the pop is down.", href: "#/integrations", url: "https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf" },
  { id: "wem", x: 470, y: 300, w: 150, h: 48, label: "WEM / QM", text: "Workforce, quality, recording. Verint is a second path.", href: "#/wfm", url: "https://www.five9.com/products/capabilities/workforce-optimization" },
  { id: "e911", x: 470, y: 40, w: 140, h: 48, label: "E911", text: "Dispatchable location. The data sheet names RedSky.", href: "#/e911", url: "https://www.five9.com/sites/default/files/2022-11/Data-sheet-Five9-emergency-services%20%28E911%29.PDF" }
];

const MAP_EDGES = [["pstn", "sbc"], ["sbc", "vcc"], ["sbc", "e911"], ["vcc", "ivr"], ["ivr", "agent"], ["vcc", "crm"], ["vcc", "wem"]];

function renderExplorer(ctx) {
  ctx.setTitle("Flow map explorer", "Click a box. The note is a teaching summary with the page it came from.");
  const edges = MAP_EDGES.map(([a, b]) => {
    const from = MAP_NODES.find((node) => node.id === a);
    const to = MAP_NODES.find((node) => node.id === b);
    return `<line class="flow-line" x1="${from.x + from.w / 2}" y1="${from.y + from.h / 2}" x2="${to.x + to.w / 2}" y2="${to.y + to.h / 2}"></line>`;
  }).join("");
  const nodes = MAP_NODES.map((node) => `<g class="hot node tone-a" data-node="${node.id}" tabindex="0" role="button"><rect x="${node.x}" y="${node.y}" width="${node.w}" height="${node.h}" rx="12"></rect><text x="${node.x + node.w / 2}" y="${node.y + 28}" text-anchor="middle">${esc(node.label)}</text></g>`).join("");
  ctx.view.innerHTML = `<div class="explorer"><div class="panel">${frameMap(edges + nodes)}</div><aside class="panel" id="map-note"><h2>Pick a box</h2><p>The dashes are the relationships this lab wants you to name. They are not a live trace.</p></aside></div>`;
  const show = (id) => {
    const node = MAP_NODES.find((item) => item.id === id);
    ctx.view.querySelectorAll(".hot").forEach((el) => el.classList.toggle("is-on", el.dataset.node === id));
    ctx.view.querySelector("#map-note").innerHTML = `<h2>${esc(node.label)}</h2><p>${esc(node.text)}</p><p><a href="${esc(node.href)}">Open the lab page</a></p><p><a href="${esc(node.url)}" rel="noopener" target="_blank">Source</a></p>`;
  };
  ctx.view.querySelectorAll(".hot").forEach((el) => {
    ctx.on(el, "click", () => show(el.dataset.node));
    ctx.on(el, "keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        show(el.dataset.node);
      }
    });
  });
}

function frameMap(body) {
  return `<svg class="diag" viewBox="0 0 680 380" role="img" aria-label="Five9 teaching map"><rect class="diag-bg" width="680" height="380" rx="16"></rect>${body}</svg>`;
}

async function renderDownloads(ctx, focusZip) {
  ctx.setTitle(focusZip ? "Downloads" : "Cheat Codes", "One-page sheets, a flashcard deck, and the offline bundle. Generated in this repo.");
  const response = await fetch("downloads/manifest.json");
  const manifest = await response.json();
  const sheets = manifest.files.map((file) => `<p><a class="btn" href="${esc(file.href)}" download>${esc(file.title)}</a> <span class="note">${esc(file.kind)}</span></p>`).join("");
  const zip = `<section id="offline-bundle" class="panel"><h2>Offline bundle</h2><p>The prebuilt zip is in the list above. This button rebuilds an uncompressed zip in the browser from the file list. It does not call another host.</p><button type="button" class="btn primary" id="build-pack">Download offline zip</button><p id="pack-status" class="note" role="status"></p></section>`;
  ctx.view.innerHTML = `<p>Each sheet carries cyphermonkeylabs.com, linktr.ee/cyphermonkey, this repo, and the independent-study disclaimer.</p>${focusZip ? zip : ""}<div class="sheet-list">${sheets}</div>${focusZip ? "" : zip}`;
  ctx.on(ctx.view.querySelector("#build-pack"), "click", () => downloadPack(ctx.view.querySelector("#pack-status")));
  if (focusZip) {
    const bundle = ctx.view.querySelector("#offline-bundle");
    if (bundle) bundle.scrollIntoView({ block: "nearest" });
  }
}

async function downloadPack(status) {
  const state = loadState();
  state.downloads = (state.downloads || 0) + 1;
  saveState(state);
  status.textContent = "Reading the file list…";
  const manifest = await (await fetch("data/pack-manifest.json")).json();
  const files = [];
  for (let i = 0; i < manifest.files.length; i += 1) {
    const name = manifest.files[i];
    status.textContent = `Fetching ${i + 1} of ${manifest.files.length}: ${name}`;
    const response = await fetch(name);
    if (!response.ok) {
      status.textContent = `Stopped. ${name} did not load.`;
      return;
    }
    files.push({ name, data: new Uint8Array(await response.arrayBuffer()) });
  }
  const blob = buildZip(files);
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "five9-lab-offline.zip";
  link.click();
  status.textContent = `Saved ${files.length} files. Open the zip and serve the campus folder, or open campus/index.html on a static server.`;
}

async function renderDaily(ctx) {
  ctx.setTitle("Daily challenge", "One real quiz item from the lesson bank. The date picks it. The answer stays hidden until you check.");
  const bank = await (await fetch("data/daily-bank.json")).json();
  const day = new Date().toISOString().slice(0, 10);
  const index = Math.abs(hashCode(day)) % bank.items.length;
  const item = bank.items[index];
  const saved = loadState();
  const done = !!saved.daily[day];
  ctx.setTitle("Daily challenge", `${day}. Question ${index + 1} in a bank of ${bank.items.length}.`);
  ctx.view.innerHTML = `<article class="panel"><p class="kicker">${esc(item.track)}</p><h2>${esc(item.q)}</h2>
    ${item.choices.map((choice, i) => `<label class="choice"><input type="radio" name="daily" value="${i}" ${done ? "disabled" : ""}> ${esc(choice)}</label>`).join("")}
    <div class="row"><button type="button" class="btn primary" id="daily-check" ${done ? "disabled" : ""}>Check</button>
    <a class="btn" href="${esc(item.href)}">Read the lesson</a></div>
    <p class="why" id="daily-why" role="status">${done ? "Already checked today." : ""}</p>
    <p class="note"><a href="${esc(item.url)}" rel="noopener" target="_blank">${esc(item.source)}</a></p></article>
    <p>Streak on this browser: ${streak(saved.daily)} day${streak(saved.daily) === 1 ? "" : "s"}.</p>
    <button type="button" class="btn" id="share-daily">Share card</button><div id="share-host"></div>`;
  ctx.on(ctx.view.querySelector("#daily-check"), "click", () => {
    const picked = ctx.view.querySelector("input[name=daily]:checked");
    const why = ctx.view.querySelector("#daily-why");
    if (!picked) { why.textContent = "Choose an answer."; return; }
    const ok = Number(picked.value) === item.answer;
    why.textContent = ok ? item.why : `Not that one. ${item.why}`;
    why.className = ok ? "why ok" : "why bad";
    if (ok) {
      ctx.audio.ok();
      window.dispatchEvent(new CustomEvent("f9-correct"));
    } else ctx.audio.bad();
    const state = loadState();
    state.daily[day] = ok;
    saveState(state);
  });
  ctx.on(ctx.view.querySelector("#share-daily"), "click", () => shareCard(ctx.view.querySelector("#share-host"), `Daily ${day}`));
}

function hashCode(text) {
  let h = 0;
  for (let i = 0; i < text.length; i += 1) h = (h * 31 + text.charCodeAt(i)) | 0;
  return h;
}

function streak(daily) {
  let count = 0;
  const cursor = new Date();
  for (let i = 0; i < 400; i += 1) {
    const key = cursor.toISOString().slice(0, 10);
    if (!Object.prototype.hasOwnProperty.call(daily, key)) break;
    count += 1;
    cursor.setUTCDate(cursor.getUTCDate() - 1);
  }
  return count;
}

function badgeList(session) {
  const progress = session ? session.progress : { lessons: {}, faults: {}, bosses: {} };
  const lessons = Object.values(progress.lessons || {}).filter((row) => row && row.done).length;
  const faults = Object.keys(progress.faults || {}).length;
  const bosses = Object.keys(progress.bosses || {}).length;
  const state = loadState();
  const days = streak(state.daily || {});
  return [
    ["First light", "Finish one lesson.", lessons >= 1],
    ["Floor walker", "Finish ten lessons.", lessons >= 10],
    ["Domain keeper", "Finish thirty lessons.", lessons >= 30],
    ["Fault ear", "Solve five fault logs.", faults >= 5],
    ["Night shift", "Clear a boss incident.", bosses >= 1],
    ["Port ace", "Score at least 10 in one ports round.", (state.portsBest || 0) >= 10],
    ["Three-day wire", "Check the daily challenge three days running.", days >= 3],
    ["Pack rat", "Build the offline zip once.", (state.downloads || 0) >= 1],
    ["Signal thief", "The arrow code. Up, up, down, down, left, right, left, right, B, A.", !!state.egg]
  ];
}

function renderBadges(ctx) {
  const rows = badgeList(ctx.session);
  const earned = rows.filter((row) => row[2]).length;
  ctx.setTitle("Badges", `${earned} of ${rows.length} earned on this browser. They read real progress, not a counter that starts empty and stays empty.`);
  ctx.view.innerHTML = `<div class="badge-grid">${rows.map(([name, detail, on]) => `<article class="badge ${on ? "earned" : ""}"><strong>${esc(name)}</strong><p>${esc(detail)}</p><p class="note">${on ? "Earned" : "Still open"}</p></article>`).join("")}</div>
    <button type="button" class="btn primary" id="share-badges">Share card</button><div id="share-host"></div>`;
  ctx.on(ctx.view.querySelector("#share-badges"), "click", () => shareCard(ctx.view.querySelector("#share-host"), `${earned}/${rows.length} badges`));
}

function shareCard(host, line) {
  const canvas = document.createElement("canvas");
  canvas.width = 1200;
  canvas.height = 630;
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "#061018";
  ctx.fillRect(0, 0, 1200, 630);
  ctx.strokeStyle = "#5ce1ff";
  ctx.lineWidth = 8;
  ctx.strokeRect(24, 24, 1152, 582);
  ctx.fillStyle = "#ffb020";
  ctx.font = "600 28px sans-serif";
  ctx.fillText("CYPHERMONKEY · FIVE9 LAB", 64, 100);
  ctx.fillStyle = "#e8f4ff";
  ctx.font = "700 64px sans-serif";
  ctx.fillText(line, 64, 240);
  ctx.font = "32px sans-serif";
  ctx.fillStyle = "#9aefff";
  ctx.fillText(LABS, 64, 340);
  ctx.fillStyle = "#b7c9dc";
  ctx.font = "24px sans-serif";
  wrapText(ctx, "Independent educational project. Not affiliated with or endorsed by Five9. Trademarks belong to their owners.", 64, 420, 1000, 34);
  const link = document.createElement("a");
  link.href = canvas.toDataURL("image/png");
  link.download = "five9-lab-card.png";
  link.textContent = "Save the card (PNG)";
  link.className = "btn";
  host.innerHTML = "";
  host.appendChild(canvas);
  host.appendChild(document.createElement("br"));
  host.appendChild(link);
  canvas.style.width = "100%";
  canvas.style.height = "auto";
}

function wrapText(ctx, text, x, y, max, line) {
  const words = text.split(" ");
  let row = "";
  words.forEach((word) => {
    const trial = row ? `${row} ${word}` : word;
    if (ctx.measureText(trial).width > max) {
      ctx.fillText(row, x, y);
      y += line;
      row = word;
    } else row = trial;
  });
  ctx.fillText(row, x, y);
}

function lessonsDone() {
  try {
    const progress = JSON.parse(localStorage.getItem("f9lab-progress") || "{}");
    return Object.values(progress.lessons || {}).filter((row) => row && row.done).length;
  } catch (err) {
    return 0;
  }
}

function counterRow(catalog) {
  const done = lessonsDone();
  const items = [
    [catalog.counts.tracks, "Tracks"],
    [catalog.counts.lessons, "Lessons"],
    [catalog.counts.quiz, "Quiz"],
    [done, "Done"]
  ];
  return `<div class="live-counters" aria-label="Lab counts">${items.map(([value, label]) => `<div class="panel stat"><strong data-count="${value}">${value}</strong><span>${esc(label)}</span></div>`).join("")}</div>`;
}

function iconRow() {
  const faces = ["Diagrams", "Flows", "Charts", "Codes"];
  return `<div class="icon-row" aria-hidden="true">${faces.map((label) => `<span class="cube"><span class="cube-face">${label}</span></span>`).join("")}</div>`;
}

function miniMascots() {
  const looks = ["dawn", "day", "dusk", "night"];
  const face = `<svg class="mascot-svg" viewBox="0 0 72 72" aria-hidden="true"><path class="tail" d="M10 46c-6 2-8 10-4 14"></path><ellipse class="ear" cx="18" cy="18" rx="8" ry="10"></ellipse><ellipse class="ear" cx="54" cy="18" rx="8" ry="10"></ellipse><circle class="head" cx="36" cy="34" r="22"></circle><ellipse class="muzzle" cx="36" cy="42" rx="10" ry="7"></ellipse><ellipse class="eye" cx="28" cy="32" rx="3" ry="3.4"></ellipse><ellipse class="eye" cx="44" cy="32" rx="3" ry="3.4"></ellipse><path class="smile" d="M30 44c2 3 10 3 12 0"></path><g class="prop prop-day"><rect x="22" y="14" width="28" height="6" rx="2" fill="#5ce1ff"></rect></g><g class="prop prop-dawn"><circle cx="58" cy="14" r="4" fill="#ffb020"></circle></g><g class="prop prop-dusk"><circle cx="58" cy="16" r="5" fill="#ff7a45"></circle></g><g class="prop prop-night"><circle cx="60" cy="12" r="2" fill="#fff"></circle><circle cx="16" cy="12" r="1.4" fill="#fff"></circle></g></svg>`;
  return `<div class="mini-row" aria-label="CypherMonkey at dawn, day, dusk, and night">${looks.map((look) => `<span class="mini" data-look="${look}">${face}<span class="mini-name">${look}</span></span>`).join("")}</div>`;
}

function heroFlow() {
  return `<div class="fold-art">
    <svg class="fold-svg" viewBox="0 0 640 200" role="img" aria-label="Animated path from the carrier through the domain to an agent">
      <rect class="diag-bg" width="640" height="200" rx="16"></rect>
      <text class="lane" x="36" y="28">PSTN</text>
      <text class="lane" x="250" y="28">VCC</text>
      <text class="lane" x="470" y="28">Agent</text>
      <line class="flow-line" x1="70" y1="96" x2="210" y2="96"></line>
      <line class="flow-line" x1="360" y1="96" x2="500" y2="96"></line>
      <rect class="node-box" x="24" y="68" width="120" height="56" rx="12"></rect>
      <rect class="node-box b" x="220" y="60" width="150" height="72" rx="12"></rect>
      <rect class="node-box c" x="500" y="68" width="116" height="56" rx="12"></rect>
      <text class="msg" x="84" y="100" text-anchor="middle">Carrier</text>
      <text class="msg" x="295" y="102" text-anchor="middle">Domain</text>
      <text class="msg" x="558" y="100" text-anchor="middle">Desktop</text>
      <circle class="packet" cx="78" cy="96" r="6"></circle>
      <circle class="packet" cx="250" cy="96" r="5"></circle>
      <circle class="packet" cx="520" cy="96" r="5"></circle>
    </svg>
    <div class="fold-side">
      <svg id="rough-mark" viewBox="0 0 120 48" aria-hidden="true"></svg>
      <div id="home-stage" aria-hidden="true"></div>
    </div>
  </div>`;
}

function themeRow() {
  const picks = [
    ["futuristic", "Futuristic", "#061018"],
    ["gaming", "Gaming", "#c6ff4a"],
    ["neon", "Neon", "#ff2bd6"],
    ["light", "Light", "#f6f1e6"]
  ];
  return `<div class="quick-themes fold-themes" role="group" aria-label="Theme">${picks.map(([id, label, color]) => `<button type="button" class="swatch" data-theme-pick="${id}" style="background:${color}" aria-label="${label}"></button>`).join("")}</div>`;
}

const SOLIDS = [
  `<svg class="iso" viewBox="0 0 88 72" aria-hidden="true"><polygon class="iso-top" points="44,8 76,24 44,40 12,24"></polygon><polygon class="iso-left" points="12,24 44,40 44,62 12,46"></polygon><polygon class="iso-right" points="76,24 44,40 44,62 76,46"></polygon></svg>`,
  `<svg class="iso" viewBox="0 0 88 72" aria-hidden="true"><polygon class="iso-top" points="44,4 70,16 44,28 18,16"></polygon><polygon class="iso-left" points="18,16 44,28 44,66 18,54"></polygon><polygon class="iso-right" points="70,16 44,28 44,66 70,54"></polygon></svg>`,
  `<svg class="iso" viewBox="0 0 88 72" aria-hidden="true"><polygon class="iso-top" points="44,18 80,32 44,46 8,32"></polygon><polygon class="iso-left" points="8,32 44,46 44,58 8,44"></polygon><polygon class="iso-right" points="80,32 44,46 44,58 80,44"></polygon></svg>`,
  `<svg class="iso" viewBox="0 0 88 72" aria-hidden="true"><polygon class="iso-top" points="44,6 72,28 16,28"></polygon><polygon class="iso-left" points="16,28 44,40 44,66 16,50"></polygon><polygon class="iso-right" points="72,28 44,40 44,66 72,50"></polygon></svg>`,
  `<svg class="iso" viewBox="0 0 88 72" aria-hidden="true"><polygon class="iso-top" points="44,10 62,20 44,30 26,20"></polygon><polygon class="iso-left" points="26,20 44,30 44,42 26,32"></polygon><polygon class="iso-right" points="62,20 44,30 44,42 62,32"></polygon><polygon class="iso-top" points="44,28 78,42 44,56 10,42" opacity="0.95"></polygon><polygon class="iso-left" points="10,42 44,56 44,68 10,54"></polygon><polygon class="iso-right" points="78,42 44,56 44,68 78,54"></polygon></svg>`
];

export function isoMarkup(index = 0) {
  const n = Number.isFinite(index) ? index : [...String(index)].reduce((sum, ch) => sum + ch.charCodeAt(0), 0);
  return SOLIDS[Math.abs(n) % SOLIDS.length];
}

export function paintHeroCopy(catalog) {
  const host = document.querySelector("#hero-copy");
  const slot = document.querySelector("#hero-slot");
  if (!host || !slot || !catalog) return;
  host.innerHTML = `<p class="hero-greet" data-i18n="greet">Signal university</p>`;
  slot.hidden = false;
  applyI18n();
}

export async function homeFoldHtml() {
  const [catalog, data] = await Promise.all([
    fetch("data/catalog.json").then((res) => res.json()),
    loadUni()
  ]);
  const spots = [
    ["#/atlas", "diagrams", "Diagrams", `${diagramIds.length} drawings`],
    ["#/flows", "flows", "Flows", `${flowIds.length} moving`],
    ["#/charts", "charts", "Charts", "6 cited charts"],
    ["#/downloads", "cheats", "Cheat Codes", "Sheets and cards"]
  ];
  return `<section id="fold" class="fold">
    ${counterRow(catalog)}
    <div class="spot-row">${spots.map(([href, key, label, detail]) => `<a class="spotlight" href="${href}"><span data-i18n="${key}">${esc(label)}</span><strong>${esc(detail)}</strong></a>`).join("")}</div>
    <div class="fold-tools"><div class="icon-row">${[["t03", "Headset"], ["t07", "IVR"], ["t05", "Dialer"], ["t10", "WEM"]].map(([key, label]) => `<span class="iso-card">${glyphImg(key)}<span>${label}</span></span>`).join("")}</div><div class="chart-snap">${chartStrip(catalog, data)}</div></div>
    <p class="note">${esc(data.banner)}</p>
  </section>`;
}

export function signalDeck(catalog) {
  const titles = Object.fromEntries(diagramMeta.map(([id, title]) => [id, title]));
  const featured = ["domain-stack", "sip-entries", "dialer-modes", "ivr-tree", "e911-path", "adapters"];
  return `<div id="uni-home" class="uni-hero">
    <div class="snap">${featured.map((id) => `<figure class="figure float-card">${diagram(id)}<figcaption>${esc(titles[id] || id)}</figcaption></figure>`).join("")}</div>
    <section>
      <h2>Study path</h2>
      <div class="path-row"><strong>Week 1</strong><span>Tracks 1–3. Domain, admin, inbound. <a href="#/track/t01">Start</a></span></div>
      <div class="path-row"><strong>Week 2</strong><span>Tracks 4–6. Lists, dialer modes, blended staffing.</span></div>
      <div class="path-row"><strong>Week 3</strong><span>Tracks 7–9. IVR, skills, Agent Desktop Plus. Then the <a href="#/ivr">sandbox</a>.</span></div>
      <div class="path-row"><strong>Week 4</strong><span>Tracks 10–12. WEM, IVA, CRM.</span></div>
      <div class="path-row"><strong>Week 5</strong><span>Tracks 13–15. SIP, APIs, the Cisco bridge. <a href="#/migrate">Cutover card</a></span></div>
      <div class="path-row"><strong>Week 6</strong><span>Tracks 16–18. Safety, ecosystem, credentials you can cite.</span></div>
      <p class="note">This pace is the lab's plan, not a Five9 University syllabus. ${catalog.counts.lessons} lessons are in the catalog.</p>
    </section>
    <section>
      <h2>Floor plan</h2>
      <div class="grid">${NAV.map(([href, label]) => `<a class="card" href="${href}"><h2>${esc(label)}</h2><p>Open ${esc(label.toLowerCase())}.</p></a>`).join("")}</div>
    </section>
  </div>`;
}

async function mountHome(view) {
  if (!view || view.querySelector("#fold")) return;
  const catalog = await fetch("data/catalog.json").then((res) => res.json());
  if ((location.hash || "#/") !== "#/" || !view.isConnected || view.querySelector("#fold")) return;
  const holder = document.createElement("div");
  holder.innerHTML = await homeFoldHtml();
  view.insertBefore(holder.firstElementChild, view.firstChild);
}

export async function decorateTrack(view) {
  if (!view || view.querySelector("#track-band")) return;
  const match = (location.hash || "").match(/^#\/track\/([a-z0-9-]+)/);
  if (!match) return;
  const [catalog, data] = await Promise.all([
    fetch("data/catalog.json").then((res) => res.json()),
    loadUni()
  ]);
  if (!view.isConnected || !location.hash.startsWith(`#/track/${match[1]}`)) return;
  const band = document.createElement("section");
  band.id = "track-band";
  band.innerHTML = `${counterRow(catalog)}<div class="icon-row">${glyphImg(match[1])}</div><div class="chart-snap">${chartStrip(catalog, data)}</div><p class="note">${esc(data.banner)}</p>`;
  view.insertBefore(band, view.firstChild);
}

function startSky() {
  const canvas = document.querySelector("#sky");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const dots = Array.from({ length: 48 }, () => ({
    x: Math.random(),
    y: Math.random(),
    r: 0.6 + Math.random() * 1.6,
    s: 0.15 + Math.random() * 0.35
  }));
  const draw = (time) => {
    const reduced = document.documentElement.dataset.motion === "reduce";
    const w = canvas.width = window.innerWidth;
    const h = canvas.height = window.innerHeight;
    ctx.clearRect(0, 0, w, h);
    const styles = getComputedStyle(document.documentElement);
    const accent = styles.getPropertyValue("--cc-accent-1").trim() || "#5ce1ff";
    ctx.fillStyle = accent;
    const shift = reduced ? 0 : (sky.pointer.x - 0.5) * 24;
    dots.forEach((dot, i) => {
      const drift = reduced ? 0 : Math.sin(time / 4000 + i) * dot.s * 8;
      ctx.globalAlpha = 0.35;
      ctx.beginPath();
      ctx.arc(dot.x * w + shift, (dot.y * h + drift) % h, dot.r, 0, Math.PI * 2);
      ctx.fill();
    });
    ctx.globalAlpha = 1;
    if (!reduced && !location.hash.startsWith("#/topology")) sky.raf = requestAnimationFrame(draw);
  };
  cancelAnimationFrame(sky.raf);
  sky.raf = requestAnimationFrame(draw);
}

function updateReadbar() {
  const bar = document.querySelector("#readbar");
  if (!bar) return;
  const max = document.documentElement.scrollHeight - window.innerHeight;
  bar.style.width = max > 0 ? `${(window.scrollY / max) * 100}%` : "0%";
}

function armKonami() {
  const code = ["ArrowUp", "ArrowUp", "ArrowDown", "ArrowDown", "ArrowLeft", "ArrowRight", "ArrowLeft", "ArrowRight", "b", "a"];
  let pos = 0;
  document.addEventListener("keydown", (event) => {
    const key = event.key.length === 1 ? event.key.toLowerCase() : event.key;
    if (key === code[pos]) {
      pos += 1;
      if (pos === code.length) {
        pos = 0;
        const state = loadState();
        state.egg = true;
        saveState(state);
        updateMascot();
        toast("Signal thief. CypherMonkey found the night market.");
      }
    } else {
      pos = key === code[0] ? 1 : 0;
    }
  });
}

export function decorateRail() {
  const rail = document.querySelector("#rail");
  if (!rail || rail.querySelector("#uni-rail")) return;
  const block = document.createElement("div");
  block.id = "uni-rail";
  block.innerHTML = `<h2>University</h2>${NAV.map(([href, label]) => `<a href="${href}"><span class="dot a3"></span>${esc(label)}</a>`).join("")}`;
  rail.appendChild(block);
}

export async function tryUniversityRoute(bare, ctx) {
  if (bare === "#/sandbox") {
    location.hash = "#/ivr";
    return true;
  }
  const pages = {
    "#/atlas": async () => renderAtlas(ctx),
    "#/flows": async () => renderFlows(ctx),
    "#/charts": async () => renderCharts(ctx),
    "#/play": async () => renderPlay(ctx),
    "#/regions": async () => renderRegions(ctx),
    "#/offline": async () => renderDownloads(ctx, true),
    "#/ports": async () => renderPorts(ctx, await loadUni()),
    "#/trouble": async () => renderTrouble(ctx, await loadUni()),
    "#/explorer": async () => renderExplorer(ctx),
    "#/downloads": async () => renderDownloads(ctx),
    "#/daily": async () => renderDaily(ctx),
    "#/badges": async () => renderBadges(ctx)
  };
  if (pages[bare]) {
    await pages[bare]();
    return true;
  }
  const section = bare.match(/^#\/(deploy|migrate|config|sip|wfm|record|e911|analytics|integrations|ai|security|roadmap|career)$/);
  if (section) {
    await renderSection(ctx, section[1]);
    return true;
  }
  return false;
}

const CRUMBS = {
  "#/atlas": "Diagrams",
  "#/flows": "Flows",
  "#/charts": "Charts",
  "#/downloads": "Cheat Codes",
  "#/play": "Play",
  "#/ecosystem": "Ecosystem",
  "#/offline": "Downloads",
  "#/career": "Careers",
  "#/regions": "Regions",
  "#/tracks": "Tracks",
  "#/tools": "Tools",
  "#/progress": "Progress",
  "#/ports": "Ports game",
  "#/daily": "Daily",
  "#/badges": "Badges",
  "#/ivr": "Call-flow sandbox",
  "#/search": "Search"
};

function paintCrumbs(bare) {
  const nav = document.querySelector("#crumbs");
  if (!nav) return;
  let label = CRUMBS[bare] || "";
  if (bare.startsWith("#/track/")) label = "Track";
  if (bare.startsWith("#/lesson/")) label = "Lesson";
  if (!label) {
    nav.innerHTML = `<a href="#/">Home</a>`;
    return;
  }
  nav.innerHTML = `<a href="#/">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">${esc(label)}</span>`;
}

function paintMenu(bare) {
  const current = (href) => {
    if (href === bare || (href === "#/" && (bare === "" || bare === "#/"))) return true;
    if (href === "#/tracks" && (bare.startsWith("#/track") || bare.startsWith("#/lesson"))) return true;
    return false;
  };
  document.querySelectorAll("#primary-menu a, #phone-nav a, #tabbar a").forEach((link) => {
    const href = link.getAttribute("href");
    if (current(href)) link.setAttribute("aria-current", "page");
    else link.removeAttribute("aria-current");
  });
  document.querySelectorAll("[data-theme-pick]").forEach((button) => {
    button.setAttribute("aria-pressed", button.dataset.themePick === document.documentElement.dataset.theme ? "true" : "false");
  });
}

let menuPushed = false;

function setMenuExpanded(open) {
  document.querySelectorAll("#menu-toggle, #tab-menu").forEach((button) => {
    button.setAttribute("aria-expanded", open ? "true" : "false");
  });
}

function closePhoneMenu(fromPop) {
  const dialog = document.querySelector("#phone-menu");
  const shouldBack = menuPushed && !fromPop;
  menuPushed = false;
  setMenuExpanded(false);
  if (dialog && dialog.open) dialog.close();
  if (shouldBack) history.back();
}

function openPhoneMenu() {
  const dialog = document.querySelector("#phone-menu");
  if (!dialog || dialog.open) return;
  dialog.showModal();
  setMenuExpanded(true);
  history.pushState({ f9menu: 1 }, "");
  menuPushed = true;
  const close = document.querySelector("#phone-close");
  if (close) close.focus();
}

let revealWatch = null;

function armReveal(root) {
  if (revealWatch) revealWatch.disconnect();
  const nodes = [...(root || document).querySelectorAll("#view .card, #view .panel, #view .fold, #view section, #view .spotlight")];
  const reduced = document.documentElement.dataset.motion === "reduce" || !("IntersectionObserver" in window);
  nodes.forEach((node) => node.classList.add("reveal"));
  if (reduced) {
    nodes.forEach((node) => node.classList.add("is-in"));
    return;
  }
  revealWatch = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("is-in");
      revealWatch.unobserve(entry.target);
    });
  }, { threshold: 0.12 });
  nodes.forEach((node) => revealWatch.observe(node));
}

function measureChrome() {
  const chrome = document.querySelector("#chrome");
  if (!chrome) return;
  const height = Math.ceil(chrome.getBoundingClientRect().height);
  if (height > 0) document.documentElement.style.setProperty("--chrome-h", `${height}px`);
}

function tickCounters(root) {
  (root || document).querySelectorAll("[data-count]").forEach((node) => {
    if (node.dataset.ticked === "1") return;
    const target = Number(node.dataset.count);
    if (!Number.isFinite(target)) return;
    node.dataset.ticked = "1";
    if (document.documentElement.dataset.motion === "reduce") {
      node.textContent = String(target);
      return;
    }
    const start = performance.now();
    const step = (now) => {
      const t = Math.min(1, (now - start) / 700);
      node.textContent = String(Math.round(target * (1 - (1 - t) ** 3)));
      if (t < 1) requestAnimationFrame(step);
    };
    node.textContent = "0";
    requestAnimationFrame(step);
  });
}

function whyFor(id, source) {
  if (id === "sip-ladder" || id === "sip-entries") {
    return "RFC 3261 teaching drawing. It is not a packet capture from a Five9 domain.";
  }
  if (id === "forecast-loop" || id.includes("erlang")) {
    return "Textbook Erlang. Five9 has not published this formula as the WEM engine.";
  }
  return `Teaching model. ${source || "The caption names the public page."}`;
}

function openLightbox(id) {
  const dialog = document.querySelector("#lightbox");
  const stage = document.querySelector("#lb-stage");
  if (!dialog || !stage) return;
  const row = diagramMeta.find((item) => item[0] === id);
  const title = row ? row[1] : id;
  const source = row ? row[2] : "";
  document.querySelector("#lb-title").textContent = title;
  stage.classList.remove("is-paused");
  stage.dataset.step = "0";
  stage.innerHTML = diagram(id) || `<p>That drawing is not in this atlas.</p>`;
  document.querySelector("#lb-why").textContent = whyFor(id, source);
  document.querySelector("#lb-legend").textContent = source;
  const play = document.querySelector("#lb-play");
  if (play) play.textContent = "Pause";
  if (!dialog.open) dialog.showModal();
}

function syncHero(bare) {
  const slot = document.querySelector("#hero-slot");
  const home = bare === "#/" || bare === "";
  if (!slot) return;
  if (!home) {
    import("./stage.js").then(async (mod) => {
      await mod.flyThrough();
      const now = (location.hash || "#/").split("?")[0];
      if (now === "#/" || now === "") return;
      slot.hidden = true;
      mod.stopHero();
    }).catch(() => { slot.hidden = true; });
    return;
  }
  slot.hidden = false;
  import("./stage.js").then((mod) => mod.mountHero(slot)).catch(() => {
    const flat = slot.querySelector("#hero-flat");
    if (flat) flat.hidden = false;
  });
}

export function afterRoute() {
  updateMascot();
  updateReadbar();
  startSky();
  measureChrome();
  const view = document.querySelector("#view");
  const bare = (location.hash || "#/").split("?")[0];
  document.body.dataset.route = bare || "#/";
  paintCrumbs(bare);
  paintMenu(bare);
  const settings = document.querySelector("#settings");
  if (settings && settings.open) settings.close();
  applyI18n();
  syncHero(bare);
  if (view && (bare === "#/" || bare === "") && !view.querySelector("#fold")) {
    mountHome(view).catch(() => {});
  }
  if (view && bare.startsWith("#/track/")) {
    decorateTrack(view).catch(() => {});
  }
  tickCounters(document);
  armReveal(document);
  import("./effects.js").then((mod) => mod.stopStage()).catch(() => {});
}

export function initUniversity() {
  const state = loadState();
  if (state.egg) document.documentElement.dataset.egg = "1";
  updateMascot();
  setInterval(updateMascot, 60000);
  armKonami();
  startSky();
  measureChrome();
  window.addEventListener("resize", () => {
    cancelAnimationFrame(sky.raf);
    startSky();
    measureChrome();
  });
  const chrome = document.querySelector("#chrome");
  if (chrome && "ResizeObserver" in window) {
    const watcher = new ResizeObserver(() => measureChrome());
    watcher.observe(chrome);
  }
  window.addEventListener("pointermove", (event) => {
    sky.pointer.x = event.clientX / window.innerWidth;
    sky.pointer.y = event.clientY / window.innerHeight;
  });
  window.addEventListener("scroll", updateReadbar, { passive: true });
  const search = document.querySelector("#uni-search");
  if (search) {
    search.addEventListener("submit", (event) => {
      event.preventDefault();
      const q = new FormData(search).get("q") || "";
      const dialog = document.querySelector("#settings");
      if (dialog && dialog.open) dialog.close();
      location.hash = `#/search?q=${encodeURIComponent(String(q))}`;
    });
  }
  const focus = document.querySelector("#read-focus");
  if (focus) {
    focus.addEventListener("click", () => {
      const on = document.documentElement.dataset.read === "1";
      document.documentElement.dataset.read = on ? "0" : "1";
      focus.setAttribute("aria-pressed", on ? "false" : "true");
      focus.textContent = on ? "Reading focus" : "Exit focus";
    });
  }
  const offline = document.querySelector("#offline-pack");
  if (offline) {
    offline.addEventListener("click", () => { location.hash = "#/offline"; });
  }
  const menu = document.querySelector("#primary-menu");
  if (menu) {
    menu.addEventListener("keydown", (event) => {
      if (event.key !== "ArrowRight" && event.key !== "ArrowLeft") return;
      const links = [...menu.querySelectorAll("a")];
      const index = links.indexOf(document.activeElement);
      if (index < 0) return;
      event.preventDefault();
      const next = event.key === "ArrowRight" ? (index + 1) % links.length : (index - 1 + links.length) % links.length;
      links[next].focus();
    });
  }
  const phoneMenu = document.querySelector("#phone-menu");
  const openers = ["#menu-toggle", "#tab-menu"];
  openers.forEach((sel) => {
    const button = document.querySelector(sel);
    if (button) button.addEventListener("click", () => openPhoneMenu());
  });
  const phoneClose = document.querySelector("#phone-close");
  if (phoneClose) phoneClose.addEventListener("click", () => closePhoneMenu(false));
  if (phoneMenu) {
    phoneMenu.addEventListener("close", () => {
      setMenuExpanded(false);
      if (menuPushed) {
        menuPushed = false;
        history.back();
      }
    });
    phoneMenu.addEventListener("click", (event) => {
      const link = event.target.closest("#phone-nav a");
      if (!link) return;
      event.preventDefault();
      const href = link.getAttribute("href") || "#/";
      const pushed = menuPushed;
      menuPushed = false;
      setMenuExpanded(false);
      if (phoneMenu.open) phoneMenu.close();
      if (!pushed) {
        if ((location.hash || "#/") !== href) location.hash = href;
        return;
      }
      const go = () => {
        window.removeEventListener("popstate", go);
        if ((location.hash || "#/") !== href) location.hash = href;
      };
      window.addEventListener("popstate", go);
      history.back();
    });
  }
  window.addEventListener("popstate", () => {
    if (phoneMenu && phoneMenu.open) closePhoneMenu(true);
  });
  const menuSettings = document.querySelector("#menu-settings");
  if (menuSettings) {
    menuSettings.addEventListener("click", () => {
      closePhoneMenu(false);
      const open = document.querySelector("#open-settings");
      if (open) open.click();
    });
  }
  const listen = document.querySelector("#tab-listen");
  if (listen) {
    listen.addEventListener("click", () => {
      if (phoneMenu && phoneMenu.open) closePhoneMenu(false);
      const dock = document.querySelector("#audio-dock");
      if (!dock) return;
      const reduced = document.documentElement.dataset.motion === "reduce";
      dock.scrollIntoView({ behavior: reduced ? "auto" : "smooth", block: "start" });
      const clip = dock.querySelector("audio");
      if (clip) clip.focus();
    });
  }
  window.addEventListener("scroll", () => {
    if (document.documentElement.dataset.motion === "reduce") return;
    const copy = document.querySelector("#hero-copy");
    if (!copy) return;
    const shift = Math.min(window.scrollY, 180) * 0.18;
    copy.style.transform = shift ? `translateY(${shift}px)` : "";
  }, { passive: true });
  document.addEventListener("click", (event) => {
    const opener = event.target.closest("[data-open-diagram]");
    if (opener) openLightbox(opener.dataset.openDiagram);
  });
  const lightbox = document.querySelector("#lightbox");
  const stage = document.querySelector("#lb-stage");
  const play = document.querySelector("#lb-play");
  const stepBtn = document.querySelector("#lb-step");
  const close = document.querySelector("#lb-close");
  if (close && lightbox) close.addEventListener("click", () => lightbox.close());
  if (play && stage) {
    play.addEventListener("click", () => {
      const paused = stage.classList.toggle("is-paused");
      play.textContent = paused ? "Play" : "Pause";
    });
  }
  if (stepBtn && stage) {
    stepBtn.addEventListener("click", () => {
      const nodes = [...stage.querySelectorAll(".node, .node-box, .flow-line, .packet")];
      nodes.forEach((node) => node.classList.remove("is-hot"));
      if (!nodes.length) return;
      const next = (Number(stage.dataset.step) || 0) % nodes.length;
      nodes[next].classList.add("is-hot");
      stage.dataset.step = String(next + 1);
      stage.classList.add("is-paused");
      if (play) play.textContent = "Play";
    });
  }
  const tip = document.querySelector("#tip");
  document.addEventListener("pointermove", (event) => {
    if (!tip) return;
    const node = event.target.closest ? event.target.closest("[data-tip]") : null;
    if (!node) {
      tip.hidden = true;
      return;
    }
    tip.hidden = false;
    tip.textContent = node.getAttribute("data-tip") || "";
    tip.style.left = `${Math.min(event.clientX + 14, window.innerWidth - 240)}px`;
    tip.style.top = `${Math.min(event.clientY + 16, window.innerHeight - 40)}px`;
  });
  document.querySelectorAll("#audio-dock audio").forEach((clip) => {
    clip.addEventListener("error", () => {
      const note = document.querySelector("#audio-fallback");
      if (note) note.hidden = false;
    });
  });
  const rate = document.querySelector("#audio-rate");
  if (rate) {
    rate.addEventListener("change", () => {
      const speed = Number(rate.value) || 1;
      document.querySelectorAll("#audio-dock audio").forEach((clip) => { clip.playbackRate = speed; });
    });
  }
  document.addEventListener("f9-theme", () => {
    warmGlyphs();
    const bare = (location.hash || "#/").split("?")[0];
    if (bare === "#/" || bare === "") syncHero(bare);
  });
  warmGlyphs();
  applyI18n();
  import("./effects.js").then((mod) => mod.armConfetti()).catch(() => {});
}

export { diagramIds };
