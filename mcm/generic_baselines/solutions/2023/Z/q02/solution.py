from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-Z",
  "year": "2023",
  "code": "Z",
  "question": "q02",
  "question_title": "永久举办地与四季分拆等策略评分",
  "statement": "Consider potential strategies such as permanent Summer/Winter locations or splitting Olympic sports into four smaller Games.",
  "methods": "在官方点名的 permanent_summer_winter_sites、four_season_split_games 基础上加入 status quo reform、regional rotation 和 distributed existing venues，对各策略做确定性多目标评分。对应模型：情景分析、多目标决策。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/F/q02/solution.py",
  "result_path": "question_results/2023/F/q02/result.json",
  "report_path": "question_reports/2023/F/q02/report.md",
  "artifact_path": "question_artifacts/2023/F/q02/olympic_strategy_scores.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'Z' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'Z' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'Z' / 'q02'


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
