from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-B",
  "year": "2017",
  "code": "B",
  "question": "q03",
  "question_title": "自动驾驶车辆比例敏感性",
  "statement": "How does your solution change as more autonomous (self-driving) vehicles are added to the traffic mix?",
  "methods": "扫描 0%-80% 自动驾驶比例，用车头时距容量倍率和建议并道长度调整估计是否需要保留 staged zipper 或设置协同并道车道。对应模型：混合交通容量、敏感性分析、政策阈值。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/B/q03/solution.py",
  "result_path": "question_results/2017/B/q03/result.json",
  "report_path": "question_reports/2017/B/q03/report.md",
  "artifact_path": "question_artifacts/2017/B/q03/autonomous_vehicle_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'B' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'B' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'B' / 'q03'


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
