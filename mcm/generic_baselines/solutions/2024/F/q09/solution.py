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
  "question": "q09",
  "question_title": "项目达成目标的可能性",
  "statement": "How likely is the project to reach the expected goal?",
  "methods": "围绕至少 20% cumulative reduction 目标给出基础达标概率，并把关键实施条件映射为概率上调或下调。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/F/q09/solution.py",
  "result_path": "question_results/2024/F/q09/result.json",
  "report_path": "question_reports/2024/F/q09/report.md",
  "artifact_path": "question_artifacts/2024/F/q09/wildlife_trade_project_frontier.png"
}
RESULT_PATH = BASE / "results" / '2024' / 'F' / 'q09' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'F' / 'q09' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'F' / 'q09'


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
