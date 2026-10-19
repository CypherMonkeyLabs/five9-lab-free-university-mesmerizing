#!/usr/bin/env python3
"""Build the Five9 round-2 university from campus/data. One static tree, no network."""

from __future__ import annotations

import html
import json
import re
import sys
import zipfile
from pathlib import Path

from build_university_assets import CSP_META, paginate, write_pdf
from go_deeper import (
    front_sources,
    lesson_sources,
    markdown_doc,
    merge_sources,
    pack_record,
    pack_sections,
    sources_from_html,
    sources_html,
    sources_lines,
    status_for,
    track_sources,
)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "campus" / "data"
OUT_DIAG = ROOT / "downloads" / "diagrams"
OUT_SHEETS = ROOT / "downloads" / "sheets"
OUT_SECTIONS = ROOT / "downloads" / "sections"
OUT_TEMPLATES = ROOT / "downloads" / "templates"

WEB = "https://cyphermonkeylabs.com"
CONTACT = "https://cyphermonkeylabs.com/#contact"
ORG = "https://github.com/CypherMonkeyLabs"
REPO = "https://github.com/CypherMonkeyLabs/five9-lab-free-university-mesmerizing"
TREE = "https://linktr.ee/cypherMonkey"

NAV = [
    ("home", "Home", "index.html", "🏠", "The front door, the tracks, and the new chapters."),
    ("learn", "Learn", "start.html", "📚", "Ten minutes, or the full course."),
    ("acd", "Skills and ACD", "tracks/t19.html", "☎️", "Skill groups as Five9 queues, and the ACD details this check could not read."),
    ("wfm", "Workforce", "tracks/t20.html", "📅", "Forecasts, schedules, intraday changes, and adherence."),
    ("quality", "Quality", "tracks/t21.html", "🎧", "Evaluations, analytics wording, and claims left as claims."),
    ("crm", "CRM and CTI", "tracks/t22.html", "🔗", "Named adapters and the CTI API, from the pages that opened."),
    ("diagrams", "Diagrams", "diagrams.html", "🗺️", "Drawings you can save as SVG, PNG, and HTML."),
    ("flows", "Flows", "flows.html", "〰️", "Animated call, signal, and data paths."),
    ("play", "Play", "play.html", "🎮", "A port game, a daily question, and a badge in this browser."),
    ("listen", "Listen", "listen.html", "🎧", "Study audio and read-along."),
    ("downloads", "Downloads", "downloads.html", "⬇️", "Sheets, cards, templates, and one bundle."),
    ("ecosystem", "Ecosystem", "ecosystem.html", "🌐", "Glossary, mind map, sisters, integration list, bridges, and hooks."),
    ("help", "Help", "help.html", "❓", "How the menu, course, bot, and downloads work."),
    ("legal", "Legal", "legal.html", "🛡️", "Copyright, licences, privacy, and removal."),
    ("careers", "Careers", "careers.html", "🎯", "Study frames. Not a job requisition."),
    ("certs", "Certifications", "certs.html", "🎓", "Public training names. No invented exam codes."),
    ("ports", "Ports", "ports.html", "🔌", "Ports named on the public pages this lab read."),
    ("glossary", "Glossary", "glossary.html", "📖", "Terms with the page that defined them."),
    ("interviews", "Interview prep", "interviews.html", "✅", "Short answers with a source. Not anyone's résumé."),
    ("charts", "Charts", "charts.html", "📊", "Counts from this repository. No traffic and no revenue."),
    ("search", "Search", "search.html", "🔎", "Find a room by its title."),
    ("practice", "Open app", "campus/index.html", "🧪", "IVR builder, dialer clock, and the topology bench."),
]

TOUR_IDS = {
    "learn": "tour-learn",
    "diagrams": "tour-diagrams",
    "play": "tour-play",
    "downloads": "tour-downloads",
}


def esc(value) -> str:
    return html.escape(str(value if value is not None else ""), quote=True)


def slug(text: str) -> str:
    return re.sub(r"^-+|-+$", "", re.sub(r"[^a-z0-9]+", "-", text.lower()))[:48]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_tracks():
    catalog = load_json(DATA / "catalog.json")
    tracks = []
    for meta in catalog["tracks"]:
        tracks.append(load_json(DATA / meta["file"]))
    return tracks


def shield() -> str:
    return (
        '<span class="disclaimer-ico"><svg viewBox="0 0 24 24" aria-hidden="true">'
        '<path d="M12 2.5 4.5 5.5v5.8c0 4.6 3.1 8.6 7.5 10.2 4.4-1.6 7.5-5.6 7.5-10.2V5.5z" '
        'fill="currentColor" opacity=".18" stroke="currentColor" stroke-width="1.6"/>'
        '<path d="M8 12.2 10.6 14.6 16 9.4" fill="none" stroke="#0f766e" stroke-width="1.8" stroke-linecap="round"/>'
        "</svg></span>"
    )


def brand_icons() -> str:
    monkey = (
        '<svg viewBox="0 0 64 64" aria-hidden="true">'
        '<ellipse cx="10" cy="26" rx="9" ry="12" fill="#c2410c"/>'
        '<ellipse cx="54" cy="26" rx="9" ry="12" fill="#c2410c"/>'
        '<ellipse cx="10" cy="26" rx="5" ry="7" fill="#fb7185"/>'
        '<ellipse cx="54" cy="26" rx="5" ry="7" fill="#fb7185"/>'
        '<circle cx="32" cy="34" r="22" fill="#f59e0b" stroke="#b45309" stroke-width="2"/>'
        '<ellipse cx="24" cy="24" rx="10" ry="6" fill="#fde68a" opacity=".85"/>'
        '<ellipse cx="32" cy="42" rx="13" ry="9" fill="#ffedd5"/>'
        '<ellipse cx="23" cy="32" rx="6" ry="7" fill="#fff" stroke="#1c1917" stroke-width="1"/>'
        '<ellipse cx="41" cy="32" rx="6" ry="7" fill="#fff" stroke="#1c1917" stroke-width="1"/>'
        '<circle cx="24" cy="33" r="2.4" fill="#1c1917"/>'
        '<circle cx="42" cy="33" r="2.4" fill="#1c1917"/>'
        '<ellipse cx="32" cy="40" rx="3.2" ry="2.2" fill="#9a3412"/>'
        '<path d="M25 46 Q32 52 39 46" fill="none" stroke="#9a3412" stroke-width="1.8" stroke-linecap="round"/>'
        '<rect x="16" y="25" width="14" height="14" rx="5" fill="none" stroke="#67e8f9" stroke-width="2"/>'
        '<rect x="34" y="25" width="14" height="14" rx="5" fill="none" stroke="#67e8f9" stroke-width="2"/>'
        '<path d="M30 32 H34" stroke="#67e8f9" stroke-width="2"/>'
        "</svg>"
    )
    github = (
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 .5A11.5 11.5 0 0 0 .5 12.3c0 5.22 3.38 9.65 8.07 11.22.59.12.8-.26.8-.57v-2.02c-3.28.73-3.97-1.42-3.97-1.42-.53-1.38-1.3-1.75-1.3-1.75-1.07-.75.08-.73.08-.73 1.18.08 1.8 1.24 1.8 1.24 1.05 1.84 2.76 1.31 3.43.99.1-.78.41-1.31.75-1.61-2.62-.31-5.37-1.34-5.37-5.98 0-1.32.46-2.4 1.22-3.25-.12-.3-.53-1.53.12-3.18 0 0 1-.33 3.3 1.25a11.3 11.3 0 0 1 6 0c2.3-1.58 3.3-1.25 3.3-1.25.65 1.65.24 2.88.12 3.18.76.85 1.22 1.93 1.22 3.25 0 4.65-2.76 5.66-5.39 5.96.42.38.8 1.12.8 2.26v3.35c0 .31.21.7.81.57A11.52 11.52 0 0 0 23.5 12.3 11.5 11.5 0 0 0 12 .5z"/></svg>'
    )
    tree = (
        '<svg viewBox="0 0 64 64" aria-hidden="true">'
        '<circle cx="32" cy="16" r="11" fill="#fff"/>'
        '<circle cx="18" cy="28" r="10" fill="#fff"/>'
        '<circle cx="46" cy="28" r="10" fill="#fff"/>'
        '<path d="M32 34v14" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
        '<path d="M22 52h20" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
        "</svg>"
    )
    return (
        f'<a class="brand-icon brand-web" href="{WEB}" aria-label="CypherMonkey Labs website">{monkey}</a>'
        f'<a class="brand-icon brand-gh" href="{ORG}" aria-label="GitHub organization">{github}</a>'
        f'<a class="brand-icon brand-tree" href="{TREE}" aria-label="Linktree">{tree}</a>'
    )


