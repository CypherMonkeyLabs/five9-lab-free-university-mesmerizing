/* Offline shell for the Five9 university. Scope is this directory.
   Precache list is rewritten by scripts/build_precache.mjs. Budget 3.5 MB. */
const CACHE_NAME = "five9-university-r8";
const SHELL_ASSETS = [
  "./",
  "./index.html",
  "./offline.html",
  "./start.html",
  "./play.html",
  "./manifest.webmanifest",
  "./favicon.svg",
  "./assets/icons/icon-192.png",
  "./assets/icons/icon-512.png",
  "./assets/icons/icon-maskable-512.png",
  "./assets/css/frame.css",
  "./assets/css/wow.css",
  "./assets/css/footer.css",
  "./assets/js/frame.js",
  "./assets/js/university.js",
  "./assets/js/route-sim.js",
  "./guide/guide.js",
  "./guide/guide.css",
  "./shared/pybot-chat/engine.js",
  "./shared/pybot-chat/ui.js",
  "./shared/pybot-chat/chat.css",
  "./js/content/f9bot-index.json",
  "./rooms/t05-l01-preview-lets-the-agent-read-first.html",
];

self.addEventListener("install", function (event) {
  event.waitUntil(caches.open(CACHE_NAME).then(function (cache) {
    return Promise.all(SHELL_ASSETS.map(function (url) {
      return cache.add(url).catch(function () { return null; });
    }));
  }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener("activate", function (event) {
  event.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (key) { return key !== CACHE_NAME; }).map(function (key) {
      return caches.delete(key);
    }));
  }).then(function () { return self.clients.claim(); }));
});

self.addEventListener("fetch", function (event) {
  var request = event.request;
  if (request.method !== "GET") return;
  var url = new URL(request.url);
  if (url.origin !== self.location.origin) return;
  event.respondWith(caches.match(request).then(function (hit) {
    var network = fetch(request).then(function (response) {
      if (response && response.ok && response.type === "basic") {
        var copy = response.clone();
        caches.open(CACHE_NAME).then(function (cache) { cache.put(request, copy); });
      }
      return response;
    }).catch(function () {
      if (hit) return hit;
      if (request.mode === "navigate") return caches.match("./offline.html");
      return hit;
    });
    return hit || network;
  }));
});
