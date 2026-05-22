from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-B",
  "year": "2022",
  "code": "B",
  "question": "q08",
  "question_title": "需求变化、可再生能源和节水节电影响",
  "statement": "What happens when demand changes over time, renewable technologies increase, and additional water and electricity conservation measures are implemented?",
  "methods": "在同一分配规则下重跑人口/产业增长、收缩、可再生能源占比提高、节水节电和组合情景。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/B/q08/solution.py",
  "result_path": "question_results/2022/B/q08/result.json",
  "report_path": "question_reports/2022/B/q08/report.md",
  "artifact_path": "question_artifacts/2022/B/q08/demand_change_scenarios.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'B' / 'q08' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'B' / 'q08' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'B' / 'q08'


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
