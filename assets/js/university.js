/* Quizzes, search filter, and the offline shell. Five9 pages only. */
(function () {
  function prefix() {
    return document.documentElement.getAttribute("data-root") || "";
  }

  document.querySelectorAll("[data-quiz]").forEach(function (form) {
    var button = form.querySelector("[data-quiz-check]");
    if (!button) return;
    button.addEventListener("click", function () {
      var sets = form.querySelectorAll("fieldset");
      var right = 0;
      sets.forEach(function (set, index) {
        var why = set.querySelector(".quiz-why");
        var answer = why ? why.getAttribute("data-answer") : "";
        var picked = form.querySelector('input[name="q' + index + '"]:checked');
        var ok = picked && picked.value === answer;
        if (ok) right += 1;
        if (why) why.hidden = false;
        set.style.outline = ok ? "2px solid #0f766e" : "2px solid #be123c";
      });
      var score = form.querySelector(".quiz-score");
      if (score) score.textContent = right + " of " + sets.length + " match the cited answer.";
      document.dispatchEvent(new CustomEvent("f9-quiz", { detail: { right: right, total: sets.length } }));
    });
  });

  var list = document.querySelector("[data-search-list]");
  if (list) {
    var params = new URLSearchParams(location.search);
    var q = (params.get("q") || "").trim().toLowerCase();
    var input = document.querySelector("[data-search-echo]");
    if (input) input.value = params.get("q") || "";
    if (q) {
      list.querySelectorAll("[data-search-item]").forEach(function (item) {
        var hay = (item.getAttribute("data-search-item") || "").toLowerCase();
        item.hidden = hay.indexOf(q) === -1;
      });
    }
  }

  if ("serviceWorker" in navigator && location.protocol !== "file:") {
    window.addEventListener("load", function () {
      navigator.serviceWorker.register(prefix() + "sw.js").catch(function () { /* offline build still readable */ });
    });
  }

  document.querySelectorAll("[data-port-game]").forEach(function (game) {
    game.addEventListener("click", function (event) {
      var btn = event.target.closest("[data-port]");
      if (!btn) return;
      var ok = btn.getAttribute("data-port") === game.getAttribute("data-answer");
      var out = game.querySelector("[data-port-result]");
      if (out) out.textContent = ok ? "That matches the community port note. Confirm before relying." : "Not the port this card is quoting. Try the table.";
    });
  });
})();
