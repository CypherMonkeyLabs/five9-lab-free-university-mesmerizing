import { loadTopology, loadIvr, loadPacing } from "./loaders.js";
import { tryUniversityRoute, afterRoute, initUniversity, decorateRail, homeFoldHtml, signalDeck, paintHeroCopy, sourcesBlock } from "./university.js";
import { glyphImg, glyphKey } from "./glyphs.js";
import { applyI18n } from "./i18n.js";
import { initGuide } from "./guide.js";

const SETTINGS_KEY = "f9lab-settings";
const PROGRESS_KEY = "f9lab-progress";

const view = document.querySelector("#view");
const titleEl = document.querySelector("#view-title");
const ledeEl = document.querySelector("#lede");
const rail = document.querySelector("#rail");
const main = document.querySelector("#main");

const session = {
  catalog: null,
  tracks: new Map(),
  extras: new Map(),
  settings: loadSettings(),
  progress: loadProgress(),
  abort: new AbortController(),
  destroy: null,
  speaking: false
};

const audio = {
  ctx: null,
  ensure() {
    if (!session.settings.sound) return null;
    if (!this.ctx) this.ctx = new AudioContext();
    if (this.ctx.state === "suspended") this.ctx.resume();
    return this.ctx;
  },
  tone(freq, dur, type, gain) {
    const ctx = this.ensure();
    if (!ctx) return;
    const osc = ctx.createOscillator();
    const amp = ctx.createGain();
    osc.type = type || "sine";
    osc.frequency.value = freq;
    amp.gain.value = gain || 0.04;
    osc.connect(amp);
    amp.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + dur);
  },
  tick() { this.tone(540, 0.04, "sine", 0.03); },
  ok() {
    this.tone(660, 0.08, "sine", 0.04);
    setTimeout(() => this.tone(880, 0.1, "sine", 0.04), 90);
  },
  bad() { this.tone(160, 0.16, "triangle", 0.04); },
  ring() {
    this.tone(440, 0.4, "sine", 0.03);
    this.tone(480, 0.4, "sine", 0.02);
  }
};

function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, (ch) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[ch]));
}

function loadSettings() {
  const base = {
    theme: "light",
    lang: "en",
    sound: false,
    narration: false,
    voiceURI: "",
    rate: 1,
    reduced: null,
    font: 16
  };
  try {
    return Object.assign(base, JSON.parse(localStorage.getItem(SETTINGS_KEY) || "{}"));
  } catch (err) {
    return base;
  }
}

function saveSettings() {
  localStorage.setItem(SETTINGS_KEY, JSON.stringify(session.settings));
  applySettings();
}

function loadProgress() {
  const base = { lessons: {}, labs: {}, faults: {}, bosses: {}, last: "" };
  try {
    return Object.assign(base, JSON.parse(localStorage.getItem(PROGRESS_KEY) || "{}"));
  } catch (err) {
    return base;
  }
}

function saveProgress() {
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(session.progress));
}

