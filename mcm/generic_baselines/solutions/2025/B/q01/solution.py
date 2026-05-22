from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-B",
  "year": "2025",
  "code": "B",
  "question": "q01",
  "question_title": "朱诺可持续旅游优化模型",
  "statement": "Build a model for a sustainable tourism industry in Juneau, Alaska. Consider visitors, overall revenue, stabilizing measures, constraints, expenditure of added revenue, feedback, and sensitivity analysis.",
  "methods": "用官方题面参数构建日游客上限、游客费和保护支出比例的确定性政策网格，最大化经济、环境和居民接受度加权可持续得分。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/B/q01/solution.py",
  "result_path": "question_results/2025/B/q01/result.json",
  "report_path": "question_reports/2025/B/q01/report.md",
  "artifact_path": "question_artifacts/2025/B/q01/policy_grid.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'B' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'B' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'B' / 'q01'


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
