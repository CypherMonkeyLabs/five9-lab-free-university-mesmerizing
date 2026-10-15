// Teaching diagrams for the Five9 lab. They are drawings, not captured traces.

function esc(value) {
  return String(value).replace(/[&<>"]/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch]));
}

let seq = 0;

function frame(w, h, label, body) {
  const mid = `ah${seq += 1}`;
  const painted = body.replaceAll("url(#ah)", `url(#${mid})`);
  return `<svg class="diag" viewBox="0 0 ${w} ${h}" role="img" aria-label="${esc(label)}"><title>${esc(label)}</title><defs><marker id="${mid}" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" class="arrow-head"></path></marker></defs><rect class="diag-bg" width="${w}" height="${h}" rx="16"></rect>${painted}</svg>`;
}

function box(x, y, w, h, text, tone) {
  const lines = String(text).split("\n");
  const start = y + h / 2 - (lines.length - 1) * 8 + 4;
  const tspans = lines.map((line, i) => `<tspan x="${x + w / 2}" y="${start + i * 16}">${esc(line)}</tspan>`).join("");
  return `<g class="node tone-${tone || "a"}"><rect x="${x}" y="${y}" width="${w}" height="${h}" rx="12"></rect><text text-anchor="middle">${tspans}</text></g>`;
}

function flowLine(x1, y1, x2, y2) {
  return `<line class="flow-line" x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" marker-end="url(#ah)"></line>`;
}

function hflow(label, steps) {
  const w = 36 + steps.length * 150;
  const body = steps.map((step, i) => {
    const x = 24 + i * 150;
    const line = i < steps.length - 1 ? flowLine(x + 128, 78, x + 148, 78) : "";
    return `${line}${box(x, 48, 124, 60, step, i % 2 ? "b" : "a")}`;
  }).join("");
  return frame(w, 160, label, body);
}

function vstack(label, rows) {
  const h = 36 + rows.length * 58;
  const body = rows.map((row, i) => box(40 + i * 10, 20 + i * 58, 360 - i * 20, 46, row, i % 2 ? "b" : "c")).join("");
  return frame(460, h, label, body);
}

const custom = {
  "dialer-modes"() {
    const modes = [
      ["Preview", "Read, then dial"],
      ["Progressive", "One call, one agent"],
      ["Power", "A ratio you set"],
      ["Predictive", "Paces, can drop"],
      ["Manual touch", "Type the number"]
    ];
    const body = modes.map((mode, i) => {
      const x = 20 + (i % 3) * 200;
      const y = 24 + Math.floor(i / 3) * 100;
      return box(x, y, 180, 78, `${mode[0]}\n${mode[1]}`, ["a", "b", "c", "d", "b"][i]);
    }).join("");
    return frame(620, 250, "Five dialing modes", body);
  },
  "sip-ladder"() {
    const heads = ["Caller", "Five9 edge", "Agent"];
    const cols = heads.map((head, i) => `<text class="lane" x="${90 + i * 180}" y="28" text-anchor="middle">${head}</text><line class="lane-line" x1="${90 + i * 180}" y1="40" x2="${90 + i * 180}" y2="300"></line>`).join("");
    const msgs = [
      [0, 1, "INVITE", 58],
      [1, 0, "100 Trying", 96],
      [1, 2, "INVITE", 134],
      [2, 1, "180 Ringing", 172],
      [2, 1, "200 OK", 210],
      [0, 1, "ACK", 248],
      [1, 2, "BYE", 286]
    ];
    const arrows = msgs.map(([a, b, text, y]) => {
      const x1 = 90 + a * 180;
      const x2 = 90 + b * 180;
      const dir = x2 > x1 ? 1 : -1;
      return `<line class="flow-line" x1="${x1 + dir * 8}" y1="${y}" x2="${x2 - dir * 10}" y2="${y}" marker-end="url(#ah)"></line><text class="msg" x="${(x1 + x2) / 2}" y="${y - 6}" text-anchor="middle">${text}</text>`;
    }).join("");
    return frame(560, 330, "Teaching SIP ladder, not a captured trace", cols + arrows);
  },
  "sip-entries"() {
    return frame(640, 280, "Three trunk stories and four station types", `
      ${box(230, 110, 180, 64, "Five9 domain", "a")}
      ${box(20, 24, 170, 56, "Five9 as ITSP", "b")}
      ${box(235, 24, 170, 56, "Your ITSP", "c")}
      ${box(450, 24, 170, 56, "Your gateway", "d")}
      ${flowLine(105, 80, 280, 110)}
      ${flowLine(320, 80, 320, 110)}
      ${flowLine(535, 80, 360, 110)}
      ${box(20, 200, 140, 52, "Softphone", "a")}
      ${box(170, 200, 140, 52, "WebRTC", "b")}
      ${box(320, 200, 140, 52, "Gateway", "c")}
      ${box(470, 200, 140, 52, "PSTN station", "d")}
      ${flowLine(320, 174, 90, 200)}
      ${flowLine(320, 174, 240, 200)}
      ${flowLine(320, 174, 390, 200)}
      ${flowLine(320, 174, 540, 200)}
    `);
  },
  "ivr-tree"() {
    return frame(640, 300, "IVR teaching tree", `
      ${box(250, 16, 140, 48, "Play greeting", "a")}
      ${flowLine(320, 64, 320, 84)}
      ${box(230, 84, 180, 48, "Menu", "b")}
      ${flowLine(250, 132, 110, 168)}
      ${flowLine(320, 132, 320, 168)}
      ${flowLine(390, 132, 520, 168)}
      ${box(30, 168, 160, 52, "1 Sales skill", "c")}
      ${box(240, 168, 160, 52, "2 If/Else hours", "a")}
      ${box(450, 168, 160, 52, "3 Lookup", "d")}
      ${flowLine(320, 220, 320, 240)}
      ${box(220, 240, 200, 44, "Else: Default queue", "b")}
    `);
  },
  "e911-path"() {
    return frame(640, 220, "Emergency call depends on location", `
      ${box(20, 70, 140, 56, "Agent phone", "a")}
      ${flowLine(160, 98, 190, 98)}
      ${box(190, 70, 150, 56, "Five9 domain", "b")}
      ${flowLine(340, 98, 370, 98)}
      ${box(370, 70, 120, 56, "RedSky", "c")}
      ${flowLine(490, 98, 520, 98)}
      ${box(500, 40, 120, 44, "PSAP", "d")}
      ${box(190, 150, 250, 48, "Dispatchable location", "b")}
    `);
  },
  "firewall"() {
    const rows = [
      ["443", "TCP", "HTTPS sign-in"],
      ["5081", "TCP", "SIP over TLS"],
      ["5060", "UDP", "SIP agent"],
      ["RTP", "UDP", "1024-65535"]
    ];
    const body = `<text class="lane" x="24" y="32">Workstation</text><text class="lane" x="430" y="32">Five9</text>${rows.map((row, i) => {
      const y = 52 + i * 48;
      return `<text class="msg" x="24" y="${y + 22}">${row[2]}</text>${flowLine(150, y + 16, 470, y + 16)}<text class="msg" x="250" y="${y + 8}">${row[0]}/${row[1]}</text>`;
    }).join("")}`;
    return frame(560, 260, "Softphone ports, teaching view", body);
  },
  "cutover"() {
    const gates = ["Objects rebuilt", "Test call", "911 location", "Recording notice", "One DNIS", "Go or stop"];
    const body = gates.map((gate, i) => `${box(24, 16 + i * 52, 280, 42, gate, i === 5 ? "d" : "a")}${i < gates.length - 1 ? flowLine(164, 58 + i * 52, 164, 68 + i * 52) : ""}`).join("");
    return frame(340, 340, "Cutover gates", body);
  },
  "forecast-loop"() {
    return frame(560, 200, "Classroom forecast loop, not the Five9 engine", `
      ${box(16, 70, 120, 56, "History", "a")}
      ${flowLine(136, 98, 160, 98)}
      ${box(160, 70, 120, 56, "Interval", "b")}
      ${flowLine(280, 98, 304, 98)}
      ${box(304, 70, 120, 56, "Erlang C", "c")}
      ${flowLine(424, 98, 448, 98)}
      ${box(430, 40, 114, 48, "Roster", "d")}
      ${flowLine(487, 88, 80, 140)}
      <text class="msg" x="200" y="168">Compare schedule to actual</text>
    `);
  },
  "predictive-loop"() {
    return frame(520, 220, "Predictive pacing can outdial the free agents", `
      ${box(30, 30, 140, 52, "Free agents", "a")}
      ${flowLine(170, 56, 200, 56)}
      ${box(200, 30, 140, 52, "Dial ahead", "b")}
      ${flowLine(340, 56, 370, 56)}
      ${box(360, 30, 130, 52, "Connect or drop", "d")}
      ${box(160, 130, 200, 52, "Abandon throttle", "c")}
      ${flowLine(425, 82, 300, 130)}
    `);
  },
  "pop-split"() {
    return frame(560, 200, "Voice and screen pop fail separately", `
      ${box(180, 16, 200, 48, "Customer call", "a")}
      ${flowLine(240, 64, 110, 100)}
      ${flowLine(320, 64, 420, 100)}
      ${box(24, 100, 180, 64, "Voice path\nSIP or WebRTC", "b")}
      ${box(340, 100, 196, 64, "Pop path\nHTTPS and WSS", "c")}
    `);
  },
  "nat-path"() {
    return frame(620, 180, "Return RTP has to be allowed", `
      ${box(16, 60, 130, 52, "Phone", "a")}
      ${flowLine(146, 86, 176, 86)}
      ${box(176, 50, 150, 72, "Firewall\nstateful?", "d")}
      ${flowLine(326, 86, 360, 86)}
      ${box(360, 60, 120, 52, "RTP", "b")}
      ${flowLine(480, 86, 510, 86)}
      ${box(500, 60, 100, 52, "Five9", "c")}
    `);
  },
  "security-layers"() {
    return vstack("Security layers to name out loud", ["TLS 1.2 on the apps", "HTTPS and WSS on adapters", "SIP TLS on 5081 when that path is yours", "Certified Caller is not the ANI field", "TCPA manual touch is a typed number", "Retention clocks are not one switch"]);
  },
  "uccx-bridge"() {
    return frame(640, 220, "Teaching bridge, there is no import button", `
      ${box(20, 40, 180, 56, "UCCX CSQ", "b")}
      ${box(20, 130, 180, 56, "UCCX script", "c")}
      ${box(420, 40, 190, 56, "Five9 skill", "a")}
      ${box(420, 130, 190, 56, "IVR modules", "d")}
      ${flowLine(200, 68, 420, 68)}
      ${flowLine(200, 158, 420, 158)}
      <text class="msg" x="310" y="24" text-anchor="middle">Rebuild, then move one number</text>
    `);
  }
};

const flows = {
  "outbound-order": ["Skills", "Users", "Lists", "Dispositions", "Profile", "Campaign"],
  "inbound-path": ["DNIS", "Running campaign", "IVR script", "Skill", "Agent"],
  "tcpa-touch": ["Record on screen", "Agent types", "Paste blocked", "Match", "Dial"],
  "skill-default": ["Skill Transfer", "Skill named", "That queue", "No skill", "Default"],
  "blend-staff": ["Inbound", "Autodial", "Outbound", "Not Ready", "After-call work"],
  "desktop": ["Voice", "Text", "Screen pop", "Assist", "WEM"],
  "wem-loop": ["Forecast", "Schedule", "Adhere", "Evaluate", "Coach"],
  "qm-loop": ["Record", "Sample", "Score", "Coach", "Watch the next call"],
  "retention": ["Audio clock", "E911 clock", "Agent data", "Call log", "DIDs"],
  "iva-handoff": ["Studio task", "Contain", "Or hand off", "Named skill", "Context"],
  "genai-hub": ["Knowledge", "Prompt", "Test", "Agent Assist", "Change control"],
  "adapters": ["Salesforce", "ServiceNow", "Dynamics", "Zendesk", "Oracle", "NetSuite", "Epic"],
  "bandwidth": ["G.711 seat", "CRM +64", "VPN +64", "Screen +160", "UC client 320"],
  "stir-ani": ["Profile ANI", "Local caller ID", "Certified Caller", "STIR/SHAKEN", "Not the same field"],
  "api-pipes": ["Web2Campaign", "CRM SDK", "Statistics", "Reporting", "Web Connector"],
  "uc-bridges": ["Teams", "Zoom", "RingCentral", "Nextiva", "Office@Hand"],
  "report-pipes": ["Reporting role", "Standard layout", "Call log", "Call variables", "Export"],
  "studio-regions": ["Pick region", "Build task", "Copy key", "Paste in VCC", "Test handoff"],
  "list-walk": ["List penetration", "First numbers", "Then next", "Or vertical", "Finish the record"],
  "acw-clock": ["Hang up", "After-call work", "Disposition", "Ready", "Next dial"],
  "career-path": ["Domain", "Voice", "IVR", "SIP", "WEM", "Migration"]
};

const stacks = {
  "domain-stack": ["Domain tenant", "Skills and users", "Lists and dispositions", "Profiles", "Campaigns", "Reports"],
  "career-stack": ["Administrator", "IVR designer", "Dialer and compliance", "SIP and carriers", "WEM analyst", "Migration lead"]
};

export function diagram(id) {
  if (custom[id]) return custom[id]();
  if (flows[id]) return hflow(id, flows[id]);
  if (stacks[id]) return vstack(id, stacks[id]);
  return "";
}

export const diagramIds = [...Object.keys(custom), ...Object.keys(flows), ...Object.keys(stacks)];

export const diagramMeta = [
  ["domain-stack", "What a domain holds", "Planning your implementation"],
  ["outbound-order", "Outbound build order", "Planning your implementation"],
  ["inbound-path", "Inbound only answers while it runs", "Inbound campaigns"],
  ["dialer-modes", "Five modes, five promises", "Dialer and outbound pages"],
  ["predictive-loop", "Predictive can drop a call", "Dialer product page"],
  ["tcpa-touch", "Manual touch is typed", "TCPA manual touch"],
  ["ivr-tree", "Modules, then a skill", "IVR modules"],
  ["skill-default", "No skill selected is a queue", "Skill Transfer article"],
  ["blend-staff", "Blended is staffing", "Outbound and desktop pages"],
  ["desktop", "One agent screen", "Agent Desktop"],
  ["wem-loop", "Workforce engagement loop", "WEM product page"],
  ["qm-loop", "Quality is a sample, not a vibe", "WEM product page"],
  ["retention", "Several clocks", "Data retention"],
  ["iva-handoff", "Contain or hand back", "Studio digital IVA"],
  ["genai-hub", "Prompts are a change", "GenAI Studio"],
  ["adapters", "Named Plus adapters", "Technical requirements"],
  ["pop-split", "Pop down, voice up", "Technical requirements"],
  ["sip-entries", "Trunks and stations", "SIP trunk options"],
  ["bandwidth", "G.711 plus the extras", "Technical requirements"],
  ["firewall", "Ports to say out loud", "Community port article"],
  ["e911-path", "Location, then the call", "E911 data sheet"],
  ["stir-ani", "Attestation is not ANI", "Certified Caller"],
  ["api-pipes", "Name the API family", "APIs and SDKs"],
  ["uccx-bridge", "No import button", "Planning and IVR guides"],
  ["uc-bridges", "UC clients are 320 kbps each", "Technical requirements"],
  ["report-pipes", "Reports need a role", "Standard reports article"],
  ["studio-regions", "Region, then a task key", "Studio digital IVA"],
  ["sip-ladder", "Teaching ladder", "RFC 3261"],
  ["list-walk", "Penetration versus vertical", "List dialing modes"],
  ["acw-clock", "After-call work feeds pacing", "Agent states in the lessons"],
  ["nat-path", "One-way audio starts here", "Technical requirements"],
  ["cutover", "A gate can stop the morning", "Migration track"],
  ["security-layers", "Name the control", "Technical requirements"],
  ["forecast-loop", "Classroom math only", "Erlang, labeled as such"],
  ["career-path", "Study frames, not job reqs", "This lab"],
  ["career-stack", "Six study frames", "This lab"]
];