function motionReduced() {
  if (session.settings.reduced === true) return true;
  if (session.settings.reduced === false) return false;
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

function applySettings() {
  const root = document.documentElement;
  root.dataset.theme = session.settings.theme || "signal";
  root.dataset.font = String(session.settings.font || 16);
  if (session.settings.ink) root.style.setProperty("--ink", session.settings.ink);
  root.dataset.motion = motionReduced() ? "reduce" : "full";
  const soundBtn = document.querySelector("#sound-toggle");
  if (soundBtn) {
    soundBtn.textContent = session.settings.sound ? "Sound on" : "Sound off";
    soundBtn.setAttribute("aria-pressed", session.settings.sound ? "true" : "false");
  }
  paintSettingsForm();
  document.dispatchEvent(new CustomEvent("f9-theme"));
  applyI18n();
}

function roboticPenalty(name) {
  const n = name.toLowerCase();
  const classic = /(david|zira|mark|hazel|susan|george)/.test(n);
  const natural = /(natural|neural|premium|enhanced|online)/.test(n);
  if (classic && !natural) return -120;
  return 0;
}

function scoreVoice(voice) {
  const name = `${voice.name} ${voice.voiceURI}`.toLowerCase();
  let score = roboticPenalty(name);
  if ((voice.lang || "").toLowerCase().startsWith("en")) score += 30;
  if (/natural|neural|premium|enhanced/.test(name)) score += 80;
  if (/siri|samantha|google/.test(name)) score += 40;
  if (/microsoft/.test(name) && /natural|online/.test(name)) score += 70;
  return score;
}

function pickVoice(voices) {
  if (!voices.length) return null;
  if (session.settings.voiceURI) {
    const saved = voices.find((voice) => voice.voiceURI === session.settings.voiceURI);
    if (saved && roboticPenalty(`${saved.name} ${saved.voiceURI}`) > -100) return saved;
  }
  return voices.slice().sort((a, b) => scoreVoice(b) - scoreVoice(a))[0];
}

function fillVoices() {
  const select = document.querySelector("#set-voice");
  const note = document.querySelector("#voice-note");
  const voices = window.speechSynthesis ? window.speechSynthesis.getVoices() : [];
  if (!select) return;
  select.innerHTML = "";
  if (!voices.length) {
    note.textContent = "No speech voices yet. The list fills after the browser fires voiceschanged.";
    return;
  }
  const ranked = voices.slice().sort((a, b) => scoreVoice(b) - scoreVoice(a));
  ranked.forEach((voice) => {
    const option = document.createElement("option");
    option.value = voice.voiceURI;
    option.textContent = `${voice.name} (${voice.lang})`;
    select.appendChild(option);
  });
  const chosen = pickVoice(voices);
  if (chosen) select.value = chosen.voiceURI;
  const best = ranked[0];
  note.textContent = best && scoreVoice(best) < 20
    ? "Only low-quality voices are installed. Pick one, or install a natural voice in the OS."
    : "Natural and neural voices are ranked first. Classic robotic desktop voices are not the default.";
}

function speak(text) {
  if (!session.settings.narration || !window.speechSynthesis) return;
  const synth = window.speechSynthesis;
  const run = () => {
    const voices = synth.getVoices();
    const voice = pickVoice(voices);
    const utterance = new SpeechSynthesisUtterance(text);
    if (voice) utterance.voice = voice;
    utterance.rate = Number(session.settings.rate) || 1;
    synth.cancel();
    synth.speak(utterance);
  };
  if (synth.getVoices().length) run();
  else {
    const onVoices = () => {
      synth.removeEventListener("voiceschanged", onVoices);
      run();
    };
    synth.addEventListener("voiceschanged", onVoices);
    synth.getVoices();
  }
}

function stopSpeech() {
  if (window.speechSynthesis) window.speechSynthesis.cancel();
}

function resetView() {
  session.abort.abort();
  session.abort = new AbortController();
  if (session.destroy) {
    session.destroy();
    session.destroy = null;
  }
  stopSpeech();
  view.innerHTML = "";
}

function setTitle(text, lede) {
  titleEl.textContent = text;
  ledeEl.textContent = lede || "";
  document.title = text === "Five9 Lab" ? "Five9 Lab" : `${text} · Five9 Lab`;
}

async function getJson(path) {
  if (session.extras.has(path)) return session.extras.get(path);
  const response = await fetch(path);
  if (!response.ok) throw new Error(`Could not load ${path}`);
  const data = await response.json();
  session.extras.set(path, data);
  return data;
}

async function getCatalog() {
  if (session.catalog) return session.catalog;
  const response = await fetch("data/catalog.json");
  if (!response.ok) throw new Error("catalog");
  session.catalog = await response.json();
  return session.catalog;
}

async function getTrack(id) {
  if (session.tracks.has(id)) return session.tracks.get(id);
  const catalog = await getCatalog();
  const meta = catalog.tracks.find((track) => track.id === id);
  if (!meta) return null;
  const response = await fetch(`data/${meta.file}`);
  if (!response.ok) throw new Error(meta.file);
  const track = await response.json();
  session.tracks.set(id, track);
  return track;
}

function on(node, type, fn) {
  node.addEventListener(type, fn, { signal: session.abort.signal });
}

function lessonCount() {
  return session.catalog.tracks.reduce((sum, track) => sum + track.lessons.length, 0);
}

function doneCount() {
  return Object.values(session.progress.lessons).filter((row) => row.done).length;
}

function card(href, kicker, heading, body, tags) {
  return `<a class="card" href="${esc(href)}">${glyphImg(glyphKey(href))}<div class="card-copy"><p class="kicker">${esc(kicker)}</p><h2>${esc(heading)}</h2><p>${esc(body)}</p>${tags ? `<div class="tags">${tags}</div>` : ""}</div></a>`;
}

function renderRail() {
  const catalog = session.catalog;
  if (!catalog) {
    rail.innerHTML = "";
    return;
  }
  const groups = {};
  catalog.tracks.forEach((track) => {
    groups[track.group] = groups[track.group] || [];
    groups[track.group].push(track);
  });
  const tools = [
    ["#/topology", "3D topology", "a1"],
    ["#/ivr", "IVR builder", "a2"],
    ["#/pacing", "Dialer pacing", "a3"],
    ["#/ecosystem", "Ecosystem", "a4"],
    ["#/certs", "Certifications", "a2"],
    ["#/boss", "Boss incidents", "a3"],
    ["#/interview", "Interview Q&A", "a4"],
    ["#/progress", "Progress", "a1"]
  ];
  rail.innerHTML = `<a href="#/"><span class="dot"></span>Floor</a>
    <a href="#/tracks"><span class="dot a2"></span>All tracks</a>
    <a href="#/tools"><span class="dot a3"></span>Tools</a>
    ${Object.entries(groups).map(([group, tracks]) => `<h2>${esc(group)}</h2>${tracks.map((track) => `<a href="#/track/${esc(track.id)}"><span class="dot a4"></span>${esc(track.short)}</a>`).join("")}`).join("")}
    <h2>Benches</h2>
    ${tools.map(([href, label, dot]) => `<a href="${href}"><span class="dot ${dot}"></span>${esc(label)}</a>`).join("")}`;
  decorateRail();
  markCurrent();
}

function markCurrent() {
  const hash = location.hash || "#/";
  document.querySelectorAll("#rail a, #tabbar a").forEach((link) => {
    const href = link.getAttribute("href");
    const on = href === hash || (href === "#/tracks" && hash.startsWith("#/track")) || (href === "#/tracks" && hash.startsWith("#/lesson"));
    if (on) link.setAttribute("aria-current", "page");
    else link.removeAttribute("aria-current");
  });
}

async function renderHome() {
  setTitle("Five9 Lab", "Run the floor. Build an IVR, pace a dialer, and break a SIP path on purpose.");
  const catalog = session.catalog;
  const last = session.progress.last;
  const fold = await homeFoldHtml();
  view.innerHTML = `
    ${fold}
    ${signalDeck(catalog)}
    <section class="panel">
      <p>A contact-center operations console for Five9 Virtual Contact Center. Campaigns, dialer modes, IVR, skills, Agent Desktop Plus, WEM, IVA, CRM adapters, SIP, APIs, and a Cisco UCCX/UCCE bridge. Every claim is linked. Anything not settled in a public page is marked uncertain.</p>
      <p class="note">Not affiliated with Five9, Inc. Names are used so the citations stay checkable.</p>
      <div class="row">
        ${last ? `<a class="btn primary" href="${esc(last)}">Resume</a>` : `<a class="btn primary" href="#/track/t01">Start with the domain</a>`}
        <a class="btn" href="#/topology">Open the 3D floor</a>
        <a class="btn" href="#/play">Play</a>
      </div>
    </section>
    <h2>Benches</h2>
    <div class="grid">
      ${card("#/topology", "WebGL", "3D topology", "Orbit the domain, SBCs, IVR, agents, CRM, and RedSky. Toggle a trunk, a WAN, or a stale 911 address.", `<span class="tag hot">Failure toggles</span>`)}
      ${card("#/ivr", "Script", "IVR builder", "Place the modules named in the IVR Administrator's Guide and walk a call with DTMF.", `<span class="tag">Learning model</span>`)}
      ${card("#/pacing", "Dialer", "Pacing simulator", "Preview, progressive, power, predictive, and TCPA manual touch on a teaching clock.", `<span class="tag">Not Five9 source</span>`)}
      ${card("#/boss", "Incidents", "Boss log", "Synthetic call logs. Find the stopped campaign, the blend, the paste block, the stale address.", "")}
    </div>
    <h2>Tracks</h2>
    <div class="grid">
      ${catalog.tracks.map((track) => card(`#/track/${track.id}`, track.group, track.title, track.blurb, `<span class="tag">${track.lessons.length} lessons</span>`)).join("")}
    </div>`;
  paintHeroCopy(catalog);
}

function renderTracks() {
  setTitle("Tracks", `${session.catalog.tracks.length} paths from the domain model through routing, workforce, quality, CRM, and the ecosystem.`);
  const groups = {};
  session.catalog.tracks.forEach((track) => {
    groups[track.group] = groups[track.group] || [];
    groups[track.group].push(track);
  });
  view.innerHTML = Object.entries(groups).map(([group, tracks]) => `
    <h2>${esc(group)}</h2>
    <div class="grid">${tracks.map((track) => card(`#/track/${track.id}`, track.level, track.title, track.blurb, `<span class="tag">${track.lessons.length} lessons</span>`)).join("")}</div>
  `).join("");
}

function renderTools() {
  setTitle("Tools", "Simulators and reference benches. They load only when you open them.");
  view.innerHTML = `<div class="grid">
    ${card("#/topology", "3D", "Topology", "Vendored Three.js scene with orbit controls and failure toggles. Reduced motion uses a flat map.", "")}
    ${card("#/ivr", "IVR", "Script builder", "Official module names, a call walkthrough, and a JSON export that is not a VCC import file.", "")}
    ${card("#/pacing", "Dialer", "Pacing simulator", "Occupancy, abandon rate, and a TCPA typing drill that refuses paste.", "")}
    ${card("#/ecosystem", "Map", "Ecosystem", "Glossary, mind map, and the systems that sit beside VCC.", "")}
    ${card("#/certs", "Study", "Certifications", "Five9 University paths and the credentials we could verify. Gaps stay marked.", "")}
    ${card("#/interview", "Oral", "Interview Q&A", "Short answers with the same citations as the lessons.", "")}
    ${card("#/boss", "On call", "Boss incidents", "Multi-step log reading.", "")}
    ${card("#/progress", "You", "Progress", "Quiz scores and lab checks stored on this device.", "")}
  </div>`;
}

async function renderTrack(id) {
  const track = await getTrack(id);
  if (!track) return renderMissing("That track is not on this floor");
  setTitle(track.title, track.summary);
  view.innerHTML = `
    <p>${esc(track.summary)}</p>
    <ol class="checks">
      ${track.lessons.map((lesson, index) => {
        const key = `${track.id}/${lesson.id}`;
        const row = session.progress.lessons[key];
        const mark = row && row.done ? "Done" : "Open";
        return `<li><a href="#/lesson/${esc(track.id)}/${esc(lesson.id)}">${index + 1}. ${esc(lesson.title)}</a> <span class="tag">${esc(lesson.level)}</span> <span class="tag">${esc(mark)}</span></li>`;
      }).join("")}
    </ol>`;
}

function figureSvg(figure) {
  const rows = figure.rows || [];
  if (figure.kind === "compare") {
    const left = figure.left || [];
    const right = figure.right || [];
    const n = Math.max(left.length, right.length);
    const h = 56 + n * 36;
    const col = (items, x, color) => items.map((item, i) => `<rect x="${x}" y="${48 + i * 36}" width="200" height="28" rx="6" fill="#102033" stroke="${color}"></rect><text x="${x + 10}" y="${67 + i * 36}" fill="#e7eef8" font-size="13">${esc(item)}</text>`).join("");
    return `<svg class="figure-svg" width="460" height="${h}" viewBox="0 0 460 ${h}" role="img" aria-label="${esc(figure.title)}"><rect width="460" height="${h}" fill="#041018"></rect><text x="16" y="28" fill="#9aefff" font-size="14">${esc(figure.leftTitle || "A")}</text><text x="244" y="28" fill="#f5b942" font-size="14">${esc(figure.rightTitle || "B")}</text>${col(left, 16, "#3ee0ff")}${col(right, 244, "#f5b942")}</svg>`;
  }
  if (figure.kind === "path") {
    const w = Math.max(460, rows.length * 120);
    return `<svg class="figure-svg" width="${w}" height="140" viewBox="0 0 ${w} 140" role="img" aria-label="${esc(figure.title)}"><rect width="${w}" height="140" fill="#041018"></rect>${rows.map((row, i) => `<line x1="${70 + i * 120}" y1="70" x2="${i === rows.length - 1 ? 70 + i * 120 : 130 + i * 120}" y2="70" stroke="#3ee0ff"></line><rect x="${20 + i * 120}" y="48" width="100" height="44" rx="8" fill="#102033" stroke="#3ddc97"></rect><text x="${70 + i * 120}" y="74" text-anchor="middle" fill="#e7eef8" font-size="12">${esc(row.label)}</text>`).join("")}</svg>`;
  }
  const h = 48 + rows.length * 52;
  return `<svg class="figure-svg" width="460" height="${h}" viewBox="0 0 460 ${h}" role="img" aria-label="${esc(figure.title)}"><rect width="460" height="${h}" fill="#041018"></rect>${rows.map((row, i) => `<rect x="24" y="${24 + i * 52}" width="${412 - i * 18}" height="40" rx="8" fill="#102033" stroke="${i % 2 ? "#f5b942" : "#3ee0ff"}"></rect><text x="36" y="${48 + i * 52}" fill="#e7eef8" font-size="14">${esc(row.label)}</text>`).join("")}</svg>`;
}

function flowSvg(flow, index) {
  const lanes = flow.lanes;
  const steps = flow.steps;
  const colW = 140;
  const width = lanes.length * colW + 20;
  const height = 54 + steps.length * 64;
  const heads = lanes.map((lane, i) => `<text x="${20 + i * colW + colW / 2}" y="22" text-anchor="middle" fill="#9aefff" font-size="12">${esc(lane)}</text><line x1="${20 + i * colW + colW / 2}" y1="30" x2="${20 + i * colW + colW / 2}" y2="${height - 10}" stroke="#1d3c52"></line>`).join("");
  const bodies = steps.map((step, i) => {
    const lane = Math.max(0, lanes.indexOf(step.lane));
    const x = 28 + lane * colW;
    const y = 40 + i * 64;
    const on = i === index;
    return `<rect x="${x}" y="${y}" width="${colW - 24}" height="46" rx="8" fill="${on ? "#173049" : "#102033"}" stroke="${on ? "#f5b942" : "#3ee0ff"}"></rect><text x="${x + 8}" y="${y + 28}" fill="#e7eef8" font-size="12">${esc(step.title)}</text>`;
  }).join("");
  return `<svg class="flow-svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-label="${esc(flow.title)}">${heads}${bodies}</svg>`;
}

