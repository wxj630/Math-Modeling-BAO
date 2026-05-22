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
  "question": "q02",
  "question_title": "客户现实上能做什么",
  "statement": "What can that client realistically do?",
  "methods": "把客户权力映射到 customs targeting、数据共享、平台协作、金融情报和社区激励五类可执行干预。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/F/q02/solution.py",
  "result_path": "question_results/2024/F/q02/result.json",
  "report_path": "question_reports/2024/F/q02/report.md",
  "artifact_path": "question_artifacts/2024/F/q02/resource_plan.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'F' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'F' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'F' / 'q02'


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
