from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-B",
  "year": "2019",
  "code": "B",
  "question": "q03",
  "question_title": "一到三个集装箱的最佳布置位置",
  "statement": "Identify best locations on Puerto Rico to position one, two, or three cargo containers for medical delivery and road reconnaissance.",
  "methods": "按需求点距离、道路视频覆盖和港口/机场接入评分 San Juan、Ceiba、Arecibo 三个 staging nodes。对应模型：设施选址、多目标评分。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/B/q03/solution.py",
  "result_path": "question_results/2019/B/q03/result.json",
  "report_path": "question_reports/2019/B/q03/report.md",
  "artifact_path": "question_artifacts/2019/B/q03/container_location_scores.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'B' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'B' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'B' / 'q03'


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
