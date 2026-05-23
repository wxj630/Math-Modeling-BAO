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
  "question": "q04",
  "question_title": "给交易员的两页以内备忘录",
  "statement": "Communicate your strategy, model, and results to the trader in a memorandum of at most two pages.",
  "methods": "把官方数据来源、交易日限制、佣金、候选策略排名、最终价值和手续费敏感性整理成交易员可读 memo。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2022/C/q04/solution.py",
  "result_path": "question_results/2022/C/q04/result.json",
  "report_path": "question_reports/2022/C/q04/report.md",
  "artifact_path": "question_artifacts/2022/C/q04/daily_trades.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'C' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'C' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'C' / 'q04'


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
