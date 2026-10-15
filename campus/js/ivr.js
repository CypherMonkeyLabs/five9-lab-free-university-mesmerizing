const MODULES = [
  { type: "Play", blurb: "Play a prompt.", fields: ["prompt"] },
  { type: "Menu", blurb: "DTMF branches. No Match is a separate exit.", fields: ["prompt"] },
  { type: "Get Digits", blurb: "Collect digits into a variable.", fields: ["variable"] },
  { type: "Input", blurb: "Named variable, as in the ZIP example.", fields: ["variable"] },
  { type: "If/Else", blurb: "Two branches. More than two needs Case.", fields: ["expression"] },
  { type: "Case", blurb: "Several branches from one value.", fields: ["expression"] },
  { type: "Set Variable", blurb: "Write a script variable.", fields: ["variable"] },
  { type: "Lookup Contact Record", blurb: "Read the contact record.", fields: [] },
  { type: "Query", blurb: "External query. The guide shows an XML web service example.", fields: ["url"] },
  { type: "Skill Transfer", blurb: "Queue to a skill. The script ends when an agent takes the call.", fields: ["skill", "pause"] },
  { type: "IVA Transfer", blurb: "Hand the call to a Studio task.", fields: ["task"] },
  { type: "Voicemail Transfer", blurb: "Send the caller to voicemail.", fields: [] },
  { type: "Set DNC", blurb: "Mark the number do-not-call.", fields: [] },
  { type: "Third Party Transfer", blurb: "Forward outside the skill queue.", fields: ["number"] },
  { type: "Foreign Script", blurb: "Jump to another IVR script.", fields: ["script"] },
  { type: "Language", blurb: "Switch the prompt language.", fields: ["language"] }
];

const PRESETS = {
  hours: [
    { type: "Play", prompt: "Thank you for calling Northwind Banking." },
    { type: "Menu", prompt: "Press 1 for balances. Press 2 for an agent. Press 3 for lost cards." },
    { type: "Skill Transfer", skill: "Banking", pause: "0" },
    { type: "Voicemail Transfer" }
  ],
  iva: [
    { type: "Language", language: "en-US" },
    { type: "IVA Transfer", task: "billing-chatbot" },
    { type: "Skill Transfer", skill: "Billing", pause: "2" }
  ]
};

function el(tag, attrs, text) {
  const node = document.createElement(tag);
  Object.entries(attrs || {}).forEach(([key, value]) => {
    if (key === "class") node.className = value;
    else node.setAttribute(key, value);
  });
  if (text != null) node.textContent = text;
  return node;
}

