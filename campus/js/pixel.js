// Screen scale for WebGL. Phones often report 3x; drawing that many pixels
// stalls the main thread. Desktop stays at 2.

export function cappedPixelRatio() {
  const dpr = window.devicePixelRatio || 1;
  const mobile = window.matchMedia("(max-width: 800px)").matches
    || window.matchMedia("(pointer: coarse)").matches;
  return Math.min(dpr, mobile ? 1.5 : 2);
}