function renderLesson(track, lesson, stem, sourceRows) {
  const key = `${track.id}/${lesson.id}`;
  session.progress.last = `#/lesson/${track.id}/${lesson.id}`;
  saveProgress();
  const state = { qi: 0, fi: 0, face: "front", flow: 0, playing: false, timer: 0, inspected: false };
  setTitle(lesson.title, `${track.title} · ${lesson.level} · ${lesson.minutes} min`);

  const paint = () => {
    const q = lesson.quiz[state.qi];
    const cardItem = lesson.cards[state.fi];
    const step = lesson.flow.steps[state.flow];
    const downloads = stem ? `<div class="section-downloads"><a class="btn" href="../rooms/${stem}.html">Open room</a><a class="btn" href="../downloads/sections/${stem}-learn.html" download>Learn</a><a class="btn" href="../downloads/diagrams/${stem}.svg" download>SVG</a><a class="btn" href="../downloads/diagrams/${stem}.png" download>PNG</a><a class="btn" href="../downloads/diagrams/${stem}.html" download>Diagram</a></div>` : "";
    view.innerHTML = `
      <div class="lesson-layout">
        <article>
          <section data-read-section="lesson">
          ${downloads}
          <p class="kicker">${esc(track.title)}</p>
          <ul>${lesson.objectives.map((item) => `<li>${esc(item)}</li>`).join("")}</ul>
          ${lesson.paragraphs.map((p) => `<p data-sentence>${esc(p)}</p>`).join("")}
          ${lesson.callout ? `<div class="callout"><strong>${esc(lesson.callout.title)}</strong><p>${esc(lesson.callout.body)}</p></div>` : ""}
          ${lesson.uncertain && lesson.uncertain.length ? `<div class="uncertain"><strong>Uncertain</strong><ul>${lesson.uncertain.map((item) => `<li>${esc(item)}</li>`).join("")}</ul></div>` : ""}
          <figure class="figure">${figureSvg(lesson.figure)}<figcaption>${esc(lesson.figure.caption)}</figcaption></figure>
          <section class="panel" id="quiz-box">
            <h2>Check yourself</h2>
            <p>Question ${state.qi + 1} of ${lesson.quiz.length}</p>
            <fieldset>
              <legend>${esc(q.q)}</legend>
              ${q.choices.map((choice, i) => `<label class="choice"><input type="radio" name="quiz" value="${i}"> ${esc(choice)}</label>`).join("")}
            </fieldset>
            <div class="row">
              <button type="button" class="btn primary" id="quiz-check">Check answer</button>
              <button type="button" class="btn" id="quiz-next" disabled>Next</button>
            </div>
            <p class="why" id="quiz-why" role="status"></p>
          </section>
          <section class="panel">
            <h2>Flashcards</h2>
            <div class="flash" id="flash"><p>${esc(state.face === "front" ? cardItem.front : cardItem.back)}</p></div>
            <div class="row">
              <button type="button" class="btn" id="flip">Flip</button>
              <button type="button" class="btn" id="card-prev">Previous</button>
              <button type="button" class="btn" id="card-next">Next</button>
            </div>
          </section>
          <section class="panel">
            <h2>Lab · ${esc(lesson.lab.title)}</h2>
            <p>${esc(lesson.lab.goal)}</p>
            <ul class="checks" id="lab-checks">
              ${lesson.lab.steps.map((stepText, i) => `<li><label><input type="checkbox" data-lab="${i}"> ${esc(stepText)}</label></li>`).join("")}
            </ul>
            <p class="note">${esc(lesson.lab.success)}</p>
            ${lesson.lab.href ? `<p><a class="btn" href="${esc(lesson.lab.href)}">Open the bench</a></p>` : ""}
          </section>
          <section class="panel">
            <h2>Fault · ${esc(lesson.fault.title)}</h2>
            <p>${esc(lesson.fault.symptom)}</p>
            <pre class="log">${esc(lesson.fault.log)}</pre>
            <fieldset>
              <legend>What failed?</legend>
              ${lesson.fault.choices.map((choice, i) => `<label class="choice"><input type="radio" name="fault" value="${i}"> ${esc(choice)}</label>`).join("")}
            </fieldset>
            <button type="button" class="btn primary" id="fault-check">Test the hypothesis</button>
            <p class="why" id="fault-why" role="status"></p>
          </section>
          ${sourcesBlock(sourceRows && sourceRows.length ? sourceRows : lesson.cites.map((cite) => ({ label: cite.label, url: cite.url, kind: "vendor", status: "confirm", lastChecked: "2026-10", note: cite.note || "" })))}
          </section>
        </article>
        <aside class="scope" id="flow-box" tabindex="0" aria-label="Call flow player">
          <h2>${esc(lesson.flow.title)}</h2>
          <div class="row">
            <button type="button" class="btn primary" id="flow-play">${state.playing ? "Pause" : "Play"}</button>
            <button type="button" class="btn" id="flow-step">Step</button>
            <button type="button" class="btn" id="flow-inspect" aria-pressed="${state.inspected ? "true" : "false"}">Inspect</button>
          </div>
          <div id="flow-svg">${flowSvg(lesson.flow, state.flow)}</div>
          <p id="flow-live" role="status">${esc(step.lane)}: ${esc(step.detail)}</p>
          ${state.inspected ? `<pre class="log">${esc(step.frame || step.detail)}</pre>` : ""}
          <div class="row">
            <button type="button" class="btn" id="narrate">Narrate lesson</button>
            <button type="button" class="btn ghost" id="narrate-stop">Stop voice</button>
          </div>
        </aside>
      </div>`;
    bindLesson();
  };

  const stopPlay = () => {
    state.playing = false;
    if (state.timer) {
      clearInterval(state.timer);
      state.timer = 0;
    }
  };

  const bindLesson = () => {
    const checks = session.progress.labs[key] || [];
    view.querySelectorAll("[data-lab]").forEach((box) => {
      box.checked = checks.includes(Number(box.dataset.lab));
      on(box, "change", () => {
        const selected = [...view.querySelectorAll("[data-lab]:checked")].map((node) => Number(node.dataset.lab));
        session.progress.labs[key] = selected;
        if (selected.length === lesson.lab.steps.length) {
          session.progress.lessons[key] = Object.assign({ quiz: 0, done: false }, session.progress.lessons[key], { done: true });
        }
        saveProgress();
      });
    });
    on(view.querySelector("#quiz-check"), "click", () => {
      const picked = view.querySelector("input[name=quiz]:checked");
      const why = view.querySelector("#quiz-why");
      if (!picked) {
        why.textContent = "Choose an answer first.";
        return;
      }
      const q = lesson.quiz[state.qi];
      const good = Number(picked.value) === q.answer;
      why.textContent = `${good ? "Correct. " : "Not yet. "}${q.why}`;
      why.className = good ? "why ok" : "why bad";
      if (good) {
        audio.ok();
        window.dispatchEvent(new CustomEvent("f9-correct"));
      } else audio.bad();
      const row = session.progress.lessons[key] || { quiz: 0, done: false };
      if (good) row.quiz = Math.max(row.quiz || 0, state.qi + 1);
      if (row.quiz >= lesson.quiz.length) row.done = true;
      session.progress.lessons[key] = row;
      saveProgress();
      view.querySelector("#quiz-next").disabled = false;
    });
    on(view.querySelector("#quiz-next"), "click", () => {
      state.qi = (state.qi + 1) % lesson.quiz.length;
      paint();
    });
    on(view.querySelector("#flip"), "click", () => {
      state.face = state.face === "front" ? "back" : "front";
      audio.tick();
      paint();
    });
    on(view.querySelector("#card-next"), "click", () => {
      state.fi = (state.fi + 1) % lesson.cards.length;
      state.face = "front";
      paint();
    });
    on(view.querySelector("#card-prev"), "click", () => {
      state.fi = (state.fi - 1 + lesson.cards.length) % lesson.cards.length;
      state.face = "front";
      paint();
    });
    on(view.querySelector("#fault-check"), "click", () => {
      const picked = view.querySelector("input[name=fault]:checked");
      const why = view.querySelector("#fault-why");
      if (!picked) {
        why.textContent = "Pick a hypothesis.";
        return;
      }
      const good = Number(picked.value) === lesson.fault.answer;
      why.textContent = good ? `Correct. ${lesson.fault.fix}` : `Not that one. ${lesson.fault.cause}`;
      why.className = good ? "why ok" : "why bad";
      if (good) {
        audio.ok();
        window.dispatchEvent(new CustomEvent("f9-correct"));
        session.progress.faults[key] = true;
        saveProgress();
      } else audio.bad();
    });
    on(view.querySelector("#flow-step"), "click", () => {
      stopPlay();
      state.flow = (state.flow + 1) % lesson.flow.steps.length;
      audio.tick();
      refreshFlow();
    });
    on(view.querySelector("#flow-inspect"), "click", () => {
      state.inspected = !state.inspected;
      refreshFlow();
    });
    const refreshFlow = () => {
      const current = lesson.flow.steps[state.flow];
      const playBtn = view.querySelector("#flow-play");
      if (playBtn) playBtn.textContent = state.playing ? "Pause" : "Play";
      const svg = view.querySelector("#flow-svg");
      if (svg) svg.innerHTML = flowSvg(lesson.flow, state.flow);
      const live = view.querySelector("#flow-live");
      if (live) live.textContent = `${current.lane}: ${current.detail}`;
      const inspect = view.querySelector("#flow-inspect");
      if (inspect) inspect.setAttribute("aria-pressed", state.inspected ? "true" : "false");
      let frame = view.querySelector("#flow-frame");
      if (state.inspected) {
        if (!frame) {
          frame = document.createElement("pre");
          frame.id = "flow-frame";
          frame.className = "log";
          inspect.insertAdjacentElement("afterend", frame);
        }
        frame.textContent = current.frame || current.detail;
      } else if (frame) frame.remove();
    };
    on(view.querySelector("#flow-play"), "click", () => {
      if (state.playing) {
        stopPlay();
        refreshFlow();
        return;
      }
      state.playing = true;
      refreshFlow();
      state.timer = window.setInterval(() => {
        state.flow = (state.flow + 1) % lesson.flow.steps.length;
        audio.tick();
        if (state.flow === 0) stopPlay();
        refreshFlow();
      }, motionReduced() ? 1600 : 1200);
    });
    on(view.querySelector("#narrate"), "click", () => {
      if (!session.settings.narration) {
        view.querySelector("#flow-live").textContent = "Turn narration on in Settings, then pick a voice.";
        return;
      }
      speak(`${lesson.title}. ${lesson.paragraphs.join(" ")}`);
    });
    on(view.querySelector("#narrate-stop"), "click", stopSpeech);
    const flowBox = view.querySelector("#flow-box");
    on(flowBox, "keydown", (event) => {
      if (event.key === "ArrowRight") view.querySelector("#flow-step").click();
      if (event.key === " ") {
        event.preventDefault();
        view.querySelector("#flow-play").click();
      }
    });
  };

  session.destroy = stopPlay;
  paint();
}

