from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-A",
  "year": "2022",
  "code": "A",
  "question": "q01",
  "question_title": "两类骑手与不同性别的功率 profile",
  "statement": "Define the power profiles of two types of riders. One rider should be a time trial specialist and the other a different type. Consider profiles of riders of different genders.",
  "methods": "用 critical-power + W prime 曲线定义 time trial specialist 与 climber-puncheur，并给出男女 profile、CdA、质量和能量预算。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/A/q01/solution.py",
  "result_path": "question_results/2022/A/q01/result.json",
  "report_path": "question_reports/2022/A/q01/report.md",
  "artifact_path": "question_artifacts/2022/A/q01/rider_power_profiles.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'A' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'A' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'A' / 'q01'


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
