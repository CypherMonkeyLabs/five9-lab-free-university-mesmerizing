/* Offline shell for the Five9 university. Same-origin GET only. */
var CACHE = "five9-university-r2";
var SHELL = [
  "./",
  "./index.html",
  "./start.html",
  "./diagrams.html",
  "./flows.html",
  "./downloads.html",
  "./play.html",
  "./listen.html",
  "./help.html",
  "./legal.html",
  "./ecosystem.html",
  "./assets/css/frame.css",
  "./assets/css/wow.css",
  "./assets/css/footer.css",
  "./assets/js/frame.js",
  "./assets/js/university.js",
  "./guide/guide.js",
  "./guide/guide.css",
  "./guide/kb.json",
  "./favicon.svg",
  "./manifest.webmanifest"
];

self.addEventListener("install", function (event) {
  event.waitUntil(caches.open(CACHE).then(function (cache) {
    return cache.addAll(SHELL);
  }).then(function () { return self.skipWaiting(); }).catch(function () { return self.skipWaiting(); }));
});

self.addEventListener("activate", function (event) {
  event.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (key) { return key !== CACHE; }).map(function (key) {
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
        caches.open(CACHE).then(function (cache) { cache.put(request, copy); });
      }
      return response;
    }).catch(function () { return hit; });
    return hit || network;
  }));
});
