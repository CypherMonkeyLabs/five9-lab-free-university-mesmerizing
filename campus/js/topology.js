import * as THREE from "three";
import { OrbitControls } from "../vendor/three/OrbitControls.js";

const NODES = [
  { id: "pstn", name: "PSTN", pos: [-6.2, 0.4, -1.2], color: 0xf5b942 },
  { id: "itsp", name: "Your ITSP", pos: [-4.2, 0.5, 1.2], color: 0xf5b942 },
  { id: "gw", name: "Customer gateway", pos: [-2.2, 0.45, 2.4], color: 0xc084fc },
  { id: "sbca", name: "Five9 SBC A", pos: [0.2, 0.7, 0.2], color: 0x3ee0ff },
  { id: "sbcb", name: "Five9 SBC B", pos: [1.5, 0.7, -1.6], color: 0x3ee0ff },
  { id: "vcc", name: "VCC domain", pos: [3.2, 1.1, 0.3], color: 0x3ee0ff },
  { id: "ivr", name: "IVR", pos: [4.6, 0.6, 1.8], color: 0x3ddc97 },
  { id: "skill", name: "Skill queues", pos: [5.4, 0.6, -0.8], color: 0x3ddc97 },
  { id: "adp", name: "Agent Desktop Plus", pos: [7, 0.5, 1.1], color: 0xc084fc },
  { id: "crm", name: "CRM adapter", pos: [7.6, 0.55, -1.3], color: 0xf5b942 },
  { id: "wem", name: "WEM", pos: [5.8, 1.5, -2.2], color: 0x3ddc97 },
  { id: "iva", name: "Studio IVA", pos: [3.4, 1.7, 2.3], color: 0xc084fc },
  { id: "redsky", name: "RedSky E911", pos: [-1.2, 1.3, -2.5], color: 0xff6b7a },
  { id: "rec", name: "Recording", pos: [2.2, 0.35, -2.3], color: 0xf5b942 }
];

const LINKS = [
  ["pstn", "itsp"], ["itsp", "sbca"], ["itsp", "sbcb"], ["gw", "sbca"], ["gw", "sbcb"],
  ["sbca", "vcc"], ["sbcb", "vcc"], ["vcc", "ivr"], ["ivr", "skill"], ["skill", "adp"],
  ["adp", "crm"], ["adp", "wem"], ["ivr", "iva"], ["adp", "redsky"], ["vcc", "rec"]
];

const FAILURES = {
  none: { links: [], text: "Both SBC paths are drawn up. DNS SRV is the published preference over pinning one address." },
  itsp: { links: ["pstn-itsp", "itsp-sbca", "itsp-sbcb"], text: "ITSP trunk down. Inbound DNIS cannot reach the domain. Outbound cannot seize a trunk. The gateway path can still be up." },
  sbca: { links: ["itsp-sbca", "gw-sbca", "sbca-vcc"], text: "SBC A is down. SBC B remains. A design that pinned a single IP would fail this test." },
  wan: { links: ["skill-adp", "adp-crm", "adp-wem", "adp-redsky"], text: "Agent WAN down. Queues still accept calls. Agents drop. Voice platforms do not fix a dead workstation." },
  crm: { links: ["adp-crm"], text: "CRM adapter down. The voice path stays up. Screen pop and connector data stop." },
  ivr: { links: ["vcc-ivr", "ivr-skill", "ivr-iva"], text: "IVR path broken. A running inbound campaign with a bad script never reaches the skill." },
  e911: { links: ["adp-redsky"], text: "E911 location is stale. The EULA says a 911 call from an unregistered or wrong address may not reach the right PSAP." }
};

function key(a, b) { return `${a}-${b}`; }