async function lessonStem(track, lesson) {
  try {
    const manifest = await getJson("../downloads/manifest.json");
    const prefix = `${track.id}-${lesson.id}-`;
    const hit = (manifest.diagrams || []).find((row) => String(row.id).startsWith(prefix));
    return hit ? hit.id : "";
  } catch (err) {
    return "";
  }
}

async function openLesson(trackId, lessonId) {
  const track = await getTrack(trackId);
  if (!track) return renderMissing("That track is not on this floor");
  const lesson = track.lessons.find((item) => item.id === lessonId);
  if (!lesson) return renderMissing("That lesson is not on this floor");
  const stem = await lessonStem(track, lesson);
  let sourceRows = [];
  if (stem) {
    try {
      const packed = await (await fetch(`../rooms/${stem}.sources.json`)).json();
      sourceRows = packed.sources || [];
    } catch (err) {
      sourceRows = [];
    }
  }
  renderLesson(track, lesson, stem, sourceRows);
}

function renderMissing(text) {
  setTitle(text, "The address does not match a track or lesson.");
  view.innerHTML = `<p>Try the track list, or go back to the floor.</p><p><a class="btn primary" href="#/tracks">All tracks</a> <a class="btn" href="#/">Floor</a></p>`;
}

function renderProgress() {
  setTitle("Progress", "Stored in localStorage on this browser. Nothing is sent to a server.");
  const lessons = lessonCount();
  const done = doneCount();
  const faults = Object.keys(session.progress.faults).length;
  view.innerHTML = `
    <div class="stats">
      <div class="panel stat"><strong>${done}/${lessons}</strong><span>Lessons marked done</span></div>
      <div class="panel stat"><strong>${faults}</strong><span>Faults solved</span></div>
      <div class="panel stat"><strong>${Object.keys(session.progress.bosses).length}</strong><span>Boss incidents cleared</span></div>
    </div>
    <p>A lesson marks done when every quiz question has been answered correctly at least once, or when every lab checkbox is checked.</p>
    <button type="button" class="btn" id="reset-progress">Clear progress on this device</button>`;
  on(view.querySelector("#reset-progress"), "click", () => {
    session.progress = { lessons: {}, labs: {}, faults: {}, bosses: {}, last: "" };
    saveProgress();
    renderProgress();
  });
}

