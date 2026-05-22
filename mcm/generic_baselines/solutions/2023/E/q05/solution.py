from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-E",
  "year": "2023",
  "code": "E",
  "question": "q05",
  "question_title": "宣传最有效干预策略的一页 flyer",
  "statement": "Finally, for one of your identified locations and its most-effective intervention strategy, produce a 1-page flyer to promote the strategy for that location.",
  "methods": "把保护夜空、暖色全截光、夜间调光、标识限光、生态迁徙和睡眠/安全收益压缩成一页公众宣传 flyer。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/E/q05/solution.py",
  "result_path": "question_results/2023/E/q05/result.json",
  "report_path": "question_reports/2023/E/q05/report.md",
  "artifact_path": "question_artifacts/2023/E/q05/light_pollution_risk_frontier.png"
}
RESULT_PATH = BASE / "results" / '2023' / 'E' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'E' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'E' / 'q05'


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
