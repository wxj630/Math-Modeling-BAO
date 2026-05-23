from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-E",
  "year": "2021",
  "code": "E",
  "question": "q02",
  "question_title": "公平与可持续优先系统的变化和实施时间",
  "statement": "What happens if a food system is optimized for equity and sustainability? How would that system differ from the current one? How long would such a system take to implement?",
  "methods": "比较 current_efficiency_profit 与 equity_sustainability_balanced 权重下的国家得分、环境压力和食品不安全差距，并用 15 年阶段计划表示实施节奏。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/E/q02/solution.py",
  "result_path": "question_results/2021/E/q02/result.json",
  "report_path": "question_reports/2021/E/q02/report.md",
  "artifact_path": "question_artifacts/2021/E/q02/food_system_transition_plan.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'E' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'E' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'E' / 'q02'


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