async function renderSearch(query) {
  setTitle("Search", "Lessons, glossary rows, and university pages. The index is built from the lesson text in this repo.");
  const q = (query || "").trim().toLowerCase();
  const hits = [];
  let index = [];
  try {
    index = (await getJson("data/search-index.json")).items;
  } catch (err) {
    index = [];
  }
  if (q) {
    index.forEach((item) => {
      const hay = `${item.title} ${item.note || ""} ${item.snippet || ""}`.toLowerCase();
      if (hay.includes(q)) hits.push(item);
    });
  }
  const shown = hits.slice(0, 40);
  view.innerHTML = `
    <form id="search-form" role="search">
      <div class="field"><label for="q">Search lessons</label><input id="q" name="q" type="search" value="${esc(query || "")}"></div>
      <button class="btn primary" type="submit">Search</button>
    </form>
    ${q ? `<p>${hits.length ? `${shown.length} shown${hits.length > shown.length ? ` of ${hits.length}` : ""}` : "No matches. Try DNIS, TCPA, RedSky, or WEM."}</p>` : `<p class="note">Enter a word. The index includes lesson openings and glossary rows.</p>`}
    <ul>${shown.map((hit) => `<li><a href="${esc(hit.href)}">${esc(hit.title)}</a> <span class="note">${esc(hit.note)}</span></li>`).join("")}</ul>`;
  on(view.querySelector("#search-form"), "submit", (event) => {
    event.preventDefault();
    location.hash = `#/search?q=${encodeURIComponent(view.querySelector("#q").value)}`;
  });
}

