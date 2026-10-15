const MODES = ["Preview", "Progressive", "Power", "Predictive", "TCPA"];

function field(label, id, min, max, step, value) {
  return `<div class="slider-row"><label for="${id}">${label}</label><output id="${id}-out">${value}</output></div><input id="${id}" type="range" min="${min}" max="${max}" step="${step}" value="${value}">`;
}

export function mountPacing(root, ctx) {
  const state = {
    mode: "Predictive",
    agents: 12,
    hit: 0.35,
    talk: 180,
    wrap: 30,
    lines: 2,
    cap: 3,
    preview: 8,
    typeSec: 6,
    running: false,
    speed: 8,
    pace: 1,
    t: 0,
    history: [],
    connects: 0,
    attempts: 0,
    abandons: 0,
    lives: 0,
    people: [],
    inflight: [],
    log: "Press Play. The chart is a lab model.",
    typed: ""
  };
  let timer = 0;
  const targetNumber = "8005550142";

  function resetPeople() {
    state.people = Array.from({ length: state.agents }, () => ({ state: "idle", left: 0 }));
    state.inflight = [];
    state.pace = 1;
    state.connects = 0;
    state.attempts = 0;
    state.abandons = 0;
    state.lives = 0;
    state.t = 0;
    state.history = [];
    state.typed = "";
  }

  function idleCount() {
    return state.people.filter((agent) => agent.state === "idle").length;
  }

  function tick() {
    state.t += 1;
    state.people.forEach((agent) => {
      if (agent.left > 0) {
        agent.left -= 1;
        if (agent.left <= 0) agent.state = "idle";
      }
    });
    const finished = [];
    state.inflight.forEach((call) => {
      call.left -= 1;
      if (call.left > 0) return;
      finished.push(call);
      const live = Math.random() < state.hit;
      if (!live) return;
      state.lives += 1;
      const agent = state.people.find((person) => person.state === "idle" || person.state === "reserved");
      if (!agent) {
        state.abandons += 1;
        return;
      }
      agent.state = "talk";
      agent.left = state.talk + state.wrap;
      state.connects += 1;
      ctx.audio.tick();
    });
    state.inflight = state.inflight.filter((call) => !finished.includes(call));

    const windowLives = state.history.slice(-80);
    const recentAbandon = windowLives.length ? windowLives.filter((row) => row.abandon).length / windowLives.length : 0;
    if (state.mode === "Predictive" || state.mode === "Power") {
      if (recentAbandon > state.cap / 100) state.pace = Math.max(0.4, state.pace * 0.9);
      else if (recentAbandon < (state.cap / 100) * 0.5) state.pace = Math.min(1.6, state.pace * 1.03);
    }

    let toPlace = 0;
    if (state.mode === "Progressive") toPlace = idleCount();
    if (state.mode === "Preview") toPlace = state.people.filter((agent) => agent.state === "idle").length;
    if (state.mode === "Power") toPlace = Math.floor(idleCount() * state.lines * state.pace);
    if (state.mode === "Predictive") toPlace = Math.round((idleCount() / Math.max(state.hit, 0.05)) * state.pace * 0.35);
    if (state.mode === "TCPA") toPlace = 0;

    if (state.mode === "Preview" || state.mode === "Progressive") {
      state.people.forEach((agent) => {
        if (agent.state === "idle" && toPlace > 0) {
          agent.state = "reserved";
          agent.left = state.mode === "Preview" ? state.preview : 1;
          toPlace -= 1;
        }
      });
    }

    for (let i = 0; i < toPlace; i += 1) {
      state.attempts += 1;
      state.inflight.push({ left: 8 });
    }

    const occ = state.people.length ? state.people.filter((agent) => agent.state === "talk").length / state.people.length : 0;
    const abandonRate = state.lives ? state.abandons / state.lives : 0;
    state.history.push({ t: state.t, occ, abandon: abandonRate > state.cap / 100, rate: abandonRate });
    if (state.history.length > 240) state.history.shift();
    state.log = `${state.mode} · t=${state.t}s · connect ${state.connects} · abandon ${state.lives ? Math.round(abandonRate * 100) : 0}% · pace ${state.pace.toFixed(2)}`;
    paintChart();
    const status = root.querySelector("#pace-log");
    if (status) status.textContent = state.log;
    const stats = root.querySelector("#pace-stats");
    if (stats) {
      stats.innerHTML = `<div class="stat"><strong>${Math.round(occ * 100)}%</strong><span>Occupancy</span></div><div class="stat"><strong>${state.lives ? Math.round(abandonRate * 100) : 0}%</strong><span>Abandon of live answers</span></div><div class="stat"><strong>${state.connects}</strong><span>Connects</span></div><div class="stat"><strong>${idleCount()}</strong><span>Idle agents</span></div>`;
    }
  }

  function paintChart() {
    const canvas = root.querySelector("canvas");
    if (!canvas) return;
    const g = canvas.getContext("2d");
    const w = canvas.width;
    const h = canvas.height;
    g.clearRect(0, 0, w, h);
    g.fillStyle = "#041018";
    g.fillRect(0, 0, w, h);
    g.strokeStyle = "#1d3c52";
    g.beginPath();
    g.moveTo(0, h * 0.7);
    g.lineTo(w, h * 0.7);
    g.stroke();
    g.strokeStyle = "#3ee0ff";
    g.beginPath();
    state.history.forEach((row, i) => {
      const x = (i / 240) * w;
      const y = h - row.occ * (h - 16) - 8;
      if (i === 0) g.moveTo(x, y);
      else g.lineTo(x, y);
    });
    g.stroke();
    g.strokeStyle = "#f5b942";
    g.beginPath();
    state.history.forEach((row, i) => {
      const x = (i / 240) * w;
      const y = h - Math.min(1, row.rate) * (h - 16) - 8;
      if (i === 0) g.moveTo(x, y);
      else g.lineTo(x, y);
    });
    g.stroke();
  }

  function draw() {
    root.innerHTML = `
      <div class="tool-layout">
        <form class="panel" id="pace-form">
          <h2>Mode</h2>
          <div class="field"><label for="mode">Dialing mode</label>
            <select id="mode">${MODES.map((mode) => `<option ${mode === state.mode ? "selected" : ""}>${mode}</option>`).join("")}</select>
          </div>
          ${field("Agents", "agents", 1, 40, 1, state.agents)}
          ${field("Live-answer rate %", "hit", 5, 80, 1, Math.round(state.hit * 100))}
          ${field("Talk seconds", "talk", 30, 600, 10, state.talk)}
          ${field("Wrap seconds", "wrap", 0, 180, 5, state.wrap)}
          ${field("Power lines / agent", "lines", 1, 6, 0.5, state.lines)}
          ${field("Teaching abandon cap %", "cap", 1, 15, 1, state.cap)}
          <p class="note">Five9's preset Max Abandoned Call Percentage is domain-specific. US domains watch a rolling 30 days and UK domains watch 24 hours. This cap is only for the chart.</p>
          <div class="row">
            <button type="button" class="btn primary" id="pace-play">${state.running ? "Pause" : "Play"}</button>
            <button type="button" class="btn" id="pace-reset">Reset</button>
          </div>
        </form>
        <div class="panel">
          <h2>Floor</h2>
          <div class="stats" id="pace-stats"></div>
          <canvas class="pacing-chart" width="640" height="180" aria-label="Occupancy in cyan and abandon rate in amber"></canvas>
          <p id="pace-log" role="status">${state.log}</p>
          <p class="note">Cyan is occupancy. Amber is abandon rate among live answers. Progressive reserves one agent per call, so abandon stays near zero. Predictive and power can overdial.</p>
        </div>
        <div class="panel">
          <h2>TCPA manual touch</h2>
          <p>On a TCPA domain the agent must type the external number. Paste and drop are refused in this drill, matching the published manual-touch rule.</p>
          <p>Type <strong>${targetNumber}</strong></p>
          <div class="field"><label for="tcpa">Number</label><input id="tcpa" type="text" autocomplete="off" value="${state.typed}"></div>
          <button type="button" class="btn primary" id="tcpa-dial" disabled>Dial</button>
          <p id="tcpa-note" class="note"></p>
        </div>
      </div>`;
    root.querySelectorAll("input[type=range]").forEach((input) => {
      const out = root.querySelector(`#${input.id}-out`);
      const sync = () => { out.textContent = input.value; };
      input.addEventListener("input", sync);
    });
    root.querySelector("#mode").addEventListener("change", (event) => { state.mode = event.target.value; });
    root.querySelector("#pace-play").addEventListener("click", toggle);
    root.querySelector("#pace-reset").addEventListener("click", () => { readForm(); resetPeople(); draw(); });
    const tcpa = root.querySelector("#tcpa");
    const dial = root.querySelector("#tcpa-dial");
    const note = root.querySelector("#tcpa-note");
    tcpa.addEventListener("paste", (event) => { event.preventDefault(); note.textContent = "Paste is blocked in TCPA manual touch."; ctx.audio.bad(); });
    tcpa.addEventListener("drop", (event) => event.preventDefault());
    tcpa.addEventListener("input", () => {
      state.typed = tcpa.value.replace(/\D/g, "");
      if (tcpa.value !== state.typed) tcpa.value = state.typed;
      dial.disabled = state.typed !== targetNumber;
    });
    dial.addEventListener("click", () => {
      if (state.typed !== targetNumber) return;
      state.connects += 1;
      state.lives += 1;
      note.textContent = "Dial unlocked after a full typed match. No automatic dial.";
      ctx.audio.ring();
      state.typed = "";
      tcpa.value = "";
      dial.disabled = true;
    });
    paintChart();
  }

  function readForm() {
    state.mode = root.querySelector("#mode").value;
    state.agents = Number(root.querySelector("#agents").value);
    state.hit = Number(root.querySelector("#hit").value) / 100;
    state.talk = Number(root.querySelector("#talk").value);
    state.wrap = Number(root.querySelector("#wrap").value);
    state.lines = Number(root.querySelector("#lines").value);
    state.cap = Number(root.querySelector("#cap").value);
    resetPeople();
  }

  function toggle() {
    if (state.running) {
      state.running = false;
      clearInterval(timer);
      draw();
      return;
    }
    readForm();
    state.running = true;
    draw();
    const delay = ctx.reduced ? 400 : 120;
    timer = window.setInterval(tick, delay);
  }

  resetPeople();
  draw();
  return function destroy() {
    clearInterval(timer);
    root.innerHTML = "";
  };
}
