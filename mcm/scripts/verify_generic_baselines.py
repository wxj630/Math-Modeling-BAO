from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
MCM_ROOT = REPO_ROOT / "mcm"
DEFAULT_BASE = MCM_ROOT / "generic_baselines"
PROHIBITED = ["np.random.default_rng", "rng.normal", "rng.uniform", "synthetic_table"]


def resolve_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify MCM generic baseline archive.")
    parser.add_argument("--base", default=str(DEFAULT_BASE), help="generic baseline root")
    args = parser.parse_args()

    base = Path(args.base).resolve()
    errors: list[str] = []
    index_path = base / "generic_baseline_index.json"
    if not index_path.exists():
        errors.append(f"missing index: {index_path}")
        rows = []
    else:
        rows = json.loads(index_path.read_text(encoding="utf-8"))

    for row in rows:
        solution_path = resolve_path(row["solution_path"])
        result_path = resolve_path(row["result_path"])
        report_path = resolve_path(row["report_path"])
        artifact_dir = resolve_path(row["artifact_dir"])
        for key, path in [("solution_path", solution_path), ("result_path", result_path), ("report_path", report_path)]:
            if not path.exists():
                errors.append(f"missing {key}: {row[key]}")
        if not artifact_dir.exists() or not any(artifact_dir.iterdir()):
            errors.append(f"missing or empty artifact_dir: {row['artifact_dir']}")
        if solution_path.exists():
            text = solution_path.read_text(encoding="utf-8", errors="ignore")
            for marker in PROHIBITED:
                if marker in text:
                    errors.append(f"prohibited marker {marker} in {row['solution_path']}")
        if result_path.exists():
            try:
                result = json.loads(result_path.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"invalid result json {row['result_path']}: {exc}")
                continue
            method = result.get("experiment_result", {}).get("method")
            if not method:
                errors.append(f"missing generic method in {row['result_path']}")
            elif method != row.get("method"):
                errors.append(f"method mismatch in {row['result_path']}: {method} != {row.get('method')}")
            if result.get("baseline_kind") != "mcm_generic_first_pass":
                errors.append(f"missing baseline_kind in {row['result_path']}")

    print(f"generic baseline index rows: {len(rows)}")
    print(f"generic solution scripts: {len(list((base / 'solutions').glob('*/*/q*/solution.py')))}")
    print(f"generic results: {len(list((base / 'results').glob('*/*/q*/result.json')))}")
    print(f"generic reports: {len(list((base / 'reports').glob('*/*/q*/report.md')))}")
    print(f"generic verification errors: {len(errors)}")
    if errors:
        for error in errors[:50]:
            print(f"- {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