def disclaimer_block() -> str:
    return (
        '<aside class="disclaimer-panel" aria-labelledby="disc-title">'
        f"{shield()}<div><h2 id=\"disc-title\">A note from the student behind this lab</h2>"
        "<p>This is an <strong>independent, free, learning-only student project</strong>. "
        "It respects every company and vendor, and every trademark belongs to its owner. "
        "It is <strong>not affiliated with or endorsed by</strong> any of them.</p>"
        f"<p>If anyone has a concern, the content will be removed or corrected promptly via the contact form at "
        f'<a href="{CONTACT}">{CONTACT}</a>. Nothing here is sold. Happy to volunteer for any organization.</p>'
        "<p>Confirm before relying on a number, a port, or a vendor case-study claim. Product behavior belongs to the cited page.</p>"
        "<p>Chapters on skills, workforce, quality, CRM, and the ecosystem repeat only what a public page returned. A page that did not return a body is marked confirm and is not linked.</p>"
        "</div></aside>"
        '<p class="footer-brand">CypherMonkey Labs</p>'
        f'<nav class="brand-row" aria-label="Brand">{brand_icons()}</nav>'
        '<p class="site-copy">© 2026 CypherMonkeyLabs 🐒 · MIT code, CC BY-NC-SA content</p>'
    )


def footer() -> str:
    return f'<footer class="site-footer lab-footer" data-canon-footer>{disclaimer_block()}</footer>'


def head(title: str, prefix: str, desc: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="bloom" data-font="md" data-motion="full" data-root="{esc(prefix)}">
<head>
<meta charset="utf-8">
{CSP_META}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{prefix}favicon.ico" sizes="48x48">
<link rel="manifest" href="{prefix}manifest.webmanifest">
<link rel="stylesheet" href="{prefix}assets/css/frame.css">
<link rel="stylesheet" href="{prefix}assets/css/wow.css">
<link rel="stylesheet" href="{prefix}assets/css/footer.css">
<script src="{prefix}assets/js/theme-boot.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def chrome(prefix: str, current: str) -> str:
    chips = []
    rows = []
    dock = []
    dock_keys = [
        ("menu", "Menu", None, "☰"),
        ("learn", "Learn", "start.html", "📚"),
        ("diagrams", "Diagrams", "diagrams.html", "🗺️"),
        ("play", "Play", "play.html", "🎮"),
        ("listen", "Listen", "listen.html", "🎧"),
        ("guide", "Guide", None, "🐒"),
    ]
    for key, label, href, icon, desc in NAV:
        here = href == current
        tour = f' id="{TOUR_IDS[key]}"' if key in TOUR_IDS else ""
        current_attr = ' aria-current="page"' if here else ""
        chips.append(
            f'<a class="section-chip" data-section="{key}" href="{prefix}{href}"{tour}{current_attr}>'
            f'<span class="chip-ico" aria-hidden="true">{icon}</span>{esc(label)}</a>'
        )
        rows.append(
            f'<li><a href="{prefix}{href}"{current_attr}><span class="row-ico" aria-hidden="true">{icon}</span>'
            f"<span><strong>{esc(label)}</strong><small>{esc(desc)}</small></span></a></li>"
        )
    for key, label, href, icon in dock_keys:
        if key == "menu":
            dock.append(
                '<button type="button" data-open-menu aria-expanded="false" aria-controls="site-drawer">'
                f'<span class="dock-ico" aria-hidden="true">{icon}</span>{esc(label)}</button>'
            )
        elif key == "guide":
            dock.append(
                '<button type="button" data-open-guide><span class="dock-ico" aria-hidden="true">🐒</span>Guide</button>'
            )
        else:
            here = href == current
            dock.append(
                f'<a href="{prefix}{href}"{" aria-current=\"page\"" if here else ""}>'
                f'<span class="dock-ico" aria-hidden="true">{icon}</span>{esc(label)}</a>'
            )
    tools = (
        '<div class="head-tools">'
        '<label>Size <select data-font-size aria-label="Font size">'
        '<option value="sm">S</option><option value="md" selected>M</option>'
        '<option value="lg">L</option><option value="xl">XL</option></select></label>'
        '<label>Colour <input data-font-color type="color" value="#142033" aria-label="Font colour"></label>'
        '<button type="button" class="ghost-btn" data-theme-toggle>Dark</button>'
        '<button type="button" class="ghost-btn" data-motion-toggle aria-pressed="false">Motion</button>'
        "</div>"
    )
    return (
        '<div class="chrome-stack"><header class="site-head">'
        '<button type="button" class="menu-btn" id="tour-menu" data-open-menu aria-expanded="false" aria-controls="site-drawer">Menu</button>'
        f'<a class="brand" id="tour-home" href="{prefix}index.html"><span><strong>Five9 Lab</strong>'
        "<small>A student's open lab: learning and sharing, free for everyone.</small></span></a>"
        f"{tools}</header>"
        '<div class="canon-banner"><button type="button" class="rail-arrow" data-rail="prev" aria-label="Scroll sections back">‹</button>'
        f'<nav class="section-rail" aria-label="Sections">{"".join(chips)}</nav>'
        '<button type="button" class="rail-arrow" data-rail="next" aria-label="Scroll sections forward">›</button></div></div>'
        '<div class="drawer-back" data-close-menu></div>'
        '<nav class="drawer" id="site-drawer" aria-hidden="true" aria-label="Menu">'
        '<div class="drawer-bar"><p>Menu</p><button type="button" class="text-btn" data-close-menu>Close</button></div>'
        f'<form class="drawer-search" data-site-search role="search"><input type="search" aria-label="Search rooms" placeholder="Search rooms"></form>'
        f'<ul class="drawer-list">{"".join(rows)}</ul></nav>'
        f'<nav class="phone-dock" aria-label="Phone">{"".join(dock)}</nav>'
    )


def scripts(prefix: str) -> str:
    return (
        f'<script src="{prefix}assets/js/frame.js"></script>'
        f'<script src="{prefix}assets/js/university.js"></script>'
        f'<script src="{prefix}guide/guide.js"></script></body></html>'
    )


def write_page(rel: str, title: str, desc: str, body: str, current: str) -> None:
    depth = rel.count("/")
    prefix = "../" * depth
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if "Sources and go deeper" not in body:
        body = body + sources_html(sources_from_html(body))
    doc = head(title, prefix, desc) + chrome(prefix, current) + f'<main id="main">{body}</main>' + footer() + scripts(prefix)
    path.write_text(doc, encoding="utf-8")


def dl_links(pairs) -> str:
    bits = []
    for kind, href in pairs:
        bits.append(f'<a class="dl-btn" data-export href="{esc(href)}" download>{esc(kind)}</a>')
    return f'<div class="dl-row">{"".join(bits)}</div>'


def section(sid: str, title: str, inner: str, downloads) -> str:
    return (
        f'<section class="panel" id="{esc(sid)}" data-read-section="{esc(sid)}">'
        f'<div class="section-head"><h2>{esc(title)}</h2>{dl_links(downloads)}</div>{inner}</section>'
    )


def sentences(text: str) -> str:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return " ".join(f'<span data-sentence>{esc(part)}</span>' for part in parts if part)


STANDALONE_CSS = """
body{font:16px/1.45 Segoe UI,system-ui,sans-serif;margin:24px;color:#142033;background:#f8fafc;overflow-wrap:anywhere}
h1{font-size:1.4rem} a{color:#0b3a8f}
.disclaimer-panel{display:flex;gap:12px;text-align:left;padding:16px;border:2px solid #0f766e;border-radius:16px;background:linear-gradient(135deg,#dcfce7,#dbeafe);color:#0b1f2a;box-sizing:border-box;max-width:100%;min-width:0}
.disclaimer-panel>div{min-width:0}
.disclaimer-ico{width:40px;flex:none;color:#0f766e}
.footer-brand{font-weight:800;font-size:1.2rem}
.brand-row{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;padding:10px;border-radius:16px;border:2px solid #a78bfa;box-shadow:0 0 16px rgba(167,139,250,.45);max-width:100%;box-sizing:border-box}
.brand-icon{display:grid;place-items:center;width:64px;height:64px;border-radius:16px;color:#fff}
.brand-icon svg{width:40px;height:40px}
.brand-web{background:#4c1d95}.brand-gh{background:#24292f}.brand-tree{background:linear-gradient(160deg,#34d399,#047857);box-shadow:0 0 0 3px rgba(52,211,153,.7),0 0 14px rgba(16,185,129,.9)}
.site-copy{font-weight:800}
.figure,svg.figure,.figure svg{max-width:100%;height:auto}
.sources-deeper{margin:16px 0;padding:14px 16px;border:2px solid #5b21b6;border-radius:16px;background:#f5f3ff;color:#1e1b4b}
.sources-deeper h2{margin:0 0 8px}
.sources-deeper a{color:#1d4ed8;font-weight:700}
"""


def emit_export(rel: str, title: str, body: str, lines: list[str], sources: list, html_ready: bool = False) -> None:
    standalone(rel, title, body if html_ready else body + sources_html(sources))
    base = ROOT / rel
    prose = [line for line in lines if line]
    base.with_suffix(".md").write_text(markdown_doc(title, prose, sources), encoding="utf-8")
    write_pdf(base.with_suffix(".pdf"), paginate([title, ""] + prose + [""] + sources_lines(sources)))
    base.with_suffix(".docx").write_bytes(docx_bytes(title, prose + sources_lines(sources)))


def write_room_formats(record_id: str, title: str, lines: list[str], sources: list) -> None:
    folder = ROOT / "downloads" / "rooms"
    folder.mkdir(parents=True, exist_ok=True)
    prose = [line for line in lines if line]
    (ROOT / "rooms" / f"{record_id}.md").write_text(markdown_doc(title, prose, sources), encoding="utf-8")
    (folder / f"{record_id}.md").write_text(markdown_doc(title, prose, sources), encoding="utf-8")
    write_pdf(folder / f"{record_id}.pdf", paginate([title, ""] + prose + [""] + sources_lines(sources)))
    (folder / f"{record_id}.docx").write_bytes(docx_bytes(title, prose + sources_lines(sources)))


def standalone(rel: str, title: str, body: str) -> None:
    depth = rel.count("/")
    prefix = "../" * depth
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = (
        "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"{CSP_META}"
        f"<title>{esc(title)}</title><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        f'<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">'
        f'<link rel="icon" href="{prefix}favicon.ico">'
        f"<style>{STANDALONE_CSS}</style></head><body>"
        f"<h1>{esc(title)}</h1>{body}"
        f'<footer class="site-footer" data-canon-footer>{disclaimer_block()}</footer></body></html>'
    )
    path.write_text(doc, encoding="utf-8")


def wrap_words(text: str, limit: int, rows: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        piece = word[:limit]
        trial = f"{current} {piece}".strip()
        if len(trial) <= limit:
            current = trial
            continue
        if current:
            lines.append(current)
        current = piece
        if len(lines) >= rows:
            break
    if current and len(lines) < rows:
        lines.append(current)
    return lines[:rows]


def flow_svg(title: str, steps: list) -> str:
    steps = steps or [{"title": "Read the lesson", "detail": "Confirm before relying."}]
    pitch = 196
    box_w = 176
    width = 32 + len(steps) * pitch
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 230" role="img" aria-label="{esc(title)}">',
        "<style>.flow-line{stroke-dasharray:8 6;animation:dash 2.4s linear infinite}@keyframes dash{to{stroke-dashoffset:-56}}@media (prefers-reduced-motion:reduce){.flow-line{animation:none}}</style>",
        '<rect width="100%" height="100%" fill="#041018"/>',
        f'<text x="20" y="32" fill="#f8fafc" font-size="16" font-family="Segoe UI,sans-serif">{esc(title)[:80]}</text>',
    ]
    for index, step in enumerate(steps):
        x = 20 + index * pitch
        label = esc((step.get("title") or "Step")[:18])
        detail_lines = [esc(line) for line in wrap_words(step.get("detail") or "", 24, 2)]
        lane = esc((step.get("lane") or "")[:16])
        parts.append(f'<clipPath id="box{index}"><rect x="{x}" y="58" width="{box_w}" height="128" rx="12"/></clipPath>')
        parts.append(f'<rect x="{x}" y="58" width="{box_w}" height="128" rx="12" fill="#102033" stroke="#67e8f9"/>')
        parts.append(f'<g clip-path="url(#box{index})">')
        parts.append(f'<text x="{x + box_w / 2}" y="86" text-anchor="middle" fill="#e7eef8" font-size="14" font-family="Segoe UI,sans-serif">{label}</text>')
        for line_index, line in enumerate(detail_lines):
            parts.append(
                f'<text x="{x + box_w / 2}" y="{110 + line_index * 16}" text-anchor="middle" fill="#b6f3ff" font-size="12" font-family="Segoe UI,sans-serif">{line}</text>'
            )
        parts.append(f'<text x="{x + box_w / 2}" y="164" text-anchor="middle" fill="#f9a8d4" font-size="11" font-family="Segoe UI,sans-serif">{lane}</text>')
        parts.append("</g>")
        if index < len(steps) - 1:
            parts.append(
                f'<line class="flow-line" x1="{x + box_w}" y1="122" x2="{x + pitch}" y2="122" stroke="#f472b6" stroke-width="3"/>'
            )
    parts.append("</svg>")
    return "".join(parts)


def quiz_html(quiz: list) -> str:
    blocks = []
    for index, item in enumerate(quiz):
        choices = []
        for choice_index, choice in enumerate(item.get("choices") or []):
            choices.append(
                f'<label><input type="radio" name="q{index}" value="{choice_index}"> {esc(choice)}</label>'
            )
        blocks.append(
            "<fieldset>"
            f"<legend>{esc(item.get('q') or '')}</legend>{''.join(choices)}"
            f'<p class="quiz-why" hidden data-answer="{int(item.get("answer") or 0)}">{esc(item.get("why") or "")}</p>'
            "</fieldset>"
        )
    return f'<form class="quiz" data-quiz>{"".join(blocks)}<button type="button" data-quiz-check>Check</button><p class="quiz-score" aria-live="polite"></p></form>'


def docx_bytes(title: str, paragraphs: list[str]) -> bytes:
    body = "".join(f"<w:p><w:r><w:t>{esc(p)}</w:t></w:r></w:p>" for p in [title, *paragraphs])
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body>{body}</w:body></w:document>"
    )
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""
    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""
    import io
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zipped:
        zipped.writestr("[Content_Types].xml", content_types)
        zipped.writestr("_rels/.rels", rels)
        zipped.writestr("word/document.xml", document)
    return buf.getvalue()


