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
  "question": "q04",
  "question_title": "各类无人机任务配置",
  "statement": "For each type of drone included in the DroneGo fleet, describe its role and capability.",
  "methods": "按 payload、range、video 和 cargo bay compatibility 给每类入选 drone 分配医疗、快速小包、重载或持续观察角色。对应模型：任务分配、能力矩阵。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/B/q04/solution.py",
  "result_path": "question_results/2019/B/q04/result.json",
  "report_path": "question_reports/2019/B/q04/report.md",
  "artifact_path": "question_artifacts/2019/B/q04/drone_fleet_plan.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'B' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'B' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'B' / 'q04'


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
