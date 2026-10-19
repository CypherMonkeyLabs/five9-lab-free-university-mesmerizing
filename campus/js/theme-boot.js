/* Apply saved campus settings before first paint. External so script-src 'self' can stay strict. */
try {
  var saved = JSON.parse(localStorage.getItem("f9lab-settings") || "{}");
  if (saved.theme) document.documentElement.dataset.theme = saved.theme;
  else document.documentElement.dataset.theme = "light";
  if (saved.font) document.documentElement.dataset.font = String(saved.font);
  if (saved.reduced === true) document.documentElement.dataset.motion = "reduce";
  if (saved.reduced === false) document.documentElement.dataset.motion = "full";
  if (saved.reduced == null && matchMedia("(prefers-reduced-motion: reduce)").matches) {
    document.documentElement.dataset.motion = "reduce";
  }
} catch (err) { /* keep defaults */ }
