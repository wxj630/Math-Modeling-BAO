from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-A",
  "year": "2022",
  "code": "A",
  "question": "q05",
  "question_title": "六人团队计时赛扩展与 Directeur Sportif 指导",
  "statement": "Discuss how to extend your model to a six-rider team time trial where the team time is determined when the fourth rider crosses the finish line. Write a two-page rider's race guidance for a Directeur Sportif.",
  "methods": "把个人功率 profile 扩展为六人拉扯分工，第 4 名过线作为目标；同时输出面向 Directeur Sportif 的非技术比赛指导。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/A/q05/solution.py",
  "result_path": "question_results/2022/A/q05/result.json",
  "report_path": "question_reports/2022/A/q05/report.md",
  "artifact_path": "question_artifacts/2022/A/q05/power_course_frontier.png"
}
RESULT_PATH = BASE / "results" / '2022' / 'A' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'A' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'A' / 'q05'


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
