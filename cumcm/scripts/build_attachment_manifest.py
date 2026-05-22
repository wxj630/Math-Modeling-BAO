# -*- coding: utf-8 -*-
"""Build a manifest of downloaded/unzipped CUMCM problem attachments."""
from __future__ import annotations

import json
import csv
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOTS = [
    Path("../../Documents/Playground/cumcm_unzipped"),
    Path("../../Documents/Playground/cumcm_reextract"),
]
DATA_EXTS = {".csv", ".xlsx", ".xls"}
DOC_EXTS = {".pdf", ".doc", ".docx"}
MEDIA_EXTS = {".tif", ".tiff", ".png", ".jpg", ".jpeg", ".mp4", ".rar", ".zip", ".txt"}
ALL_EXTS = DATA_EXTS | DOC_EXTS | MEDIA_EXTS


def known_problem_ids() -> set[str]:
    return {f"{p.parent.name}-{p.stem}" for p in (ROOT / "problems").glob("*/*.md")}


def infer_year(path: Path) -> str | None:
    match = re.search(r"20\d{2}|201\d", str(path))
    return match.group(0) if match else None


def infer_code(path: Path) -> str | None:
    parts = path.parts
    filename = path.name
    parent_names = list(path.parts[:-1])[-5:]
    for part in reversed(parent_names):
        stripped = part.strip()
        if stripped in {"A", "B", "C", "D", "E"}:
            return stripped
        m = re.search(r"(?:^|[^A-Za-z])([A-E])(?:题|$|[^A-Za-z])", stripped, flags=re.IGNORECASE)
        if m:
            return m.group(1).upper()
        m = re.search(r"20\d{2}\s*([A-E])\b", stripped, flags=re.IGNORECASE)
        if m:
            return m.group(1).upper()
    patterns = [
        r"([A-E])题",
        r"Problem[-_ ]*([A-E])",
        r"problem[-_ ]*([A-E])",
        r"CUMCM[-_ ]*20\d{2}[-_ ]*([A-E])",
        r"cumcm20\d{2}([A-E])",
        r"20\d{2}([A-E])",
        r"问题([A-E])",
    ]
    for pattern in patterns:
        m = re.search(pattern, filename, flags=re.IGNORECASE)
        if m:
            return m.group(1).upper()
    return None


def classify(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in DATA_EXTS:
        return "data"
    if ext in DOC_EXTS:
        return "document"
    return "media_or_archive"


def should_skip(path: Path) -> bool:
    name = path.name.lower()
    if path.suffix.lower() not in ALL_EXTS:
        return True
    return name.startswith("format") or "论文格式" in name or "参赛规则" in name or "报名" in name


def main() -> None:
    known = known_problem_ids()
    manifest: dict[str, dict[str, Any]] = {pid: {"problem_id": pid, "attachments": []} for pid in sorted(known)}
    for source_root in SOURCE_ROOTS:
        if not source_root.exists():
            continue
        for path in sorted(source_root.rglob("*")):
            if not path.is_file() or should_skip(path):
                continue
            year = infer_year(path)
            code = infer_code(path)
            if not year or not code:
                continue
            pid = f"{year}-{code}"
            if pid not in known:
                continue
            item = {
                "path": str(path),
                "name": path.name,
                "suffix": path.suffix.lower(),
                "kind": classify(path),
                "size_bytes": path.stat().st_size,
                "source_root": str(source_root),
            }
            if item not in manifest[pid]["attachments"]:
                manifest[pid]["attachments"].append(item)
    manifest = {pid: data for pid, data in manifest.items() if data["attachments"]}
    (ROOT / "attachment_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    with (ROOT / "attachment_manifest.csv").open("w", encoding="utf-8-sig", newline="") as f:
        fieldnames = ["problem_id", "kind", "suffix", "name", "path", "size_bytes"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for pid, data in sorted(manifest.items()):
            for item in data["attachments"]:
                writer.writerow({
                    "problem_id": pid,
                    "kind": item["kind"],
                    "suffix": item["suffix"],
                    "name": item["name"],
                    "path": item["path"],
                    "size_bytes": item["size_bytes"],
                })
    print(f"wrote {ROOT / 'attachment_manifest.json'}")
    print(f"wrote {ROOT / 'attachment_manifest.csv'}")
    print(f"problems with attachments: {len(manifest)}")
    print(f"attachments: {sum(len(v['attachments']) for v in manifest.values())}")
    for pid in sorted(manifest)[:12]:
        print(pid, len(manifest[pid]["attachments"]))


if __name__ == "__main__":
    main()
