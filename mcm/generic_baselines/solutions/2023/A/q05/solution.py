from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-A",
  "year": "2023",
  "code": "A",
  "question": "q05",
  "question_title": "污染和栖息地减少对结论的影响",
  "statement": "How do other factors such as pollution and habitat reduction impact your conclusions?",
  "methods": "把污染负荷作为生长惩罚、栖息地质量作为承载量约束，比较 baseline、high pollution、habitat reduction、combined stress 和 restoration buffer。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/A/q05/solution.py",
  "result_path": "question_results/2023/A/q05/result.json",
  "report_path": "question_reports/2023/A/q05/report.md",
  "artifact_path": "question_artifacts/2023/A/q05/stressor_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'A' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'A' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'A' / 'q05'


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
