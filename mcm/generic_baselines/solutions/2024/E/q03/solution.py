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
  "question": "q03",
  "question_title": "业主可影响承保决策的措施",
  "statement": "Is there anything a property owner could do to influence this decision?",
  "methods": "比较屋顶加固、抬高设施、防火围护、社区排水预警、参数化准备金等减灾行动的风险降低、成本负担和保险信心增益。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/E/q03/solution.py",
  "result_path": "question_results/2024/E/q03/result.json",
  "report_path": "question_reports/2024/E/q03/report.md",
  "artifact_path": "question_artifacts/2024/E/q03/mitigation_levers.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'E' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'E' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'E' / 'q03'


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
