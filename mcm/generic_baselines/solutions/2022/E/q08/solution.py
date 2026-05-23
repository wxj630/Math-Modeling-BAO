from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-E",
  "year": "2022",
  "code": "E",
  "question": "q08",
  "question_title": "识别建议纳入采伐的森林并计算 100 年固碳",
  "statement": "Identify a forest that your decision model would suggest the inclusion of harvesting in its management plan. How much carbon dioxide will this forest and its products sequester over 100 years?",
  "methods": "选择社会得分最高且包含采伐的森林案例，报告 100 年活树、土壤、产品和替代信用 CO2e。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/E/q08/solution.py",
  "result_path": "question_results/2022/E/q08/result.json",
  "report_path": "question_reports/2022/E/q08/report.md",
  "artifact_path": "question_artifacts/2022/E/q08/forest_application_results.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'E' / 'q08' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'E' / 'q08' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'E' / 'q08'


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
