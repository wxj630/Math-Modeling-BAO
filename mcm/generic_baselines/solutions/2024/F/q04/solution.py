from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-F",
  "year": "2024",
  "code": "F",
  "question": "q04",
  "question_title": "用数据驱动分析说服客户",
  "statement": "Using a data-driven analysis, how will you convince your client that this is a project they should undertake?",
  "methods": "比较无项目贸易额增长路径与 5 年项目干预路径，输出第 5 年降低比例和年度影响表。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/F/q04/solution.py",
  "result_path": "question_results/2024/F/q04/result.json",
  "report_path": "question_reports/2024/F/q04/report.md",
  "artifact_path": "question_artifacts/2024/F/q04/intervention_impact_projection.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'F' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'F' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'F' / 'q04'


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
