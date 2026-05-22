from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-F",
  "year": "2022",
  "code": "F",
  "question": "q03",
  "question_title": "影响公平结果的关键因素",
  "statement": "What are the factors that influence that impact, and how?",
  "methods": "显式记录资金门槛、治理开放度、收益分配、开放科学、风险控制和和平使用等因素如何进入公平模型。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/F/q03/solution.py",
  "result_path": "question_results/2022/F/q03/result.json",
  "report_path": "question_reports/2022/F/q03/report.md",
  "artifact_path": "question_artifacts/2022/F/q03/asteroid_mining_scenarios.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'F' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'F' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'F' / 'q03'


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
