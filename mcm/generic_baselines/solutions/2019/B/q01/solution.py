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
  "question": "q01",
  "question_title": "DroneGo 波多黎各灾害响应系统",
  "statement": "Develop a DroneGo disaster response system to support the Puerto Rico hurricane disaster scenario.",
  "methods": "读取官方 PDF 附件表中的 drone 尺寸、载荷、速度、飞行时间、货舱、MED 包尺寸和需求地点，构造三集装箱 DroneGo 响应系统。对应模型：设施选址、配送调度、装箱规划。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/B/q01/solution.py",
  "result_path": "question_results/2019/B/q01/result.json",
  "report_path": "question_reports/2019/B/q01/report.md",
  "artifact_path": "question_artifacts/2019/B/q01/drone_fleet_plan.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'B' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'B' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'B' / 'q01'


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
