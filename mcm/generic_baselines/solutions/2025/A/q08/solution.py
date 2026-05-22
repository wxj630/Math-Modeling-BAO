from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-A",
  "year": "2025",
  "code": "A",
  "question": "q08",
  "question_title": "典型日人数与短时峰值",
  "statement": "What information can be determined with respect to the numbers of people using the stairs in a typical day and were there large numbers of people using the stairs over a short time or a small number of people over a longer time?",
  "methods": "综合日均使用人数、同时使用指数和年龄可靠性区间，把典型日拆成短时峰值使用和长时低强度通行两部分。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/A/q08/solution.py",
  "result_path": "question_results/2025/A/q08/result.json",
  "report_path": "question_reports/2025/A/q08/report.md",
  "artifact_path": "question_artifacts/2025/A/q08/traffic_pattern_summary.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'A' / 'q08' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'A' / 'q08' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'A' / 'q08'


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
