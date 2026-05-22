from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-F",
  "year": "2020",
  "code": "F",
  "question": "q01",
  "question_title": "环境迁移人口规模和文化风险",
  "statement": "Analyze the scope of the EDP issue in terms of population at risk and risk of loss of culture.",
  "methods": "对 Maldives、Tuvalu、Kiribati 和 Marshall Islands 在 managed/middle/high sea-level scenarios 下投影 80 年 population at risk，并计算 culture loss risk。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/F/q01/solution.py",
  "result_path": "question_results/2020/F/q01/result.json",
  "report_path": "question_reports/2020/F/q01/report.md",
  "artifact_path": "question_artifacts/2020/F/q01/edp_scope_projection.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'F' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'F' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'F' / 'q01'


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
