import * as THREE from "../vendor/three/three.module.js";

const cache = new Map();
let warming = null;
let colorKey = "";

function materials(colors) {
  const make = (hex) => new THREE.MeshStandardMaterial({
    color: hex,
    roughness: 0.32,
    metalness: 0.42,
    emissive: hex,
    emissiveIntensity: 0.05
  });
  return { a: make(colors.a), b: make(colors.b), c: make(colors.c) };
}

function mesh(geometry, material, x, y, z, rot) {
  const item = new THREE.Mesh(geometry, material);
  item.position.set(x, y, z);
  if (rot) item.rotation.set(rot[0], rot[1], rot[2]);
  return item;
}

function build(key, M) {
  const g = new THREE.Group();
  const add = (...items) => items.forEach((item) => g.add(item));
  if (key === "t01") {
    add(mesh(new THREE.IcosahedronGeometry(0.85, 0), M.a, 0, 0, 0));
    add(mesh(new THREE.OctahedronGeometry(0.38, 0), M.c, 0, 0, 0));
  } else if (key === "t02") {
    add(mesh(new THREE.BoxGeometry(1.3, 0.82, 0.12), M.a, 0, 0.1, 0));
    add(mesh(new THREE.BoxGeometry(0.7, 0.4, 0.08), M.b, 0, 0.12, 0.08));
    add(mesh(new THREE.CylinderGeometry(0.08, 0.12, 0.55, 10), M.c, 0, -0.55, 0));
  } else if (key === "t03") {
    const band = mesh(new THREE.TorusGeometry(0.72, 0.07, 10, 28, Math.PI), M.a, 0, 0.15, 0, [0, 0.5, Math.PI]);
    const cup = new THREE.CylinderGeometry(0.2, 0.2, 0.16, 14);
    add(band, mesh(cup, M.b, -0.62, -0.05, 0, [0, 0, Math.PI / 2]), mesh(cup, M.c, 0.62, -0.05, 0, [0, 0, Math.PI / 2]));
    add(mesh(new THREE.CylinderGeometry(0.03, 0.03, 0.62, 8), M.a, 0.42, -0.42, 0.15, [0, 0, 0.9]));
    add(mesh(new THREE.SphereGeometry(0.08, 10, 10), M.b, 0.18, -0.68, 0.2));
  } else if (key === "t04") {
    add(mesh(new THREE.BoxGeometry(1.15, 0.16, 0.8), M.a, 0, -0.28, 0));
    add(mesh(new THREE.BoxGeometry(1.05, 0.16, 0.74), M.b, 0.08, 0, 0.04));
    add(mesh(new THREE.BoxGeometry(0.95, 0.16, 0.68), M.c, -0.06, 0.28, -0.02));
  } else if (key === "t05") {
    add(mesh(new THREE.TorusGeometry(0.72, 0.1, 12, 28), M.a, 0, 0, 0));
    add(mesh(new THREE.SphereGeometry(0.18, 12, 12), M.c, 0, 0, 0.05));
    add(mesh(new THREE.BoxGeometry(0.16, 0.42, 0.12), M.b, 0.55, 0.45, 0));
  } else if (key === "t06") {
    add(mesh(new THREE.TorusGeometry(0.62, 0.09, 10, 24), M.a, 0, 0, 0, [Math.PI / 2, 0, 0]));
    add(mesh(new THREE.TorusGeometry(0.62, 0.09, 10, 24), M.b, 0, 0, 0, [0, 0, Math.PI / 3]));
  } else if (key === "t07") {
    add(mesh(new THREE.CylinderGeometry(0.08, 0.12, 0.9, 8), M.c, 0, -0.35, 0));
    add(mesh(new THREE.ConeGeometry(0.55, 0.7, 8), M.a, 0, 0.25, 0));
    add(mesh(new THREE.ConeGeometry(0.36, 0.5, 8), M.b, 0, 0.62, 0));
    add(mesh(new THREE.SphereGeometry(0.1, 8, 8), M.c, 0.28, 0.15, 0.2));
  } else if (key === "t08") {
    [ -0.66, -0.22, 0.22, 0.66 ].forEach((x, i) => {
      const mat = i % 2 ? M.b : M.a;
      add(mesh(new THREE.SphereGeometry(0.22 - i * 0.02, 12, 12), mat, x, 0, 0));
    });
  } else if (key === "t09") {
    add(mesh(new THREE.BoxGeometry(1.25, 0.82, 0.1), M.a, 0, 0.15, 0));
    add(mesh(new THREE.BoxGeometry(0.95, 0.55, 0.06), M.b, 0, 0.16, 0.06));
    add(mesh(new THREE.CylinderGeometry(0.06, 0.08, 0.45, 8), M.c, 0, -0.48, 0));
    add(mesh(new THREE.BoxGeometry(0.55, 0.06, 0.28), M.c, 0, -0.72, 0));
  } else if (key === "t10") {
    add(mesh(new THREE.TorusGeometry(0.72, 0.08, 10, 28), M.a, 0, 0, 0));
    add(mesh(new THREE.BoxGeometry(0.06, 0.55, 0.06), M.b, 0, 0.18, 0.05));
    add(mesh(new THREE.BoxGeometry(0.42, 0.06, 0.06), M.c, 0.12, 0, 0.06));
    add(mesh(new THREE.SphereGeometry(0.08, 8, 8), M.b, 0, 0, 0.08));
  } else if (key === "t11") {
    add(mesh(new THREE.SphereGeometry(0.48, 16, 16), M.a, 0, 0.05, 0));
    add(mesh(new THREE.TorusGeometry(0.72, 0.05, 8, 24), M.c, 0, 0.05, 0, [Math.PI / 2, 0, 0]));
    add(mesh(new THREE.ConeGeometry(0.16, 0.36, 8), M.b, 0.55, -0.35, 0, [0, 0, -0.6]));
  } else if (key === "t12") {
    add(mesh(new THREE.TorusGeometry(0.34, 0.08, 8, 18), M.a, -0.38, 0, 0));
    add(mesh(new THREE.TorusGeometry(0.34, 0.08, 8, 18), M.b, 0.38, 0, 0));
    add(mesh(new THREE.TorusGeometry(0.34, 0.08, 8, 18), M.c, 0, 0.42, 0));
  } else if (key === "t13") {
    add(mesh(new THREE.CylinderGeometry(0.08, 0.16, 1.15, 8), M.a, 0, -0.1, 0));
    add(mesh(new THREE.SphereGeometry(0.22, 12, 12), M.b, 0, 0.62, 0));
    add(mesh(new THREE.TorusGeometry(0.38, 0.03, 6, 16), M.c, 0, 0.2, 0, [Math.PI / 2, 0, 0]));
  } else if (key === "t14") {
    add(mesh(new THREE.OctahedronGeometry(0.42, 0), M.a, 0, 0, 0));
    [[0.7, 0.35], [-0.7, 0.2], [0.2, -0.7], [-0.25, 0.7]].forEach(([x, y], i) => {
      add(mesh(new THREE.SphereGeometry(0.14, 10, 10), i % 2 ? M.b : M.c, x, y, 0));
    });
  } else if (key === "t15") {
    add(mesh(new THREE.BoxGeometry(0.38, 0.7, 0.38), M.a, -0.7, -0.1, 0));
    add(mesh(new THREE.BoxGeometry(0.38, 0.7, 0.38), M.b, 0.7, -0.1, 0));
    add(mesh(new THREE.BoxGeometry(1.15, 0.1, 0.28), M.c, 0, 0.22, 0));
  } else if (key === "t16") {
    add(mesh(new THREE.ConeGeometry(0.7, 1.15, 4), M.a, 0, 0, 0, [0, Math.PI / 4, 0]));
    add(mesh(new THREE.SphereGeometry(0.16, 10, 10), M.c, 0, 0.12, 0.2));
  } else if (key === "t17") {
    add(mesh(new THREE.SphereGeometry(0.72, 18, 14), M.a, 0, 0, 0));
    add(mesh(new THREE.TorusGeometry(0.74, 0.03, 6, 24), M.b, 0, 0, 0, [Math.PI / 2.2, 0, 0]));
    add(mesh(new THREE.TorusGeometry(0.74, 0.03, 6, 24), M.c, 0, 0, 0, [0.4, 0.6, 0]));
  } else if (key === "t19") {
    add(mesh(new THREE.ConeGeometry(0.72, 0.9, 4), M.a, 0, -0.15, 0, [Math.PI, 0, 0]));
    [-0.28, 0, 0.28].forEach((x, i) => add(mesh(new THREE.SphereGeometry(0.16, 10, 10), i === 1 ? M.c : M.b, x, 0.42, 0)));
  } else if (key === "t20") {
    add(mesh(new THREE.BoxGeometry(1.05, 0.9, 0.12), M.a, 0, 0, 0));
    add(mesh(new THREE.BoxGeometry(1.05, 0.16, 0.14), M.c, 0, 0.37, 0.02));
    [[-0.28, 0.05], [0, 0.05], [0.28, 0.05], [-0.28, -0.28], [0, -0.28], [0.28, -0.28]].forEach(([x, y]) => {
      add(mesh(new THREE.BoxGeometry(0.16, 0.12, 0.08), M.b, x, y, 0.08));
    });
  } else if (key === "t21") {
    add(mesh(new THREE.TorusGeometry(0.46, 0.08, 10, 20), M.a, -0.34, 0.05, 0, [0, Math.PI / 2, 0]));
    add(mesh(new THREE.TorusGeometry(0.46, 0.08, 10, 20), M.b, 0.34, 0.05, 0, [0, Math.PI / 2, 0]));
    add(mesh(new THREE.BoxGeometry(0.7, 0.08, 0.08), M.c, 0, 0.42, 0));
    add(mesh(new THREE.SphereGeometry(0.12, 10, 10), M.c, 0, -0.15, 0.1));
  } else if (key === "t22") {
    add(mesh(new THREE.BoxGeometry(0.55, 0.42, 0.2), M.a, -0.38, 0, 0));
    add(mesh(new THREE.BoxGeometry(0.55, 0.42, 0.2), M.b, 0.38, 0, 0));
    add(mesh(new THREE.CylinderGeometry(0.05, 0.05, 0.36, 8), M.c, 0, 0, 0, [0, 0, Math.PI / 2]));
  } else if (key === "t23") {
    [[0, 0.55], [-0.55, -0.15], [0.55, -0.15], [0, -0.55]].forEach(([x, y], i) => {
      add(mesh(new THREE.SphereGeometry(0.18, 12, 12), i % 2 ? M.b : M.a, x, y, 0));
    });
    add(mesh(new THREE.OctahedronGeometry(0.22, 0), M.c, 0, 0, 0.05));
  } else {
    add(mesh(new THREE.TorusGeometry(0.55, 0.12, 10, 24), M.c, 0, 0, 0));
    add(mesh(new THREE.OctahedronGeometry(0.32, 0), M.b, 0, 0, 0.05));
  }
  return g;
}