def pptx_bytes(slides: list[tuple[str, str]]) -> bytes:
    slide_xml = []
    rels_items = []
    content_overrides = []
    for index, (title, body) in enumerate(slides, start=1):
        slide_xml.append((
            f"ppt/slides/slide{index}.xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
            'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">'
            "<p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id=\"1\" name=\"\"/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>"
            '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
            f'<p:sp><p:nvSpPr><p:cNvPr id="2" name="Title"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            '<p:spPr><a:xfrm><a:off x="400000" y="300000"/><a:ext cx="8000000" cy="800000"/></a:xfrm></p:spPr>'
            f'<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:t>{esc(title)}</a:t></a:r></a:p></p:txBody></p:sp>'
            f'<p:sp><p:nvSpPr><p:cNvPr id="3" name="Body"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            '<p:spPr><a:xfrm><a:off x="400000" y="1400000"/><a:ext cx="8000000" cy="4000000"/></a:xfrm></p:spPr>'
            f'<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:t>{esc(body)}</a:t></a:r></a:p></p:txBody></p:sp>'
            "</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>"
        ))
        rels_items.append(
            f'<Relationship Id="rId{index}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{index}.xml"/>'
        )
        content_overrides.append(
            f'<Override PartName="/ppt/slides/slide{index}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        )
    sld_id = "".join(
        f'<p:sldId id="{255 + index}" r:id="rId{index}"/>' for index in range(1, len(slides) + 1)
    )
    presentation = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
        'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">'
        f"<p:sldIdLst>{sld_id}</p:sldIdLst>"
        '<p:sldSz cx="9144000" cy="5143500"/>'
        "</p:presentation>"
    )
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>'
        + "".join(content_overrides) + "</Types>"
    )
    rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        + "".join(rels_items) + "</Relationships>"
    )
    import io
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zipped:
        zipped.writestr("[Content_Types].xml", content_types)
        zipped.writestr("_rels/.rels", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/></Relationships>')
        zipped.writestr("ppt/presentation.xml", presentation)
        zipped.writestr("ppt/_rels/presentation.xml.rels", rels)
        for name, xml in slide_xml:
            zipped.writestr(name, xml)
    return buf.getvalue()


def room_records(tracks):
    records = []
    for track in tracks:
        for lesson in track["lessons"]:
            rid = f"{track['id']}-{lesson['id']}-{slug(lesson['title'])}"
            records.append({"track": track, "lesson": lesson, "id": rid, "href": f"rooms/{rid}.html"})
    return records


def build_diagrams(records):
    manifest = []
    for record in records:
        lesson = record["lesson"]
        svg = flow_svg(lesson["flow"]["title"] if lesson.get("flow") else lesson["title"], (lesson.get("flow") or {}).get("steps"))
        svg_rel = f"downloads/diagrams/{record['id']}.svg"
        html_rel = f"downloads/diagrams/{record['id']}.html"
        (ROOT / svg_rel).parent.mkdir(parents=True, exist_ok=True)
        (ROOT / svg_rel).write_text(svg, encoding="utf-8")
        standalone(html_rel, lesson["title"], f'<div class="figure">{svg}</div><p>Teaching drawing from the lesson flow. Confirm before relying.</p>')
        manifest.append({"id": record["id"], "title": lesson["title"], "svg": svg_rel, "html": html_rel, "flow": True})
    return manifest


def build_rooms(records, eco):
    glossary = eco.get("glossary") or []
    integrations = eco.get("integrations") or []
    kb = []
    for index, record in enumerate(records):
        lesson = record["lesson"]
        track = record["track"]
        rid = record["id"]
        prefix_dl = f"../downloads/sections/{rid}"
        diagram = f"../downloads/diagrams/{rid}"
        paras = lesson.get("paragraphs") or []
        learn_inner = (
            f'<p class="kicker">{esc(track["title"])} · {esc(lesson.get("level") or "")} · {esc(lesson.get("minutes") or "")} min full read</p>'
            f"<p>{sentences(paras[0] if paras else lesson['title'])}</p>"
            "<ul>" + "".join(f"<li>{esc(item)}</li>" for item in (lesson.get("objectives") or [])) + "</ul>"
            + "".join(f"<p>{sentences(p)}</p>" for p in paras[1:])
        )
        if lesson.get("callout"):
            learn_inner += f'<p class="callout"><strong>{esc(lesson["callout"].get("title"))}</strong> {esc(lesson["callout"].get("body"))}</p>'
        svg = (ROOT / "downloads" / "diagrams" / f"{rid}.svg").read_text(encoding="utf-8")
        visual = f'<div class="figure">{svg}</div><p>{esc((lesson.get("figure") or {}).get("caption") or "Lesson flow.")}</p>'
        lab = lesson.get("lab") or {}
        example = (
            f"<h3>{esc(lab.get('title') or 'Worked example')}</h3><p>{sentences(lab.get('goal') or '')}</p><ol>"
            + "".join(f"<li>{esc(step)}</li>" for step in (lab.get("steps") or []))
            + f"</ol><p>{esc(lab.get('success') or '')}</p>"
        )
        cards = lesson.get("cards") or []
        if cards:
            example += "<ul>" + "".join(f"<li><strong>{esc(card.get('front'))}</strong> {esc(card.get('back'))}</li>" for card in cards) + "</ul>"
        source_rows = lesson_sources(lesson)
        (ROOT / "rooms" / f"{rid}.sources.json").write_text(
            json.dumps(pack_record(rid, lesson["title"], source_rows), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        room_lines = list(paras) + list(lesson.get("objectives") or [])
        write_room_formats(rid, lesson["title"], room_lines, source_rows)
        sources = sources_html(source_rows)
        term = glossary[index % len(glossary)] if glossary else {"term": "Domain", "meaning": "The tenant.", "url": WEB, "source": "Five9"}
        integ = integrations[index % len(integrations)] if integrations else {"system": "CRM SDK", "how": "Bring your own.", "url": WEB, "source": "APIs"}
        fault = lesson.get("fault") or {}
        eco_inner = (
            f"<p><strong>Glossary.</strong> {esc(term.get('term'))}: {esc(term.get('meaning'))} "
            f'<a href="{esc(term.get("url"))}">{esc(term.get("source"))}</a></p>'
            f"<p><strong>Sister technologies.</strong> {esc(integ.get('system'))}. {esc(integ.get('how'))} "
            f'<a href="{esc(integ.get("url"))}">{esc(integ.get("source"))}</a></p>'
            f"<p><strong>Config.</strong> {esc(lab.get('goal') or 'Follow the worked example, then check the cited admin page.')}</p>"
            f"<p><strong>Troubleshooting.</strong> {esc(fault.get('symptom') or '')} {esc(fault.get('fix') or '')}</p>"
            "<p><strong>Cross-platform bridge.</strong> A mapping to another PBX or contact center is a teaching bridge. It is not an import button.</p>"
            "<p><strong>Future hook.</strong> The guide's cloud endpoint stays unset. Confirm before relying on a dated catalog or a case-study number.</p>"
        )
        parts = {
            "learn": ("Learn it in 5 minutes", learn_inner, paras),
            "visual": ("Visual", visual, [(lesson.get("figure") or {}).get("caption") or "Lesson flow."]),
            "example": ("Worked example", example, [lab.get("goal") or "", *(lab.get("steps") or []), lab.get("success") or ""]),
            "quiz": ("Quiz", quiz_html(lesson.get("quiz") or []), [item.get("q") or "" for item in lesson.get("quiz") or []]),
            "sources": ("Sources and go deeper", sources, []),
            "ecosystem": ("Ecosystem", eco_inner, []),
        }
        chunks = []
        for key, (title, inner, lines) in parts.items():
            section_rel = f"downloads/sections/{rid}-{key}.html"
            emit_export(section_rel, f"{lesson['title']} · {title}", inner, lines, source_rows, html_ready=(key == "sources"))
            links = [
                ("HTML", f"{prefix_dl}-{key}.html"),
                ("MD", f"{prefix_dl}-{key}.md"),
                ("PDF", f"{prefix_dl}-{key}.pdf"),
                ("DOCX", f"{prefix_dl}-{key}.docx"),
            ]
            if key == "visual":
                links = [("SVG", f"{diagram}.svg"), ("PNG", f"{diagram}.png"), ("HTML", f"{diagram}.html"), ("MD", f"{diagram}.md"), ("PDF", f"{diagram}.pdf")]
            if key == "sources":
                links.extend([
                    ("JSON", f"{rid}.sources.json"),
                    ("MD", f"{rid}.md"),
                    ("PDF", f"../downloads/rooms/{rid}.pdf"),
                    ("DOCX", f"../downloads/rooms/{rid}.docx"),
                ])
            visible = sources_html(source_rows, heading=False) if key == "sources" else inner
            chunks.append(section(key, title, visible, links))
        emit_export(
            f"downloads/diagrams/{rid}.html",
            lesson["title"],
            f'<div class="figure">{svg}</div><p>{esc((lesson.get("figure") or {}).get("caption") or "Lesson flow.")}</p>',
            [(lesson.get("figure") or {}).get("caption") or "Lesson flow."],
            source_rows,
        )
        body = (
            f'<p class="kicker">{esc(track["short"] if track.get("short") else track["title"])}</p>'
            f'<h1>{esc(lesson["title"])}</h1>'
            f'<p class="lede">{sentences(track.get("blurb") or track.get("summary") or "")}</p>'
            + "".join(chunks)
            + f'<p class="actions"><a href="../tracks/{track["id"]}.html">Back to {esc(track["title"])}</a></p>'
        )
        write_page(record["href"], lesson["title"], paras[0] if paras else lesson["title"], body, record["href"])
        kb.append({"id": rid, "title": lesson["title"], "href": record["href"], "blurb": (paras[0] if paras else lesson["title"])[:240]})
    (ROOT / "guide").mkdir(exist_ok=True)
    (ROOT / "guide" / "kb.json").write_text(json.dumps({"rooms": kb}, ensure_ascii=False), encoding="utf-8")
    return kb


def sheet(name: str, title: str, body: str, sources: list | None = None) -> None:
    rows = sources if sources is not None else sources_from_html(f"{title} {body}")
    plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body)).strip()
    emit_export(f"downloads/sheets/{name}.html", title, body, [plain], rows)


def build_sheets(tracks, uni, eco, certs, interview):
    for track in tracks:
        items = "".join(f"<li><strong>{esc(lesson['title'])}</strong> {esc((lesson.get('paragraphs') or [''])[0])}</li>" for lesson in track["lessons"])
        sheet(track["id"], track["title"], f"<p>{esc(track.get('summary') or '')}</p><ol>{items}</ol>", track_sources(track))
    glossary = "".join(
        f"<li><strong>{esc(term['term'])}</strong> {esc(term['meaning'])} <a href=\"{esc(term['url'])}\">{esc(term['source'])}</a></li>"
        for term in eco.get("glossary") or []
    )
    sheet("glossary", "Glossary", f"<ul>{glossary}</ul>")
    ports = "".join(
        f"<li>{esc(row['port'])} {esc(row['proto'])} {esc(row['dir'])} {esc(row['use'])} <a href=\"{esc(row['url'])}\">{esc(row['source'])}</a></li>"
        for row in uni.get("ports") or []
    )
    sheet("ports-protocols", "Ports and protocols", f"<p>Read on {esc(uni.get('readOn') or '')}. Confirm before relying.</p><ul>{ports}</ul>")
    plays = "".join(
        f"<li><strong>{esc(row['symptom'])}</strong> {esc(row['meaning'])}</li>" for row in uni.get("playbooks") or []
    )
    sheet("troubleshooting", "Troubleshooting", f"<ul>{plays}</ul>")
    bandwidth = "".join(
        f"<li>{esc(row['use'])}: min {esc(row['min'])}, recommended {esc(row['rec'])}. {esc(row['note'])}</li>"
        for row in uni.get("bandwidth") or []
    )
    sheet("bandwidth", "Bandwidth notes", f"<ul>{bandwidth}</ul><p>Source: the technical requirements PDF. Confirm before relying.</p>")
    customers = "".join(
        f"<li><strong>{esc(row['name'])}</strong> Vendor claims: {esc('; '.join(row.get('claims') or []))}. <a href=\"{esc(row['href'])}\">Case study</a></li>"
        for row in uni.get("customers") or []
    )
    sheet("customer-claims", "Vendor case studies", f"<p>These are the vendor's claims, not an audit. Confirm before relying.</p><ul>{customers}</ul>")
    roadmap = "".join(
        f"<li>{esc(row['when'])}: {esc(row['what'])} <a href=\"{esc(row['url'])}\">{esc(row['source'])}</a></li>"
        for row in uni.get("roadmap") or []
    )
    sheet("roadmap", "Dated notes", f"<ul>{roadmap}</ul>")
    cert_items = "".join(
        f"<li><strong>{esc(item['name'])}</strong> {esc(item['status'])}. {esc(item['detail'])}</li>" for item in certs.get("items") or []
    )
    sheet("certifications", "Certifications", f"<ul>{cert_items}</ul><p>Empty exam codes are intentional. Confirm before relying.</p>")
    qs = "".join(f"<li><strong>{esc(item['q'])}</strong> {esc(item['a'])}</li>" for item in interview.get("items") or [])
    sheet("interview", "Interview prompts", f"<p>Generic study answers. Not a person's work history.</p><ul>{qs}</ul>")
    sheet("config-checklist", "Config checklist", "<ol><li>Skills before users.</li><li>Lists and dispositions before the campaign.</li><li>One campaign profile at a time.</li><li>Start an inbound campaign or the DNIS stays quiet.</li><li>Confirm the live admin page before you change a domain.</li></ol>")
    sheet("crm-adapters", "CRM adapters", "<p>Named Plus adapters and the CRM SDK are different pipes. Package numbers move. Confirm before relying.</p>")
    sheet("e911", "E911 notes", "<p>The public E911 data sheet names emergency services and RedSky. Coverage claims are dated. Confirm before relying.</p>")
    sheet("security-compliance", "Security notes", "<p>Name the control you mean: profile permissions, trusted IP, STIR/SHAKEN, or retention. This sheet does not invent a control that the cited page does not name.</p>")
    sheet("migration-cutover", "Migration and cutover", "<p>A gateway story is not a UCCX import. Stop the morning if the gate you wrote down is red. Confirm before relying.</p>")


def build_templates():
    templates = {
        "campaign-checklist": (
            "Campaign checklist",
            ["Skills, users, lists, dispositions, and one profile before the campaign.", "Inbound and autodial add prompts and IVR.", "Confirm the planning topic before you rely on this order."],
        ),
        "ivr-notes": (
            "IVR notes",
            ["Module names follow the IVR Administrator's Guide.", "A Skill Transfer with no skill is described as the Default queue in the community article.", "This file is not a VCC import."],
        ),
        "cutover-plan": (
            "Cutover plan",
            ["Write the gate that can stop the morning.", "A Cisco, Avaya, or Asterisk gateway is a SIP story, not an importer.", "Confirm the technical requirements PDF before cutover."],
        ),
        "crm-worksheet": (
            "CRM worksheet",
            ["Name the Plus adapter or the CRM SDK.", "Do not copy a package number from memory.", "Confirm the technical requirements PDF."],
        ),
    }
    disclaimer = (
        "Independent, free, learning-only student project. Trademarks belong to their owners. "
        "Not affiliated or endorsed. Contact https://cyphermonkeylabs.com/#contact. Nothing is sold."
    )
    for name, (title, lines) in templates.items():
        body = "<ol>" + "".join(f"<li>{esc(line)}</li>" for line in lines) + "</ol>"
        rows = front_sources(title + " " + " ".join(lines))
        emit_export(f"downloads/templates/{name}.html", title, body, lines + [disclaimer], rows)


def build_flashcards(records):
    cards = []
    for record in records:
        lesson = record["lesson"]
        cite = (lesson.get("cites") or [{}])[0]
        for card in lesson.get("cards") or []:
            cards.append({
                "front": card.get("front") or "",
                "back": card.get("back") or "",
                "source": cite.get("label") or "",
                "url": cite.get("url") or "",
                "room": record["href"],
            })
    card_sources = {}
    for record in records:
        card_sources[record["href"]] = lesson_sources(record["lesson"])
    for card in cards:
        card["sources"] = card_sources.get(card["room"], [])
    (ROOT / "downloads" / "flashcards.json").write_text(json.dumps({"cards": cards}, ensure_ascii=False, indent=2), encoding="utf-8")
    items = "".join(
        f"<article><h2>{esc(card['front'])}</h2><p>{esc(card['back'])}</p><p><a href=\"{esc(card['url'])}\">{esc(card['source'])}</a></p>{sources_html(card['sources'])}</article>"
        for card in cards
    )
    lines = []
    for card in cards:
        lines.extend([card["front"], card["back"], card["source"], ""])
        lines.extend(sources_lines(card["sources"]))
        lines.append("")
    emit_export("downloads/flashcards.html", "Flashcards", items, lines, front_sources("flashcards ivr sip"), html_ready=True)


def build_deck(tracks):
    slides = [("Five9 Lab", "Independent study floor. Confirm before relying. Nothing here is a Five9 product.")]
    for track in tracks:
        slides.append((track["title"], track.get("summary") or track.get("blurb") or ""))
    slides.append(("Disclaimer", "Independent, free, learning-only student project. Contact https://cyphermonkeylabs.com/#contact."))
    door = front_sources("study deck")
    slides.append(("Sources and go deeper", " ".join(sources_lines(door))))
    (ROOT / "downloads" / "five9-study-deck.pptx").write_bytes(pptx_bytes(slides))


def find_record(records, track_id: str, lesson_id: str):
    for record in records:
        if record["track"]["id"] == track_id and record["lesson"]["id"] == lesson_id:
            return record
    return None


def opened_cite_bits(lesson: dict) -> str:
    bits = []
    for cite in lesson.get("cites") or []:
        label = str(cite.get("label") or "Source")
        url = str(cite.get("url") or "")
        if url.startswith("https://") and status_for(url) == "ok":
            bits.append(f'<a href="{esc(url)}">{esc(label)}</a>')
        else:
            bits.append(f"<strong>confirm</strong>. {esc(label)}. last checked 2026-10.")
    return " ".join(bits)


def cited_lesson(record) -> str:
    lesson = record["lesson"]
    paras = "".join(f"<p>{sentences(part)}</p>" for part in (lesson.get("paragraphs") or [])[:2])
    return (
        f'<article class="cite-block"><h3><a href="{esc(record["href"])}">{esc(lesson["title"])}</a></h3>'
        f"{paras}<p class=\"cite-line\">Opened in 2026-10: {opened_cite_bits(lesson)}</p></article>"
    )


def home_sources(records):
    picked = [
        find_record(records, "t01", "l01"),
        find_record(records, "t01", "l02"),
        find_record(records, "t01", "l04"),
    ]
    groups = [lesson_sources(record["lesson"]) for record in picked if record]
    groups.append(front_sources("domain skill sip ivr campaign contact center"))
    return merge_sources(groups)


def home_document(tracks, records, drawing_count: int):
    stats = (
        f'<div class="stat-row"><div class="stat"><b>{len(tracks)}</b> tracks</div>'
        f'<div class="stat"><b>{len(records)}</b> rooms</div>'
        f'<div class="stat"><b>{drawing_count}</b> drawings</div></div>'
    )
    track_cards = []
    for track in tracks:
        track_cards.append(
            f'<a class="room-card" href="tracks/{esc(track["id"])}.html"><p class="kicker">{esc(track.get("level") or "")}</p>'
            f'<strong>{esc(track["title"])}</strong><p>{esc(track.get("blurb") or "")}</p></a>'
        )
    overview_note = (
        f'<p class="lane-copy" data-sentence>{drawing_count} drawings. Each SVG is the diagram and the flow, counted once. '
        'The practice atlas is a separate set.</p>'
    )
    l01 = find_record(records, "t01", "l01")
    l02 = find_record(records, "t01", "l02")
    l04 = find_record(records, "t01", "l04")
    order = "".join(
        f'<li>{esc(row.get("label") or "")}</li>'
        for row in ((l01["lesson"].get("figure") or {}).get("rows") or [])
    ) if l01 else ""
    week = "".join(
        f'<li><a href="tracks/{esc(track["id"])}.html">{esc(track["title"])}</a>. {esc(track.get("summary") or track.get("blurb") or "")}</li>'
        for track in tracks[:8]
    )
    primer = (
        '<p data-sentence>The front door used to stop at the track tiles. These three rooms are the published build, with the pages that were opened in 2026-10.</p>'
        + (cited_lesson(l01) if l01 else "")
        + (cited_lesson(l02) if l02 else "")
        + (cited_lesson(l04) if l04 else "")
        + f'<h3>Outbound build order</h3><ol>{order}</ol>'
        + '<p data-sentence>Inbound and autodial add prompts and IVR scripts on that path. A DNIS stays quiet until the inbound campaign is running. A page that did not open is marked confirm and is not given a link.</p>'
        + f'<h3>A first pass through the floor</h3><ol>{week}</ol>'
    )
    rows = home_sources(records)
    return (
        '<section class="hero-stage">'
        '<div class="hero-grid" aria-hidden="true"></div>'
        '<div class="hero-orb hero-orb-a" aria-hidden="true"></div>'
        '<div class="hero-orb hero-orb-b" aria-hidden="true"></div>'
        '<div class="hero-orb hero-orb-c" aria-hidden="true"></div>'
        '<div class="hero-token hero-token-a" aria-hidden="true">🎧</div>'
        '<div class="hero-token hero-token-b" aria-hidden="true">📞</div>'
        '<div class="hero-copy">'
        '<p class="kicker">Five9 Virtual Contact Center</p>'
        '<h1 class="hero-title">Learn the floor without a live domain.</h1>'
        f'<p class="lede" data-sentence>{len(tracks)} tracks, from the domain model to skills, workforce, quality, CRM, and the ecosystem. Citations stay on the page. Confirm before relying.</p>'
        '<div class="actions"><a href="start.html#ten">Finish in 10 minutes</a><a href="start.html#full">Full course</a>'
        '<a href="downloads.html">Just download</a><a href="campus/index.html">Open app</a>'
        f'<a href="{REPO}">View repo</a></div>'
        '</div></section>'
        + section("primer", "Read this before you pick a track", primer, [("HTML", "downloads/sections/home-primer.html")])
        + section("sources", "Sources and go deeper", sources_html(rows, heading=False), [("HTML", "downloads/sections/home-sources.html")])
        + section("overview", "Start here", stats + overview_note, [("HTML", "downloads/sections/home-overview.html")])
        + section("tracks", "Tracks", f'<div class="card-grid">{"".join(track_cards)}</div>', [("HTML", "downloads/sections/home-tracks.html")])
    ), stats, overview_note, track_cards, primer, rows


def page_bodies(tracks, records, uni, eco, certs, interview, manifest):
    home, stats, overview_note, track_cards, primer, rows = home_document(tracks, records, len(manifest))
    door = front_sources("overview")
    emit_export("downloads/sections/home-primer.html", "Read this before you pick a track", primer, ["Domain, campaign types, and the outbound build order."], rows)
    emit_export("downloads/sections/home-sources.html", "Sources and go deeper", sources_html(rows), ["Sources and go deeper"], rows, html_ready=True)
    emit_export("downloads/sections/home-overview.html", "Five9 Lab overview", stats + overview_note, [f"{len(manifest)} drawings. Each SVG is the diagram and the flow, counted once."], door)
    emit_export("downloads/sections/home-tracks.html", "Tracks", f'<div class="card-grid">{"".join(track_cards)}</div>', [track["title"] for track in tracks], door)
    write_page("index.html", "Five9 Lab", "Independent study floor for Five9 Virtual Contact Center.", home, "index.html")

    ten = records[:3]
    ten_links = "".join(f'<li><a href="{esc(item["href"])}">{esc(item["lesson"]["title"])}</a></li>' for item in ten)
    full = "".join(
        f'<li><a href="tracks/{esc(track["id"])}.html">{esc(track["title"])}</a></li>' for track in tracks
    )
    start = (
        '<h1>Learn</h1>'
        + section("ten", "Finish in 10 minutes", f'<p data-sentence>Read these three rooms, then stop. They are the build order, the tenant, and the next object.</p><ol>{ten_links}</ol>', [("HTML", "downloads/sections/start-ten.html")])
        + section("full", "Full course", f'<p data-sentence>The full course is the {len(tracks)} tracks. Each room has a five-minute read, a drawing, an example, a quiz, sources, and an ecosystem panel.</p><ol>{full}</ol>', [("HTML", "downloads/sections/start-full.html")])
    )
    emit_export("downloads/sections/start-ten.html", "Ten minutes", f"<ol>{ten_links}</ol>", ["Ten minutes"], door)
    emit_export("downloads/sections/start-full.html", "Full course", f"<ol>{full}</ol>", ["Full course"], door)
    write_page("start.html", "Learn", "Ten-minute path and the full Five9 course.", start, "start.html")

    for track in tracks:
        links = []
        for record in records:
            if record["track"]["id"] == track["id"]:
                links.append(f'<a class="room-card" href="../{esc(record["href"])}"><strong>{esc(record["lesson"]["title"])}</strong><p>{esc((record["lesson"].get("paragraphs") or [""])[0][:180])}</p></a>')
        body = (
            f'<h1>{esc(track["title"])}</h1><p data-sentence>{esc(track.get("summary") or "")}</p>'
            f'<div class="card-grid">{"".join(links)}</div>{sources_html(track_sources(track))}'
        )
        write_page(f'tracks/{track["id"]}.html', track["title"], track.get("blurb") or track["title"], body, f'tracks/{track["id"]}.html')

    diagram_links = []
    for item in manifest:
        diagram_links.append(
            f'<article class="room-card"><h2>{esc(item["title"])}</h2>'
            f'{dl_links([("SVG", "../" + item["svg"] if False else item["svg"]), ("PNG", item["svg"].replace(".svg", ".png")), ("HTML", item["html"])])}</article>'
        )
    # hrefs from root
    cards = []
    for item in manifest:
        cards.append(
            f'<article class="panel"><h2>{esc(item["title"])}</h2>'
            f'{dl_links([("SVG", item["svg"]), ("PNG", item["svg"].replace(".svg", ".png")), ("HTML", item["html"])])}</article>'
        )
    sample = []
    for item in manifest[:8]:
        svg = (ROOT / item["svg"]).read_text(encoding="utf-8")
        sample.append(f'<article class="panel"><h2>{esc(item["title"])}</h2><div class="figure">{svg}</div></article>')
    diagrams_body = f'<h1>Diagrams</h1><p data-sentence>{len(manifest)} drawings. Eight are on this page. Every drawing has SVG, PNG, and HTML. The Flows page animates these same files. It is not a second library.</p>{"".join(sample)}<div class="card-grid">{"".join(cards)}</div>'
    write_page("diagrams.html", "Diagrams", "Five9 teaching diagrams.", section("gallery", "Gallery", diagrams_body, [("HTML", "downloads/sheets/t01.html")]), "diagrams.html")
    flows_body = f'<h1>Flows</h1><p data-sentence>The same {len(manifest)} drawings. The dashed line between steps is the motion. Count them once.</p>{"".join(sample)}'
    write_page("flows.html", "Flows", "Animated Five9 flows.", section("flows", "Flows", flows_body, [("HTML", "downloads/sheets/t01.html")]), "flows.html")

    bars = []
    max_lessons = max(len(track["lessons"]) for track in tracks)
    for track in tracks:
        width = int(100 * len(track["lessons"]) / max_lessons)
        bars.append(
            f'<div data-chart="lessons"><span>{esc(track["title"])}</span>'
            f'<svg viewBox="0 0 100 16" width="100%" height="16" role="img" aria-label="{esc(len(track["lessons"]))} lessons">'
            f'<rect x="0" y="2" width="{width}" height="12" fill="#7c3aed"/></svg></div>'
        )
    charts = f'<h1>Charts</h1><p data-sentence>These bars count lessons in this repository. They are not traffic, revenue, or a Five9 report.</p>{"".join(bars)}'
    write_page("charts.html", "Charts", "Repository counts.", section("charts", "Lesson counts", charts, [("HTML", "downloads/sections/charts.html")]), "charts.html")
    emit_export("downloads/sections/charts.html", "Lesson counts", charts, ["Lesson counts"], door)

    port = (uni.get("ports") or [{}])[0]
    play = (
        '<h1>Play</h1>'
        + section(
            "port-game",
            "Port match",
            f'<div data-port-game data-answer="{esc(port.get("port"))}"><p data-sentence>{esc(port.get("use") or "")}</p>'
            '<button type="button" data-port="80">80</button> <button type="button" data-port="443">443</button> '
            f'<button type="button" data-port="{esc(port.get("port"))}">{esc(port.get("port"))}</button>'
            '<p data-port-result aria-live="polite"></p><p>Confirm before relying. The community article wins if it moved.</p></div>',
            [("HTML", "downloads/sheets/ports-protocols.html")],
        )
        + section(
            "daily",
            "Daily question",
            quiz_html([records[0]["lesson"]["quiz"][0]]) if records[0]["lesson"].get("quiz") else "<p>No question.</p>",
            [("HTML", "downloads/sheets/interview.html")],
        )
    )
    write_page("play.html", "Play", "Port game and a daily question.", play, "play.html")

    listen = (
        '<h1>Listen</h1>'
        + section(
            "audio",
            "Study audio",
            '<p data-sentence>These clips are an espeak-ng study dialogue, not a Five9 recording.</p>'
            '<p><strong>How to use the floor</strong><br><audio controls preload="none" src="campus/audio/architect-floor.mp3"></audio></p>'
            '<p><strong>How to share the lab</strong><br><audio controls preload="none" src="campus/audio/architect-share.mp3"></audio></p>'
            '<p><a href="campus/audio/scripts/architect-floor.md">Script</a></p>',
            [("HTML", "downloads/sections/listen.html")],
        )
    )
    emit_export("downloads/sections/listen.html", "Listen", "<p>Study audio lives with the practice console.</p>", ["Study audio lives with the practice console."], door)
    write_page("listen.html", "Listen", "Study audio.", listen, "listen.html")

    help_body = (
        '<h1>Help</h1>'
        + section("menu", "Menu", '<p data-sentence>The Menu button is at the top left. The drawer slides in. Escape or the backdrop closes it. On a phone the bottom bar is Menu, Learn, Diagrams, Play, Listen, and Guide.</p>', [("HTML", "downloads/sections/help-menu.html")])
        + section("course", "Course", '<p data-sentence>Learn offers ten minutes or the full course. Every room has a short read, a drawing, an example, a quiz, sources, and an ecosystem panel.</p>', [("HTML", "downloads/sections/help-course.html")])
        + section("bot", "Bot", '<p data-sentence>The monkey greets once from the middle, then docks on the right. Drag it. Read along highlights the sentence and the menu chip. Voice input falls back to typing. Idle offers stop when you choose stop offering.</p><p><button type="button" data-replay-tour>Replay the tour</button></p>', [("HTML", "downloads/sections/help-bot.html")])
        + section("downloads-help", "Downloads", '<p data-sentence>Every section has a coloured download button. The Downloads page lists sheets, cards, templates, the deck, and one bundle.</p>', [("HTML", "downloads.html")])
    )
    for name, title in [("help-menu", "Menu"), ("help-course", "Course"), ("help-bot", "Bot")]:
        emit_export(f"downloads/sections/{name}.html", title, f"<p>{esc(title)} help for the Five9 lab.</p>", [f"{title} help for the Five9 lab."], door)
    write_page("help.html", "Help", "How to use the Five9 lab.", help_body, "help.html")

    legal = (
        '<h1>Legal and credits</h1>'
        + section("copyright", "Copyright and trademark", '<p data-sentence>Code is MIT. Lesson text is CC BY-NC-SA 4.0. Five9 names are trademarks of their owners. This lab is not a Five9 product.</p>', [("HTML", "downloads/sections/legal.html")])
        + section("licences", "Third-party licences", '<p data-sentence>Anime, D3, Rough, canvas-confetti, markmap, and Three.js keep their MIT licences under campus/vendor. The practice console loads them. This front door does not.</p>', [("HTML", "downloads/sections/legal.html")])
        + section("privacy", "Privacy", '<p data-sentence>No tracker is installed. Settings, the tour flag, and guide position stay in this browser. The guide does not call a server. The cloud endpoint is unset.</p>', [("HTML", "downloads/sections/legal.html")])
        + section("access", "Accessibility", '<p data-sentence>Font size and font colour are in the header. The drawer is a list of links. Reduced motion stops the glow loop and the flow dash.</p>', [("HTML", "downloads/sections/legal.html")])
        + section("removal", "Removal", f'<p data-sentence>A concern goes through the contact form at {CONTACT}. The page will be removed or corrected.</p>', [("HTML", "downloads/sections/legal.html")])
    )
    emit_export("downloads/sections/legal.html", "Legal", "<p>MIT code. CC BY-NC-SA content. Independent study.</p>", ["MIT code. CC BY-NC-SA content. Independent study."], door)
    write_page("legal.html", "Legal and credits", "Copyright, licences, privacy, and removal.", legal, "legal.html")

    glossary = "".join(
        f'<li><strong>{esc(term["term"])}</strong> {esc(term["meaning"])} <a href="{esc(term["url"])}">{esc(term["source"])}</a></li>'
        for term in eco.get("glossary") or []
    )
    integ = "".join(
        f'<li><strong>{esc(item["system"])}</strong> {esc(item["how"])} <a href="{esc(item["url"])}">{esc(item["source"])}</a></li>'
        for item in eco.get("integrations") or []
    )
    plays = "".join(f'<li><strong>{esc(row["symptom"])}</strong> {esc(row["meaning"])}</li>' for row in uni.get("playbooks") or [])
    customers = "".join(
        f'<li><strong>{esc(row["name"])}</strong> {esc("; ".join(row.get("claims") or []))} <a href="{esc(row["href"])}">Vendor page</a></li>'
        for row in uni.get("customers") or []
    )
    roadmap = "".join(f'<li>{esc(row["when"])}: {esc(row["what"])}</li>' for row in uni.get("roadmap") or [])
    eco_body = (
        '<h1>Ecosystem</h1>'
        + '<p data-sentence>This section is the glossary, the mind map, the sister technologies, the integration list, the teaching bridges, and the future hooks. The study track walks the same six parts.</p>'
        + '<p class="actions"><a href="tracks/t23.html">Open the ecosystem track</a></p>'
        + section("glossary", "Glossary", f'<ul>{glossary}</ul>', [("HTML", "downloads/sheets/glossary.html")])
        + section("map", "Mind map", f'<div class="figure">{eco.get("map") or ""}</div><p>{esc(eco.get("mapCaption") or "")}</p>', [("HTML", "downloads/sheets/glossary.html")])
        + section("sisters", "Sister technologies and integrations", f'<ul>{integ}</ul>', [("HTML", "downloads/sheets/crm-adapters.html")])
        + section("config", "Config and troubleshooting", f'<ul>{plays}</ul>', [("HTML", "downloads/sheets/troubleshooting.html"), ("HTML", "downloads/sheets/config-checklist.html")])
        + section("bridges", "Cross-platform bridges", '<p data-sentence>Cisco, Avaya, and Asterisk appear as gateway stories on the technical requirements PDF. UCCX and UCCE are teaching bridges in the migration track. There is no import button.</p>', [("HTML", "downloads/sheets/migration-cutover.html")])
        + section("customers", "Customer integrations", f'<p>Vendor case-study claims. Confirm before relying.</p><ul>{customers}</ul>', [("HTML", "downloads/sheets/customer-claims.html")])
        + section("future", "Future hooks and the roadmap", f'<ul>{roadmap}</ul><p>The guide cloud endpoint is unset. Confirm before relying on a date.</p>', [("HTML", "downloads/sheets/roadmap.html")])
    )
    write_page("ecosystem.html", "Ecosystem", "Glossary, map, bridges, and future hooks.", eco_body, "ecosystem.html")
    write_page("glossary.html", "Glossary", "Five9 terms with sources.", section("terms", "Terms", f'<ul>{glossary}</ul>', [("HTML", "downloads/sheets/glossary.html"), ("JSON", "downloads/flashcards.json")]), "glossary.html")

    ports = "".join(
        f'<tr><td>{esc(row["port"])}</td><td>{esc(row["proto"])}</td><td>{esc(row["dir"])}</td><td>{esc(row["use"])}</td><td><a href="{esc(row["url"])}">{esc(row["source"])}</a></td></tr>'
        for row in uni.get("ports") or []
    )
    write_page("ports.html", "Ports", "Ports named on public Five9 pages.", section("ports", "Ports", f'<p>Read on {esc(uni.get("readOn") or "")}. Confirm before relying.</p><table><thead><tr><th>Port</th><th>Proto</th><th>Dir</th><th>Use</th><th>Source</th></tr></thead><tbody>{ports}</tbody></table>', [("HTML", "downloads/sheets/ports-protocols.html")]), "ports.html")

    cert_items = "".join(
        f'<li><strong>{esc(item["name"])}</strong> {esc(item["status"])}. {esc(item["detail"])} <a href="{esc(item["url"])}">{esc(item["source"])}</a></li>'
        for item in certs.get("items") or []
    )
    uncertain = "".join(f'<li class="callout">Confirm before relying. {esc(item)}</li>' for item in certs.get("uncertain") or [])
    write_page("certs.html", "Certifications", "Public Five9 training names.", section("certs", "What this lab could verify", f'<ul>{cert_items}</ul><ul>{uncertain}</ul>', [("HTML", "downloads/sheets/certifications.html")]), "certs.html")

    qs = "".join(
        f'<article class="panel"><h2>{esc(item["q"])}</h2><p>{esc(item["a"])}</p><p><a href="{esc(item["url"])}">{esc(item["source"])}</a></p></article>'
        for item in interview.get("items") or []
    )
    write_page("interviews.html", "Interview prep", "Generic study answers with sources.", section("bank", "Question bank", f'<p data-sentence>These answers are generic. They are not a claim about anyone\'s job history.</p>{qs}', [("HTML", "downloads/sheets/interview.html"), ("JSON", "downloads/flashcards.json")]), "interviews.html")

    careers = (
        '<h1>Careers</h1>'
        + section("frames", "Study frames", '<p data-sentence>Administrator, IVR, dialer and compliance, SIP, workforce engagement, and migration are study frames in this lab. They are not job requisitions and they are not a person\'s résumé.</p><p>No salary, no headcount, and no claim that a certificate is required.</p>', [("HTML", "downloads/sheets/certifications.html")])
    )
    write_page("careers.html", "Careers", "Study frames, not job requisitions.", careers, "careers.html")

    search_items = []
    for record in records:
        hay = f'{record["lesson"]["title"]} {record["track"]["title"]}'
        search_items.append(
            f'<a class="room-card" data-search-item="{esc(hay)}" href="{esc(record["href"])}"><strong>{esc(record["lesson"]["title"])}</strong><p>{esc(record["track"]["title"])}</p></a>'
        )
    search = f'<h1>Search</h1><form data-site-search role="search"><input data-search-echo type="search" aria-label="Search rooms" placeholder="Search rooms"></form><div class="card-grid" data-search-list>{"".join(search_items)}</div>'
    write_page("search.html", "Search", "Find a Five9 room.", search, "search.html")

    groups = [
        ("Sheets", "downloads/sheets"),
        ("Diagrams", "downloads/diagrams"),
        ("Templates", "downloads/templates"),
    ]
    download_cards = [
        '<article class="panel"><h2>Flashcards</h2>' + dl_links([
            ("JSON", "downloads/flashcards.json"),
            ("HTML", "downloads/flashcards.html"),
            ("PDF", "downloads/flashcards.pdf"),
            ("MD", "downloads/flashcards.md"),
            ("DOCX", "downloads/flashcards.docx"),
        ]) + "</article>",
        '<article class="panel"><h2>Study deck</h2>' + dl_links([("PPTX", "downloads/five9-study-deck.pptx")]) + "</article>",
        '<article class="panel"><h2>Everything</h2><p>One optional bundle of this downloads folder.</p>' + dl_links([("ZIP", "downloads/five9-lab-bundle.zip")]) + "</article>",
        '<div class="actions"><a href="campus/index.html">Open app</a>'
        f'<a href="{REPO}">View repo</a></div>',
    ]
    for folder_name, folder in groups:
        links = []
        for path in sorted((ROOT / folder).glob("*")):
            if path.suffix.lower() not in {".html", ".svg", ".png", ".pdf", ".docx", ".json", ".md"}:
                continue
            if path.name.endswith(".html") or path.suffix.lower() in {".svg", ".png", ".pdf", ".docx"}:
                links.append((path.suffix.upper().lstrip("."), f"{folder}/{path.name}"))
        # Keep the downloads page from listing every diagram twice in a giant unreadable dump: group by stem for diagrams.
        download_cards.append(f'<h2>{esc(folder_name)}</h2>')
        if folder_name == "Diagrams":
            download_cards.append(f'<p>{len(manifest)} diagrams. Open the <a href="diagrams.html">diagrams page</a> for the full list. A sample:</p>')
            for item in manifest[:6]:
                download_cards.append(
                    f'<article class="panel"><h3>{esc(item["title"])}</h3>'
                    + dl_links([
                        ("SVG", item["svg"]),
                        ("PNG", item["svg"].replace(".svg", ".png")),
                        ("HTML", item["html"]),
                    ])
                    + "</article>"
                )
        else:
            stems = {}
            for path in sorted((ROOT / folder).glob("*")):
                stems.setdefault(path.stem, []).append(path)
            for stem, paths in list(stems.items())[:40]:
                download_cards.append(
                    f'<article class="panel"><h3>{esc(stem)}</h3>'
                    + dl_links([(p.suffix.upper().lstrip("."), f"{folder}/{p.name}") for p in paths])
                    + "</article>"
                )
    download_sources = front_sources("downloads sheets flashcards ivr sip ports contact center")
    downloads = (
        '<h1>Downloads</h1><p data-sentence>Standalone files. Each one carries the disclaimer and a Sources and go deeper block. '
        'A page that did not open is marked confirm and is not given a link.</p>'
        + sources_html(download_sources)
        + "".join(download_cards)
    )
    write_page("downloads.html", "Downloads", "Sheets, cards, templates, and a bundle.", section("library", "Library", downloads, [("ZIP", "downloads/five9-lab-bundle.zip")]), "downloads.html")


def make_zip():
    target = ROOT / "downloads" / "five9-lab-bundle.zip"
    if target.exists():
        target.unlink()
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as zipped:
        for path in (ROOT / "downloads").rglob("*"):
            if not path.is_file() or path.name == "five9-lab-bundle.zip":
                continue
            zipped.write(path, path.relative_to(ROOT / "downloads"))


def patch_campus():
    page_path = ROOT / "campus" / "index.html"
    text = page_path.read_text(encoding="utf-8")
    text = text.replace('data-theme="neon"', 'data-theme="light"', 1)
    text = text.replace('document.documentElement.dataset.theme = "neon";', 'document.documentElement.dataset.theme = "light";')
    text = re.sub(r'\s*<div class="utilbar" id="utilbar">[\s\S]*?</div>\s*', "\n", text, count=1)
    text = re.sub(r'\s*<button type="button" class="btn links-toggle"[\s\S]*?</button>', "", text, count=1)
    text = re.sub(
        r'<a class="brand-link" href="https://(?:github\.com/cipher0x9|x\.com/[^"]+|huggingface\.co/[^"]+)"[\s\S]*?</a>',
        "",
        text,
    )
    text = re.sub(r'<nav class="brand-links" aria-label="Site links">[\s\S]*?</nav>', "", text, count=1)
    text = re.sub(r'<p><a href="https://github.com/CypherMonkeyLabs/five9-lab-free-university-mesmerizing">Rate, comment, help</a>[\s\S]*?</p>', "", text)
    text = re.sub(r'<div>\s*<p class="kicker">Next lab</p>[\s\S]*?</div>\s*', "", text, count=1)
    if "learning-only student project" not in text:
        text = text.replace(
            '<footer class="site-footer">',
            footer(),
            1,
        )
    else:
        text = re.sub(
            r'<footer class="site-footer lab-footer" data-canon-footer>[\s\S]*?</footer>',
            footer(),
            text,
            count=1,
        )
    if 'href="../assets/css/footer.css"' not in text:
        text = text.replace(
            '<link rel="stylesheet" href="css/app.css">',
            '<link rel="stylesheet" href="css/app.css">\n  <link rel="stylesheet" href="../assets/css/footer.css">',
            1,
        )
    text = text.replace('id="menu-toggle"', 'id="tour-menu"', 1)
    text = text.replace('<a class="brand" href="#/">', '<a class="brand" id="tour-home" href="#/">', 1)
    text = text.replace('<a href="#/tracks" data-tab="learn">', '<a id="tour-learn" href="#/tracks" data-tab="learn">', 1)
    text = text.replace('<a href="#/atlas" data-tab="diagrams">', '<a id="tour-diagrams" href="#/atlas" data-tab="diagrams">', 1)
    text = text.replace('<a href="#/play" data-tab="play">', '<a id="tour-play" href="#/play" data-tab="play">', 1)
    if 'id="tour-downloads"' not in text:
        text = text.replace(
            '<a href="#/offline"',
            '<a id="tour-downloads" href="#/offline"',
            1,
        )
    old_bar = """  <nav class="tabbar" id="tabbar" aria-label="Quick bar">
    <a id="tour-learn" href="#/tracks" data-tab="learn">"""
    # Reorder only if the learn link is still first. Build a known bar if the original order remains.
    if 'id="tab-menu"' in text and 'data-open-guide' not in text:
        text = text.replace(
            '<nav class="tabbar" id="tabbar" aria-label="Quick bar">',
            '<nav class="tabbar" id="tabbar" aria-label="Quick bar">\n    <button type="button" id="tab-menu" data-open-menu aria-expanded="false" aria-controls="phone-menu"><span class="tab-ico" data-icon="menu" aria-hidden="true"></span><span class="tab-label">Menu</span></button>',
            1,
        )
        text = re.sub(
            r'\s*<button type="button" id="tab-menu" aria-expanded="false" aria-controls="phone-menu"><span class="tab-ico" data-icon="menu" aria-hidden="true"></span><span class="tab-label">Menu</span><span class="tab-desc">All pages</span></button>',
            "",
            text,
            count=1,
        )
        text = text.replace(
            "</nav>\n  <dialog id=\"phone-menu\"",
            '<button type="button" data-open-guide><span class="tab-label">Guide</span></button>\n  </nav>\n  <dialog id="phone-menu"',
            1,
        )
    if 'id="set-ink"' not in text:
        text = text.replace(
            '<label for="set-font">Text size</label>',
            '<label for="set-ink">Font colour</label>\n      <input id="set-ink" type="color" value="#142033">\n    </div>\n    <div class="field">\n      <label for="set-font">Text size</label>',
            1,
        )
    if 'src="../guide/guide.js"' not in text:
        text = text.replace(
            '<html lang="en"',
            '<html lang="en" data-root="../"',
            1,
        )
        text = text.replace(
            '<script type="module" src="js/app.js"></script>',
            '<script type="module" src="js/app.js"></script>\n  <script src="../guide/guide.js"></script>',
            1,
        )
    page_path.write_text(text, encoding="utf-8")

    footer_html = f'<footer data-canon-footer>{disclaimer_block()}</footer>'
    for path in (ROOT / "campus" / "downloads").glob("*.html"):
        file_text = path.read_text(encoding="utf-8")
        file_text = re.sub(r"<footer[\s\S]*?</footer>", footer_html, file_text, count=1)
        if "data-canon-footer" not in file_text:
            file_text = file_text.replace("</body>", footer_html + "</body>")
        path.write_text(file_text, encoding="utf-8")


def main():
    if "--zip-only" in sys.argv:
        make_zip()
        print("zip", (ROOT / "downloads" / "five9-lab-bundle.zip").stat().st_size)
        return
    tracks = load_tracks()
    eco = load_json(DATA / "ecosystem.json")
    uni = load_json(DATA / "university.json")
    certs = load_json(DATA / "certs.json")
    interview = load_json(DATA / "interview.json")
    records = room_records(tracks)
    for folder in (OUT_DIAG, OUT_SHEETS, OUT_SECTIONS, OUT_TEMPLATES, ROOT / "rooms", ROOT / "tracks", ROOT / "guide"):
        folder.mkdir(parents=True, exist_ok=True)
    manifest = build_diagrams(records)
    build_rooms(records, eco)
    build_sheets(tracks, uni, eco, certs, interview)
    build_templates()
    build_flashcards(records)
    build_deck(tracks)
    page_bodies(tracks, records, uni, eco, certs, interview, manifest)
    (ROOT / "downloads" / "manifest.json").write_text(json.dumps({"diagrams": manifest, "rooms": len(records), "tracks": len(tracks)}, ensure_ascii=False), encoding="utf-8")
    (DATA / "section-sources.json").write_text(
        json.dumps({"checked": "2026-10", "sections": pack_sections(uni, eco)}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    patch_campus()
    print(f"rooms {len(records)} diagrams {len(manifest)} tracks {len(tracks)}")


if __name__ == "__main__":
    main()
