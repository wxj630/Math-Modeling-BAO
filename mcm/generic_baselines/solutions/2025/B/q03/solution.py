from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-B",
  "year": "2025",
  "code": "B",
  "question": "q03",
  "question_title": "给朱诺旅游委员会的一页备忘录",
  "statement": "Write a one-page memo to the tourist council of Juneau outlining predictions, effects of measures, and advice on how to optimize outcomes.",
  "methods": "将最优政策、敏感性排序、收入支出反馈和迁移建议压缩为 Juneau Tourism Board 可执行备忘录。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/B/q03/solution.py",
  "result_path": "question_results/2025/B/q03/result.json",
  "report_path": "question_reports/2025/B/q03/report.md",
  "artifact_path": "question_artifacts/2025/B/q03/tourism_policy_frontier.png"
}
RESULT_PATH = BASE / "results" / '2025' / 'B' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'B' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'B' / 'q03'


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
