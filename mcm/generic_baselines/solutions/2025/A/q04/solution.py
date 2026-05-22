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
  "question": "q04",
  "question_title": "磨损与历史信息一致性",
  "statement": "Is the wear consistent with the information available?",
  "methods": "把日均使用人数、候选年龄区间、中心通行槽、补丁边界和相邻踏步突变放入一致性检查表，识别需要降权的维修踏步。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/A/q04/solution.py",
  "result_path": "question_results/2025/A/q04/result.json",
  "report_path": "question_reports/2025/A/q04/report.md",
  "artifact_path": "question_artifacts/2025/A/q04/wear_profile.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'A' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'A' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'A' / 'q04'


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
