from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-F",
  "year": "2020",
  "code": "F",
  "question": "q02",
  "question_title": "人权迁移和文化保护政策",
  "statement": "Propose policies to address EDPs in terms of human rights and cultural preservation.",
  "methods": "比较 migration compacts、portable citizenship、cultural continuity trust、host adaptation finance 和 UN-triggered EDP protocol。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/F/q02/solution.py",
  "result_path": "question_results/2020/F/q02/result.json",
  "report_path": "question_reports/2020/F/q02/report.md",
  "artifact_path": "question_artifacts/2020/F/q02/policy_impact_scores.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'F' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'F' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'F' / 'q02'


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