async function renderEcosystem() {
  const data = await getJson("data/ecosystem.json");
  setTitle("Ecosystem", "Glossary, mind map, and the systems that sit next to a Five9 domain.");
  view.innerHTML = `
    <div class="figure">${data.map}<p class="note">${esc(data.mapCaption)}</p></div>
    <div class="field"><label for="gloss">Filter glossary</label><input id="gloss" type="search"></div>
    <div class="table-wrap"><table id="gloss-table"><thead><tr><th>Term</th><th>Meaning</th><th>Source</th></tr></thead><tbody>
      ${data.glossary.map((row) => `<tr><td>${esc(row.term)}</td><td>${esc(row.meaning)}</td><td><a href="${esc(row.url)}" rel="noopener" target="_blank">${esc(row.source)}</a></td></tr>`).join("")}
    </tbody></table></div>
    <h2>Integration map</h2>
    <div class="table-wrap"><table><thead><tr><th>System</th><th>How it meets VCC</th><th>Source</th></tr></thead><tbody>
      ${data.integrations.map((row) => `<tr><td>${esc(row.system)}</td><td>${esc(row.how)}</td><td><a href="${esc(row.url)}" rel="noopener" target="_blank">${esc(row.source)}</a></td></tr>`).join("")}
    </tbody></table></div>
    ${data.uncertain.length ? `<div class="uncertain"><strong>Uncertain</strong><ul>${data.uncertain.map((item) => `<li>${esc(item)}</li>`).join("")}</ul></div>` : ""}`;
  on(view.querySelector("#gloss"), "input", (event) => {
    const q = event.target.value.toLowerCase();
    view.querySelectorAll("#gloss-table tbody tr").forEach((row) => {
      row.hidden = q && !row.textContent.toLowerCase().includes(q);
    });
  });
}

