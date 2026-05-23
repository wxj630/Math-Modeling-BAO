from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-E",
  "year": "2021",
  "code": "E",
  "question": "q01",
  "question_title": "效率、利润、可持续与公平的食物系统目标函数",
  "statement": "Provide a food system model robust enough to be adjusted to optimize for various levels of efficiency, profitability, sustainability, and/or equity.",
  "methods": "将官方题面四类优先级扩展为 efficiency、profitability、sustainability、equity 和 nutrition resilience 的透明加权指标，比较当前效率-利润导向与再优化方案。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/E/q01/solution.py",
  "result_path": "question_results/2021/E/q01/result.json",
  "report_path": "question_reports/2021/E/q01/report.md",
  "artifact_path": "question_artifacts/2021/E/q01/food_system_priority_scores.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'E' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'E' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'E' / 'q01'


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
