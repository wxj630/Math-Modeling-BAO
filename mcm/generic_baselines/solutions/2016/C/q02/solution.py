from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-C",
  "year": "2016",
  "code": "C",
  "question": "q02",
  "question_title": "1 亿美元年度预算的优先资助组合",
  "statement": "Identify the schools, the investment amount per school, and the duration the money should be provided to maximize the likelihood of a strong positive effect on student performance.",
  "methods": "按 rank_score 排序，在 annual budget 100,000,000 USD 和 5 年持续资助下贪心选择学校；每校年度 grant 在 2M-10M 之间，随官方 UGDS 规模调整。对应模型：预算约束组合选择、背包思想、投资组合排序。",
  "source_type": "official_comap_xlsx_zip",
  "solution_path": "question_solutions/2016/C/q02/solution.py",
  "result_path": "question_results/2016/C/q02/result.json",
  "report_path": "question_reports/2016/C/q02/report.md",
  "artifact_path": "question_artifacts/2016/C/q02/goodgrant_funding_plan.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'C' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'C' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'C' / 'q02'


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
