from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-F",
  "year": "2022",
  "code": "F",
  "question": "q02",
  "question_title": "小行星采矿未来愿景及公平影响",
  "statement": "What might asteroid mining look like in the future, and how might asteroid mining impact global equity?",
  "methods": "比较 private first mover、state-led blocs、UN licensed benefit sharing、open science coalition 四种未来愿景，计算公平、可行性和条约对齐得分。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/F/q02/solution.py",
  "result_path": "question_results/2022/F/q02/result.json",
  "report_path": "question_reports/2022/F/q02/report.md",
  "artifact_path": "question_artifacts/2022/F/q02/asteroid_mining_scenarios.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'F' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'F' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'F' / 'q02'


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
