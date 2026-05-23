from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-A",
  "year": "2020",
  "code": "A",
  "question": "q03",
  "question_title": "小型渔业公司的运营适应策略",
  "statement": "Recommend operational changes that small fishing companies can make as fish move north.",
  "methods": "比较 gear modernization、cooperative vessel sharing、cold-chain landing partnership、alternative species portfolio 和 joint access agreement 的 range gain、成本和配额韧性。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/A/q03/solution.py",
  "result_path": "question_results/2020/A/q03/result.json",
  "report_path": "question_reports/2020/A/q03/report.md",
  "artifact_path": "question_artifacts/2020/A/q03/fishery_strategy_scores.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'A' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'A' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'A' / 'q03'


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
