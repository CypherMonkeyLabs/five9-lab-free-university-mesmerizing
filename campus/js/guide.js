import { diagramIds, flowIds } from "./diagrams.js";
import { chartIds } from "./charts.js";

/**
 * Future cloud-agent endpoint. Stay null until a real route exists.
 * When set, askGuide POSTs { message } and expects { reply: string, href?: string }.
 * A missing, failed, or empty reply falls back to the local guide notes.
 */
export const GUIDE_AGENT_URL = null;

const KB_URL = "data/guide-kb.json";

function normalize(value) {
  return String(value || "")
    .toLowerCase()
    .replace(/&/g, " and ")
    .replace(/[^a-z0-9+#.\s-]/g, " ")
    .replace(/[-_.]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function tokens(value) {
  return normalize(value).split(" ").filter((word) => word.length >= 2);
}

function phraseScore(query, phrase) {
  const needle = normalize(phrase);
  if (!needle) return 0;
  if (query === needle) return 10;
  if (needle.length >= 3 && (query.includes(needle) || needle.includes(query))) return 6;
  const qTokens = tokens(query);
  const pTokens = tokens(needle);
  if (!pTokens.length || !qTokens.length) return 0;
  const hits = pTokens.filter((word) => qTokens.includes(word)).length;
  if (!hits) return 0;
  return (hits / pTokens.length) * 4;
}

export function scoreEntry(query, entry) {
  const q = normalize(query);
  if (!q) return 0;
  const phrases = [entry.title, ...(entry.keywords || []), ...(entry.synonyms || [])];
  return phrases.reduce((best, phrase) => Math.max(best, phraseScore(q, phrase)), 0);
}

export function rankEntries(query, entries) {
  return entries
    .map((entry) => ({ entry, score: scoreEntry(query, entry) }))
    .filter((row) => row.score >= 4)
    .sort((a, b) => b.score - a.score);
}

function fill(text) {
  return String(text || "")
    .replaceAll("{{diagrams}}", String(diagramIds.length))
    .replaceAll("{{flows}}", String(flowIds.length))
    .replaceAll("{{charts}}", String(chartIds.length))
    .replaceAll("{{chartList}}", chartIds.join(", "));
}

function freshState() {
  return { mode: "chat", quiz: 0, score: 0, tour: "", step: 0 };
}

async function askRemote(text) {
  if (!GUIDE_AGENT_URL) return null;
  try {
    const response = await fetch(GUIDE_AGENT_URL, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ message: text })
    });
    if (!response.ok) return null;
    const data = await response.json();
    if (!data || typeof data.reply !== "string" || !data.reply.trim()) return null;
    return {
      reply: data.reply.trim(),
      href: typeof data.href === "string" ? data.href : "",
      chips: Array.isArray(data.chips) ? data.chips.map(String) : [],
      source: "agent"
    };
  } catch (err) {
    return null;
  }
}

export function answerLocal(text, kb, prev) {
  const state = { ...freshState(), ...(prev || {}) };
  const q = normalize(text);
  const starters = kb.starters || [];
  if (!q || q === "stop" || q === "stop tour" || q === "stop quiz") {
    return {
      reply: q ? "Stopped. Ask about a page, or start a tour or a quiz." : fill(kb.greeting),
      href: "",
      chips: starters,
      state: freshState()
    };
  }
  if (q === "tour" || q === "tours" || q === "start a tour") {
    const chips = (kb.tours || []).map((tour) => tour.title);
    return {
      reply: chips.length ? "Pick a tour. I only walk pages that exist in this lab." : "No tours are in the guide notes.",
      href: "",
      chips: chips.length ? chips : starters,
      state: freshState()
    };
  }
  const tour = (kb.tours || []).find((item) => normalize(item.title) === q || normalize(item.id) === q);
  if (tour) {
    const step = tour.steps[0];
    return {
      reply: fill(step.say),
      href: step.href,
      chips: ["Next stop", "Stop tour"],
      state: { mode: "tour", quiz: 0, score: 0, tour: tour.id, step: 0 },
      go: step.href
    };
  }
  if (state.mode === "tour" && (q === "next" || q === "next stop")) {
    const active = (kb.tours || []).find((item) => item.id === state.tour);
    const next = active ? state.step + 1 : 0;
    if (!active || next >= active.steps.length) {
      return {
        reply: "That tour is finished. Every stop was a page in this lab.",
        href: "",
        chips: starters,
        state: freshState()
      };
    }
    const step = active.steps[next];
    return {
      reply: fill(step.say),
      href: step.href,
      chips: ["Next stop", "Stop tour"],
      state: { ...state, step: next },
      go: step.href
    };
  }
  if (q === "quiz" || q === "quiz me" || q === "start quiz") {
    const card = (kb.quizzes || [])[0];
    if (!card) {
      return { reply: "No quiz cards are in the guide notes.", href: "", chips: starters, state: freshState() };
    }
    return {
      reply: `Card 1 of ${kb.quizzes.length}. ${card.prompt}`,
      href: "",
      chips: card.choices,
      state: { mode: "quiz", quiz: 0, score: 0, tour: "", step: 0 }
    };
  }
  if (state.mode === "quiz") {
    const card = kb.quizzes[state.quiz];
    if (!card) {
      return { reply: fill(kb.fallback), href: "#/search", chips: starters, state: freshState() };
    }
    const pick = card.choices.findIndex((choice) => normalize(choice) === q);
    if (pick < 0) {
      return {
        reply: "Pick one of the choices on this card. I only grade those answers.",
        href: "",
        chips: [...card.choices, "Stop quiz"],
        state
      };
    }
    const right = pick === card.answer;
    const score = state.score + (right ? 1 : 0);
    const mark = right ? "That's the one this lab states." : "That's not the answer these notes give.";
    const nextIndex = state.quiz + 1;
    if (nextIndex >= kb.quizzes.length) {
      return {
        reply: `${mark} ${card.why} Score ${score} of ${kb.quizzes.length}. I only graded what these pages say.`,
        href: "",
        chips: starters,
        state: freshState()
      };
    }
    const next = kb.quizzes[nextIndex];
    return {
      reply: `${mark} ${card.why} Card ${nextIndex + 1} of ${kb.quizzes.length}. ${next.prompt}`,
      href: "",
      chips: next.choices,
      state: { mode: "quiz", quiz: nextIndex, score, tour: "", step: 0 }
    };
  }
  const ranked = rankEntries(text, kb.entries || []);
  if (!ranked.length) {
    return { reply: fill(kb.fallback), href: "#/search", chips: starters, state };
  }
  const best = ranked[0].entry;
  const second = ranked[1] && ranked[0].score - ranked[1].score <= 2 ? ranked[1].entry : null;
  const extra = second ? ` Also related in these notes: ${second.title}.` : "";
  let chips = second ? [second.title, ...starters.filter((chip) => chip !== second.title)].slice(0, 6) : starters;
  if (state.mode === "tour") chips = ["Next stop", "Stop tour", ...chips].slice(0, 6);
  return {
    reply: `${fill(best.answer)}${extra}`,
    href: best.href || "",
    chips,
    state
  };
}

export async function askGuide(text, kb, state) {
  const remote = await askRemote(text);
  if (remote) return { ...remote, state: state || freshState() };
  return answerLocal(text, kb, state);
}

function wait(ms) {
  return new Promise((resolve) => { setTimeout(resolve, ms); });
}

export function initGuide() {
  const root = document.querySelector("#guide");
  const panel = document.querySelector("#guide-panel");
  const openBtn = document.querySelector("#guide-open");
  const closeBtn = document.querySelector("#guide-close");
  const log = document.querySelector("#guide-log");
  const chips = document.querySelector("#guide-chips");
  const form = document.querySelector("#guide-form");
  const input = document.querySelector("#guide-q");
  if (!root || !panel || !openBtn || !log || !chips || !form || !input) return;

  let kb = null;
  let kbFailed = false;
  let state = freshState();
  let gen = 0;
  let greeted = false;
  let opener = openBtn;

  function reduced() {
    return document.documentElement.dataset.motion === "reduce";
  }

  function paintChips(labels) {
    chips.replaceChildren();
    (labels || []).forEach((label) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "guide-chip";
      button.textContent = label;
      button.addEventListener("click", () => { submit(label); });
      chips.append(button);
    });
  }

  function bubble(role, text, href) {
    const item = document.createElement("div");
    item.className = `guide-bubble guide-${role}`;
    const body = document.createElement("p");
    if (text) body.textContent = text;
    item.append(body);
    if (href) {
      const link = document.createElement("a");
      link.href = href;
      link.textContent = "Open this page";
      item.append(link);
    }
    log.append(item);
    log.scrollTop = log.scrollHeight;
    return body;
  }

  async function typeInto(node, text, token) {
    if (reduced()) {
      node.textContent = text;
      return;
    }
    let index = 0;
    while (index < text.length) {
      if (token !== gen) return;
      index += 2;
      node.textContent = text.slice(0, index);
      log.scrollTop = log.scrollHeight;
      await wait(14);
    }
  }

  async function say(text, href) {
    const token = ++gen;
    const typing = document.createElement("div");
    typing.className = "guide-bubble guide-bot guide-typing";
    typing.innerHTML = "<span></span><span></span><span></span>";
    log.append(typing);
    log.scrollTop = log.scrollHeight;
    if (!reduced()) await wait(380);
    if (token !== gen) {
      typing.remove();
      return;
    }
    typing.remove();
    const node = bubble("bot", "", href);
    await typeInto(node, text, token);
  }

  async function submit(raw) {
    const text = String(raw || "").trim();
    if (!text) return;
    if (!kb) {
      bubble("user", text, "");
      await say("The guide notes did not load, so I won't guess.");
      return;
    }
    bubble("user", text, "");
    input.value = "";
    const result = await askGuide(text, kb, state);
    state = result.state || freshState();
    paintChips(result.chips);
    if (result.go && location.hash !== result.go) location.hash = result.go;
    await say(result.reply, result.href || "");
  }

  function greet() {
    if (greeted || (!kb && !kbFailed)) return;
    greeted = true;
    paintChips(kb ? kb.starters : []);
    say(kb ? kb.greeting : "The guide notes did not load, so I won't guess.", "");
  }

  function setOpen(open) {
    panel.hidden = !open;
    openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    if (open) {
      opener = document.activeElement instanceof HTMLElement ? document.activeElement : openBtn;
      input.focus();
      greet();
    } else if (opener) {
      opener.focus();
    }
  }

  openBtn.addEventListener("click", () => setOpen(panel.hidden));
  if (closeBtn) closeBtn.addEventListener("click", () => setOpen(false));
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    submit(input.value);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !panel.hidden) setOpen(false);
  });

  fetch(KB_URL)
    .then((response) => {
      if (!response.ok) throw new Error("guide kb");
      return response.json();
    })
    .then((data) => {
      kb = data;
      if (!panel.hidden) greet();
    })
    .catch(() => {
      kbFailed = true;
      if (!panel.hidden) greet();
    });
}
