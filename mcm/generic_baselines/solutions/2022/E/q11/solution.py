from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-E",
  "year": "2022",
  "code": "E",
  "question": "q11",
  "question_title": "面向当地社区的非技术报纸文章",
  "statement": "Write a one- to two-page non-technical newspaper article explaining why your analysis identified including harvesting in the management of this forest rather than it being left untouched.",
  "methods": "把碳账户、森林差异、为什么不是所有森林都砍伐、以及渐进式过渡写成社区可读说明。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/E/q11/solution.py",
  "result_path": "question_results/2022/E/q11/result.json",
  "report_path": "question_reports/2022/E/q11/report.md",
  "artifact_path": "question_artifacts/2022/E/q11/management_tradeoff_frontier.png"
}
RESULT_PATH = BASE / "results" / '2022' / 'E' / 'q11' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'E' / 'q11' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'E' / 'q11'


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