function labelSprite(text) {
  const canvas = document.createElement("canvas");
  canvas.width = 256;
  canvas.height = 64;
  const g = canvas.getContext("2d");
  g.fillStyle = "rgba(4,16,24,0.88)";
  g.fillRect(0, 0, 256, 64);
  g.strokeStyle = "#3ee0ff";
  g.strokeRect(3, 3, 250, 58);
  g.fillStyle = "#e7eef8";
  g.font = "22px sans-serif";
  g.textAlign = "center";
  g.textBaseline = "middle";
  g.fillText(text, 128, 32);
  const texture = new THREE.CanvasTexture(canvas);
  const sprite = new THREE.Sprite(new THREE.SpriteMaterial({ map: texture, transparent: true }));
  sprite.scale.set(1.9, 0.48, 1);
  return sprite;
}

function makeLink(a, b) {
  const start = new THREE.Vector3(...a.pos);
  const end = new THREE.Vector3(...b.pos);
  const dir = new THREE.Vector3().subVectors(end, start);
  const length = dir.length();
  const mesh = new THREE.Mesh(
    new THREE.CylinderGeometry(0.035, 0.035, length, 6),
    new THREE.MeshBasicMaterial({ color: 0x3ee0ff })
  );
  mesh.position.copy(start).add(end).multiplyScalar(0.5);
  mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), dir.normalize());
  const glow = new THREE.Mesh(
    new THREE.CylinderGeometry(0.09, 0.09, length, 6),
    new THREE.MeshBasicMaterial({ color: 0x3ee0ff, transparent: true, opacity: 0.28 })
  );
  mesh.add(glow);
  mesh.userData.link = key(a.id, b.id);
  mesh.userData.glow = glow;
  return mesh;
}

function fallback(root, onStatus, active) {
  const wrap = document.createElement("div");
  wrap.className = "panel";
  const buttons = document.createElement("div");
  buttons.className = "row";
  const map = document.createElement("div");
  map.className = "figure";
  const note = document.createElement("p");
  note.className = "note";
  note.setAttribute("role", "status");
  const positions = {
    pstn: [40, 120], itsp: [120, 70], gw: [120, 170], sbca: [220, 80], sbcb: [220, 160],
    vcc: [320, 110], ivr: [400, 60], skill: [400, 160], adp: [490, 110], crm: [560, 180],
    wem: [490, 200], iva: [400, 20], redsky: [120, 220], rec: [320, 200]
  };
  function paint(name) {
    const fail = FAILURES[name];
    onStatus(fail.text);
    note.textContent = fail.text;
    const nodes = NODES.map((node) => `<rect x="${positions[node.id][0]}" y="${positions[node.id][1]}" width="70" height="28" rx="6" fill="#102033" stroke="#3ee0ff"></rect><text x="${positions[node.id][0] + 6}" y="${positions[node.id][1] + 18}" fill="#e7eef8" font-size="9">${node.name}</text>`).join("");
    const lines = LINKS.map(([a, b]) => {
      const bad = fail.links.includes(key(a, b));
      const p = positions[a];
      const q = positions[b];
      return `<line x1="${p[0] + 35}" y1="${p[1] + 14}" x2="${q[0] + 35}" y2="${q[1] + 14}" stroke="${bad ? "#ff6b7a" : "#3ee0ff"}" stroke-width="${bad ? 3 : 1.5}"></line>`;
    }).join("");
    map.innerHTML = `<svg class="mind" viewBox="0 0 660 280" role="img" aria-label="Flat topology fallback">${lines}${nodes}</svg>`;
    buttons.querySelectorAll("button").forEach((button) => {
      button.setAttribute("aria-pressed", button.dataset.fail === name ? "true" : "false");
    });
  }
  Object.entries({
    none: "Healthy", itsp: "ITSP down", sbca: "SBC A down", wan: "Agent WAN", crm: "CRM down", ivr: "IVR break", e911: "Stale E911"
  }).forEach(([id, label]) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "btn";
    button.dataset.fail = id;
    button.textContent = label;
    button.addEventListener("click", () => paint(id));
    buttons.append(button);
  });
  const list = document.createElement("ul");
  NODES.forEach((node) => {
    const item = document.createElement("li");
    item.textContent = node.name;
    list.append(item);
  });
  wrap.append(buttons, map, note, list);
  root.append(wrap);
  paint(active || "none");
  return function destroy() { root.innerHTML = ""; };
}

