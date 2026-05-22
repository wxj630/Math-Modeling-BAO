from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-F",
  "year": "2017",
  "code": "F",
  "question": "q10",
  "question_title": "Needs met across income, education, and equality",
  "statement": "Analyze how closely subgroup needs are met across income, education, and equality.",
  "methods": "Score subgroup fit with transparent income, education, and equality metrics instead of hidden simulation draws.",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/F/q10/solution.py",
  "result_path": "question_results/2017/F/q10/result.json",
  "report_path": "question_reports/2017/F/q10/report.md",
  "artifact_path": "question_artifacts/2017/F/q10/subgroup_equity_scores.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'F' / 'q10' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'F' / 'q10' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'F' / 'q10'


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
