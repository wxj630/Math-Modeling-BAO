from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-F",
  "year": "2024",
  "code": "F",
  "question": "q07",
  "question_title": "对非法野生动物贸易的可测量影响",
  "statement": "In other words, what will the measurable impact on illegal wildlife trade be?",
  "methods": "以 no-project 5 年路径为反事实基线，计算第 5 年贸易额差值和 cumulative reduction percent。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/F/q07/solution.py",
  "result_path": "question_results/2024/F/q07/result.json",
  "report_path": "question_reports/2024/F/q07/report.md",
  "artifact_path": "question_artifacts/2024/F/q07/intervention_impact_projection.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'F' / 'q07' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'F' / 'q07' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'F' / 'q07'


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