export function mountTopology(root, opts) {
  const onStatus = opts.onStatus || (() => {});
  if (opts.reduced) {
    onStatus("Reduced motion is on, so the floor is a flat map instead of a rotating WebGL scene.");
    return fallback(root, onStatus, "none");
  }
  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
  } catch (err) {
    onStatus("WebGL did not start. Showing the flat map.");
    return fallback(root, onStatus, "none");
  }
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x041018);
  const camera = new THREE.PerspectiveCamera(50, 1, 0.1, 100);
  camera.position.set(8.5, 6.2, 9.5);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  const wrap = document.createElement("div");
  wrap.className = "canvas-wrap";
  wrap.append(renderer.domElement);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.target.set(2.2, 0.6, 0);
  scene.add(new THREE.AmbientLight(0xffffff, 0.7));
  const sun = new THREE.DirectionalLight(0xffffff, 1.1);
  sun.position.set(6, 10, 4);
  scene.add(sun);
  scene.add(new THREE.GridHelper(18, 18, 0x1d3c52, 0x102033));
  const byId = {};
  NODES.forEach((node) => {
    const mesh = new THREE.Mesh(
      new THREE.BoxGeometry(0.7, 0.45, 0.7),
      new THREE.MeshStandardMaterial({ color: node.color, emissive: node.color, emissiveIntensity: 0.25, roughness: 0.4 })
    );
    mesh.position.set(node.pos[0], node.pos[1], node.pos[2]);
    const sprite = labelSprite(node.name);
    sprite.position.y = 0.55;
    mesh.add(sprite);
    scene.add(mesh);
    byId[node.id] = node;
  });
  const linkMeshes = LINKS.map(([a, b]) => {
    const mesh = makeLink(byId[a], byId[b]);
    scene.add(mesh);
    return mesh;
  });
  const ui = document.createElement("div");
  ui.className = "row";
  ui.style.marginTop = "8px";
  let active = "none";
  let raf = 0;
  function applyFailure(name) {
    active = name;
    const fail = FAILURES[name];
    onStatus(fail.text);
    linkMeshes.forEach((mesh) => {
      const bad = fail.links.includes(mesh.userData.link);
      mesh.material.color.set(bad ? 0xff6b7a : 0x3ee0ff);
      mesh.userData.glow.material.color.set(bad ? 0xff6b7a : 0x3ee0ff);
    });
    ui.querySelectorAll("button").forEach((button) => {
      button.setAttribute("aria-pressed", button.dataset.fail === name ? "true" : "false");
    });
  }
  Object.entries({
    none: "Healthy", itsp: "ITSP down", sbca: "SBC A down", wan: "Agent WAN", crm: "CRM down", ivr: "IVR break", e911: "Stale E911"
  }).forEach(([id, label]) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "btn";
    button.dataset.fail = id;
    button.textContent = label;
    button.addEventListener("click", () => applyFailure(id));
    ui.append(button);
  });
  const list = document.createElement("ul");
  NODES.forEach((node) => {
    const item = document.createElement("li");
    item.textContent = `${node.name} is on the map.`;
    list.append(item);
  });
  root.append(wrap, ui, list);
  applyFailure("none");
  const resize = () => {
    const width = wrap.clientWidth || 640;
    const height = 420;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
  };
  resize();
  window.addEventListener("resize", resize);
  const loop = () => {
    controls.update();
    renderer.render(scene, camera);
    raf = requestAnimationFrame(loop);
  };
  loop();
  return function destroy() {
    cancelAnimationFrame(raf);
    window.removeEventListener("resize", resize);
    controls.dispose();
    renderer.dispose();
    root.innerHTML = "";
  };
}
