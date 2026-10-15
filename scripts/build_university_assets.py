#!/usr/bin/env python3
"""Build search, daily, flashcard, cheat-sheet, and offline-pack files.

Sheets are original study notes that point at Five9's pages. They do not copy
vendor manuals.
"""

from __future__ import annotations

import html
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAMPUS = ROOT / "campus"
DOWNLOADS = CAMPUS / "downloads"
REPO = "https://github.com/cipher0x9/five9-lab-free-university-mesmerizing"
FOOT = [
    "CYPHER0X9 Five9 Lab. Independent study. Not affiliated with Five9.",
    "https://cyphermonkeylabs.com",
    "https://linktr.ee/cyphermonkey",
    REPO,
    "MIT code, CC BY-NC-SA content. Trademarks belong to their owners.",
]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def pdf_escape(text: str) -> str:
    clean = "".join(ch if 32 <= ord(ch) < 127 else " " for ch in text)
    return clean.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def write_pdf(path: Path, pages: list[list[str]]) -> None:
    objects: list[bytes] = []

    def add(data: bytes) -> int:
        objects.append(data)
        return len(objects)

    font_id = add(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    page_ids = []
    content_ids = []
    for lines in pages:
        commands = ["BT", "/F1 10 Tf", "48 740 Td", "14 TL"]
        for line in lines:
            commands.append(f"({pdf_escape(line)}) Tj")
            commands.append("T*")
        commands.append("ET")
        stream = "\n".join(commands).encode("latin-1", "replace")
        content_ids.append(add(b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream"))
        page_ids.append(None)
    kids = []
    for content_id in content_ids:
        kids.append(
            add(
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
                f"/Contents {content_id} 0 R /Resources << /Font << /F1 {font_id} 0 R >> >> >>".encode()
            )
        )
    pages_id = add(f"<< /Type /Pages /Kids [{' '.join(f'{kid} 0 R' for kid in kids)}] /Count {len(kids)} >>".encode())
    # Parent was hard-coded as 2 0 R. Rebuild page objects so parent matches pages_id.
    # Simpler: write catalog pointing at pages_id and fix parent by regenerating.
    catalog_id = add(f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode())
    # Fix parent references now that pages_id is known.
    fixed = []
    for obj in objects:
        fixed.append(obj.replace(b"/Parent 2 0 R", f"/Parent {pages_id} 0 R".encode()))
    objects = fixed
    out = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for index, obj in enumerate(objects, start=1):
        offsets.append(len(out))
        out.extend(f"{index} 0 obj\n".encode())
        out.extend(obj)
        out.extend(b"\nendobj\n")
    xref = len(out)
    out.extend(f"xref\n0 {len(objects) + 1}\n".encode())
    out.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        out.extend(f"{offset:010d} 00000 n \n".encode())
    out.extend(f"trailer << /Size {len(objects) + 1} /Root {catalog_id} 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    path.write_bytes(out)


def wrap_lines(lines: list[str], width: int = 92) -> list[str]:
    wrapped = []
    for line in lines:
        words = line.split()
        if not words:
            wrapped.append("")
            continue
        current = words[0]
        for word in words[1:]:
            trial = f"{current} {word}"
            if len(trial) > width:
                wrapped.append(current)
                current = word
            else:
                current = trial
        wrapped.append(current)
    return wrapped


def paginate(lines: list[str], size: int = 46) -> list[list[str]]:
    lines = wrap_lines(lines, 92)
    pages = []
    chunk: list[str] = []
    for line in lines:
        chunk.append(line)
        if len(chunk) >= size:
            pages.append(chunk)
            chunk = []
    if chunk:
        pages.append(chunk)
    return pages or [["(empty)"]]


def sheet_html(title: str, lines: list[str], sources: list[tuple[str, str]]) -> str:
    body = "\n".join(f"<li>{html.escape(line)}</li>" for line in lines)
    cites = "\n".join(
        f'<li><a href="{html.escape(url)}">{html.escape(label)}</a></li>' for label, url in sources
    )
    foot = " · ".join(f'<a href="{html.escape(item)}">{html.escape(item)}</a>' if item.startswith("http") else html.escape(item) for item in FOOT)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{html.escape(title)}</title>
  <style>
    @page {{ size: letter; margin: 0.6in; }}
    body {{ font: 13px/1.35 "Segoe UI", sans-serif; color: #142033; margin: 24px; }}
    h1 {{ font-size: 22px; margin: 0 0 8px; }}
    ol {{ margin: 0; padding-left: 18px; }}
    li {{ margin: 3px 0; }}
    footer {{ margin-top: 16px; font-size: 11px; color: #334; border-top: 1px solid #ccc; padding-top: 8px; }}
    a {{ color: #0b4f66; }}
  </style>
</head>
<body>
  <h1>{html.escape(title)}</h1>
  <p>Five9 Lab study card. Numbers and names point at the sources. This is not a Five9 document.</p>
  <ol>{body}</ol>
  <h2>Sources</h2>
  <ol>{cites}</ol>
  <footer>{foot}</footer>
</body>
</html>
"""


def write_png(path: Path, title: str, lines: list[str]) -> None:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        path.write_bytes(tiny_png(title))
        return
    image = Image.new("RGB", (1100, 1400), "#f6f1e6")
    draw = ImageDraw.Draw(image)
    draw.rectangle((24, 24, 1076, 1376), outline="#0f5f78", width=4)
    draw.text((48, 48), title[:70], fill="#0f5f78")
    y = 100
    for line in wrap_lines(lines, 78)[:42]:
        draw.text((48, y), line, fill="#1c1915")
        y += 26
    y = 1280
    for line in FOOT:
        draw.text((48, y), line[:110], fill="#3f3a33")
        y += 18
    image.save(path, "PNG")


def tiny_png(title: str) -> bytes:
    # 1x1 fallback if Pillow is missing. The HTML and PDF still exist.
    return bytes.fromhex(
        "89504e470d0a1a0a0000000d4948445200000001000000010802000000907753de"
        "0000000c4944415408d763f8cf0000000300015af5a5c00000000049454e44ae426082"
    )


def main() -> None:
    DOWNLOADS.mkdir(exist_ok=True)
    uni = load(CAMPUS / "data" / "university.json")
    eco = load(CAMPUS / "data" / "ecosystem.json")
    catalog = load(CAMPUS / "data" / "catalog.json")
    items = []
    bank = []
    cards = []
    for meta in catalog["tracks"]:
        track = load(CAMPUS / "data" / meta["file"])
        items.append({
            "href": f"#/track/{track['id']}",
            "title": track["title"],
            "note": track.get("group", ""),
            "snippet": track.get("summary", ""),
        })
        for lesson in track["lessons"]:
            href = f"#/lesson/{track['id']}/{lesson['id']}"
            snippet = " ".join(lesson.get("paragraphs") or [])[:240]
            items.append({
                "href": href,
                "title": lesson["title"],
                "note": track["title"],
                "snippet": snippet,
            })
            cite = (lesson.get("cites") or [{"label": "Lesson", "url": REPO}])[0]
            for quiz in lesson.get("quiz") or []:
                bank.append({
                    "q": quiz["q"],
                    "choices": quiz["choices"],
                    "answer": quiz["answer"],
                    "why": quiz.get("why", ""),
                    "href": href,
                    "track": track["title"],
                    "url": cite["url"],
                    "source": cite["label"],
                })
            for card in lesson.get("cards") or []:
                cards.append({
                    "front": card["front"],
                    "back": card["back"],
                    "track": track["title"],
                    "lesson": lesson["title"],
                    "href": href,
                })
    for row in eco["glossary"]:
        items.append({
            "href": "#/ecosystem",
            "title": row["term"],
            "note": "Glossary",
            "snippet": row["meaning"],
        })
    for book in uni["playbooks"]:
        items.append({
            "href": "#/trouble",
            "title": book["symptom"],
            "note": "Playbook",
            "snippet": " ".join(book["tree"]),
        })
    pages = [
        ("#/atlas", "Architecture atlas"),
        ("#/deploy", "Deployment"),
        ("#/migrate", "Migration and cutover"),
        ("#/ports", "Ports and protocols"),
        ("#/sip", "SIP and PSTN"),
        ("#/wfm", "Workforce management"),
        ("#/record", "Recording and quality"),
        ("#/e911", "E911"),
        ("#/analytics", "Reporting"),
        ("#/integrations", "CRM and APIs"),
        ("#/ai", "AI agents"),
        ("#/security", "Security"),
        ("#/roadmap", "Roadmap"),
        ("#/career", "Career"),
        ("#/downloads", "Cheat codes"),
        ("#/daily", "Daily challenge"),
    ]
    for href, title in pages:
        items.append({"href": href, "title": title, "note": "University", "snippet": title})
    (CAMPUS / "data" / "search-index.json").write_text(json.dumps({"items": items}, indent=2), encoding="utf-8")
    (CAMPUS / "data" / "daily-bank.json").write_text(json.dumps({"items": bank}, indent=2), encoding="utf-8")
    (DOWNLOADS / "flashcards.json").write_text(json.dumps({"cards": cards}, indent=2), encoding="utf-8")

    pdf_src = "https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf"
    port_src = "https://community.five9.com/s/article/Network-Port-Requirements-for-Softphone-Gateway-PSTN-Customers?language=en_US"
    sheets = []

    def add_sheet(slug, title, lines, sources):
        sheets.append({"slug": slug, "title": title, "lines": lines, "sources": sources})

    add_sheet(
        "ports-protocols",
        "Ports and protocols",
        [f"{row['port']} {row['proto']} {row['dir']}: {row['use']}" for row in uni["ports"]],
        [(row["source"], row["url"]) for row in uni["ports"][:4]] + [("Community port article", port_src)],
    )
    add_sheet(
        "bandwidth",
        "G.711 bandwidth extras",
        [f"{row['use']}: min {row['min']}, recommended {row['rec']}. {row['note']}" for row in uni["bandwidth"]],
        [("Technical requirements PDF", pdf_src)],
    )
    add_sheet(
        "call-flows",
        "Call flows to say out loud",
        [
            "Inbound: DNIS, running campaign, IVR, named skill, agent.",
            "No skill on Skill Transfer: Default queue.",
            "Outbound build: skills, users, lists, dispositions, one profile, campaign.",
            "Preview reads first. Progressive is one call per free agent on the outbound page.",
            "Power uses a ratio. Predictive can drop. Manual touch is typed.",
            "Voice up and pop down means the adapter path, HTTPS and WSS, failed separately.",
            "SIP ladder on the atlas is a teaching drawing, not a pcap.",
        ],
        [
            ("Planning your implementation", "https://documentation.five9.com/bundle/basic-admin/page/basic-admin/intro/planning-your-implementation.htm"),
            ("Inbound campaigns", "https://documentation.five9.com/bundle/campaign-admin/page/campaign-admin/creating-campaigns/types-of-campaigns/inbound-campaigns.htm"),
            ("Skill Transfer", "https://community.five9.com/s/article/Administrator-IVR-Skill-Transfer-Module-Functions-and-Features"),
        ],
    )
    config_lines = []
    for block in uni["sections"]["config"]["blocks"]:
        if block["kind"] in ("steps",):
            config_lines.append(block["h"])
            config_lines.extend(block["items"])
    add_sheet(
        "config-checklist",
        "Configuration checklist",
        config_lines,
        [(item["label"], item["url"]) for item in uni["sections"]["config"]["blocks"][-1]["items"]],
    )
    add_sheet(
        "troubleshooting",
        "Troubleshooting tree",
        [f"{book['symptom']} First check: {book['tree'][0]}" for book in uni["playbooks"]],
        [(book["source"], book["url"]) for book in uni["playbooks"]],
    )
    add_sheet(
        "glossary",
        "Glossary starter",
        [f"{row['term']}: {row['meaning']}" for row in eco["glossary"][:18]],
        [(row["source"], row["url"]) for row in eco["glossary"][:8]],
    )
    add_sheet(
        "migration-cutover",
        "Migration cutover card",
        uni["sections"]["migrate"]["blocks"][2]["items"] + uni["sections"]["migrate"]["blocks"][1]["items"],
        [(item["label"], item["url"]) for item in uni["sections"]["migrate"]["blocks"][-1]["items"]],
    )
    add_sheet(
        "crm-adapters",
        "CRM and API card",
        [
            "Plus adapters: Toolkit, Epic, Dynamics 365, NetSuite, Oracle, Salesforce, ServiceNow, Zendesk.",
            "They use HTTPS and Secure WebSocket.",
            "ServiceNow releases named in the October 2026 PDF read: Australia, Zurich, Yokohama.",
            "A Web Connector is not an adapter. IVR Salesforce modules are not the desktop adapter.",
            "Do not quote a Salesforce package number from this card.",
        ],
        [("Technical requirements PDF", pdf_src), ("APIs and SDKs", "https://www.five9.com/platform/integrations-and-ecosystem/apis-and-sdks")],
    )
    add_sheet(
        "e911",
        "E911 card",
        [
            "Dispatchable location is the room, not the headquarters lobby.",
            "The November 2022 data sheet names RedSky. It is a dated source.",
            "MyE911 history can show time, user, number, location, recording, and SIP invite.",
            "Do not place a live 911 test except the way local rules allow.",
        ],
        [
            ("E911 data sheet", "https://www.five9.com/sites/default/files/2022-11/Data-sheet-Five9-emergency-services%20%28E911%29.PDF"),
            ("MyE911 call history", "https://community.five9.com/s/article/MyE911-Call-History?language=en_US"),
        ],
    )
    add_sheet(
        "security-compliance",
        "Security and compliance card",
        [
            "TLS 1.2 is required. TLS 1.1 is not supported.",
            "This card does not copy the cipher list. Open the PDF.",
            "Certified Caller is STIR/SHAKEN. Profile ANI is a different field.",
            "TCPA manual touch blocks paste.",
            "The abandon percentage is a campaign field. This card states no default.",
            "Web admin bypasses Trusted IP, per the September 2026 page.",
        ],
        [
            ("Technical requirements PDF", pdf_src),
            ("Certified Caller", "https://www.five9.com/resources/five9_certified_caller"),
            ("TCPA manual touch", "https://community.five9.com/s/article/Administrator-TCPA-Manual-Touch-Dialing-Mode?language=en_US"),
        ],
    )
    manifest_files = []
    for sheet in sheets:
        lines = sheet["lines"] + [""] + FOOT
        html_name = f"{sheet['slug']}.html"
        pdf_name = f"{sheet['slug']}.pdf"
        png_name = f"{sheet['slug']}.png"
        (DOWNLOADS / html_name).write_text(sheet_html(sheet["title"], sheet["lines"], sheet["sources"]), encoding="utf-8")
        write_pdf(DOWNLOADS / pdf_name, paginate(lines))
        write_png(DOWNLOADS / png_name, sheet["title"], sheet["lines"])
        for kind, name in (("HTML", html_name), ("PDF", pdf_name), ("PNG", png_name)):
            manifest_files.append({"title": f"{sheet['title']} ({kind})", "href": f"downloads/{name}", "kind": kind})

    card_lines = []
    for card in cards:
        card_lines.append(f"Q: {card['front']}")
        card_lines.append(f"A: {card['back']}")
        card_lines.append(f"   {card['track']}")
        card_lines.append("")
    write_pdf(DOWNLOADS / "flashcards.pdf", paginate(card_lines + FOOT, 40))
    card_items = "\n".join(
        f"<article class='card'><h2>{html.escape(card['front'])}</h2><p>{html.escape(card['back'])}</p><p>{html.escape(card['track'])}</p></article>"
        for card in cards
    )
    (DOWNLOADS / "flashcards.html").write_text(
        f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Five9 Lab flashcards</title>
        <style>body{{font:15px/1.4 sans-serif;margin:24px}} .card{{break-inside:avoid;border:1px solid #ccc;padding:12px;margin:8px 0}} footer{{font-size:12px}}</style></head>
        <body><h1>Flashcards ({len(cards)})</h1>{card_items}<footer>{" · ".join(html.escape(x) for x in FOOT)}</footer></body></html>""",
        encoding="utf-8",
    )
    manifest_files.append({"title": "Flashcards (JSON)", "href": "downloads/flashcards.json", "kind": "JSON"})
    manifest_files.append({"title": "Flashcards (printable HTML)", "href": "downloads/flashcards.html", "kind": "HTML"})
    manifest_files.append({"title": "Flashcards (PDF)", "href": "downloads/flashcards.pdf", "kind": "PDF"})

    (DOWNLOADS / "manifest.json").write_text(json.dumps({"files": manifest_files}, indent=2), encoding="utf-8")
    (DOWNLOADS / "START.txt").write_text(
        "Serve this folder (it is the campus) and open index.html.\n"
        "ES modules may not run from a file:// URL.\n" + "\n".join(FOOT) + "\n",
        encoding="utf-8",
    )

    pack = []
    for path in sorted(CAMPUS.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(CAMPUS).as_posix()
        if rel == "downloads/five9-lab-offline.zip":
            continue
        pack.append(rel)
    (CAMPUS / "data" / "pack-manifest.json").write_text(json.dumps({"files": pack}, indent=2), encoding="utf-8")
    # The manifest must include itself. It was written after the walk, so add it.
    if "data/pack-manifest.json" not in pack:
        pack.append("data/pack-manifest.json")
        (CAMPUS / "data" / "pack-manifest.json").write_text(json.dumps({"files": pack}, indent=2), encoding="utf-8")

    manifest_files.append({"title": "Full offline bundle (zip)", "href": "downloads/five9-lab-offline.zip", "kind": "ZIP"})
    (DOWNLOADS / "manifest.json").write_text(json.dumps({"files": manifest_files}, indent=2), encoding="utf-8")
    zip_path = DOWNLOADS / "five9-lab-offline.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for rel in pack:
            if rel == "downloads/five9-lab-offline.zip":
                continue
            archive.write(CAMPUS / rel, rel)
    print(json.dumps({
        "search": len(items),
        "daily": len(bank),
        "cards": len(cards),
        "sheets": len(sheets),
        "pack": len(pack),
        "zip": zip_path.stat().st_size,
    }))


if __name__ == "__main__":
    main()
