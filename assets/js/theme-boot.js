/* Apply saved frame settings before first paint. External so script-src 'self' can stay strict. */
try {
  var t = localStorage.getItem("f9-theme");
  if (t === "dark" || t === "bloom") document.documentElement.dataset.theme = t;
  var f = localStorage.getItem("f9-font");
  if (f) document.documentElement.dataset.font = f;
  var m = localStorage.getItem("f9-motion");
  if (m === "reduce" || m === "full") document.documentElement.dataset.motion = m;
  var ink = localStorage.getItem("f9-ink");
  if (ink && /^#[0-9a-f]{6}$/i.test(ink)) document.documentElement.style.setProperty("--ink", ink);
} catch (e) {}
