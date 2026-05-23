from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-C",
  "year": "2022",
  "code": "C",
  "question": "q02",
  "question_title": "策略最优性的证据与基准比较",
  "statement": "Present evidence that your model provides the best strategy.",
  "methods": "在现金、黄金买入持有、比特币买入持有、等权再平衡、60/180 日动量等透明因果候选规则中比较最终价值、收益率、最大回撤和交易次数。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2022/C/q02/solution.py",
  "result_path": "question_results/2022/C/q02/result.json",
  "report_path": "question_reports/2022/C/q02/report.md",
  "artifact_path": "question_artifacts/2022/C/q02/strategy_comparison.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'C' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'C' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'C' / 'q02'


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
