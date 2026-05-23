from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-E",
  "year": "2025",
  "code": "E",
  "question": "q06",
  "question_title": "给探索有机农业农民的一页信",
  "statement": "Include a one-page letter to a farmer who is exploring organic farming practices.",
  "methods": "把食物网模型、有机情景排序、成本/生态权衡和实施监测指标压缩成非技术农民信。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/E/q06/solution.py",
  "result_path": "question_results/2025/E/q06/result.json",
  "report_path": "question_reports/2025/E/q06/report.md",
  "artifact_path": "question_artifacts/2025/E/q06/scenario_summary.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'E' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'E' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'E' / 'q06'


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
