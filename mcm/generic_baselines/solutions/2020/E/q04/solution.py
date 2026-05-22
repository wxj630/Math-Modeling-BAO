from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-E",
  "year": "2020",
  "code": "E",
  "question": "q04",
  "question_title": "全球危机与解决方案的公平问题",
  "statement": "Discuss equity issues that arise from the global crisis and intended solutions, and how ICM should address them.",
  "methods": "构造 responsibility_score 与 support_need_score，区分高消费高能力地区的义务和高负担低能力地区的资金技术支持需求。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/E/q04/solution.py",
  "result_path": "question_results/2020/E/q04/result.json",
  "report_path": "question_reports/2020/E/q04/report.md",
  "artifact_path": "question_artifacts/2020/E/q04/plastic_equity_analysis.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'E' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'E' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'E' / 'q04'


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
