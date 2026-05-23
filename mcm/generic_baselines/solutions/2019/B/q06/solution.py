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
  "question": "q06",
  "question_title": "道路网络视频侦察飞行计划",
  "statement": "Provide a flight plan for onboard video cameras to assess major highways and roads.",
  "methods": "把 PR-3、PR-52、PR-22 和 San Juan metro hospital ring 作为视频侦察走廊，安排 video-capable drones 在医疗波次之间巡检。对应模型：覆盖路径规划、侦察调度。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/B/q06/solution.py",
  "result_path": "question_results/2019/B/q06/result.json",
  "report_path": "question_reports/2019/B/q06/report.md",
  "artifact_path": "question_artifacts/2019/B/q06/video_recon_flight_plan.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'B' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'B' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'B' / 'q06'


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
