const CACHE = "f9lab-shell-v2";
const SHELL = [
  "./",
  "./index.html",
  "./css/app.css",
  "./css/university.css",
  "./js/app.js",
  "./js/university.js",
  "./js/diagrams.js",
  "./js/zipstore.js",
  "./js/ivr.js",
  "./js/pacing.js",
  "./js/topology.js",
  "./manifest.webmanifest",
  "./data/catalog.json",
  "./data/university.json",
  "./data/search-index.json"
];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((key) => key !== CACHE).map((key) => caches.delete(key)))).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;
  event.respondWith(
    fetch(request)
      .then((response) => {
        if (response && response.ok) {
          const copy = response.clone();
          caches.open(CACHE).then((cache) => cache.put(request, copy));
        }
        return response;
      })
      .catch(() => caches.match(request).then((cached) => cached || caches.match("./index.html")))
  );
});
