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
  "question": "q08",
  "question_title": "如何确定上述影响",
  "statement": "What analysis did you do to determine this?",
  "methods": "组合多指标客户选择、资源约束项目成本、干预影响投影、复杂系统影响网络和 one-at-a-time 敏感性分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/F/q08/solution.py",
  "result_path": "question_results/2024/F/q08/result.json",
  "report_path": "question_reports/2024/F/q08/report.md",
  "artifact_path": "question_artifacts/2024/F/q08/complex_system_edges.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'F' / 'q08' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'F' / 'q08' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'F' / 'q08'


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
