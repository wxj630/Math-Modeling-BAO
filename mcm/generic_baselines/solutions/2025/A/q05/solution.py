from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-A",
  "year": "2025",
  "code": "A",
  "question": "q05",
  "question_title": "楼梯年龄与可靠性",
  "statement": "What is the age of the stairwell and how reliable is the estimate?",
  "methods": "在材料磨损系数和可能日均交通量上做确定性网格，输出与历史年龄先验重叠的年龄区间和可靠性等级。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/A/q05/solution.py",
  "result_path": "question_results/2025/A/q05/result.json",
  "report_path": "question_reports/2025/A/q05/report.md",
  "artifact_path": "question_artifacts/2025/A/q05/age_reliability_grid.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'A' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'A' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'A' / 'q05'


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
