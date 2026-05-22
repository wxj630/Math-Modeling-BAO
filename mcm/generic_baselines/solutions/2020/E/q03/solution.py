from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-E",
  "year": "2020",
  "code": "E",
  "question": "q03",
  "question_title": "2050 全球最低可达目标及影响",
  "statement": "Set a target for the minimal achievable level of global single-use or disposable plastic product waste and discuss impacts.",
  "methods": "以 2050 年剩余 single-use waste 是否低于全球安全容量作为目标判据，并说明对生活方式、环境和塑料产业的影响。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/E/q03/solution.py",
  "result_path": "question_results/2020/E/q03/result.json",
  "report_path": "question_reports/2020/E/q03/report.md",
  "artifact_path": "question_artifacts/2020/E/q03/plastic_waste_reduction_frontier.png"
}
RESULT_PATH = BASE / "results" / '2020' / 'E' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'E' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'E' / 'q03'


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
