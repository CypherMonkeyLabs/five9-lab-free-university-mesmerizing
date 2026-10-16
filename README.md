# Five9 Lab

An independent study floor for Five9 Virtual Contact Center. It walks VCC administration, inbound, outbound, and autodial campaigns, dialer modes, IVR, skills, Agent Desktop Plus, workforce engagement, IVA and GenAI Studio, CRM adapters, SIP, APIs and reporting, and a teaching bridge from Cisco UCCX and UCCE.

Five9 Lab is not affiliated with, endorsed by, or sponsored by Five9, Inc. Product behavior belongs to Five9's own documentation. When a number or a mapping might have moved, the lesson marks it uncertain.

## Run it

From the repository root:

```bash
python3 -m http.server 8741
```

Open [http://127.0.0.1:8741/](http://127.0.0.1:8741/). That is the round-2 front door: menu, banner, guide, and downloads. The practice console stays at [http://127.0.0.1:8741/campus/](http://127.0.0.1:8741/campus/). GitHub Pages can serve this tree as a static site.

Rebuild the lesson JSON after editing a track module:

```bash
python3 scripts/build_curriculum.py
python3 scripts/build_university_assets.py
node scripts/verify.mjs
```

## What you can do

- Twenty-three tracks, loaded one at a time. The first paint does not download Three.js or the track files. Skills and ACD, workforce, quality, CRM and CTI, and the ecosystem are in the menu.
- Each lesson has a figure, a Play / Pause / Step / Inspect flow, a quiz, flashcards, a lab, and a fault log.
- IVR script builder. Module names follow the IVR Administrator's Guide. The export is a learning JSON, not a file VCC can import.
- Dialer pacing simulator for preview, progressive, power, predictive, and TCPA manual touch. It is a classroom clock, not the Five9 dialer.
- 3D topology with failure toggles. Reduced motion draws a flat map instead of WebGL.
- Eight boss incidents, an interview deck, a glossary, and a certification page that refuses invented exam codes.
- Settings stay in this browser. The floor opens on the neon theme: black-violet space, cyan and magenta. Light is the pastel theme. Futuristic, gaming, holographic, sunset, cyberpunk, signal, paper, high contrast, amber, and aurora stay in the swatches. Sound, narration, reduced motion, and four text sizes stay local.
- University pages for deployment, SIP and PSTN, migration checklists, ports, playbooks, WFM (the calculator is Erlang C, not Five9's engine), recording, E911, reporting, CRM, AI, security, a 2026 notes page, and study frames.
- Cheat sheets in `campus/downloads/` as HTML, PDF, and PNG, plus flashcards and an offline zip. The in-app pack builds the same zip in the browser.
- Ports game, flow map, daily challenge drawn from the lesson bank, badges tied to real progress, and a share card.

## Counts

`node scripts/verify.mjs` reports 23 tracks, 161 lessons, 805 quiz questions, 644 flashcards, 161 labs, 161 faults, 36 interview answers, 8 boss incidents, and 44 glossary rows. The round-2 build writes 161 drawings, one SVG and one PNG per lesson. The counted shell (HTML, `app.css`, `app.js`, and loaders) stays under the script's limit. Three.js stays off the first paint. University CSS, diagrams, and the cheat-sheet files load with the pages that need them.

## Screenshots

Round-2 checks at 1440×900 and 390×844 are in `docs/screenshots/round2/`.

![Home on a desktop width](docs/screenshots/round2/home-desktop.png)

![Home on a phone width](docs/screenshots/round2/home-phone.png)

![Guide open on a phone](docs/screenshots/round2/bot-phone.png)

Earlier campus shots:

![Campus home](docs/screenshots/home-desktop.png)

![Home with the mobile tab bar](docs/screenshots/home-mobile.png)

![A lesson with the call-flow player](docs/screenshots/lesson.png)

![IVR script builder](docs/screenshots/ivr.png)

![Dialer pacing simulator](docs/screenshots/pacing.png)

![3D topology with failure toggles](docs/screenshots/topology.png)

## License

Code is [MIT](LICENSE). Lesson content is [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Three.js is MIT, under `campus/vendor/three/LICENSE`.
