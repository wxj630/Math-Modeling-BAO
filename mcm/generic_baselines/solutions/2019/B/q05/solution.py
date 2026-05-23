from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-B",
  "year": "2019",
  "code": "B",
  "question": "q05",
  "question_title": "医疗包载荷、路线与日程",
  "statement": "Provide payload packing configurations, delivery routes and schedule to meet the emergency medical package requirements.",
  "methods": "为每个医院需求行选择最近 staging base 和合适 drone type，计算 round-trip km、sortie minutes 和 morning/midday/afternoon schedule block。对应模型：车辆路径近似、日程调度。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/B/q05/solution.py",
  "result_path": "question_results/2019/B/q05/result.json",
  "report_path": "question_reports/2019/B/q05/report.md",
  "artifact_path": "question_artifacts/2019/B/q05/delivery_route_schedule.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'B' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'B' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'B' / 'q05'


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
