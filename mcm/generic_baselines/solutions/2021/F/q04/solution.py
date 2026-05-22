from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-F",
  "year": "2021",
  "code": "F",
  "question": "q04",
  "question_title": "当前状态与拟议健康状态测量",
  "statement": "Use your model to measure the health of both the current system and proposed, healthy, sustainable system for your selected nation.",
  "methods": "在 0-10 年轨迹上计算选定国家当前健康分、最终健康分以及 access、affordability、funding、innovation 等维度变化。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/F/q04/solution.py",
  "result_path": "question_results/2021/F/q04/result.json",
  "report_path": "question_reports/2021/F/q04/report.md",
  "artifact_path": "question_artifacts/2021/F/q04/higher_ed_health_scores.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'F' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'F' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'F' / 'q04'


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
