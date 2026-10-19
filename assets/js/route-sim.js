/* Routing desk. A classroom model. It does not call Five9 or a carrier. */
(function () {
  var root = document.querySelector("[data-route-sim]");
  if (!root) return;
  var entry = root.querySelector("[data-entry]");
  var mode = root.querySelector("[data-mode]");
  var skill = root.querySelector("[data-skill]");
  var out = root.querySelector("[data-route-out]");
  var nodes = root.querySelectorAll("[data-node]");

  var copy = {
    entry: "Simulation. The call enters here. This desk did not open a trunk.",
    campaign: "Simulation. A campaign has to be running before a DNIS or a list is used.",
    treatment: "Simulation. Inbound uses a script. Outbound uses the dial mode you picked. Autodial uses the IVR.",
    skill: "Simulation. Skill transfer names a skill. The name is only the text in the field.",
    agent: "Simulation. The agent step is a drawing. No desktop was signed in."
  };

  function sentence() {
    var who = (skill.value || "").trim() || "Support";
    var path = entry.value;
    var dial = mode.value;
    var head = "Simulation only. This does not call Five9, a carrier, or a CRM. ";
    var mid = "";
    if (path === "inbound") mid = "Inbound path: a DNIS is answered while its campaign runs, then the script can transfer to " + who + ". ";
    else if (path === "autodial") mid = "Autodial path: the IVR places the outbound attempt, then " + who + " is the skill name on this card. ";
    else mid = "Outbound path: the list is not the campaign. Dial mode is " + dial + ". Skill name on this card: " + who + ". ";
    var tail = "";
    if (dial === "preview") tail = "Preview, in this model, lets the agent read the record first.";
    else if (dial === "progressive") tail = "Progressive, in this model, keeps one attempt for a free agent.";
    else if (dial === "power") tail = "Power, in this model, uses a ratio a person chose. This card does not invent the ratio.";
    else if (dial === "predictive") tail = "Predictive, in this model, can leave unanswered calls. Confirm the live rule on the cited lesson.";
    else tail = "TCPA manual touch, in this model, is a typed number. This card does not place the call.";
    return head + mid + tail + " Source check on the lesson pages is 2026-10; unconfirmed if a vendor page moved.";
  }

  function paint(active) {
    nodes.forEach(function (node) {
      var on = node.getAttribute("data-node") === active;
      node.setAttribute("aria-pressed", on ? "true" : "false");
    });
    out.textContent = (copy[active] ? copy[active] + " " : "") + sentence();
  }

  root.querySelector("[data-route-run]").addEventListener("click", function () { paint("agent"); });
  entry.addEventListener("change", function () { paint("entry"); });
  mode.addEventListener("change", function () { paint("treatment"); });
  skill.addEventListener("input", function () { paint("skill"); });
  nodes.forEach(function (node) {
    node.addEventListener("click", function () { paint(node.getAttribute("data-node")); });
  });
  paint("entry");
})();
