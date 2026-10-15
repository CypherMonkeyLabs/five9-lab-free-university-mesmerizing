"""Compile track modules into campus/data JSON."""

import importlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from site_extras import boss, certs, ecosystem, interview

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "campus" / "data"
TRACKS = DATA / "tracks"

REQUIRED = ("id", "title", "level", "objectives", "paragraphs", "cites", "figure", "flow", "quiz", "cards", "lab", "fault")


def main():
    built = []
    quiz = cards = labs = faults = cites = 0
    for n in range(1, 19):
        mod = importlib.import_module(f"t{n:02d}")
        track = mod.build()
        if track["id"] != f"t{n:02d}":
            raise SystemExit(f"id mismatch {track['id']}")
        if len(track["lessons"]) < 7:
            raise SystemExit(f"{track['id']} has {len(track['lessons'])} lessons")
        for lesson in track["lessons"]:
            missing = [key for key in REQUIRED if key not in lesson]
            if missing:
                raise SystemExit(f"{track['id']} {lesson.get('id')} missing {missing}")
            if len(lesson["quiz"]) < 5 or len(lesson["cards"]) < 4:
                raise SystemExit(f"{track['id']} {lesson['id']} short quiz or cards")
            if len(lesson["flow"]["steps"]) < 5:
                raise SystemExit(f"{track['id']} {lesson['id']} short flow")
            if not lesson["cites"]:
                raise SystemExit(f"{track['id']} {lesson['id']} has no cites")
            for cite in lesson["cites"]:
                if not str(cite.get("url", "")).startswith("https://"):
                    raise SystemExit(f"bad url in {track['id']} {lesson['id']}: {cite}")
            quiz += len(lesson["quiz"])
            cards += len(lesson["cards"])
            labs += 1
            faults += 1
            cites += len(lesson["cites"])
        built.append(track)

    TRACKS.mkdir(parents=True, exist_ok=True)
    catalog_tracks = []
    for track in built:
        path = TRACKS / f"{track['id']}.json"
        path.write_text(json.dumps(track, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        catalog_tracks.append({
            "id": track["id"],
            "file": f"tracks/{track['id']}.json",
            "title": track["title"],
            "short": track["short"],
            "blurb": track["blurb"],
            "group": track["group"],
            "level": track["level"],
            "summary": track["summary"],
            "lessons": [{"id": lesson["id"], "title": lesson["title"]} for lesson in track["lessons"]],
        })

    catalog = {
        "tracks": catalog_tracks,
        "counts": {
            "tracks": len(built),
            "lessons": sum(len(t["lessons"]) for t in built),
            "quiz": quiz,
            "cards": cards,
            "labs": labs,
            "faults": faults,
            "cites": cites,
        },
    }
    (DATA / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DATA / "ecosystem.json").write_text(json.dumps(ecosystem(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DATA / "certs.json").write_text(json.dumps(certs(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DATA / "interview.json").write_text(json.dumps(interview(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DATA / "boss.json").write_text(json.dumps(boss(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(catalog["counts"]))


if __name__ == "__main__":
    main()
