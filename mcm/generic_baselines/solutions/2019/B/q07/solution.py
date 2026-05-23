from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-B",
  "year": "2019",
  "code": "B",
  "question": "q07",
  "question_title": "HELP, Inc. 管理层备忘录",
  "statement": "Prepare the Part 2 memo for HELP, Inc. leadership.",
  "methods": "把机队、装箱、选址、配送和视频侦察权衡整理为 HELP, Inc. 可读备忘录。对应模型：执行摘要、灾害响应建议。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/B/q07/solution.py",
  "result_path": "question_results/2019/B/q07/result.json",
  "report_path": "question_reports/2019/B/q07/report.md",
  "artifact_path": "question_artifacts/2019/B/q07/dronego_response_frontier.png"
}
RESULT_PATH = BASE / "results" / '2019' / 'B' / 'q07' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'B' / 'q07' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'B' / 'q07'


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