export function mountIvr(root, ctx) {
  const state = {
    nodes: PRESETS.hours.map((item, index) => ({ id: `n${index}`, ...item })),
    selected: 0,
    cursor: 0,
    running: false,
    log: "Ready.",
    seq: 3
  };
  let timer = 0;

  function stop() {
    state.running = false;
    if (timer) clearInterval(timer);
    timer = 0;
  }

  function draw() {
    root.innerHTML = "";
    const layout = el("div", { class: "ivr-layout" });
    const palette = el("div", { class: "panel" });
    palette.append(el("h2", {}, "Modules"));
    palette.append(el("p", { class: "note" }, "Names match the IVR modules chapter. Hangup is not in that list, so this bench ends on a transfer."));
    MODULES.forEach((mod) => {
      const button = el("button", { type: "button", class: "btn", title: mod.blurb }, mod.type);
      button.style.marginBottom = "6px";
      button.style.width = "100%";
      button.addEventListener("click", () => {
        state.seq += 1;
        const node = { id: `n${state.seq}`, type: mod.type, prompt: "", skill: "Support", pause: "0", variable: "digits", expression: "openHours", url: "https://example.invalid/soap", task: "task-key", number: "+18005550199", script: "after-hours", language: "en-US" };
        state.nodes.splice(state.selected + 1, 0, node);
        state.selected += 1;
        ctx.audio.tick();
        draw();
      });
      palette.append(button);
    });

    const script = el("div", { class: "panel" });
    script.append(el("h2", {}, "Script"));
    const row = el("div", { class: "row" });
    const presets = el("button", { type: "button", class: "btn" }, "Hours menu");
    const presetIva = el("button", { type: "button", class: "btn" }, "IVA then skill");
    const run = el("button", { type: "button", class: "btn primary" }, state.running ? "Pause" : "Play call");
    const step = el("button", { type: "button", class: "btn" }, "Step");
    const exp = el("button", { type: "button", class: "btn" }, "Export learning JSON");
    presets.addEventListener("click", () => loadPreset("hours"));
    presetIva.addEventListener("click", () => loadPreset("iva"));
    run.addEventListener("click", toggle);
    step.addEventListener("click", () => advance(true));
    exp.addEventListener("click", download);
    row.append(run, step, presets, presetIva, exp);
    script.append(row);
    state.nodes.forEach((node, index) => {
      const card = el("article", { class: `script-node${index === state.cursor ? " active" : ""}` });
      card.append(el("h3", {}, `${index + 1}. ${node.type}`));
      const summary = node.prompt || node.skill || node.task || node.expression || node.variable || "";
      if (summary) card.append(el("p", {}, summary));
      const actions = el("div", { class: "row" });
      const up = el("button", { type: "button", class: "btn" }, "Up");
      const down = el("button", { type: "button", class: "btn" }, "Down");
      const del = el("button", { type: "button", class: "btn" }, "Remove");
      up.addEventListener("click", () => move(index, -1));
      down.addEventListener("click", () => move(index, 1));
      del.addEventListener("click", () => remove(index));
      const pick = el("button", { type: "button", class: "btn ghost" }, "Edit");
      pick.addEventListener("click", () => { state.selected = index; draw(); });
      actions.append(pick, up, down, del);
      card.append(actions);
      script.append(card);
    });
    script.append(el("p", { class: "note", role: "status" }, state.log));

    const side = el("div", { class: "panel" });
    side.append(el("h2", {}, "Module properties"));
    const current = state.nodes[state.selected];
    if (current) {
      side.append(el("p", {}, current.type));
      ["prompt", "skill", "pause", "variable", "expression", "url", "task", "number", "script", "language"].forEach((field) => {
        if (current[field] == null) return;
        const wrap = el("div", { class: "field" });
        const label = el("label", { for: `f-${field}` }, field);
        const input = el("input", { id: `f-${field}`, type: "text", value: current[field] });
        input.addEventListener("input", () => { current[field] = input.value; });
        wrap.append(label, input);
        side.append(wrap);
      });
      if (current.type === "Menu" || current.type === "Skill Transfer") {
        side.append(el("h3", {}, "Caller pad"));
        const pad = el("div", { class: "dtmf" });
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#"].forEach((digit) => {
          const key = el("button", { type: "button", class: "btn" }, digit);
          key.addEventListener("click", () => {
            ctx.audio.tone(800 + digit.charCodeAt(0), 0.08, "sine", 0.03);
            state.log = `DTMF ${digit} on ${current.type}.`;
            if (current.type === "Menu" && digit === "2") {
              state.cursor = Math.min(state.nodes.length - 1, state.cursor + 1);
              state.log = "Menu took branch 2 toward the next module.";
            }
            draw();
          });
          pad.append(key);
        });
        side.append(pad);
      }
    }
    side.append(el("p", { class: "note" }, "Export is a lab JSON file. Five9 stores IVR scripts in the Administrator application. This bench does not claim a public import schema."));
    layout.append(palette, script, side);
    root.append(layout);
  }

  function loadPreset(name) {
    stop();
    state.nodes = PRESETS[name].map((item, index) => ({ id: `${name}${index}`, prompt: "", skill: "", pause: "0", variable: "", expression: "", url: "", task: "", number: "", script: "", language: "", ...item }));
    state.selected = 0;
    state.cursor = 0;
    state.log = `Loaded the ${name} preset.`;
    draw();
  }

  function move(index, delta) {
    const next = index + delta;
    if (next < 0 || next >= state.nodes.length) return;
    const [node] = state.nodes.splice(index, 1);
    state.nodes.splice(next, 0, node);
    state.selected = next;
    draw();
  }

  function remove(index) {
    state.nodes.splice(index, 1);
    state.selected = Math.max(0, state.selected - 1);
    draw();
  }

  function advance(manual) {
    if (!state.nodes.length) return;
    const node = state.nodes[state.cursor];
    if (node.type === "Play") ctx.audio.tick();
    if (node.type === "Skill Transfer" || node.type === "Voicemail Transfer" || node.type === "Third Party Transfer") {
      ctx.audio.ring();
      state.log = `${node.type} ends this walk. ${node.type === "Skill Transfer" ? "The guide says the IVR script is complete after the agent answers." : ""}`;
      stop();
      draw();
      return;
    }
    state.log = `${node.type}: ${node.prompt || node.skill || node.expression || node.task || "advanced"}.`;
    state.cursor = (state.cursor + 1) % state.nodes.length;
    if (manual) draw();
  }

  function toggle() {
    if (state.running) {
      stop();
      draw();
      return;
    }
    state.running = true;
    draw();
    const delay = ctx.reduced ? 1400 : 900;
    timer = window.setInterval(() => {
      advance(false);
      draw();
    }, delay);
  }

  function download() {
    const payload = {
      kind: "five9-lab-ivr-model",
      warning: "Learning model only. Not an official Five9 IVR script and not importable into VCC.",
      modules: state.nodes
    };
    const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "ivr-learning-model.json";
    link.click();
    URL.revokeObjectURL(link.href);
  }

  draw();
  return function destroy() {
    stop();
    root.innerHTML = "";
  };
}
