import * as THREE from "three";

let live = null;

function hexToInt(hex, fallback) {
  const raw = String(hex || "").trim();
  const body = raw.startsWith("#") ? raw.slice(1) : "";
  if (/^[0-9a-fA-F]{3}$/.test(body)) {
    return parseInt(body.split("").map((ch) => ch + ch).join(""), 16);
  }
  if (/^[0-9a-fA-F]{6}/.test(body)) return parseInt(body.slice(0, 6), 16);
  return fallback;
}

function sceneColors() {
  const style = getComputedStyle(document.documentElement);
  return {
    a: hexToInt(style.getPropertyValue("--scene-a"), 0x7cf7ff),
    b: hexToInt(style.getPropertyValue("--scene-b"), 0xff4fd8),
    c: hexToInt(style.getPropertyValue("--scene-c"), 0xffe56a),
    bg: hexToInt(style.getPropertyValue("--cc-bg"), 0x12081f)
  };
}

function glowTexture() {
  const canvas = document.createElement("canvas");
  canvas.width = 64;
  canvas.height = 64;
  const g = canvas.getContext("2d");
  const grad = g.createRadialGradient(32, 32, 0, 32, 32, 32);
  grad.addColorStop(0, "rgba(255,255,255,0.95)");
  grad.addColorStop(0.35, "rgba(255,255,255,0.35)");
  grad.addColorStop(1, "rgba(255,255,255,0)");
  g.fillStyle = grad;
  g.fillRect(0, 0, 64, 64);
  return new THREE.CanvasTexture(canvas);
}

function labelTexture(text, ink) {
  const canvas = document.createElement("canvas");
  canvas.width = 512;
  canvas.height = 128;
  const g = canvas.getContext("2d");
  g.fillStyle = "rgba(5, 1, 16, 0.82)";
  g.strokeStyle = ink;
  g.lineWidth = 4;
  g.beginPath();
  g.roundRect(16, 24, 480, 80, 28);
  g.fill();
  g.stroke();
  g.font = "700 54px sans-serif";
  g.textAlign = "center";
  g.textBaseline = "middle";
  g.fillStyle = ink;
  g.fillText(text, 256, 64);
  const texture = new THREE.CanvasTexture(canvas);
  texture.needsUpdate = true;
  return texture;
}

function showFlat(host, on) {
  const flat = host.querySelector("#hero-flat");
  if (flat) flat.hidden = !on;
}

export function stopHero() {
  if (!live) return;
  cancelAnimationFrame(live.clock.raf);
  if (live.fly) live.fly.resolve();
  live.host.removeEventListener("pointermove", live.onMove);
  window.removeEventListener("resize", live.onResize);
  live.renderer.dispose();
  live.renderer.forceContextLoss();
  live.canvas.remove();
  live = null;
}

export function flyThrough() {
  if (!live || document.documentElement.dataset.motion === "reduce") return Promise.resolve();
  return new Promise((resolve) => {
    live.fly = { from: live.camera.position.z, to: 1.15, start: performance.now(), dur: 720, resolve };
  });
}

export function recolorHero() {
  if (!live) return;
  const colors = sceneColors();
  live.renderer.setClearColor(colors.bg, 1);
  live.mats.forEach((mat, index) => {
    const color = index % 3 === 0 ? colors.a : index % 3 === 1 ? colors.b : colors.c;
    mat.color.setHex(color);
  });
}

