from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-B",
  "year": "2020",
  "code": "B",
  "question": "q03",
  "question_title": "降雨下的形状稳健性",
  "statement": "Adjust your model as needed to determine how the best 3-dimensional sandcastle foundation is affected by rain, and whether it remains best when it is raining.",
  "methods": "把 light shower、steady rain、heavy burst 作为额外径流负荷施加到 erosion index，比较推荐形状与备选低矮形状在雨中的寿命。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/B/q03/solution.py",
  "result_path": "question_results/2020/B/q03/result.json",
  "report_path": "question_reports/2020/B/q03/report.md",
  "artifact_path": "question_artifacts/2020/B/q03/rain_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'B' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'B' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'B' / 'q03'


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
