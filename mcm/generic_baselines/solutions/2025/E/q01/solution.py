from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-E",
  "year": "2025",
  "code": "E",
  "question": "q01",
  "question_title": "自然过程与森林转农田框架",
  "statement": "Natural Processes.",
  "methods": "官方 PDF 题面参数 + 确定性月度系统动力学：把森林转农田后的作物、野生植物、害虫、授粉者、蝙蝠、鸟类、土壤和天敌作为状态变量。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/E/q01/solution.py",
  "result_path": "question_results/2025/E/q01/result.json",
  "report_path": "question_reports/2025/E/q01/report.md",
  "artifact_path": "question_artifacts/2025/E/q01/food_web_edges.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'E' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'E' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'E' / 'q01'


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
