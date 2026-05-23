from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-E",
  "year": "2024",
  "code": "E",
  "question": "q07",
  "question_title": "社区保护程度、计划、时间表与成本建议信",
  "statement": "Develop a preservation model for community leaders to use to determine the extent of measures they should take to preserve buildings in their community. Select a historic landmark - not Cape Hatteras Lighthouse - that is in a location that experiences extreme weather events. Apply your insurance and preservation models to assess the value of this landmark. Compose a one-page letter to the community recommending a plan, timeline, and cost proposal.",
  "methods": "用保护紧迫度和 benefit/cost ratio 给出分阶段保护计划、7 年时间表、成本建议和给社区的一页信。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/E/q07/solution.py",
  "result_path": "question_results/2024/E/q07/result.json",
  "report_path": "question_reports/2024/E/q07/report.md",
  "artifact_path": "question_artifacts/2024/E/q07/insurance_preservation_frontier.png"
}
RESULT_PATH = BASE / "results" / '2024' / 'E' / 'q07' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'E' / 'q07' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'E' / 'q07'


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
