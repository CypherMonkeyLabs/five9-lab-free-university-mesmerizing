// Offline motion. anime.js, rough.js, canvas-confetti, three.js, and markmap
// are vendored. Nothing here loads a CDN. GSAP is not used.

import { cappedPixelRatio } from "./pixel.js";

let stageStop = 0;

export function armConfetti() {
  if (window.__f9Confetti) return;
  window.__f9Confetti = true;
  window.addEventListener("f9-correct", () => {
    if (document.documentElement.dataset.motion === "reduce") return;
    import("../vendor/confetti/confetti.module.mjs").then((mod) => {
      const fire = mod.default;
      if (typeof fire !== "function") return;
      fire({
        particleCount: 70,
        spread: 68,
        origin: { y: 0.72 },
        disableForReducedMotion: true
      });
    }).catch(() => {});
  });
}

export async function dressFold(root) {
  if (!root) return;
  const reduced = document.documentElement.dataset.motion === "reduce";
  if (!reduced) {
    try {
      const { animate } = await import("../vendor/anime/anime.esm.min.js");
      animate(root.querySelectorAll(".packet"), {
        translateX: [0, 280],
        opacity: [0.35, 1],
        duration: 1400,
        loop: true,
        alternate: true,
        ease: "inOutQuad",
        delay: (element, index) => index * 180
      });
    } catch (err) { /* CSS offset-path still moves the packets */ }
    try {
      const roughMod = await import("../vendor/rough/rough.esm.js");
      const rough = roughMod.default;
      const host = root.querySelector("#rough-mark");
      if (host && rough && !host.dataset.drawn) {
        host.dataset.drawn = "1";
        const color = getComputedStyle(document.documentElement).getPropertyValue("--cc-accent-2").trim() || "#ffb020";
        host.appendChild(rough.svg(host).rectangle(6, 6, 108, 36, {
          stroke: color,
          fill: "rgba(255, 176, 32, 0.18)",
          roughness: 1.6,
          strokeWidth: 1.5
        }));
      }
    } catch (err) { /* stamp is decorative */ }
    mountStage(root.querySelector("#home-stage"));
  }
  const icons = root.querySelector(".icon-row");
  if (icons && !reduced && !icons.dataset.tilt) {
    icons.dataset.tilt = "1";
    root.addEventListener("pointermove", (event) => {
      const box = root.getBoundingClientRect();
      const x = (event.clientX - box.left) / box.width - 0.5;
      const y = (event.clientY - box.top) / box.height - 0.5;
      icons.style.transform = `rotateY(${x * 14}deg) rotateX(${-y * 8}deg)`;
    });
  }
}

async function mountStage(host) {
  if (!host || host.dataset.live === "1") return;
  if (document.documentElement.dataset.motion === "reduce") return;
  host.dataset.live = "1";
  const THREE = await import("../vendor/three/three.module.js");
  const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
  renderer.setPixelRatio(cappedPixelRatio());
  renderer.setSize(108, 108, false);
  host.replaceChildren(renderer.domElement);
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 20);
  camera.position.z = 3.1;
  const mesh = new THREE.Mesh(
    new THREE.IcosahedronGeometry(0.95, 0),
    new THREE.MeshBasicMaterial({ color: 0x5ce1ff, wireframe: true })
  );
  scene.add(mesh);
  const token = stageStop + 1;
  stageStop = token;
  const tick = () => {
    if (stageStop !== token || !host.isConnected) {
      renderer.dispose();
      return;
    }
    if (document.documentElement.dataset.motion === "reduce") {
      renderer.render(scene, camera);
      return;
    }
    mesh.rotation.y += 0.012;
    mesh.rotation.x += 0.004;
    renderer.render(scene, camera);
    requestAnimationFrame(tick);
  };
  tick();
}

export function stopStage() {
  stageStop += 1;
}

export function mountMindmap(svg) {
  const markmap = window.markmap;
  if (!svg || !markmap || !window.d3) return;
  const leaf = (content) => ({ content, children: [] });
  const root = {
    content: "Five9 study map",
    children: [
      { content: "Voice", children: [leaf("IVR"), leaf("Dialer"), leaf("SIP")] },
      { content: "People", children: [leaf("WEM"), leaf("Quality"), leaf("E911")] },
      { content: "Edges", children: [leaf("CRM adapters"), leaf("APIs"), leaf("Reporting")] }
    ]
  };
  try {
    const box = svg.getBoundingClientRect();
    const width = Math.max(320, Math.round(box.width || 720));
    svg.setAttribute("width", String(width));
    svg.setAttribute("height", "360");
    markmap.Markmap.create(svg, { embedGlobalCSS: true, duration: 0, maxInitialScale: 1 }, root);
  } catch (err) {
    svg.replaceChildren();
  }
}