async function renderCerts() {
  const data = await getJson("data/certs.json");
  setTitle("Certifications and courses", "Official names we could verify. Missing exam codes stay blank on purpose.");
  view.innerHTML = `
    <p>${esc(data.intro)}</p>
    <div class="table-wrap"><table><thead><tr><th>Name</th><th>Status</th><th>What is public</th><th>Source</th></tr></thead><tbody>
      ${data.items.map((item) => `<tr><td>${esc(item.name)}</td><td><span class="tag ${item.status === "Verified" ? "ok" : "warn"}">${esc(item.status)}</span></td><td>${esc(item.detail)}</td><td><a href="${esc(item.url)}" rel="noopener" target="_blank">${esc(item.source)}</a></td></tr>`).join("")}
    </tbody></table></div>
    <div class="uncertain"><strong>Uncertain</strong><ul>${data.uncertain.map((item) => `<li>${esc(item)}</li>`).join("")}</ul></div>`;
}

async function renderInterview() {
  const data = await getJson("data/interview.json");
  setTitle("Interview Q&A", "Short answers a hiring panel can check against the linked page.");
  let index = 0;
  const paint = () => {
    const item = data.items[index];
    view.innerHTML = `
      <p>Question ${index + 1} of ${data.items.length}</p>
      <article class="panel"><h2>${esc(item.q)}</h2><p>${esc(item.a)}</p><p><a href="${esc(item.url)}" rel="noopener" target="_blank">${esc(item.source)}</a></p></article>
      <div class="row"><button type="button" class="btn" id="prev">Previous</button><button type="button" class="btn primary" id="next">Next</button></div>`;
    on(view.querySelector("#next"), "click", () => { index = (index + 1) % data.items.length; paint(); });
    on(view.querySelector("#prev"), "click", () => { index = (index - 1 + data.items.length) % data.items.length; paint(); });
  };
  paint();
}

async function renderBoss(id) {
  const data = await getJson("data/boss.json");
  if (!id) {
    setTitle("Boss incidents", "Synthetic logs. The failure modes are real; the phone numbers and names are not.");
    view.innerHTML = `<div class="grid">${data.items.map((item) => card(`#/boss/${item.id}`, item.severity, item.title, item.symptom, "")).join("")}</div>`;
    return;
  }
  const item = data.items.find((row) => row.id === id);
  if (!item) return renderMissing("That incident is not on the board");
  setTitle(item.title, item.symptom);
  let step = 0;
  const paint = () => {
    const current = item.steps[step];
    const cleared = session.progress.bosses[item.id];
    view.innerHTML = `
      <pre class="log">${esc(item.log)}</pre>
      <p>Step ${step + 1} of ${item.steps.length}${cleared ? " · cleared" : ""}</p>
      <fieldset>
        <legend>${esc(current.q)}</legend>
        ${current.choices.map((choice, i) => `<label class="choice"><input type="radio" name="boss" value="${i}"> ${esc(choice)}</label>`).join("")}
      </fieldset>
      <button type="button" class="btn primary" id="boss-check">Commit</button>
      <p class="why" id="boss-why" role="status"></p>
      <p class="note"><a href="${esc(item.url)}" rel="noopener" target="_blank">${esc(item.source)}</a></p>`;
    on(view.querySelector("#boss-check"), "click", () => {
      const picked = view.querySelector("input[name=boss]:checked");
      const why = view.querySelector("#boss-why");
      if (!picked) { why.textContent = "Choose a step."; return; }
      if (Number(picked.value) !== current.answer) {
        why.textContent = `Not that action. ${current.why}`;
        why.className = "why bad";
        audio.bad();
        return;
      }
      audio.ok();
      if (step < item.steps.length - 1) {
        step += 1;
        paint();
        return;
      }
      session.progress.bosses[item.id] = true;
      saveProgress();
      why.textContent = item.resolution;
      why.className = "why ok";
    });
  };
  paint();
}

async function renderTopology() {
  setTitle("3D topology", "A teaching map of a Five9 domain and its neighbors. Failure toggles describe symptoms. They are not a live network.");
  view.innerHTML = `<p class="note" id="topo-status">Loading the floor…</p><div id="topo-root"></div>`;
  const mod = await loadTopology();
  const root = view.querySelector("#topo-root");
  session.destroy = mod.mountTopology(root, {
    reduced: motionReduced(),
    onStatus: (text) => {
      const node = document.querySelector("#topo-status");
      if (node) node.textContent = text;
    }
  });
}

async function renderIvr() {
  setTitle("IVR script builder", "Modules use the names in the IVR Administrator's Guide. The export is a learning model, not a file VCC can import.");
  view.innerHTML = `<div id="ivr-root"></div>`;
  const mod = await loadIvr();
  session.destroy = mod.mountIvr(view.querySelector("#ivr-root"), { audio, reduced: motionReduced() });
}

async function renderPacing() {
  setTitle("Dialer pacing simulator", "A teaching clock for five dialing modes. It is not the Five9 dialer and it does not use the vendor's abandon window.");
  view.innerHTML = `<div id="pacing-root"></div>`;
  const mod = await loadPacing();
  session.destroy = mod.mountPacing(view.querySelector("#pacing-root"), { audio, reduced: motionReduced() });
}

function renderError(message) {
  setTitle("The floor did not load", message);
  view.innerHTML = `<p>The catalog or a track file did not load. If you are offline, open a section once while online so the service worker can keep it.</p><button type="button" class="btn primary" id="retry">Retry</button>`;
  on(view.querySelector("#retry"), "click", () => { session.catalog = null; route(); });
}

