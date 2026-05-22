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
  "question": "q03",
  "question_title": "兼顾社会价值的森林利用决策模型",
  "statement": "Develop a decision model to inform forest managers of the best use of a forest, balancing the various ways that forests are valued.",
  "methods": "将碳封存、生物多样性、游憩、文化价值和林产品需求写入透明加权评分，并保留权重审计。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/E/q03/solution.py",
  "result_path": "question_results/2022/E/q03/result.json",
  "report_path": "question_reports/2022/E/q03/report.md",
  "artifact_path": "question_artifacts/2022/E/q03/management_plan_scores.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'E' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'E' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'E' / 'q03'


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
