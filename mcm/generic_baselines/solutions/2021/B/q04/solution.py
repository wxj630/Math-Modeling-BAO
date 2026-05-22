from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-B",
  "year": "2021",
  "code": "B",
  "question": "q04",
  "question_title": "面向 Victoria State Government 的注释预算请求",
  "statement": "Prepare a one- to two-page annotated Budget Request supported by your models for CFA to submit to the Victoria State Government.",
  "methods": "将推荐 SSA/repeater 采购、训练备件储备、能力安全前沿和十年投影压缩成 CFA 可提交预算请求。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/B/q04/solution.py",
  "result_path": "question_results/2021/B/q04/result.json",
  "report_path": "question_reports/2021/B/q04/report.md",
  "artifact_path": "question_artifacts/2021/B/q04/wildfire_budget_frontier.png"
}
RESULT_PATH = BASE / "results" / '2021' / 'B' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'B' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'B' / 'q04'


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