async function route() {
  resetView();
  let hash = location.hash || "#/";
  if (hash.length > 2 && hash.endsWith("/")) {
    location.hash = hash.slice(0, -1);
    return;
  }
  const bare = hash.split("?")[0];
  if (bare === "#/track" || bare === "#/lesson" || bare === "#/lab") {
    location.hash = "#/tracks";
    return;
  }
  try {
    await getCatalog();
    renderRail();
    if (await tryUniversityRoute(bare, { view, setTitle, esc, getJson, getTrack, getCatalog, session, audio, on, motionReduced })) return;
    if (bare === "#/" || bare === "") return await renderHome();
    if (bare === "#/tracks") return renderTracks();
    if (bare === "#/tools") return renderTools();
    if (bare === "#/progress") return renderProgress();
    if (bare === "#/topology") return await renderTopology();
    if (bare === "#/ivr") return await renderIvr();
    if (bare === "#/pacing") return await renderPacing();
    if (bare === "#/ecosystem") return await renderEcosystem();
    if (bare === "#/certs") return await renderCerts();
    if (bare === "#/interview") return await renderInterview();
    if (bare === "#/search") {
      const params = new URLSearchParams(hash.split("?")[1] || "");
      return await renderSearch(params.get("q") || "");
    }
    let match = bare.match(/^#\/track\/([a-z0-9-]+)$/);
    if (match) return await renderTrack(match[1]);
    match = bare.match(/^#\/lesson\/([a-z0-9-]+)\/([a-z0-9-]+)$/);
    if (match) return await openLesson(match[1], match[2]);
    match = bare.match(/^#\/boss\/([a-z0-9-]+)$/);
    if (match) return await renderBoss(match[1]);
    if (bare === "#/boss") return await renderBoss("");
    return renderMissing("That page is not on this floor");
  } catch (err) {
    renderError("Check the network and reload. Track files stay out of the first download until you open them.");
  } finally {
    afterRoute();
  }
}

function paintSettingsForm() {
  const dialog = document.querySelector("#settings");
  if (!dialog) return;
  document.querySelector("#set-sound").checked = !!session.settings.sound;
  document.querySelector("#set-narration").checked = !!session.settings.narration;
  document.querySelector("#set-motion").checked = motionReduced();
  document.querySelector("#set-font").value = String(session.settings.font || 16);
  document.querySelector("#set-rate").value = String(session.settings.rate || 1);
  document.querySelector("#rate-out").textContent = Number(session.settings.rate || 1).toFixed(2);
  document.querySelectorAll("[data-theme-pick]").forEach((button) => {
    button.setAttribute("aria-pressed", button.dataset.themePick === session.settings.theme ? "true" : "false");
  });
}

function bindChrome() {
  const linksToggle = document.querySelector("#links-toggle");
  const utilbar = document.querySelector("#utilbar");
  if (linksToggle && utilbar) {
    linksToggle.addEventListener("click", () => {
      const open = utilbar.classList.toggle("is-open");
      linksToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  document.querySelector("#open-settings").addEventListener("click", () => {
    fillVoices();
    paintSettingsForm();
    document.querySelector("#settings").showModal();
  });
  document.querySelector("#settings-close").addEventListener("click", () => document.querySelector("#settings").close());
  const soundToggle = document.querySelector("#sound-toggle");
  if (soundToggle) {
    soundToggle.addEventListener("click", () => {
      session.settings.sound = !session.settings.sound;
      saveSettings();
      audio.tick();
    });
  }
  document.addEventListener("click", (event) => {
    const button = event.target.closest("[data-theme-pick]");
    if (!button) return;
    session.settings.theme = button.dataset.themePick;
    saveSettings();
  });
  const lang = document.querySelector("#lang-pick");
  const menuLang = document.querySelector("#menu-lang");
  const applyLang = (value) => {
    session.settings.lang = value;
    if (lang) lang.value = value;
    if (menuLang) menuLang.value = value;
    saveSettings();
  };
  if (lang) {
    lang.value = session.settings.lang || "en";
    lang.addEventListener("change", () => applyLang(lang.value));
  }
  if (menuLang) {
    menuLang.value = session.settings.lang || "en";
    menuLang.addEventListener("change", () => applyLang(menuLang.value));
  }
  const mode = document.querySelector("#mode-toggle");
  if (mode) {
    mode.addEventListener("click", () => {
      session.settings.theme = session.settings.theme === "light" ? "neon" : "light";
      saveSettings();
    });
  }
  document.querySelector("#set-sound").addEventListener("change", (event) => {
    session.settings.sound = event.target.checked;
    saveSettings();
  });
  document.querySelector("#set-narration").addEventListener("change", (event) => {
    session.settings.narration = event.target.checked;
    saveSettings();
  });
  document.querySelector("#set-motion").addEventListener("change", (event) => {
    session.settings.reduced = event.target.checked;
    saveSettings();
  });
  document.querySelector("#set-font").addEventListener("change", (event) => {
    session.settings.font = Number(event.target.value);
    saveSettings();
  });
  const ink = document.querySelector("#set-ink");
  if (ink) {
    ink.value = session.settings.ink || "#142033";
    ink.addEventListener("input", (event) => {
      session.settings.ink = event.target.value;
      saveSettings();
    });
  }
  document.querySelector("#set-rate").addEventListener("input", (event) => {
    session.settings.rate = Number(event.target.value);
    document.querySelector("#rate-out").textContent = session.settings.rate.toFixed(2);
    saveSettings();
  });
  document.querySelector("#set-voice").addEventListener("change", (event) => {
    session.settings.voiceURI = event.target.value;
    saveSettings();
  });
  document.querySelector("#narrate-sample").addEventListener("click", () => {
    session.settings.narration = true;
    document.querySelector("#set-narration").checked = true;
    saveSettings();
    speak("Five9 Lab. Signal floor. This is the narration sample.");
  });
  if (window.speechSynthesis) {
    window.speechSynthesis.addEventListener("voiceschanged", fillVoices);
    fillVoices();
  }
  const motionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
  const onMotionPreference = () => {
    if (session.settings.reduced == null) applySettings();
  };
  if (typeof motionQuery.addEventListener === "function") {
    motionQuery.addEventListener("change", onMotionPreference);
  }
  window.addEventListener("hashchange", route);
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("./sw.js").catch(() => {});
  }
}

applySettings();
bindChrome();
initUniversity();
initGuide();
route();
