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
  "question": "q04",
  "question_title": "决策模型可能建议的管理计划谱系",
  "statement": "What is the spectrum of management plans that your decision model may suggest?",
  "methods": "输出 no harvest、selective 60-year、extended 50-year、current 40-year、short 30-year 五类透明方案及适用条件。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/E/q04/solution.py",
  "result_path": "question_results/2022/E/q04/result.json",
  "report_path": "question_reports/2022/E/q04/report.md",
  "artifact_path": "question_artifacts/2022/E/q04/management_plan_scores.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'E' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'E' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'E' / 'q04'


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
