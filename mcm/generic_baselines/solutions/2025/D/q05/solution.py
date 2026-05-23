from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-D",
  "year": "2025",
  "code": "D",
  "question": "q05",
  "question_title": "项目扰动和实施代价",
  "statement": "Explain the ways the project disrupts other transportation needs and people's lives.",
  "methods": "用项目建议中的 construction/capital/curb trade-off 字段，列出施工、绕行、停车装卸和人行道施工扰动。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2025/D/q05/solution.py",
  "result_path": "question_results/2025/D/q05/result.json",
  "report_path": "question_reports/2025/D/q05/report.md",
  "artifact_path": "question_artifacts/2025/D/q05/bridge_od_impacts.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'D' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'D' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'D' / 'q05'


def main() -> None:
    result = solve_question_generic_baseline(PAYLOAD, ARTIFACT_DIR)
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_generic_report(result, REPORT_PATH, Path(__file__).resolve())
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