export function mountHero(host) {
  if (!host) return;
  const reduced = document.documentElement.dataset.motion === "reduce";
  const probe = document.createElement("canvas");
  const gl = probe.getContext("webgl") || probe.getContext("experimental-webgl");
  if (reduced || !gl) {
    stopHero();
    showFlat(host, true);
    return;
  }
  const theme = document.documentElement.dataset.theme || "";
  if (live && live.host === host && live.theme === theme) {
    recolorHero();
    showFlat(host, false);
    return;
  }
  stopHero();
  showFlat(host, false);
  const colors = sceneColors();
  if (theme === "neon") colors.bg = 0x05010c;
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: "high-performance" });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
  renderer.setClearColor(colors.bg, 1);
  renderer.domElement.className = "hero-gl";
  host.insertBefore(renderer.domElement, host.firstChild);
  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(colors.bg, 14, 38);
  const camera = new THREE.PerspectiveCamera(58, 1, 0.1, 80);
  camera.position.set(0, 0.9, 5.6);
  const mats = [];
  const mat = (color) => {
    const material = new THREE.MeshBasicMaterial({ color, wireframe: true });
    mats.push(material);
    return material;
  };
  const lightTheme = theme === "light" || theme === "paper" || theme === "aurora" || theme === "holographic";
  const glowMat = (color) => {
    const material = new THREE.SpriteMaterial({
      map: glowTexture(),
      color,
      transparent: true,
      opacity: lightTheme ? 0.45 : 0.55,
      blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending,
      depthWrite: false
    });
    mats.push(material);
    return material;
  };
  const ico = new THREE.Mesh(new THREE.IcosahedronGeometry(1.7, 1), mat(colors.a));
  const bloomIco = new THREE.Mesh(new THREE.IcosahedronGeometry(2.15, 1), new THREE.MeshBasicMaterial({
    color: colors.b,
    wireframe: true,
    transparent: true,
    opacity: lightTheme ? 0.28 : 0.55,
    blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending,
    depthWrite: false
  }));
  mats.push(bloomIco.material);
  const core = new THREE.Mesh(new THREE.OctahedronGeometry(0.72, 0), mat(colors.c));
  const knot = new THREE.Mesh(new THREE.TorusKnotGeometry(0.38, 0.08, 64, 8), mat(colors.b));
  scene.add(ico, bloomIco, core, knot);
  const halo = new THREE.Sprite(glowMat(colors.b));
  halo.scale.set(3.4, 3.4, 1);
  halo.material.opacity = lightTheme ? 0.35 : 0.22;
  const haloB = new THREE.Sprite(glowMat(colors.a));
  haloB.scale.set(2.1, 2.1, 1);
  haloB.material.opacity = lightTheme ? 0.4 : 0.28;
  const haloC = new THREE.Sprite(glowMat(colors.c));
  haloC.scale.set(1.3, 1.3, 1);
  haloC.material.opacity = 0.35;
  scene.add(halo, haloB, haloC);
  const shaft = new THREE.Mesh(new THREE.ConeGeometry(1.15, 7.5, 28, 1, true), new THREE.MeshBasicMaterial({
    color: colors.b,
    transparent: true,
    opacity: lightTheme ? 0.04 : 0.07,
    side: THREE.DoubleSide,
    blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending,
    depthWrite: false
  }));
  shaft.position.y = 0.4;
  mats.push(shaft.material);
  const shaftB = new THREE.Mesh(new THREE.ConeGeometry(0.55, 6.2, 20, 1, true), new THREE.MeshBasicMaterial({
    color: colors.a,
    transparent: true,
    opacity: lightTheme ? 0.05 : 0.1,
    side: THREE.DoubleSide,
    blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending,
    depthWrite: false
  }));
  shaftB.position.y = 0.2;
  mats.push(shaftB.material);
  scene.add(shaft, shaftB);
  const ringA = new THREE.Mesh(new THREE.TorusGeometry(3.15, 0.018, 8, 96), mat(colors.b));
  const ringB = new THREE.Mesh(new THREE.TorusGeometry(3.85, 0.012, 8, 96), mat(colors.c));
  ringB.rotation.x = Math.PI / 2.4;
  scene.add(ringA, ringB);
  const grid = new THREE.GridHelper(34, 34, colors.a, colors.b);
  grid.position.y = -2.35;
  const gridMats = Array.isArray(grid.material) ? grid.material : [grid.material];
  gridMats.forEach((material) => {
    material.transparent = true;
    material.opacity = 0.28;
  });
  scene.add(grid);
  const names = ["PSTN", "SBC", "IVR", "ACD", "Agent", "CRM", "WEM"];
  const ink = lightTheme ? "#241433" : "#e8fbff";
  const nodes = names.map((name, index) => {
    const color = index % 3 === 0 ? colors.a : index % 3 === 1 ? colors.b : colors.c;
    const mesh = new THREE.Mesh(new THREE.OctahedronGeometry(0.16, 0), new THREE.MeshBasicMaterial({ color }));
    mats.push(mesh.material);
    const sprite = new THREE.Sprite(glowMat(color));
    sprite.scale.set(1.5, 1.5, 1);
    mesh.add(sprite);
    const labelMat = new THREE.SpriteMaterial({ map: labelTexture(name, ink), transparent: true, depthWrite: false });
    mats.push(labelMat);
    const label = new THREE.Sprite(labelMat);
    label.position.y = 0.62;
    label.scale.set(2.4, 0.6, 1);
    mesh.add(label);
    scene.add(mesh);
    return mesh;
  });
  const lineGeom = new THREE.BufferGeometry();
  const linePos = new Float32Array(nodes.length * 3);
  lineGeom.setAttribute("position", new THREE.BufferAttribute(linePos, 3));
  const lineMat = new THREE.LineBasicMaterial({
    color: colors.a,
    transparent: true,
    opacity: 0.9,
    blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending
  });
  mats.push(lineMat);
  scene.add(new THREE.LineLoop(lineGeom, lineMat));
  const TRAIL = 28;
  const trails = nodes.map(() => {
    const geom = new THREE.BufferGeometry();
    const pos = new Float32Array(TRAIL * 3);
    const col = new Float32Array(TRAIL * 3);
    geom.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    geom.setAttribute("color", new THREE.BufferAttribute(col, 3));
    const material = new THREE.LineBasicMaterial({
      vertexColors: true,
      transparent: true,
      blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending
    });
    mats.push(material);
    scene.add(new THREE.Line(geom, material));
    return { pos, col, geom };
  });
  const packet = new THREE.Sprite(glowMat(0xffffff));
  packet.scale.set(1.15, 1.15, 1);
  const packetCore = new THREE.Mesh(new THREE.SphereGeometry(0.07, 12, 12), new THREE.MeshBasicMaterial({ color: 0xffffff }));
  mats.push(packetCore.material);
  scene.add(packet, packetCore);
  const dustCount = 2400;
  const nearCount = 700;
  const makeDust = (count, spread, size, color) => {
    const pos = new Float32Array(count * 3);
    for (let i = 0; i < count; i += 1) {
      pos[i * 3] = (Math.random() - 0.5) * spread;
      pos[i * 3 + 1] = (Math.random() - 0.5) * spread * 0.55;
      pos[i * 3 + 2] = (Math.random() - 0.5) * spread;
    }
    const geom = new THREE.BufferGeometry();
    geom.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    const material = new THREE.PointsMaterial({
      color,
      size,
      map: glowTexture(),
      transparent: true,
      opacity: 0.55,
      sizeAttenuation: true,
      blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending,
      depthWrite: false
    });
    mats.push(material);
    const points = new THREE.Points(geom, material);
    scene.add(points);
    return points;
  };
  const stars = makeDust(dustCount, 36, 0.07, colors.a);
  const dust = makeDust(nearCount, 18, 0.16, colors.b);
  const pointer = { x: 0.5, y: 0.4 };
  const onMove = (event) => {
    const box = host.getBoundingClientRect();
    pointer.x = (event.clientX - box.left) / Math.max(box.width, 1);
    pointer.y = (event.clientY - box.top) / Math.max(box.height, 1);
  };
  host.addEventListener("pointermove", onMove);
  const fit = () => {
    const box = host.getBoundingClientRect();
    const w = Math.max(1, box.width);
    const h = Math.max(1, box.height);
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  };
  fit();
  const onResize = () => fit();
  window.addEventListener("resize", onResize);
  const clock = { raf: 0 };
  const tick = (now) => {
    if (!live || live.renderer !== renderer) return;
    const t = now * 0.001;
    ico.rotation.y = t * 0.18;
    ico.rotation.x = Math.sin(t * 0.3) * 0.2;
    core.rotation.y = -t * 0.32;
    core.rotation.z = t * 0.12;
    knot.rotation.y = t * 0.6;
    knot.position.set(Math.cos(t * 0.7) * 1.15, Math.sin(t * 0.9) * 0.35, Math.sin(t * 0.7) * 1.15);
    ringA.rotation.x = t * 0.22;
    ringA.rotation.y = t * 0.08;
    ringB.rotation.z = t * 0.16;
    shaft.rotation.y = t * 0.15;
    shaftB.rotation.y = -t * 0.22;
    nodes.forEach((node, index) => {
      const angle = t * 0.32 + index * (Math.PI * 2 / nodes.length);
      const radius = 3.35 + (index % 2) * 0.45;
      node.position.set(Math.cos(angle) * radius, Math.sin(t * 0.8 + index) * 0.7, Math.sin(angle) * radius);
      linePos[index * 3] = node.position.x;
      linePos[index * 3 + 1] = node.position.y;
      linePos[index * 3 + 2] = node.position.z;
      const trail = trails[index];
      if (!live.seeded) {
        for (let step = 0; step < TRAIL; step += 1) {
          trail.pos[step * 3] = node.position.x;
          trail.pos[step * 3 + 1] = node.position.y;
          trail.pos[step * 3 + 2] = node.position.z;
        }
      } else trail.pos.copyWithin(3, 0);
      trail.pos[0] = node.position.x;
      trail.pos[1] = node.position.y;
      trail.pos[2] = node.position.z;
      for (let step = 0; step < TRAIL; step += 1) {
        const fade = 1 - step / TRAIL;
        const tint = index % 2 ? colors.b : colors.a;
        trail.col[step * 3] = ((tint >> 16) & 255) / 255 * fade;
        trail.col[step * 3 + 1] = ((tint >> 8) & 255) / 255 * fade;
        trail.col[step * 3 + 2] = (tint & 255) / 255 * fade;
      }
      trail.geom.attributes.position.needsUpdate = true;
      trail.geom.attributes.color.needsUpdate = true;
    });
    live.seeded = true;
    lineGeom.attributes.position.needsUpdate = true;
    const hop = (t * 0.45) % nodes.length;
    const from = nodes[Math.floor(hop)];
    const to = nodes[(Math.floor(hop) + 1) % nodes.length];
    const u = hop - Math.floor(hop);
    packet.position.lerpVectors(from.position, to.position, u);
    packetCore.position.copy(packet.position);
    stars.rotation.y = t * 0.02;
    dust.rotation.y = -t * 0.04;
    dust.rotation.x = Math.sin(t * 0.1) * 0.05;
    const scroll = Math.min(window.scrollY / 800, 1);
    let z = 5.6 - scroll * 0.8;
    if (live.intro) {
      const u = Math.min(1, (now - live.intro.start) / live.intro.dur);
      const ease = 1 - (1 - u) ** 3;
      z = 8.4 + (5.6 - 8.4) * ease - scroll * 0.8;
      if (u >= 1) live.intro = null;
    }
    if (live.fly) {
      const u = Math.min(1, (now - live.fly.start) / live.fly.dur);
      z = live.fly.from + (live.fly.to - live.fly.from) * u * u;
      if (u >= 1) {
        const done = live.fly.resolve;
        live.fly = null;
        done();
      }
    }
    bloomIco.rotation.y = -t * 0.12;
    haloB.scale.setScalar(2.1 + Math.sin(t * 1.4) * 0.18);
    camera.position.x = (pointer.x - 0.5) * 2.2;
    camera.position.y = 0.85 + (0.5 - pointer.y) * 0.8 - scroll * 0.4;
    camera.position.z = z;
    camera.lookAt(0, 0, 0);
    renderer.render(scene, camera);
    if (live && live.renderer === renderer) live.clock.raf = requestAnimationFrame(tick);
  };
  live = {
    host,
    renderer,
    camera,
    canvas: renderer.domElement,
    mats,
    onMove,
    onResize,
    clock,
    theme,
    intro: document.documentElement.dataset.motion === "reduce" ? null : { start: performance.now(), dur: 1300 },
    fly: null
  };
  live.clock.raf = requestAnimationFrame(tick);
}

export function heroIsLive() {
  return !!live;
}
