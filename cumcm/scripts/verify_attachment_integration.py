# -*- coding: utf-8 -*-
"""Verify that per-question experiments are wired to real CUMCM attachments."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    errors: list[str] = []
    manifest_path = ROOT / "attachment_manifest.json"
    if not manifest_path.exists():
        errors.append("missing cumcm/attachment_manifest.json")
        manifest = {}
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if len(manifest) < 20:
            errors.append(f"attachment manifest too small: {len(manifest)} problems")
        for pid in ["2021-A", "2021-C", "2020-C", "2019-A"]:
            if not manifest.get(pid, {}).get("attachments"):
                errors.append(f"manifest missing attachments for {pid}")

    sample_solution = ROOT / "question_solutions" / "2021" / "A" / "q01" / "solution.py"
    if sample_solution.exists():
        text = sample_solution.read_text(encoding="utf-8")
        if '"attachments"' not in text:
            errors.append("2021-A q01 payload has no attachments")
    else:
        errors.append("missing 2021-A q01 solution")

    real_data_results = 0
    for path in (ROOT / "question_results").glob("*/*/q*/result.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        source = data.get("data_source", {})
        if source.get("source_type") == "attachment":
            real_data_results += 1
            if not source.get("path"):
                errors.append(f"{path.relative_to(ROOT)} attachment data_source missing path")
    if real_data_results < 120:
        errors.append(f"too few attachment-backed results: {real_data_results}")

    print(f"manifest problems: {len(manifest)}")
    print(f"attachment-backed results: {real_data_results}")
    print(f"attachment integration errors: {len(errors)}")
    for error in errors[:80]:
        print(f"ERROR: {error}")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
