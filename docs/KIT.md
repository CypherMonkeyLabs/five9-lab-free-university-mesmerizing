# Lab kit

The round-2 shell is the shared kit, adapted for this Five9 lab. Copy these files into another lab and keep the topic data separate.

## Chrome

- `assets/css/frame.css` — menu button, one banner row, sliding drawer, phone dock, font size, font colour, theme and motion controls.
- `assets/css/wow.css` — bright default, optional dark theme, reduced-motion cuts.
- `assets/css/footer.css` — boxed disclaimer and the three brand icons.
- `assets/js/frame.js` — drawer, banner arrows, display controls. No network calls.
- `assets/js/university.js` — search filter and the service worker registration.

The header and the banner sit in one `.chrome-stack`. That stack sticks to the top of the viewport. It does not stick in the middle of the page.

## Guide

- `guide/guide.js` and `guide/guide.css`
- First-open tour, then a centre greeting, then the monkey docks on the right.
- On a phone the open guide is a bottom sheet. Its max height is 60vh and it sits above the phone bar.
- Offers are the first buttons. Voice, read-along, and the mic sit under More tools.
- `window.F9_GUIDE.endpoint` stays null. The guide does not send text anywhere.

## Build

- `scripts/build_round2.py` writes rooms, tracks, diagrams, sheets, templates, the deck, and the top-level pages from `campus/data/`.
- `scripts/raster_png.mjs` writes a PNG beside every diagram SVG.
- `scripts/export_sheets.mjs` writes PDF and PNG for the HTML sheets, and PDF for templates and flashcards.
- `scripts/verify.mjs` checks the curriculum counts and the three allowed brand links.
- `scripts/gzip-static.mjs` compresses the static files for a gzip check.

## Brand and disclaimer

Only three brand destinations appear in the footer: the website, the GitHub organization, and `https://linktr.ee/cypherMonkey`. Contact is `https://cyphermonkeylabs.com/#contact`. The disclaimer box is on every generated page and inside every standalone download.
