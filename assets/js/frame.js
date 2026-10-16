/* Five9 frame. Banner arrows, top-left menu, sliding drawer, font size and colour.
   The guide bot mounts on #guide-mount. Adapted from the Webex lab frame.js.
   Brand links are only the website, the GitHub organization, and Linktree. */
(function () {
  var root = document.documentElement;
  var drawer = document.querySelector(".drawer");
  var back = document.querySelector(".drawer-back");
  var openers = document.querySelectorAll("[data-open-menu]");
  var closer = document.querySelector("[data-close-menu]");

  function setTheme(name) {
    root.dataset.theme = name === "dark" ? "dark" : "bloom";
    try { localStorage.setItem("f9-theme", root.dataset.theme); } catch (err) { /* private mode */ }
    var btn = document.querySelector("[data-theme-toggle]");
    if (btn) btn.textContent = root.dataset.theme === "dark" ? "Bright" : "Dark";
  }
  function setFont(size) {
    if (["sm", "md", "lg", "xl"].indexOf(size) < 0) size = "md";
    root.dataset.font = size;
    try { localStorage.setItem("f9-font", size); } catch (err) { /* private mode */ }
    var sel = document.querySelector("[data-font-size]");
    if (sel && sel.value !== size) sel.value = size;
  }
  function setInk(color) {
    if (!/^#[0-9a-f]{6}$/i.test(color || "")) return;
    root.style.setProperty("--ink", color);
    try { localStorage.setItem("f9-ink", color); } catch (err) { /* private mode */ }
    var input = document.querySelector("[data-font-color]");
    if (input && input.value.toLowerCase() !== color.toLowerCase()) input.value = color;
  }
  function setMotion(reduce) {
    root.dataset.motion = reduce ? "reduce" : "full";
    try { localStorage.setItem("f9-motion", root.dataset.motion); } catch (err) { /* private mode */ }
  }

  try {
    var theme = localStorage.getItem("f9-theme");
    if (theme === "dark" || theme === "bloom") setTheme(theme);
    var font = localStorage.getItem("f9-font");
    if (font) setFont(font);
    var ink = localStorage.getItem("f9-ink");
    if (ink) setInk(ink);
    var motion = localStorage.getItem("f9-motion");
    if (motion === "reduce" || motion === "full") setMotion(motion === "reduce");
    else setMotion(window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  } catch (err) { /* keep the bright default */ }

  function setOpen(open) {
    if (!drawer) return;
    drawer.classList.toggle("is-open", open);
    if (back) back.classList.toggle("is-open", open);
    drawer.setAttribute("aria-hidden", open ? "false" : "true");
    openers.forEach(function (btn) { btn.setAttribute("aria-expanded", open ? "true" : "false"); });
    if (open) {
      var search = drawer.querySelector("input");
      if (search) search.focus();
    }
  }
  openers.forEach(function (btn) {
    btn.addEventListener("click", function () { setOpen(!drawer.classList.contains("is-open")); });
  });
  if (closer) closer.addEventListener("click", function () { setOpen(false); });
  if (back) back.addEventListener("click", function () { setOpen(false); });
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") setOpen(false);
  });

  var rail = document.querySelector(".section-rail");
  document.querySelectorAll("[data-rail]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      if (!rail) return;
      var dir = btn.getAttribute("data-rail") === "prev" ? -1 : 1;
      rail.scrollBy({ left: dir * Math.max(180, rail.clientWidth * 0.7), behavior: root.dataset.motion === "reduce" ? "auto" : "smooth" });
    });
  });

  var fontSel = document.querySelector("[data-font-size]");
  if (fontSel) fontSel.addEventListener("change", function () { setFont(fontSel.value); });
  var color = document.querySelector("[data-font-color]");
  if (color) color.addEventListener("input", function () { setInk(color.value); });
  var themeBtn = document.querySelector("[data-theme-toggle]");
  if (themeBtn) {
    themeBtn.textContent = root.dataset.theme === "dark" ? "Bright" : "Dark";
    themeBtn.addEventListener("click", function () {
      setTheme(root.dataset.theme === "dark" ? "bloom" : "dark");
    });
  }
  var motionBtn = document.querySelector("[data-motion-toggle]");
  if (motionBtn) {
    motionBtn.addEventListener("click", function () {
      setMotion(root.dataset.motion !== "reduce");
      motionBtn.setAttribute("aria-pressed", root.dataset.motion === "reduce" ? "true" : "false");
    });
  }

  if (!document.getElementById("guide-mount")) {
    var mount = document.createElement("div");
    mount.id = "guide-mount";
    document.body.appendChild(mount);
  }

  var search = document.querySelector("[data-site-search]");
  if (search) {
    search.addEventListener("submit", function (event) {
      event.preventDefault();
      var q = (search.querySelector("input").value || "").trim();
      var prefix = document.documentElement.getAttribute("data-root") || "";
      location.href = prefix + "search.html?q=" + encodeURIComponent(q);
    });
  }
})();
