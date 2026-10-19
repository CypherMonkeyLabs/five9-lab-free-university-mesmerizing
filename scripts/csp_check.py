#!/usr/bin/env python3
"""Report off-origin loads in HTML, CSS, and JS.

Anchor hrefs to vendor docs are citations, not loads. Exit 1 when a script,
stylesheet, image, font, fetch, or CSS url() points off this origin.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKIP = {"node_modules", ".git", "downloads"}
patterns = [
    (r'<(?:script|img|iframe|source|video|audio)[^>]+\bsrc="(https?://[^"]+)"', "html src"),
    (r'<link[^>]+href="(https?://[^"]+)"', "html link"),
    (r'url\(\s*["\']?(https?://[^)"\']+)', "css url()"),
    (r'@import\s+["\'](https?://[^"\']+)', "css @import"),
    (r'\bimport\s*(?:\(|[^;]*from\s*)["\'](https?://[^"\']+)', "js import"),
    (r'\bfetch\(\s*["\'`](https?://[^"\'`]+)', "js fetch"),
    (r'new (?:Worker|WebSocket|EventSource)\(\s*["\'`](https?://[^"\'`]+)', "js net"),
]
fail = []
for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if any(part in SKIP for part in path.parts):
        continue
    if path.suffix.lower() not in {".html", ".css", ".js", ".mjs"}:
        continue
    text = path.read_text(errors="replace")
    rel = path.relative_to(ROOT).as_posix()
    for pat, kind in patterns:
        for match in re.finditer(pat, text):
            url = match.group(1)
            if url.startswith("http://www.w3.org/"):
                continue
            fail.append(f"{rel}: off-origin {kind}: {url}")
for line in fail:
    print("FAIL", line)
print("csp_check:", len(fail), "off-origin loads")
sys.exit(1 if fail else 0)
