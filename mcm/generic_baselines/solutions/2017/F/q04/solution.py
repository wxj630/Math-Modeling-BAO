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
  "question": "q04",
  "question_title": "Population Zero demographic analysis",
  "statement": "From the 10,000-person data set, analyze demographic distributions such as gender, age, ethnicity or education levels.",
  "methods": "Build a deterministic 10,000-record Population Zero design matrix from official statement categories and summarize the auditable demographic profile.",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/F/q04/solution.py",
  "result_path": "question_results/2017/F/q04/result.json",
  "report_path": "question_reports/2017/F/q04/report.md",
  "artifact_path": "question_artifacts/2017/F/q04/population_zero_profile.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'F' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'F' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'F' / 'q04'


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
