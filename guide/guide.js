/**
 * Five9 guide. Poses, first-open tour, read-along, and voice stay in this browser.
 * window.F9_GUIDE.endpoint is null. Nothing is sent until that string is set on purpose.
 */
(function () {
  var root = document.documentElement;
  var base = root.getAttribute("data-root") || "";
  window.F9_GUIDE = window.F9_GUIDE || { endpoint: null };

  var store = {
    get: function (key) { try { return localStorage.getItem(key); } catch (err) { return null; } },
    set: function (key, value) { try { localStorage.setItem(key, value); } catch (err) { /* private mode */ } }
  };

  var host = document.createElement("div");
  host.className = "cg-root";
  host.id = "tour-bot";
  host.dataset.pose = "idle";
  host.innerHTML =
    '<button type="button" class="cg-monkey" aria-expanded="false" aria-controls="cg-panel" aria-label="Five9 guide. Open the monkey.">' +
    '<span class="cg-halo" aria-hidden="true"></span>' + monkeySvg() + "</button>" +
    '<div class="cg-nudge" hidden><p>Need a path through this page?</p>' +
    '<div class="cg-chips"><button type="button" data-nudge-yes>Show me</button>' +
    '<button type="button" data-nudge-later>Not now</button>' +
    '<button type="button" data-nudge-stop>Stop offering</button></div></div>' +
    '<section class="cg-panel" id="cg-panel" hidden role="dialog" aria-labelledby="cg-title">' +
    '<div class="cg-handle" aria-hidden="true"></div>' +
    '<div class="cg-bar"><h2 id="cg-title">Five9 guide</h2>' +
    '<button type="button" data-close>Close</button></div>' +
    '<div class="cg-speak"><button type="button" data-read>Read this page</button>' +
    '<label>Voice <select data-voice-name aria-label="Speaking voice"></select></label></div>' +
    '<div class="cg-cards"></div><div class="cg-log" role="log"></div>' +
    '<div data-f9-chat></div>' +
    '<details class="cg-extra"><summary>More tools</summary>' +
    '<div class="cg-voice"><label>Rate <input data-rate type="range" min="0.8" max="1.2" step="0.05" value="0.95"></label>' +
    '<label>Pitch <input data-pitch type="range" min="0.8" max="1.2" step="0.05" value="1"></label>' +
    '<label><input data-ambient type="checkbox"> Soft ambient sound, off unless you check this</label></div>' +
    '</details></section>' +
    '<div class="cg-greet" hidden><div class="cg-greet-card" role="dialog" aria-modal="true" aria-labelledby="cg-greet-title">' +
    '<div class="cg-greet-art" aria-hidden="true">' + monkeySvg() + '</div>' +
    '<h2 id="cg-greet-title">Welcome</h2>' +
    '<p>Welcome to CypherMonkey Labs. I am the Five9 guide. Pick a way through the lab, then I will dock at the side.</p>' +
    '<div class="cg-cards" data-greet-cards></div>' +
    '<button type="button" data-greet-dock>Dock the guide</button></div></div>' +
    '<div class="cg-tour" hidden><div class="cg-tour-back"></div><div class="cg-spot" hidden></div>' +
    '<div class="cg-callout" role="dialog" aria-label="First visit tour">' +
    '<p class="cg-tour-count"><span class="cg-tour-num" data-tour-num>1</span> <span data-tour-count>1 of 6</span></p>' +
    '<p data-tour-copy></p>' +
    '<div class="cg-callout-actions"><button type="button" data-tour-back>Back</button>' +
    '<button type="button" data-tour-next>Next</button><button type="button" data-tour-skip>Skip</button></div></div></div>';
  document.body.appendChild(host);

  var css = document.createElement("link");
  css.rel = "stylesheet";
  css.href = base + "guide/guide.css";
  document.head.appendChild(css);
  var chatCss = document.createElement("link");
  chatCss.rel = "stylesheet";
  chatCss.href = base + "shared/pybot-chat/chat.css";
  document.head.appendChild(chatCss);

  var monkey = host.querySelector(".cg-monkey");
  var panel = host.querySelector(".cg-panel");
  var log = host.querySelector(".cg-log");
  var cards = host.querySelector(".cg-cards");
  var chips = host.querySelector(".cg-chips");
  var nudge = host.querySelector(".cg-nudge");
  var tour = host.querySelector(".cg-tour");
  var spot = tour.querySelector(".cg-spot");
  var tourCopy = tour.querySelector("[data-tour-copy]");
  var voiceBox = host.querySelector(".cg-voice");
  var voiceSel = host.querySelector("[data-voice-name]");
  var rate = host.querySelector("[data-rate]");
  var pitch = host.querySelector("[data-pitch]");
  var ambientBox = host.querySelector("[data-ambient]");
  var kb = [];
  var messages = [];
  var paintChat = null;
  var chatRoot = null;
  var retriever = null;
  var chatReady = Promise.resolve();
  var topics = [
    "What is a skill group?",
    "What is a disposition?",
    "What is preview dialing?",
    "What is a DNIS?",
    "What is TCPA manual touch?",
    "Where do I start?",
    "What can you help with?"
  ];
  var speaking = false;
  var audioCtx = null;
  var step = 0;
  var offers = Number(store.get("f9-offer-count") || "0");
  var stopped = store.get("f9-offers-stop") === "1";

  var steps = [
    { sel: "#tour-home", text: "Home is the front door. Twenty-three tracks start here." },
    { sel: "#tour-menu", text: "Menu opens the drawer. Skills and ACD, Workforce, Quality, CRM and CTI, and Ecosystem each have an icon, a label, and one line." },
    { sel: "#tour-learn", text: "Learn is the ten-minute path and the full course." },
    { sel: "#tour-diagrams", text: "Diagrams are the drawings. Every one can be saved." },
    { sel: "#tour-play", text: "Play is the port game and the daily question. Listen is the study audio beside it." },
    { sel: "#tour-downloads", text: "Downloads holds the sheets, cards, and the bundle. The monkey can read a page aloud. Replay this tour from Help." }
  ];

  function arm(x, y, rotate) {
    return '<rect x="' + x + '" y="' + y + '" width="22" height="58" rx="11" fill="#f59e0b" stroke="#b45309" stroke-width="3" transform="rotate(' + rotate + ' ' + (x + 11) + ' ' + (y + 10) + ')"/>';
  }
  function monkeySvg() {
    return '<svg viewBox="0 0 220 250" role="img" aria-label="A colourful monkey with ears, eyes, and glasses">' +
      '<ellipse cx="36" cy="86" rx="28" ry="36" fill="#c2410c"/>' +
      '<ellipse cx="184" cy="86" rx="28" ry="36" fill="#c2410c"/>' +
      '<ellipse cx="36" cy="86" rx="16" ry="22" fill="#fb7185"/>' +
      '<ellipse cx="184" cy="86" rx="16" ry="22" fill="#fb7185"/>' +
      '<circle cx="110" cy="98" r="64" fill="#f59e0b" stroke="#b45309" stroke-width="4"/>' +
      '<ellipse cx="92" cy="72" rx="28" ry="14" fill="#fde68a" opacity=".8"/>' +
      '<ellipse cx="110" cy="118" rx="38" ry="28" fill="#ffedd5"/>' +
      '<ellipse cx="84" cy="90" rx="16" ry="18" fill="#ffffff" stroke="#1c1917" stroke-width="2"/>' +
      '<ellipse cx="136" cy="90" rx="16" ry="18" fill="#ffffff" stroke="#1c1917" stroke-width="2"/>' +
      '<circle cx="86" cy="94" r="7" fill="#1c1917"/><circle cx="138" cy="94" r="7" fill="#1c1917"/>' +
      '<circle cx="89" cy="91" r="2.5" fill="#ffffff"/><circle cx="141" cy="91" r="2.5" fill="#ffffff"/>' +
      '<ellipse cx="110" cy="112" rx="7" ry="5" fill="#9a3412"/>' +
      '<path d="M90 124 Q110 142 130 124" fill="none" stroke="#9a3412" stroke-width="3" stroke-linecap="round"/>' +
      '<rect x="66" y="74" width="38" height="34" rx="12" fill="none" stroke="#0891b2" stroke-width="4"/>' +
      '<rect x="116" y="74" width="38" height="34" rx="12" fill="none" stroke="#0891b2" stroke-width="4"/>' +
      '<path d="M104 91 H116" stroke="#0891b2" stroke-width="4"/>' +
      '<ellipse cx="110" cy="196" rx="52" ry="38" fill="#f59e0b" stroke="#b45309" stroke-width="4"/>' +
      '<ellipse cx="110" cy="204" rx="24" ry="16" fill="#ffedd5"/>' +
      '<path d="M158 188 q36 8 24 34" fill="none" stroke="#ea580c" stroke-width="8" stroke-linecap="round"/>' +
      '<g class="pose pose-idle">' + arm(46, 168, 24) + arm(152, 168, -24) + '</g>' +
      '<g class="pose pose-wave">' + arm(46, 168, 24) + arm(150, 108, -70) + '</g>' +
      '<g class="pose pose-think">' + arm(58, 150, 40) + arm(148, 168, -8) + '</g>' +
      '<g class="pose pose-cheer">' + arm(48, 112, 70) + arm(150, 112, -70) + '</g>' +
      '<g class="pose pose-listen">' + arm(150, 118, -40) + arm(48, 168, 16) + '</g>' +
      '<g class="pose pose-speak">' + arm(40, 158, 8) + arm(158, 158, -8) + '</g>' +
      '</svg>';
  }

  function pose(name) { host.dataset.pose = name; }
  function say(text, who) {
    var p = document.createElement("p");
    p.textContent = text;
    if (who) p.dataset.who = who;
    log.appendChild(p);
    log.scrollTop = log.scrollHeight;
  }
  function titleTextBottom() {
    var title = document.querySelector(".hero-title, #main > h1");
    if (!title) title = document.querySelector("#main h1, .section-head h2");
    if (!title) return 0;
    var range = document.createRange();
    range.selectNodeContents(title);
    var rects = range.getClientRects();
    var bottom = 0;
    for (var i = 0; i < rects.length; i++) {
      if (rects[i].width > 1 && rects[i].height > 1) bottom = Math.max(bottom, rects[i].bottom);
    }
    return bottom;
  }
  function fitPanel() {
    if (!panel) return;
    panel.style.maxHeight = "";
    if (panel.hidden || window.innerWidth > 720) return;
    var bottom = titleTextBottom();
    if (!bottom) return;
    var dock = parseFloat(getComputedStyle(document.documentElement).getPropertyValue("--dock-h")) || 72;
    var gap = 12;
    if (panel.getBoundingClientRect().top >= bottom + gap) return;
    var limit = window.innerHeight - dock - bottom - gap;
    if (limit < 96) limit = 96;
    panel.style.maxHeight = limit + "px";
  }
  function setOpen(open) {
    panel.hidden = !open;
    monkey.setAttribute("aria-expanded", open ? "true" : "false");
    pose(open ? "wave" : "idle");
    if (open) showCards();
    fitPanel();
  }

  function voices() {
    var list = window.speechSynthesis ? window.speechSynthesis.getVoices() : [];
    return list.slice().sort(function (a, b) {
      return rank(b) - rank(a);
    });
  }
  function rank(voice) {
    var name = (voice.name || "") + " " + (voice.lang || "");
    var score = /en/i.test(voice.lang || "") ? 2 : 0;
    if (/natural|neural|aria|jenny|guy|samantha|google uk english female|enhanced/i.test(name)) score += 5;
    if (/english/i.test(name)) score += 1;
    return score;
  }
  function fillVoices() {
    var list = voices();
    voiceSel.innerHTML = "";
    if (!list.length) {
      var empty = document.createElement("option");
      empty.value = "";
      empty.textContent = "Browser default";
      voiceSel.appendChild(empty);
    }
    list.forEach(function (voice) {
      var opt = document.createElement("option");
      opt.value = voice.name;
      opt.textContent = voice.name;
      voiceSel.appendChild(opt);
    });
    var saved = store.get("f9-voice");
    if (saved && list.some(function (voice) { return voice.name === saved; })) voiceSel.value = saved;
    else if (list[0]) voiceSel.value = list[0].name;
  }
  function pickVoice() {
    var list = voices();
    var name = voiceSel.value;
    for (var i = 0; i < list.length; i++) if (list[i].name === name) return list[i];
    return list[0] || null;
  }
  function speak(text, onend) {
    if (!window.speechSynthesis) {
      window.setTimeout(function () { if (onend) onend(); }, 2400);
      return;
    }
    window.speechSynthesis.cancel();
    var utter = new SpeechSynthesisUtterance(text);
    var voice = pickVoice();
    if (voice) utter.voice = voice;
    utter.rate = Number(rate.value) || 0.95;
    utter.pitch = Number(pitch.value) || 1;
    utter.onend = function () { pose("idle"); if (onend) onend(); };
    pose("speak");
    window.speechSynthesis.speak(utter);
  }
  function stopSpeak() {
    speaking = false;
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    document.querySelectorAll(".is-spoken, .is-reading").forEach(function (node) {
      node.classList.remove("is-spoken", "is-reading");
    });
    pose("idle");
  }

  function readAlong() {
    var nodes = Array.prototype.slice.call(document.querySelectorAll("[data-sentence]"));
    if (!nodes.length) {
      say("This page has no read-along sentences yet. Open a room or Learn.");
      return;
    }
    speaking = true;
    var index = 0;
    function next() {
      if (!speaking || index >= nodes.length) { stopSpeak(); return; }
      var node = nodes[index];
      document.querySelectorAll(".is-spoken").forEach(function (el) { el.classList.remove("is-spoken"); });
      document.querySelectorAll("section.is-reading, .section-chip.is-reading").forEach(function (el) { el.classList.remove("is-reading"); });
      node.classList.add("is-spoken");
      var motion = root.dataset.motion === "reduce" ? "auto" : "smooth";
      node.scrollIntoView({ block: "center", behavior: motion });
      var section = node.closest("section");
      if (section) {
        section.classList.add("is-reading");
        var key = section.getAttribute("data-read-section");
        if (key) {
          var chip = document.querySelector('.section-chip[data-section="' + key + '"]');
          if (chip) {
            chip.classList.add("is-reading");
            chip.scrollIntoView({ inline: "center", block: "nearest" });
          }
        }
        section.scrollIntoView({ block: "nearest", behavior: motion });
      }
      index += 1;
      speak(node.textContent || "", next);
    }
    setOpen(true);
    say("Reading this page. The yellow line is the sentence, and the menu chip glows with the section.");
    next();
  }

  function fillCards(into) {
    if (!into) return;
    into.innerHTML = "";
    [
      ["Finish in 10 minutes", base + "start.html#ten"],
      ["Full course", base + "start.html#full"],
      ["Just download", base + "downloads.html"]
    ].forEach(function (item) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.textContent = item[0];
      btn.addEventListener("click", function () {
        dock();
        location.href = item[1];
      });
      into.appendChild(btn);
    });
  }
  function showCards() {
    fillCards(cards);
    fillCards(host.querySelector("[data-greet-cards]"));
  }

  function exportForHere() {
    var section = document.querySelector("main section");
    var link = document.querySelector("[data-export]");
    if (link) return "The download for this view is " + link.textContent + ".";
    if (section) return "Use the coloured download buttons in this section.";
    return "Open Downloads for the sheets and the bundle.";
  }

  function reply(text) {
    var q = text.toLowerCase();
    say(text, "you");
    var route = [
      ["diagram", "diagrams.html"],
      ["flow", "flows.html"],
      ["download", "downloads.html"],
      ["play", "play.html"],
      ["listen", "listen.html"],
      ["help", "help.html"],
      ["legal", "legal.html"],
      ["credit", "legal.html"],
      ["learn", "start.html"],
      ["course", "start.html"],
      ["port", "ports.html"],
      ["career", "careers.html"],
      ["cert", "certs.html"],
      ["ecosystem", "ecosystem.html"],
      ["gloss", "glossary.html"],
      ["search", "search.html"],
      ["home", "index.html"],
      ["quiz", ""],
      ["interview", "interviews.html"]
    ];
    if (/export|download this|sheet|svg|pdf/.test(q)) {
      say(exportForHere());
      pose("cheer");
      return;
    }
    if (/10 minute|ten minute|finish fast/.test(q)) {
      location.href = base + "start.html#ten";
      return;
    }
    if (/don't know|do not know|not sure|unsure/.test(q)) {
      say("I only answer from this lab's notes. Confirm before relying, and check the cited page.");
      return;
    }
    for (var i = 0; i < kb.length; i++) {
      if (q.indexOf(kb[i].title.toLowerCase()) !== -1 || (kb[i].id && q.indexOf(kb[i].id) !== -1)) {
        say(kb[i].blurb + " Opening that room.");
        location.href = base + kb[i].href;
        return;
      }
    }
    for (var r = 0; r < route.length; r++) {
      if (q.indexOf(route[r][0]) !== -1 && route[r][1]) {
        say("Opening " + route[r][0] + ".");
        location.href = base + route[r][1];
        return;
      }
    }
    if (window.F9_GUIDE.endpoint) {
      say("A cloud endpoint is set, and this build does not call it. Ask with a word from the menu.");
      return;
    }
    say("I can open Learn, Diagrams, Play, Listen, Downloads, Help, or a room by its title. " + exportForHere());
    pose("think");
  }

  function place() {
    var saved = store.get("f9-guide-pos");
    if (saved && !host.classList.contains("is-greet")) {
      try {
        var pos = JSON.parse(saved);
        host.style.left = pos.left + "px";
        host.style.top = pos.top + "px";
        host.style.right = "auto";
        host.style.bottom = "auto";
      } catch (err) { /* ignore bad json */ }
    }
    var footer = document.querySelector(".site-footer");
    var hide = false;
    if (footer && !host.classList.contains("is-greet")) {
      var rect = footer.getBoundingClientRect();
      if (rect.top < window.innerHeight - 80 && rect.bottom > 80) hide = rect.top < window.innerHeight * 0.72;
    }
    host.classList.toggle("is-clear", hide);
    fitPanel();
  }

  function greet() {
    if (store.get("f9-greeted") === "1") { place(); return; }
    host.classList.add("is-greet");
    host.style.left = "";
    host.style.top = "";
    host.style.right = "";
    host.style.bottom = "";
    pose("wave");
    setOpen(false);
    var modal = host.querySelector(".cg-greet");
    if (modal) modal.hidden = false;
    showCards();
    speak("Welcome to CypherMonkey Labs. I am the Five9 guide.");
    store.set("f9-greeted", "1");
  }
  function dock() {
    host.classList.remove("is-greet");
    var modal = host.querySelector(".cg-greet");
    if (modal) modal.hidden = true;
    host.style.left = "";
    host.style.top = "";
    host.style.right = "";
    host.style.bottom = "";
    pose("idle");
    place();
  }

  function overlaps(a, b, gap) {
    return !(a.right + gap < b.left || a.left - gap > b.right || a.bottom + gap < b.top || a.top - gap > b.bottom);
  }
  function revealRail(target) {
    var rail = target && target.closest(".section-rail");
    if (!rail) return;
    var railRect = rail.getBoundingClientRect();
    var rect = target.getBoundingClientRect();
    var delta = (rect.left + rect.width / 2) - (railRect.left + rail.clientWidth / 2);
    rail.scrollLeft += delta;
  }
  function placeCallout(callout, target) {
    var vw = window.innerWidth;
    var vh = window.innerHeight;
    var margin = 8;
    var dock = 88;
    callout.style.width = Math.min(340, vw - margin * 2) + "px";
    var cw = callout.offsetWidth;
    var ch = callout.offsetHeight;
    var left = Math.max(margin, Math.round((vw - cw) / 2));
    if (left + cw > vw - margin) left = Math.max(margin, vw - cw - margin);
    var blocked = [];
    var title = document.querySelector(".hero-title, #main h1");
    var hero = document.querySelector(".hero-stage");
    if (title) blocked.push({ rect: title.getBoundingClientRect(), weight: 20 });
    if (hero) blocked.push({ rect: hero.getBoundingClientRect(), weight: 8 });
    if (target) blocked.push({ rect: target.getBoundingClientRect(), weight: 6 });
    var candidates = [vh - ch - margin - dock, margin];
    blocked.forEach(function (item) {
      candidates.push(item.rect.bottom + 12);
      candidates.push(item.rect.top - ch - 12);
    });
    var best = vh - ch - margin - dock;
    var bestScore = Infinity;
    candidates.forEach(function (top) {
      var y = top;
      if (y + ch > vh - margin - dock) y = vh - ch - margin - dock;
      if (y < margin) y = margin;
      var box = { left: left, right: left + cw, top: y, bottom: y + ch };
      var score = Math.abs(y - (vh - ch - margin - dock)) * 0.04;
      blocked.forEach(function (item) {
        if (!overlaps(box, item.rect, 8)) return;
        var width = Math.max(0, Math.min(box.right, item.rect.right) - Math.max(box.left, item.rect.left));
        var height = Math.max(0, Math.min(box.bottom, item.rect.bottom) - Math.max(box.top, item.rect.top));
        score += width * height * item.weight;
      });
      if (score < bestScore) {
        bestScore = score;
        best = y;
      }
    });
    callout.style.left = left + "px";
    callout.style.top = best + "px";
    callout.style.right = "auto";
    callout.style.bottom = "auto";
  }
  function showStep() {
    var item = steps[step];
    var target = document.querySelector(item.sel) || document.querySelector("#tour-menu");
    if (target && target.getBoundingClientRect().height < 8) {
      target = document.querySelector("[data-open-guide]") || document.querySelector("#tour-menu");
    }
    host.classList.add("is-touring");
    tour.hidden = false;
    var num = tour.querySelector("[data-tour-num]");
    var count = tour.querySelector("[data-tour-count]");
    if (num) num.textContent = String(step + 1);
    if (count) count.textContent = (step + 1) + " of " + steps.length;
    tourCopy.textContent = item.text;
    if (target) revealRail(target);
    var callout = tour.querySelector(".cg-callout");
    if (!target) {
      spot.hidden = true;
      placeCallout(callout, null);
      return;
    }
    var rect = target.getBoundingClientRect();
    var left = Math.max(4, rect.left - 6);
    var top = Math.max(4, rect.top - 6);
    spot.hidden = false;
    spot.style.left = left + "px";
    spot.style.top = top + "px";
    spot.style.width = Math.max(12, Math.min(rect.width + 12, window.innerWidth - left - 4)) + "px";
    spot.style.height = Math.max(12, Math.min(rect.height + 12, window.innerHeight - top - 4)) + "px";
    placeCallout(callout, target);
  }
  function endTour(skipped) {
    tour.hidden = true;
    spot.hidden = true;
    host.classList.remove("is-touring");
    store.set("f9-tour", "1");
    if (!skipped) pose("cheer");
    greet();
  }

  monkey.addEventListener("click", function () {
    if (host.classList.contains("is-greet")) { dock(); return; }
    setOpen(panel.hidden);
  });
  document.addEventListener("keydown", function (event) {
    if (event.key !== "Escape") return;
    if (!tour.hidden) { endTour(true); return; }
    if (host.classList.contains("is-greet")) dock();
  });
  host.querySelectorAll("[data-greet-dock]").forEach(function (btn) {
    btn.addEventListener("click", function () { dock(); });
  });
  var handle = host.querySelector(".cg-handle");
  var dragY = 0;
  if (handle) {
    handle.addEventListener("pointerdown", function (event) {
      dragY = event.clientY;
      handle.setPointerCapture(event.pointerId);
    });
    handle.addEventListener("pointermove", function (event) {
      if (!handle.hasPointerCapture(event.pointerId)) return;
      var dy = Math.max(0, event.clientY - dragY);
      panel.style.transform = "translateY(" + dy + "px)";
    });
    handle.addEventListener("pointerup", function (event) {
      if (event.clientY - dragY > 48) setOpen(false);
      panel.style.transform = "";
    });
  }
  host.querySelector("[data-close]").addEventListener("click", function () { setOpen(false); dock(); });
  host.querySelector("[data-read]").addEventListener("click", readAlong);
  function siteUrl(path) {
    var rel = base || "./";
    if (rel && rel.charAt(rel.length - 1) !== "/") rel += "/";
    return new URL(path, new URL(rel, document.baseURI)).href;
  }
  function localize(answer) {
    function fix(href) {
      if (!href || /^(https?:|#)/.test(href)) return href || "";
      return (base || "") + href;
    }
    return {
      role: "bot",
      text: answer.text || "",
      href: fix(answer.href || ""),
      link: answer.link || "",
      example: answer.example || "",
      follow: answer.follow || "",
      followQ: answer.followQ || "",
      closest: (answer.closest || []).map(function (hit) {
        return { title: hit.title, href: fix(hit.href) };
      })
    };
  }
  function askGuide(text) {
    messages.push({ role: "user", text: text });
    if (paintChat && chatRoot) paintChat(chatRoot, messages, true);
    pose("think");
    var run = function () {
      if (!retriever) {
        messages.push({ role: "bot", text: "I don't have that yet. The lesson index is not on this page yet." });
        if (paintChat && chatRoot) paintChat(chatRoot, messages, false);
        return;
      }
      var answer = retriever.ask(text, {
        progress: function () {
          return { done: 0, total: 161, xpLevel: 1, nextHref: "start.html", nextTitle: "Learn" };
        }
      });
      messages.push(localize(answer));
      if (paintChat && chatRoot) paintChat(chatRoot, messages, false);
      pose(answer.mode === "answer" || answer.mode === "intent" ? "speak" : "think");
    };
    if (retriever) run();
    else chatReady.then(run, run);
  }
  chatReady = Promise.all([
    import(siteUrl("shared/pybot-chat/engine.js")),
    import(siteUrl("shared/pybot-chat/ui.js")),
    fetch(siteUrl("js/content/f9bot-index.json")).then(function (res) { return res.json(); })
  ]).then(function (parts) {
    var engine = parts[0];
    var ui = parts[1];
    paintChat = ui.paintChat;
    retriever = engine.createRetriever(parts[2]);
    var slot = host.querySelector("[data-f9-chat]");
    if (!slot) return;
    slot.innerHTML = ui.chatMarkup(topics);
    chatRoot = slot.querySelector("[data-py-chat]");
    paintChat(chatRoot, messages, false);
    var form = chatRoot.querySelector(".py-chat-form");
    var input = ui.chatInput(chatRoot);
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var text = input.value.trim();
      if (!text) return;
      input.value = "";
      askGuide(text);
    });
    chatRoot.addEventListener("click", function (event) {
      var chip = event.target.closest("[data-py-ask]");
      if (chip) {
        askGuide(chip.getAttribute("data-py-ask"));
        return;
      }
      if (event.target.closest("[data-py-clear]")) {
        messages = [];
        if (retriever) retriever.reset();
        paintChat(chatRoot, messages, false);
      }
    });
    var mic = chatRoot.querySelector("[data-py-mic]");
    if (mic) mic.addEventListener("click", function () {
      var Rec = window.SpeechRecognition || window.webkitSpeechRecognition;
      pose("listen");
      if (!Rec) {
        messages.push({ role: "bot", text: "This browser has no voice input. Type in the box." });
        paintChat(chatRoot, messages, false);
        input.focus();
        return;
      }
      var rec = new Rec();
      rec.lang = "en-US";
      rec.onresult = function (event) {
        input.value = event.results[0][0].transcript;
        pose("speak");
      };
      rec.onerror = function () { input.focus(); };
      try { rec.start(); } catch (err) { input.focus(); }
    });
    window.__f9botReady = true;
  }).catch(function () {
    window.__f9botReady = false;
  });
  voiceSel.addEventListener("change", function () { store.set("f9-voice", voiceSel.value); });
  rate.addEventListener("change", function () { store.set("f9-rate", rate.value); });
  pitch.addEventListener("change", function () { store.set("f9-pitch", pitch.value); });
  if (store.get("f9-rate")) rate.value = store.get("f9-rate");
  if (store.get("f9-pitch")) pitch.value = store.get("f9-pitch");

  ambientBox.addEventListener("change", function () {
    if (!ambientBox.checked) {
      if (audioCtx) audioCtx.suspend();
      return;
    }
    var Ctx = window.AudioContext || window.webkitAudioContext;
    if (!Ctx) return;
    if (!audioCtx) {
      audioCtx = new Ctx();
      var osc = audioCtx.createOscillator();
      var gain = audioCtx.createGain();
      osc.frequency.value = 174;
      gain.gain.value = 0.008;
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
    } else audioCtx.resume();
  });

  tour.querySelector("[data-tour-next]").addEventListener("click", function () {
    if (step >= steps.length - 1) endTour(false);
    else { step += 1; showStep(); }
  });
  tour.querySelector("[data-tour-back]").addEventListener("click", function () {
    step = Math.max(0, step - 1);
    showStep();
  });
  tour.querySelector("[data-tour-skip]").addEventListener("click", function () { endTour(true); });
  document.querySelectorAll("[data-replay-tour]").forEach(function (btn) {
    btn.addEventListener("click", function () { step = 0; showStep(); });
  });
  document.querySelectorAll("[data-open-guide]").forEach(function (btn) {
    btn.addEventListener("click", function () { dock(); setOpen(true); showCards(); });
  });

  host.querySelector("[data-nudge-yes]").addEventListener("click", function () { nudge.hidden = true; setOpen(true); showCards(); });
  host.querySelector("[data-nudge-later]").addEventListener("click", function () { nudge.hidden = true; });
  host.querySelector("[data-nudge-stop]").addEventListener("click", function () {
    nudge.hidden = true;
    stopped = true;
    store.set("f9-offers-stop", "1");
  });

  var drag = null;
  monkey.addEventListener("pointerdown", function (event) {
    if (host.classList.contains("is-greet")) return;
    drag = { x: event.clientX, y: event.clientY, left: host.getBoundingClientRect().left, top: host.getBoundingClientRect().top };
  });
  window.addEventListener("pointermove", function (event) {
    if (!drag) return;
    var left = Math.max(8, Math.min(window.innerWidth - 80, drag.left + event.clientX - drag.x));
    var top = Math.max(8, Math.min(window.innerHeight - 80, drag.top + event.clientY - drag.y));
    host.style.left = left + "px";
    host.style.top = top + "px";
    host.style.right = "auto";
    host.style.bottom = "auto";
  });
  window.addEventListener("pointerup", function () {
    if (!drag) return;
    drag = null;
    var rect = host.getBoundingClientRect();
    store.set("f9-guide-pos", JSON.stringify({ left: rect.left, top: rect.top }));
  });

  document.addEventListener("f9-quiz", function (event) {
    pose(event.detail.right === event.detail.total ? "cheer" : "think");
  });

  if (window.speechSynthesis) {
    fillVoices();
    window.speechSynthesis.addEventListener("voiceschanged", fillVoices);
  }
  fetch(base + "guide/kb.json").then(function (res) { return res.json(); }).then(function (data) {
    kb = data.rooms || [];
  }).catch(function () { kb = []; });

  showCards();
  if (store.get("f9-tour") !== "1") showStep();
  else greet();

  window.setTimeout(function () {
    if (stopped || offers >= 3 || !panel.hidden || !tour.hidden) return;
    offers += 1;
    store.set("f9-offer-count", String(offers));
    nudge.hidden = false;
    pose("wave");
  }, 180000);

  window.addEventListener("scroll", place, { passive: true });
  window.addEventListener("resize", function () {
    place();
    if (!tour.hidden) showStep();
  });
  place();
})();
