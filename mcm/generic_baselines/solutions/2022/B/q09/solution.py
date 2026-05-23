from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-B",
  "year": "2022",
  "code": "B",
  "question": "q09",
  "question_title": "Drought and Thirst 杂志文章",
  "statement": "Prepare a one- to two-page article of your findings suitable for publication in Drought and Thirst magazine.",
  "methods": "把串联系统、透明分配标准、Mexico/Gulf flow、短缺触发和季度重算写成面向美国西南水基础设施经理的文章。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/B/q09/solution.py",
  "result_path": "question_results/2022/B/q09/result.json",
  "report_path": "question_reports/2022/B/q09/report.md",
  "artifact_path": "question_artifacts/2022/B/q09/reservoir_allocation_frontier.png"
}
RESULT_PATH = BASE / "results" / '2022' / 'B' / 'q09' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'B' / 'q09' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'B' / 'q09'


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
