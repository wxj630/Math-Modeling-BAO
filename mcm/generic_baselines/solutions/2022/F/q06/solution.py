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
  "question": "q06",
  "question_title": "未来小行星采矿部门的可能结构",
  "statement": "Present, describe, and justify one likely vision for the future of asteroid mining.",
  "methods": "推荐 open science public-private coalition 或 UN licensed benefit-sharing regime，并说明技术可行、资本可得和条约对齐之间的权衡。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/F/q06/solution.py",
  "result_path": "question_results/2022/F/q06/result.json",
  "report_path": "question_reports/2022/F/q06/report.md",
  "artifact_path": "question_artifacts/2022/F/q06/space_equity_frontier.png"
}
RESULT_PATH = BASE / "results" / '2022' / 'F' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'F' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'F' / 'q06'


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
