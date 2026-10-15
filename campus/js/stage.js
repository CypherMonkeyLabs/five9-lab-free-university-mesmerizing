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

function paintQueue(host, count) {
  const meter = host.querySelector("#queue-count");
  const bars = host.querySelectorAll(".qm-bars i");
  if (meter) meter.textContent = String(count);
  const lit = Math.max(1, Math.min(bars.length, Math.round(count / 2)));
  bars.forEach((bar, index) => bar.classList.toggle("on", index < lit));
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
    paintQueue(host, 6);
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
  scene.fog = new THREE.Fog(colors.bg, 16, 42);
  const camera = new THREE.PerspectiveCamera(50, 1, 0.1, 80);
  camera.position.set(0, 1.05, 7.6);
  const mats = [];
  const mat = (color) => {
    const material = new THREE.MeshBasicMaterial({ color });
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
  const wash = new THREE.Sprite(glowMat(colors.b));
  wash.scale.set(7.2, 3.4, 1);
  wash.material.opacity = lightTheme ? 0.18 : 0.12;
  wash.position.y = 0.15;
  scene.add(wash);
  const shaft = new THREE.Mesh(new THREE.ConeGeometry(3.2, 9, 24, 1, true), new THREE.MeshBasicMaterial({
    color: colors.a,
    transparent: true,
    opacity: lightTheme ? 0.03 : 0.05,
    side: THREE.DoubleSide,
    blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending,
    depthWrite: false
  }));
  shaft.position.set(0.2, 0.1, -1.4);
  mats.push(shaft.material);
  scene.add(shaft);
  const grid = new THREE.GridHelper(30, 24, colors.a, colors.b);
  grid.position.y = -1.85;
  const gridMats = Array.isArray(grid.material) ? grid.material : [grid.material];
  gridMats.forEach((material) => {
    material.transparent = true;
    material.opacity = 0.2;
  });
  scene.add(grid);
  const names = ["PSTN", "SBC", "IVR", "ACD", "Agent", "CRM", "WEM"];
  const anchors = [
    new THREE.Vector3(-3.55, 0.45, 0.3),
    new THREE.Vector3(-2.1, 1.15, -0.5),
    new THREE.Vector3(-0.4, 0.25, 0.45),
    new THREE.Vector3(1.2, 1.05, -0.15),
    new THREE.Vector3(2.95, 0.2, 0.45),
    new THREE.Vector3(1.25, -0.95, 0.8),
    new THREE.Vector3(3.05, -0.9, -0.45)
  ];
  const ink = lightTheme ? "#241433" : "#e8fbff";
  const palette = [colors.a, colors.b, colors.c, colors.a, colors.b, colors.c, colors.a];
  const buildNode = (name, color) => {
    const group = new THREE.Group();
    if (name === "PSTN") {
      group.add(new THREE.Mesh(new THREE.CylinderGeometry(0.16, 0.26, 0.95, 8), mat(color)));
      const cap = new THREE.Mesh(new THREE.TorusGeometry(0.32, 0.028, 6, 28), mat(color));
      cap.rotation.x = Math.PI / 2;
      cap.position.y = 0.5;
      group.add(cap);
    } else if (name === "SBC") {
      group.add(new THREE.Mesh(new THREE.BoxGeometry(0.82, 0.46, 0.46), mat(color)));
    } else if (name === "IVR") {
      group.add(new THREE.Mesh(new THREE.CylinderGeometry(0.045, 0.045, 0.8, 6), mat(color)));
      [[-0.34, 0.3, 0], [0.34, 0.3, 0], [0, 0.55, 0.08]].forEach(([x, y, z]) => {
        const bud = new THREE.Mesh(new THREE.SphereGeometry(0.12, 12, 8), mat(color));
        bud.position.set(x, y, z);
        group.add(bud);
      });
    } else if (name === "ACD") {
      for (let i = 0; i < 4; i += 1) {
        const seat = new THREE.Mesh(new THREE.BoxGeometry(0.22, 0.18, 0.24), mat(color));
        seat.position.set((i - 1.5) * 0.28, 0, 0);
        group.add(seat);
      }
    } else if (name === "Agent") {
      const band = new THREE.Mesh(new THREE.TorusGeometry(0.36, 0.045, 8, 20, Math.PI), mat(color));
      band.rotation.z = Math.PI;
      const ear = new THREE.Mesh(new THREE.SphereGeometry(0.11, 10, 8), mat(color));
      ear.position.set(0.36, 0, 0);
      const mic = new THREE.Mesh(new THREE.BoxGeometry(0.045, 0.32, 0.045), mat(color));
      mic.position.set(0.24, -0.24, 0.08);
      group.add(band, ear, mic);
    } else if (name === "CRM") {
      const ringA = new THREE.Mesh(new THREE.TorusGeometry(0.36, 0.04, 8, 28), mat(color));
      const ringB = new THREE.Mesh(new THREE.TorusGeometry(0.36, 0.04, 8, 28), mat(color));
      ringB.rotation.x = Math.PI / 2;
      group.add(ringA, ringB);
    } else if (name === "WEM") {
      group.add(new THREE.Mesh(new THREE.TorusGeometry(0.38, 0.04, 8, 32), mat(color)));
      const hand = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.32, 0.04), mat(color));
      hand.position.y = 0.08;
      group.add(hand);
      group.userData.hand = hand;
    } else {
      group.add(new THREE.Mesh(new THREE.OctahedronGeometry(0.28, 0), mat(color)));
    }
    const sprite = new THREE.Sprite(glowMat(color));
    sprite.scale.set(1.55, 1.55, 1);
    group.add(sprite);
    const labelMat = new THREE.SpriteMaterial({ map: labelTexture(name, ink), transparent: true, depthWrite: false });
    mats.push(labelMat);
    const label = new THREE.Sprite(labelMat);
    label.position.y = 1.02;
    label.scale.set(1.45, 0.36, 1);
    group.add(label);
    scene.add(group);
    return group;
  };
  const nodes = names.map((name, index) => buildNode(name, palette[index]));
  const flowSpecs = [
    { indices: [0, 1, 2, 3, 4], lift: 0.32, steps: 72, color: colors.a },
    { indices: [3, 5], lift: 0.24, steps: 28, color: colors.b },
    { indices: [4, 6], lift: 0.2, steps: 28, color: colors.c }
  ];
  const flows = flowSpecs.map((spec) => {
    const pos = new Float32Array((spec.steps + 1) * 3);
    const geom = new THREE.BufferGeometry();
    geom.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    const material = new THREE.LineDashedMaterial({
      color: spec.color,
      transparent: true,
      opacity: 0.95,
      dashSize: 0.18,
      gapSize: 0.1,
      blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending
    });
    mats.push(material);
    const line = new THREE.Line(geom, material);
    scene.add(line);
    return { ...spec, pos, geom, line };
  });
  const beads = Array.from({ length: 8 }, (_, index) => {
    const bead = new THREE.Sprite(glowMat(index % 2 ? colors.b : colors.a));
    bead.scale.set(0.42, 0.42, 1);
    scene.add(bead);
    return bead;
  });
  const packet = new THREE.Sprite(glowMat(0xffffff));
  packet.scale.set(0.95, 0.95, 1);
  const packetCore = new THREE.Mesh(new THREE.SphereGeometry(0.09, 12, 12), new THREE.MeshBasicMaterial({ color: 0xffffff }));
  mats.push(packetCore.material);
  scene.add(packet, packetCore);
  const scratch = new THREE.Vector3();
  const placeOn = (indices, lift, amount, target) => {
    const span = indices.length - 1;
    const x = ((amount % 1) + 1) % 1 * span;
    const i = Math.min(span - 1, Math.floor(x));
    const f = x - i;
    const from = nodes[indices[i]].position;
    const to = nodes[indices[i + 1]].position;
    target.set(
      from.x + (to.x - from.x) * f,
      from.y + (to.y - from.y) * f + Math.sin(f * Math.PI) * lift,
      from.z + (to.z - from.z) * f
    );
    return target;
  };
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
      opacity: 0.5,
      sizeAttenuation: true,
      blending: lightTheme ? THREE.NormalBlending : THREE.AdditiveBlending,
      depthWrite: false
    });
    mats.push(material);
    const points = new THREE.Points(geom, material);
    scene.add(points);
    return points;
  };
  const stars = makeDust(dustCount, 36, 0.065, colors.a);
  const dust = makeDust(nearCount, 18, 0.14, colors.b);
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
    nodes.forEach((node, index) => {
      const anchor = anchors[index];
      node.position.set(anchor.x, anchor.y + Math.sin(t * 0.9 + index) * 0.06, anchor.z);
      node.rotation.y = Math.sin(t * 0.4 + index) * 0.18;
    });
    const hand = nodes[6].userData.hand;
    if (hand) hand.rotation.z = t * 0.8;
    flows.forEach((flow) => {
      const steps = flow.steps;
      for (let step = 0; step <= steps; step += 1) {
        placeOn(flow.indices, flow.lift, step / steps, scratch);
        flow.pos[step * 3] = scratch.x;
        flow.pos[step * 3 + 1] = scratch.y;
        flow.pos[step * 3 + 2] = scratch.z;
      }
      flow.geom.attributes.position.needsUpdate = true;
      flow.line.computeLineDistances();
      flow.line.material.dashOffset = -t * 0.65;
    });
    beads.forEach((bead, index) => {
      placeOn(flows[0].indices, flows[0].lift, (t * 0.16 + index / beads.length) % 1, bead.position);
    });
    placeOn(flows[0].indices, flows[0].lift, (t * 0.16) % 1, packet.position);
    packetCore.position.copy(packet.position);
    const queue = 4 + Math.round((Math.sin(t * 0.85) + 1) * 4);
    if (live.qtick !== Math.floor(t * 2)) {
      live.qtick = Math.floor(t * 2);
      paintQueue(host, queue);
    }
    shaft.rotation.y = t * 0.08;
    stars.rotation.y = t * 0.015;
    dust.rotation.y = -t * 0.03;
    const scroll = Math.min(window.scrollY / 800, 1);
    let z = 7.6 - scroll * 0.8;
    if (live.intro) {
      const introU = Math.min(1, (now - live.intro.start) / live.intro.dur);
      const ease = 1 - (1 - introU) ** 3;
      z = 10.2 + (7.6 - 10.2) * ease - scroll * 0.8;
      if (introU >= 1) live.intro = null;
    }
    if (live.fly) {
      const flyU = Math.min(1, (now - live.fly.start) / live.fly.dur);
      z = live.fly.from + (live.fly.to - live.fly.from) * flyU * flyU;
      if (flyU >= 1) {
        const done = live.fly.resolve;
        live.fly = null;
        done();
      }
    }
    camera.position.x = (pointer.x - 0.5) * 1.4;
    camera.position.y = 1.05 + (0.5 - pointer.y) * 0.6 - scroll * 0.3;
    camera.position.z = z;
    camera.lookAt(0.15, 0.15, 0);
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
    qtick: -1,
    intro: document.documentElement.dataset.motion === "reduce" ? null : { start: performance.now(), dur: 1300 },
    fly: null
  };
  live.clock.raf = requestAnimationFrame(tick);
}

export function heroIsLive() {
  return !!live;
}
