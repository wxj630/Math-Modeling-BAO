# -*- coding: utf-8 -*-
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "generic_baselines"


def main() -> None:
    errors: list[str] = []
    index_path = BASE / "generic_baseline_index.json"
    if not index_path.exists():
        errors.append("missing cumcm/generic_baselines/generic_baseline_index.json")
        rows = []
    else:
        rows = json.loads(index_path.read_text(encoding="utf-8"))

    for row in rows:
        for key in ["solution_path", "result_path", "report_path"]:
            path = ROOT.parent / row[key]
            if not path.exists():
                errors.append(f"missing {key}: {row[key]}")
        artifact_dir = ROOT.parent / row["artifact_dir"]
        if not artifact_dir.exists() or not any(artifact_dir.iterdir()):
            errors.append(f"missing or empty artifact_dir: {row['artifact_dir']}")
        result_path = ROOT.parent / row["result_path"]
        if result_path.exists():
            try:
                data = json.loads(result_path.read_text(encoding="utf-8"))
                method = data.get("experiment_result", {}).get("method")
                if not method:
                    errors.append(f"missing generic method in {row['result_path']}")
            except Exception as exc:
                errors.append(f"invalid result json {row['result_path']}: {exc}")

    print(f"generic baseline index rows: {len(rows)}")
    print(f"generic solution scripts: {len(list((BASE / 'solutions').glob('*/*/q*/solution.py')))}")
    print(f"generic results: {len(list((BASE / 'results').glob('*/*/q*/result.json')))}")
    print(f"generic reports: {len(list((BASE / 'reports').glob('*/*/q*/report.md')))}")
    print(f"generic verification errors: {len(errors)}")
    if errors:
        for err in errors[:50]:
            print(f"- {err}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
