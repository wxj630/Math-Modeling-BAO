from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-B",
  "year": "2022",
  "code": "B",
  "question": "q05",
  "question_title": "无新增来水时的可持续年限与补水需求",
  "statement": "If no additional water is supplied and demands are fixed, how long will it take before demands are not met? How much additional water must be supplied over time?",
  "methods": "枚举供给 100% 到 42% 的短缺情景，按可规划库容和年缺口估计需求不满足时间和补水量。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/B/q05/solution.py",
  "result_path": "question_results/2022/B/q05/result.json",
  "report_path": "question_reports/2022/B/q05/report.md",
  "artifact_path": "question_artifacts/2022/B/q05/shortage_response_scenarios.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'B' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'B' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'B' / 'q05'


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
