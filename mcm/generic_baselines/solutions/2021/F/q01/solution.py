from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-F",
  "year": "2021",
  "code": "F",
  "question": "q01",
  "question_title": "国家高等教育系统健康度模型",
  "statement": "Develop and validate a model or suite of models that allow you to assess the health of any nation's system of higher education.",
  "methods": "用 access/equity、affordability、degree value、quality、research/exchange、funding stability 和 innovation renewal 七维加权健康度模型定义健康阈值。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/F/q01/solution.py",
  "result_path": "question_results/2021/F/q01/result.json",
  "report_path": "question_reports/2021/F/q01/report.md",
  "artifact_path": "question_artifacts/2021/F/q01/higher_ed_health_scores.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'F' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'F' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'F' / 'q01'


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
