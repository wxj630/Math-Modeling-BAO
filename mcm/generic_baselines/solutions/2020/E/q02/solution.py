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
  "question": "q02",
  "question_title": "达到环境安全水平的政策减量路径",
  "statement": "Discuss to what extent plastic waste can be reduced to reach an environmentally safe level, considering sources, alternatives, citizen impact, and policy effectiveness.",
  "methods": "组合包装标准、reuse/refill、生产者责任、非正规回收支持和必要替代，计算 2020-2050 三年步长的剩余 single-use waste 和海洋输入。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/E/q02/solution.py",
  "result_path": "question_results/2020/E/q02/result.json",
  "report_path": "question_reports/2020/E/q02/report.md",
  "artifact_path": "question_artifacts/2020/E/q02/plastic_policy_pathway.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'E' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'E' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'E' / 'q02'


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
