from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-E",
  "year": "2022",
  "code": "E",
  "question": "q10",
  "question_title": "从现行时间线过渡到延长 10 年的采伐间隔",
  "statement": "Suppose the best management plan includes a time between harvests that is 10 years longer than current practices in the forest. Discuss a transition strategy.",
  "methods": "把 40 年现行间隔逐步过渡到 50 年目标间隔，列出库存基线、合同缓冲、长寿命产品转向和社区阈值。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/E/q10/solution.py",
  "result_path": "question_results/2022/E/q10/result.json",
  "report_path": "question_reports/2022/E/q10/report.md",
  "artifact_path": "question_artifacts/2022/E/q10/transition_schedule.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'E' / 'q10' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'E' / 'q10' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'E' / 'q10'


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
