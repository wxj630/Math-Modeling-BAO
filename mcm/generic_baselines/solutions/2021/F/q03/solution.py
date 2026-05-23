from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-F",
  "year": "2021",
  "code": "F",
  "question": "q03",
  "question_title": "健康且可持续的目标状态愿景",
  "statement": "Propose an attainable and reasonable vision for your selected nation's system that supports a healthy and sustainable system of higher education.",
  "methods": "对选定国家给出 affordability、access、funding、research 和 renewal 的目标 operating zone，而不是单一排名目标。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/F/q03/solution.py",
  "result_path": "question_results/2021/F/q03/result.json",
  "report_path": "question_reports/2021/F/q03/report.md",
  "artifact_path": "question_artifacts/2021/F/q03/higher_ed_health_dimensions.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'F' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'F' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'F' / 'q03'


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
