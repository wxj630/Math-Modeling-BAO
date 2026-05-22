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
  "question": "q09",
  "question_title": "推荐森林管理计划及理由",
  "statement": "What forest management plan should be used for this forest? Why is this the best approach?",
  "methods": "用 100 年 CO2e、林产品需求、生物多样性敏感度和社会得分解释推荐方案。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/E/q09/solution.py",
  "result_path": "question_results/2022/E/q09/result.json",
  "report_path": "question_reports/2022/E/q09/report.md",
  "artifact_path": "question_artifacts/2022/E/q09/management_tradeoff_frontier.png"
}
RESULT_PATH = BASE / "results" / '2022' / 'E' / 'q09' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'E' / 'q09' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'E' / 'q09'


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
