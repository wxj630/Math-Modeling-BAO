from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-E",
  "year": "2019",
  "code": "E",
  "question": "q05",
  "question_title": "对土地利用项目规划者和管理者的影响",
  "statement": "What are the implications of your modeling on land use project planners and managers?",
  "methods": "提出把 mitigation/restoration 列为核心资本成本、报告 before/after service CBR、建立累计影响账本等管理建议。对应模型：规划政策建议、项目治理。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/E/q05/solution.py",
  "result_path": "question_results/2019/E/q05/result.json",
  "report_path": "question_reports/2019/E/q05/report.md",
  "artifact_path": "question_artifacts/2019/E/q05/project_true_costs.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'E' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'E' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'E' / 'q05'


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
