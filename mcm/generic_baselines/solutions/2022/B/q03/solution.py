from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-B",
  "year": "2022",
  "code": "B",
  "question": "q03",
  "question_title": "固定供需条件下的坝体放水与重算频率",
  "statement": "When Lake Mead is M and Lake Powell is P, how much water should be drawn from each lake to meet stated demands? Recommend how often the model should be re-run.",
  "methods": "在给定 Powell/Mead 水位下输出两坝推荐释放量、州部门分配、需求缺口和每 3 个月重算规则。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/B/q03/solution.py",
  "result_path": "question_results/2022/B/q03/result.json",
  "report_path": "question_reports/2022/B/q03/report.md",
  "artifact_path": "question_artifacts/2022/B/q03/reservoir_allocation_plan.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'B' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'B' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'B' / 'q03'


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
