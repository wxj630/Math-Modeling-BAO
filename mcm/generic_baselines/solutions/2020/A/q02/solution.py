from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-A",
  "year": "2020",
  "code": "A",
  "question": "q02",
  "question_title": "最佳、最差、最可能情景下的小渔业压力时间",
  "statement": "Estimate elapsed times for best, worst, and most likely scenarios in which fish move too far north for small Scottish fishing firms.",
  "methods": "在五年步长上寻找 habitat center 超出 small boat range 的首次年份，输出 best/worst/most_likely elapsed times。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/A/q02/solution.py",
  "result_path": "question_results/2020/A/q02/result.json",
  "report_path": "question_reports/2020/A/q02/report.md",
  "artifact_path": "question_artifacts/2020/A/q02/accessibility_timeline.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'A' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'A' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'A' / 'q02'


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
