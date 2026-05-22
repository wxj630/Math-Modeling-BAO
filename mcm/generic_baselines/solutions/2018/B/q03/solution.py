from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2018-B",
  "year": "2018",
  "code": "B",
  "question": "q03",
  "question_title": "Geographic distribution shift",
  "statement": "Predict how global population and migration patterns may change the geographic distribution of languages.",
  "methods": "Score regional language shifts from growth pressure and migration connectivity.",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2018/B/q03/solution.py",
  "result_path": "question_results/2018/B/q03/result.json",
  "report_path": "question_reports/2018/B/q03/report.md",
  "artifact_path": "question_artifacts/2018/B/q03/language_geography_shift.csv"
}
RESULT_PATH = BASE / "results" / '2018' / 'B' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2018' / 'B' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2018' / 'B' / 'q03'


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
