# Publishing notes

This lab is a static site. Nothing here phones home. The guide endpoint stays null.

## What is built

- Static HTML, CSS, and JavaScript. Serve the repository root.
- `manifest.webmanifest` and `sw.js` register a small offline shell. The service worker caches the frame, the guide, and the pages it has seen. That is the installable PWA path.
- `downloads/five9-lab-bundle.zip` is the optional offline bundle of the downloads folder.

## Prepared, not shipped as store builds

- Chrome extension: a Manifest V3 wrapper can point `chrome_url_overrides` or a popup at `index.html`. No extension package is in this repository.
- Capacitor iOS and Android: the web root can be copied into a Capacitor `webDir`. No Xcode or Android project is generated here.
- Embed widget: a host page can iframe `index.html`. The frame does not assume it is the top window. No separate widget script is published.

## Serve

```bash
python3 -m http.server 8741
```

Open `http://127.0.0.1:8741/`. The campus app remains at `http://127.0.0.1:8741/campus/`.

GitHub Pages can publish this tree. Use the organization repository. Do not add a personal profile, X, LinkedIn, or Hugging Face link to the footer.
