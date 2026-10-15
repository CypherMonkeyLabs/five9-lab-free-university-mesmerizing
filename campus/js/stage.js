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
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: "high-performance" });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
  renderer.setClearColor(colors.bg, 1);
  renderer.domElement.className = "hero-gl";
  host.insertBefore(renderer.domElement, host.firstChild);
  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(colors.bg, 10, 28);
  const camera = new THREE.PerspectiveCamera(48, 1, 0.1, 40);
  camera.position.set(0, 1.6, 7.2);
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
      opacity: lightTheme ? 0.55 : 1,
      blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending,
      depthWrite: false
    });
    mats.push(material);
    return material;
  };
  const ico = new THREE.Mesh(new THREE.IcosahedronGeometry(2.05, 1), mat(colors.a));
  const bloomIco = new THREE.Mesh(new THREE.IcosahedronGeometry(2.45, 1), new THREE.MeshBasicMaterial({
    color: colors.b,
    wireframe: true,
    transparent: true,
    opacity: lightTheme ? 0.28 : 0.45,
    blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending,
    depthWrite: false
  }));
  mats.push(bloomIco.material);
  const core = new THREE.Mesh(new THREE.IcosahedronGeometry(1.05, 0), mat(colors.c));
  scene.add(ico, bloomIco, core);
  const halo = new THREE.Sprite(glowMat(colors.b));
  halo.scale.set(8.5, 8.5, 1);
  const haloB = new THREE.Sprite(glowMat(colors.a));
  haloB.scale.set(4.2, 4.2, 1);
  scene.add(halo, haloB);
  const ringA = new THREE.Mesh(new THREE.TorusGeometry(3.1, 0.015, 8, 80), mat(colors.b));
  const ringB = new THREE.Mesh(new THREE.TorusGeometry(3.7, 0.012, 8, 80), mat(colors.c));
  ringB.rotation.x = Math.PI / 2.4;
  scene.add(ringA, ringB);
  const grid = new THREE.GridHelper(28, 28, colors.a, colors.b);
  grid.position.y = -2.2;
  scene.add(grid);
  const nodes = [];
  for (let i = 0; i < 6; i += 1) {
    const color = i % 2 ? colors.b : colors.c;
    const mesh = new THREE.Mesh(new THREE.SphereGeometry(0.16, 16, 16), new THREE.MeshBasicMaterial({ color }));
    mats.push(mesh.material);
    const sprite = new THREE.Sprite(glowMat(color));
    sprite.scale.set(1.6, 1.6, 1);
    mesh.add(sprite);
    scene.add(mesh);
    nodes.push(mesh);
  }
  const lineGeom = new THREE.BufferGeometry();
  const linePos = new Float32Array(nodes.length * 3);
  lineGeom.setAttribute("position", new THREE.BufferAttribute(linePos, 3));
  const lineMat = new THREE.LineBasicMaterial({ color: colors.a, transparent: true, opacity: 0.85 });
  mats.push(lineMat);
  scene.add(new THREE.LineLoop(lineGeom, lineMat));
  const count = 420;
  const starPos = new Float32Array(count * 3);
  for (let i = 0; i < count; i += 1) {
    starPos[i * 3] = (Math.random() - 0.5) * 24;
    starPos[i * 3 + 1] = (Math.random() - 0.5) * 12;
    starPos[i * 3 + 2] = (Math.random() - 0.5) * 18;
  }
  const starGeom = new THREE.BufferGeometry();
  starGeom.setAttribute("position", new THREE.BufferAttribute(starPos, 3));
  const stars = new THREE.Points(
    starGeom,
    new THREE.PointsMaterial({
      color: colors.c,
      size: 0.12,
      map: glowTexture(),
      transparent: true,
      opacity: 0.9,
      blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending,
      depthWrite: false
    })
  );
  mats.push(stars.material);
  scene.add(stars);
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
    ringA.rotation.x = t * 0.22;
    ringA.rotation.y = t * 0.08;
    ringB.rotation.z = t * 0.16;
    nodes.forEach((node, index) => {
      const angle = t * 0.35 + index * (Math.PI * 2 / nodes.length);
      node.position.set(Math.cos(angle) * 3.2, Math.sin(t * 0.8 + index) * 0.45, Math.sin(angle) * 3.2);
      linePos[index * 3] = node.position.x;
      linePos[index * 3 + 1] = node.position.y;
      linePos[index * 3 + 2] = node.position.z;
    });
    lineGeom.attributes.position.needsUpdate = true;
    stars.rotation.y = t * 0.02;
    const scroll = Math.min(window.scrollY / 800, 1);
    let z = 7.2 - scroll * 1.2;
    if (live.intro) {
      const u = Math.min(1, (now - live.intro.start) / live.intro.dur);
      const ease = 1 - (1 - u) ** 3;
      z = 12.5 + (7.2 - 12.5) * ease - scroll * 1.2;
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
    haloB.scale.setScalar(4.2 + Math.sin(t * 1.4) * 0.35);
    camera.position.x = (pointer.x - 0.5) * 2.2;
    camera.position.y = 1.6 + (0.5 - pointer.y) * 1.1 - scroll * 0.6;
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
