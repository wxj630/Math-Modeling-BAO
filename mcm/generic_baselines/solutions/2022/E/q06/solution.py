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
  "question": "q06",
  "question_title": "管理计划之间的过渡点",
  "statement": "Are there transition points between management plans that apply to all forests? How are characteristics about a specific forest and its location used to determine transition points?",
  "methods": "比较不采伐与最佳采伐方案的 CO2e 差距和社会得分差距，形成每类森林的过渡规则。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/E/q06/solution.py",
  "result_path": "question_results/2022/E/q06/result.json",
  "report_path": "question_reports/2022/E/q06/report.md",
  "artifact_path": "question_artifacts/2022/E/q06/management_plan_scores.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'E' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'E' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'E' / 'q06'


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
