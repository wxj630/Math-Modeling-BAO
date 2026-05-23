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
  "question": "q03",
  "question_title": "交易成本敏感性",
  "statement": "Determine how sensitive the strategy is to transaction costs. How do transaction costs affect the strategy and results?",
  "methods": "保持官方黄金手续费 1% 基线，枚举比特币手续费 0%-12%，重新运行同一因果策略并输出最终价值、收益率和交易次数。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2022/C/q03/solution.py",
  "result_path": "question_results/2022/C/q03/result.json",
  "report_path": "question_reports/2022/C/q03/report.md",
  "artifact_path": "question_artifacts/2022/C/q03/transaction_cost_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'C' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'C' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'C' / 'q03'


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
