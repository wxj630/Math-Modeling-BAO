from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-D",
  "year": "2022",
  "code": "D",
  "question": "q01",
  "question_title": "ICM Corporation 当前 D&A 成熟度指标",
  "statement": "A metric to measure the current D&A system maturity level for ICM Corporation, including KPIs for D&A people, technologies, and processes.",
  "methods": "将官方题面的人、技术、流程三组成转成 1-5 级成熟度 rubric，按 KPI 重要度和组件权重计算当前成熟度。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/P01/q01/solution.py",
  "result_path": "question_results/2022/P01/q01/result.json",
  "report_path": "question_reports/2022/P01/q01/report.md",
  "artifact_path": "question_artifacts/2022/P01/q01/maturity_component_scores.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'D' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'D' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'D' / 'q01'


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
