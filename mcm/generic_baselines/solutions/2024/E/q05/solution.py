from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-E",
  "year": "2024",
  "code": "E",
  "question": "q05",
  "question_title": "在哪里、如何、是否建设",
  "statement": "How can your insurance model be adapted to assess where, how, and whether to build on certain sites?",
  "methods": "把承保模型迁移为建址评分：危险暴露、公共服务可行性、社区需求和韧性成本共同决定 build / conditional build / avoid。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/E/q05/solution.py",
  "result_path": "question_results/2024/E/q05/result.json",
  "report_path": "question_reports/2024/E/q05/report.md",
  "artifact_path": "question_artifacts/2024/E/q05/site_build_decisions.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'E' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'E' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'E' / 'q05'


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
