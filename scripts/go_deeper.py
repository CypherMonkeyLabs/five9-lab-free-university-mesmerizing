"""Sources and go deeper. Statuses come from campus/data/source-checks.json.

Each URL in that file was opened in October 2026. ok means the page came back.
confirm means it did not. Missing URLs stay confirm. This module does not invent URLs.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = json.loads((ROOT / "campus" / "data" / "source-checks.json").read_text(encoding="utf-8"))
CHECKED = CHECKS["checked"]

# keyword pattern, primary pages, wikipedia only when no primary for that topic was added.
TOPICS = [
    {
        "keywords": [r"\bports?\b", r"\bfirewall\b"],
        "primary": [("IANA service names and port numbers", "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml", "ports")],
        "fallback": None,
    },
    {
        "keywords": [r"\bsip\b", r"\binvite\b", r"\bsbc\b", r"\btrunks?\b"],
        "primary": [("RFC 3261, SIP: Session Initiation Protocol", "https://www.rfc-editor.org/rfc/rfc3261", "rfc")],
        "fallback": ("Session Initiation Protocol", "https://en.wikipedia.org/wiki/Session_Initiation_Protocol", "wikipedia"),
    },
    {
        "keywords": [r"\brtp\b", r"\bg\.711\b", r"\bg711\b", r"\bcodecs?\b"],
        "primary": [
            ("RFC 3550, RTP", "https://www.rfc-editor.org/rfc/rfc3550", "rfc"),
            ("RFC 3551, RTP profile for audio and video", "https://www.rfc-editor.org/rfc/rfc3551", "rfc"),
            ("ITU-T G.711", "https://www.itu.int/rec/T-REC-G.711", "standard"),
        ],
        "fallback": ("Real-time Transport Protocol", "https://en.wikipedia.org/wiki/Real-time_Transport_Protocol", "wikipedia"),
    },
    {
        "keywords": [r"\bsrtp\b", r"\bsrtcp\b"],
        "primary": [("RFC 3711, SRTP", "https://www.rfc-editor.org/rfc/rfc3711", "rfc")],
        "fallback": ("Secure Real-time Transport Protocol", "https://en.wikipedia.org/wiki/Secure_Real-time_Transport_Protocol", "wikipedia"),
    },
    {
        "keywords": [r"\bsdp\b", r"\bsession description\b"],
        "primary": [("RFC 8866, SDP", "https://www.rfc-editor.org/rfc/rfc8866", "rfc")],
        "fallback": ("Session Description Protocol", "https://en.wikipedia.org/wiki/Session_Description_Protocol", "wikipedia"),
    },
    {
        "keywords": [r"\bdtmf\b", r"\brfc 4733\b"],
        "primary": [("RFC 4733, DTMF digits, telephone tones, and telephony signals", "https://www.rfc-editor.org/rfc/rfc4733", "rfc")],
        "fallback": None,
    },
    {
        "keywords": [r"\btls\b"],
        "primary": [("RFC 8446, TLS 1.3", "https://www.rfc-editor.org/rfc/rfc8446", "rfc")],
        "fallback": ("Transport Layer Security", "https://en.wikipedia.org/wiki/Transport_Layer_Security", "wikipedia"),
    },
    {
        "keywords": [r"\bdns\b", r"\bsrv\b"],
        "primary": [
            ("RFC 1035, domain names", "https://www.rfc-editor.org/rfc/rfc1035", "rfc"),
            ("RFC 2782, DNS SRV", "https://www.rfc-editor.org/rfc/rfc2782", "rfc"),
        ],
        "fallback": ("Domain Name System", "https://en.wikipedia.org/wiki/Domain_Name_System", "wikipedia"),
    },
    {
        "keywords": [r"\btcp\b"],
        "primary": [("RFC 9293, Transmission Control Protocol", "https://www.rfc-editor.org/rfc/rfc9293", "rfc")],
        "fallback": ("Transmission Control Protocol", "https://en.wikipedia.org/wiki/Transmission_Control_Protocol", "wikipedia"),
    },
    {
        "keywords": [r"\budp\b"],
        "primary": [("RFC 768, User Datagram Protocol", "https://www.rfc-editor.org/rfc/rfc768", "rfc")],
        "fallback": ("User Datagram Protocol", "https://en.wikipedia.org/wiki/User_Datagram_Protocol", "wikipedia"),
    },
    {
        "keywords": [r"\bwebsocket\b", r"\bwss\b"],
        "primary": [("RFC 6455, The WebSocket Protocol", "https://www.rfc-editor.org/rfc/rfc6455", "rfc")],
        "fallback": ("WebSocket", "https://en.wikipedia.org/wiki/WebSocket", "wikipedia"),
    },
    {
        "keywords": [r"\bwebrtc\b"],
        "primary": [("RFC 8825, WebRTC overview", "https://www.rfc-editor.org/rfc/rfc8825", "rfc")],
        "fallback": ("WebRTC", "https://en.wikipedia.org/wiki/WebRTC", "wikipedia"),
    },
    {
        "keywords": [r"\bstir\b", r"\bshaken\b", r"\battestation\b"],
        "primary": [("RFC 8224, Authenticated Identity Management in SIP", "https://www.rfc-editor.org/rfc/rfc8224", "rfc")],
        "fallback": ("STIR/SHAKEN", "https://en.wikipedia.org/wiki/STIR/SHAKEN", "wikipedia"),
    },
    {
        "keywords": [r"\be\.?164\b", r"\bdnis\b", r"\bani\b"],
        "primary": [("ITU-T E.164, international public telecommunication numbering", "https://www.itu.int/rec/T-REC-E.164", "standard")],
        "fallback": ("E.164", "https://en.wikipedia.org/wiki/E.164", "wikipedia"),
    },
    {
        "keywords": [r"\bnat\b", r"\brfc 1918\b", r"\bprivate address"],
        "primary": [
            ("RFC 1918, private internet addresses", "https://www.rfc-editor.org/rfc/rfc1918", "rfc"),
            ("RFC 4787, NAT behavior for UDP", "https://www.rfc-editor.org/rfc/rfc4787", "rfc"),
        ],
        "fallback": ("Network address translation", "https://en.wikipedia.org/wiki/Network_address_translation", "wikipedia"),
    },
    {
        "keywords": [r"\be911\b", r"\b911\b", r"\bemergency\b"],
        "primary": [],
        "fallback": ("Enhanced 9-1-1", "https://en.wikipedia.org/wiki/Enhanced_9-1-1", "wikipedia"),
    },
    {
        "keywords": [r"\btcpa\b"],
        "primary": [],
        "fallback": ("Telephone Consumer Protection Act of 1991", "https://en.wikipedia.org/wiki/Telephone_Consumer_Protection_Act_of_1991", "wikipedia"),
    },
    {
        "keywords": [r"\bivr\b"],
        "primary": [],
        "fallback": ("Interactive voice response", "https://en.wikipedia.org/wiki/Interactive_voice_response", "wikipedia"),
    },
    {
        "keywords": [r"\berlang\b"],
        "primary": [],
        "fallback": ("Erlang (unit)", "https://en.wikipedia.org/wiki/Erlang_(unit)", "wikipedia"),
    },
    {
        "keywords": [r"\bacd\b"],
        "primary": [],
        "fallback": ("Automatic call distributor", "https://en.wikipedia.org/wiki/Automatic_call_distributor", "wikipedia"),
    },
]


def status_for(url: str) -> str:
    return CHECKS["results"].get(url, "confirm")


def kind_for(url: str) -> str:
    host = url.lower()
    if "rfc-editor.org" in host or "ietf.org" in host:
        return "rfc"
    if "iana.org" in host:
        return "ports"
    if "itu.int" in host:
        return "standard"
    if "wikipedia.org" in host:
        return "wikipedia"
    if "community.five9.com" in host:
        return "community"
    if "five9.com" in host or "credly.com" in host:
        return "vendor"
    return "community"


def _row(label: str, url: str, kind: str | None = None, note: str = "") -> dict:
    status = status_for(url)
    return {
        "label": label or url,
        "url": url,
        "kind": kind or kind_for(url),
        "status": status,
        "lastChecked": CHECKED,
        "note": note,
    }


def assemble(blob: str, cites: list | None = None, limit: int = 12) -> list[dict]:
    """Lesson cites first, then standards that match the text. Wikipedia only as fallback."""
    items: list[dict] = []
    seen: set[str] = set()

    def add(row: dict, deeper: bool) -> None:
        url = row["url"]
        if not url or url in seen:
            return
        if deeper and row["status"] != "ok":
            return
        if deeper and len([item for item in items if item.get("deeper")]) >= limit:
            return
        seen.add(url)
        if deeper:
            row = dict(row)
            row["deeper"] = True
        items.append(row)

    for cite in cites or []:
        url = str(cite.get("url") or "")
        if not url.startswith("https://"):
            continue
        add(_row(str(cite.get("label") or cite.get("source") or url), url, note=str(cite.get("note") or "")), False)

    text = blob or ""
    primaries: list[dict] = []
    fallbacks: list[dict] = []
    for topic in TOPICS:
        if not any(re.search(pattern, text, re.I) for pattern in topic["keywords"]):
            continue
        matched_primary = False
        for label, url, kind in topic["primary"]:
            if url in seen or status_for(url) == "ok":
                matched_primary = matched_primary or url in seen or status_for(url) == "ok"
            if url in seen or status_for(url) != "ok":
                continue
            primaries.append(_row(label, url, kind))
            matched_primary = True
        fallback = topic["fallback"]
        if not matched_primary and fallback:
            label, url, kind = fallback
            if url not in seen and status_for(url) == "ok":
                fallbacks.append(_row(label, url, kind))
    for row in primaries + fallbacks:
        add(row, True)
    return items


def lesson_blob(lesson: dict) -> str:
    parts = [lesson.get("title") or ""]
    parts.extend(lesson.get("paragraphs") or [])
    parts.extend(lesson.get("objectives") or [])
    flow = lesson.get("flow") or {}
    parts.append(flow.get("title") or "")
    for cite in lesson.get("cites") or []:
        parts.append(str(cite.get("label") or ""))
    return " ".join(parts)


FRONT_CITES = [
    {"label": "Planning your implementation", "url": "https://documentation.five9.com/bundle/basic-admin/page/basic-admin/intro/planning-your-implementation.htm"},
    {"label": "Technical requirements PDF", "url": "https://documentation-be.five9.com/bundle/five9-technical-requirements/raw/resource/enus/five9-technical-requirements.pdf"},
]


def front_sources(extra: str = "") -> list[dict]:
    return assemble(f"sip ivr ports contact center {extra}", FRONT_CITES)


def lesson_sources(lesson: dict) -> list[dict]:
    rows = assemble(lesson_blob(lesson), lesson.get("cites") or [])
    for item in lesson.get("uncertain") or []:
        rows.append({
            "label": str(item),
            "url": "",
            "kind": "note",
            "status": "confirm",
            "lastChecked": CHECKED,
            "note": "",
        })
    return rows


def merge_sources(groups: list[list[dict]]) -> list[dict]:
    seen: set[str] = set()
    merged: list[dict] = []
    for group in groups:
        for row in group:
            key = row.get("url") or f"note:{row.get('label')}"
            if key in seen:
                continue
            seen.add(key)
            merged.append(row)
    return merged


def track_sources(track: dict) -> list[dict]:
    return merge_sources([lesson_sources(lesson) for lesson in track.get("lessons") or []])


def cites_in_html(body: str) -> list[dict]:
    found = []
    for url, label in re.findall(r'href="(https://[^"]+)"[^>]*>(.*?)</a>', body, re.S):
        found.append({"label": re.sub(r"<[^>]+>", "", label).strip() or url, "url": url})
    return found


def sources_from_html(body: str) -> list[dict]:
    plain = re.sub(r"<[^>]+>", " ", body)
    return assemble(plain, cites_in_html(body))


def _line(row: dict) -> str:
    checked = f"last checked {row['lastChecked']}"
    mark = " confirm" if row.get("status") == "confirm" else ""
    if row.get("url"):
        return f"{row['label']}. {row['kind']}. {row['url']}. {checked}.{mark}".rstrip()
    return f"confirm. {row['label']}. {checked}."


def sources_lines(rows: list[dict]) -> list[str]:
    lines = ["Sources and go deeper"]
    if not rows:
        lines.append("confirm. No page was opened for this export. last checked " + CHECKED + ".")
        return lines
    lines.extend(_line(row) for row in rows)
    return lines


def sources_html(rows: list[dict], heading: bool = True) -> str:
    items = []
    for row in rows:
        checked = f"last checked {html.escape(row['lastChecked'])}"
        kind = html.escape(row.get("kind") or "")
        if row.get("url"):
            label = html.escape(row["label"])
            url = html.escape(row["url"], quote=True)
            tail = f' <span class="source-kind">{kind}</span>. {checked}.'
            if row.get("status") == "confirm":
                tail += " <strong>confirm</strong>"
            if row.get("note"):
                tail += f" {html.escape(row['note'])}"
            items.append(f'<li><a href="{url}">{label}</a>.{tail}</li>')
        else:
            items.append(f"<li><strong>confirm</strong>. {html.escape(row['label'])}. {checked}.</li>")
    if not items:
        items.append(f"<li><strong>confirm</strong>. No page was opened for this export. last checked {html.escape(CHECKED)}.</li>")
    head = "<h2>Sources and go deeper</h2>" if heading else ""
    return f'<section class="sources-deeper">{head}<ul>' + "".join(items) + "</ul></section>"


def sources_md(rows: list[dict]) -> str:
    lines = ["## Sources and go deeper", ""]
    if not rows:
        lines.append(f"- confirm. No page was opened for this export. last checked {CHECKED}.")
        return "\n".join(lines) + "\n"
    for row in rows:
        checked = f"last checked {row['lastChecked']}"
        mark = " confirm" if row.get("status") == "confirm" else ""
        if row.get("url"):
            note = f" {row['note']}" if row.get("note") else ""
            lines.append(f"- [{row['label']}]({row['url']}). {row['kind']}. {checked}.{mark}{note}")
        else:
            lines.append(f"- confirm. {row['label']}. {checked}.")
    return "\n".join(lines) + "\n"


def markdown_doc(title: str, lines: list[str], rows: list[dict]) -> str:
    body = "\n".join(f"- {line}" if line else "" for line in lines)
    return f"# {title}\n\n{body}\n\n{sources_md(rows)}"


def pack_record(record_id: str, title: str, rows: list[dict]) -> dict:
    public = []
    for row in rows:
        item = {
            "label": row["label"],
            "url": row.get("url") or "",
            "kind": row.get("kind") or "",
            "status": row.get("status") or "confirm",
            "lastChecked": row.get("lastChecked") or CHECKED,
        }
        if row.get("note"):
            item["note"] = row["note"]
        public.append(item)
    return {"id": record_id, "title": title, "checked": CHECKED, "sources": public}


def _walk_urls(node, cites: list[dict], texts: list[str]) -> None:
    if isinstance(node, dict):
        url = node.get("url") or node.get("href")
        if isinstance(url, str) and url.startswith("https://"):
            label = node.get("label") or node.get("source") or node.get("name") or node.get("title") or url
            cites.append({"label": str(label), "url": url})
        for value in node.values():
            _walk_urls(value, cites, texts)
    elif isinstance(node, list):
        for value in node:
            _walk_urls(value, cites, texts)
    elif isinstance(node, str) and not node.startswith("http") and not node.startswith("#"):
        texts.append(node)


def pack_sections(uni: dict, eco: dict | None = None) -> dict:
    packed = {}
    for key, section in (uni.get("sections") or {}).items():
        cites: list[dict] = []
        texts: list[str] = []
        _walk_urls(section, cites, texts)
        packed[key] = pack_record(key, section.get("title") or key, assemble(" ".join(texts), cites))["sources"]
    if eco:
        cites = []
        texts = []
        _walk_urls(eco.get("glossary") or [], cites, texts)
        packed["glossary"] = pack_record("glossary", "Glossary", assemble(" ".join(texts), cites))["sources"]
    cites = []
    texts = []
    _walk_urls(uni.get("playbooks") or [], cites, texts)
    packed["trouble"] = pack_record("trouble", "Troubleshooting", assemble(" ".join(texts), cites))["sources"]
    return packed
