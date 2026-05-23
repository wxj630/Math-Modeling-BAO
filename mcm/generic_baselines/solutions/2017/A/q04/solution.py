from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-A",
  "year": "2017",
  "code": "A",
  "question": "q04",
  "question_title": "洪水与长期低水位极端流量指导",
  "statement": "Provide guidance for emergency water flow situations, including flooding and/or prolonged low water conditions, from maximum expected discharges to minimum expected discharges.",
  "methods": "建立 maximum expected discharge、high flood、low flow、minimum expected discharge 四类情景，分别给出预泄、错峰、限制下游上升率、干旱配给和生态最小流量。对应模型：应急调度、洪水控制、干旱管理、情景分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/A/q04/solution.py",
  "result_path": "question_results/2017/A/q04/result.json",
  "report_path": "question_reports/2017/A/q04/report.md",
  "artifact_path": "question_artifacts/2017/A/q04/extreme_flow_guidance.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'A' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'A' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'A' / 'q04'


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
