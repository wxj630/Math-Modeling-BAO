from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-B",
  "year": "2024",
  "code": "B",
  "question": "q02",
  "question_title": "主船与救援船搜索装备准备",
  "statement": "Prepare - What, if any, additional search equipment would you recommend the company carry on the host ship to deploy if necessary? You may consider different types of equipment but must also consider costs associated with availability, maintenance, readiness, and usage of this equipment. What additional equipment might a rescue vessel need to bring in to assist if necessary?",
  "methods": "多指标装备评价：覆盖面积、探测质量、准备时间、使用成本和维护负担加权，区分主船常备设备与救援船重型设备。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/B/q02/solution.py",
  "result_path": "question_results/2024/B/q02/result.json",
  "report_path": "question_reports/2024/B/q02/report.md",
  "artifact_path": "question_artifacts/2024/B/q02/equipment_tradeoffs.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'B' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'B' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'B' / 'q02'


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
