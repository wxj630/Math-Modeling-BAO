from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-C",
  "year": "2020",
  "code": "C",
  "question": "q05",
  "question_title": "给 Sunshine Company 营销总监的两页信",
  "statement": "Write a one- to two-page letter to the Marketing Director of Sunshine Company summarizing your analysis and results.",
  "methods": "把最可信建议压缩为 low-star share、helpfulness-weighted review length 和 descriptor lift 的上市后监测方案。",
  "source_type": "official_comap_tsv_zip",
  "solution_path": "question_solutions/2020/C/q05/solution.py",
  "result_path": "question_results/2020/C/q05/result.json",
  "report_path": "question_reports/2020/C/q05/report.md",
  "artifact_path": "question_artifacts/2020/C/q05/product_reputation_frontier.png"
}
RESULT_PATH = BASE / "results" / '2020' / 'C' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'C' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'C' / 'q05'


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
