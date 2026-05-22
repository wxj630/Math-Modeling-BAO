from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-F",
  "year": "2017",
  "code": "F",
  "question": "q06",
  "question_title": "Minimum wage and salary distribution",
  "statement": "Determine the optimal minimum wage and salary distribution balancing wellbeing and support for citizens less equipped to provide labor services.",
  "methods": "Score explicit wage and benefit policies against output, wellbeing, equality, and living-wage coverage.",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/F/q06/solution.py",
  "result_path": "question_results/2017/F/q06/result.json",
  "report_path": "question_reports/2017/F/q06/report.md",
  "artifact_path": "question_artifacts/2017/F/q06/wage_policy_scores.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'F' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'F' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'F' / 'q06'


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
