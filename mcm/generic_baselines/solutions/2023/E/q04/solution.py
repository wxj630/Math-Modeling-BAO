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
  "question": "q04",
  "question_title": "两类地点的最有效干预选择",
  "statement": "Choose two of your locations and use your metric to determine which of your intervention strategies is most effective for each of them. Discuss how the chosen intervention strategy impacts the risk level for the location.",
  "methods": "对 protected_land 和 urban 两类地点枚举干预策略，在风险降低、安全惩罚和可行性约束下选择 post-intervention risk 最低方案。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/E/q04/solution.py",
  "result_path": "question_results/2023/E/q04/result.json",
  "report_path": "question_reports/2023/E/q04/report.md",
  "artifact_path": "question_artifacts/2023/E/q04/selected_intervention_impacts.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'E' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'E' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'E' / 'q04'


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
