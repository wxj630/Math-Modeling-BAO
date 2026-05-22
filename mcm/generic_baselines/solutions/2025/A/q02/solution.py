from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-A",
  "year": "2025",
  "code": "A",
  "question": "q02",
  "question_title": "上下行方向偏好识别",
  "statement": "Was a certain direction of travel favored by the people using the stairs?",
  "methods": "利用踏步前/后缘圆角差、沿行进方向坡度和磨损非对称性构造方向偏好指标，判断上行、下行或平衡使用。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/A/q02/solution.py",
  "result_path": "question_results/2025/A/q02/result.json",
  "report_path": "question_reports/2025/A/q02/report.md",
  "artifact_path": "question_artifacts/2025/A/q02/traffic_pattern_summary.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'A' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'A' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'A' / 'q02'


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
