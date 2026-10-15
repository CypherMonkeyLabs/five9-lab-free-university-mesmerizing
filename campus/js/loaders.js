// On-demand loaders. Static imports would pull Three.js and the simulators
// into the first paint. The lab shell budget forbids that, so the dynamic
// import lives in this module and nowhere else.

export const loadTopology = () => import("./topology.js");
export const loadIvr = () => import("./ivr.js");
export const loadPacing = () => import("./pacing.js");
