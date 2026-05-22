from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-F",
  "year": "2024",
  "code": "F",
  "question": "q05",
  "question_title": "需要哪些额外权力和资源",
  "statement": "What additional powers and resources will your client need to carry out the project?",
  "methods": "把每项干预拆成启动成本、年成本、5 年成本和所需权限，形成资源与权力清单。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/F/q05/solution.py",
  "result_path": "question_results/2024/F/q05/result.json",
  "report_path": "question_reports/2024/F/q05/report.md",
  "artifact_path": "question_artifacts/2024/F/q05/resource_plan.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'F' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'F' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'F' / 'q05'


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
