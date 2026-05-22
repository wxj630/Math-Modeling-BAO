from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-B",
  "year": "2022",
  "code": "B",
  "question": "q01",
  "question_title": "Powell-Mead 串联系统与水库高度-库容模型",
  "statement": "The operations of Glen Canyon Dam (Lake Powell) and Hoover Dam (Lake Mead) should be closely coordinated because Powell outflows supply part of Mead input.",
  "methods": "把 Powell 和 Mead 作为串联系统，用题面要求的水位-库容关系估算可规划库容、净入流、推荐释放量和水电产出。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/B/q01/solution.py",
  "result_path": "question_results/2022/B/q01/result.json",
  "report_path": "question_reports/2022/B/q01/report.md",
  "artifact_path": "question_artifacts/2022/B/q01/reservoir_allocation_plan.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'B' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'B' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'B' / 'q01'


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
