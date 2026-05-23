from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-A",
  "year": "2015",
  "code": "A",
  "question": "q02",
  "question_title": "世界医学协会非技术公告信",
  "statement": "Prepare a 1-2 page non-technical letter for the world medical association to use in their announcement.",
  "methods": "政策备忘录、风险沟通、模型结论摘要。",
  "source_type": "official_html_statement",
  "solution_path": "question_solutions/2015/A/q02/solution.py",
  "result_path": "question_results/2015/A/q02/result.json",
  "report_path": "question_reports/2015/A/q02/report.md",
  "artifact_path": "question_artifacts/2015/A/q02/experiment_table.csv"
}
RESULT_PATH = BASE / "results" / '2015' / 'A' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'A' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'A' / 'q02'


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