function readColors() {
  const style = getComputedStyle(document.documentElement);
  const hex = (name, fallback) => {
    const raw = style.getPropertyValue(name).trim();
    const body = raw.startsWith("#") ? raw.slice(1, 7) : "";
    return /^[0-9a-fA-F]{6}$/.test(body) ? parseInt(body, 16) : fallback;
  };
  return {
    a: hex("--scene-a", 0x7cf7ff),
    b: hex("--scene-b", 0xff4fd8),
    c: hex("--scene-c", 0xffe56a)
  };
}

function paintImages() {
  document.querySelectorAll("[data-glyph]").forEach((img) => {
    const url = cache.get(img.dataset.glyph);
    if (url && img.getAttribute("src") !== url) img.src = url;
  });
}

export function glyphImg(key) {
  const safe = cache.has(key) ? key : (cache.has("t01") ? "t01" : key);
  const src = cache.get(safe) || "";
  return `<img class="glyph" data-glyph="${safe}" alt="" width="168" height="168"${src ? ` src="${src}"` : ""}>`;
}

export function warmGlyphs() {
  const colors = readColors();
  const nextKey = `${colors.a}-${colors.b}-${colors.c}`;
  if (cache.size && nextKey === colorKey) {
    paintImages();
    return Promise.resolve();
  }
  if (warming) return warming.then(paintImages);
  colorKey = nextKey;
  const keys = Array.from({ length: 23 }, (_, i) => `t${String(i + 1).padStart(2, "0")}`);
  warming = (async () => {
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, preserveDrawingBuffer: true });
    renderer.setPixelRatio(1);
    renderer.setSize(256, 256, false);
    renderer.setClearColor(0x000000, 0);
    const camera = new THREE.PerspectiveCamera(32, 1, 0.1, 20);
    camera.position.set(1.7, 1.15, 3.15);
    camera.lookAt(0, 0, 0);
    const M = materials(colors);
    keys.forEach((key) => {
      const scene = new THREE.Scene();
      scene.add(new THREE.AmbientLight(0xffffff, 0.9));
      const dir = new THREE.DirectionalLight(0xffffff, 1.35);
      dir.position.set(3, 4, 5);
      scene.add(dir);
      scene.add(new THREE.PointLight(colors.b, 6, 8));
      scene.add(build(key, M));
      renderer.render(scene, camera);
      cache.set(key, renderer.domElement.toDataURL("image/png"));
    });
    renderer.dispose();
    renderer.forceContextLoss();
    paintImages();
  })().catch(() => {
    keys.forEach((key, index) => {
      if (cache.has(key)) return;
      const canvas = document.createElement("canvas");
      canvas.width = 128;
      canvas.height = 128;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = ["#e879f9", "#22d3ee", "#fbbf24", "#39ff14"][index % 4];
      ctx.beginPath();
      ctx.arc(64, 54, 28 + (index % 5) * 4, 0, Math.PI * 2);
      ctx.fill();
      cache.set(key, canvas.toDataURL("image/png"));
    });
    paintImages();
  }).finally(() => { warming = null; });
  return warming;
}

export function glyphKey(href) {
  const id = String(href).match(/t\d{2}/);
  if (id) return id[0];
  if (String(href).includes("ivr")) return "t07";
  if (String(href).includes("pacing")) return "t05";
  if (String(href).includes("topology")) return "t17";
  if (String(href).includes("boss")) return "t16";
  if (String(href).includes("interview")) return "t02";
  if (String(href).includes("certs") || String(href).includes("progress")) return "t18";
  if (String(href).includes("ecosystem")) return "t17";
  return "t01";
}
