from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-P06",
  "year": "2019",
  "code": "P06",
  "question": "q03",
  "question_title": "监督机制与长期影响",
  "statement": "Include oversight mechanisms and consider long-term effects on banking, economies, and international relations.",
  "methods": "列出 reserve/collateral audit、privacy-preserving identity、consumer protection、cyber stress tests 和 monetary-policy interface，并评估银行、本地/区域/全球经济与国际关系影响。对应模型：治理机制、长期影响矩阵。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/P06/q03/solution.py",
  "result_path": "question_results/2019/P06/q03/result.json",
  "report_path": "question_reports/2019/P06/q03/report.md",
  "artifact_path": "question_artifacts/2019/P06/q03/currency_long_term_effects.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'P06' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'P06' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'P06' / 'q03'


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
