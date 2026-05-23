from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-E",
  "year": "2021",
  "code": "E",
  "question": "q05",
  "question_title": "十五年迁移路线图",
  "statement": "Discuss how long an equity and sustainability transition would take to implement and how the benefits and costs would occur over time.",
  "methods": "生成 1-15 年 diagnose and pilot、scale and finance、institutionalize 三阶段路线图，跟踪区域采购、减损、营养覆盖和再生面积比例。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/E/q05/solution.py",
  "result_path": "question_results/2021/E/q05/result.json",
  "report_path": "question_reports/2021/E/q05/report.md",
  "artifact_path": "question_artifacts/2021/E/q05/food_system_transition_plan.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'E' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'E' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'E' / 'q05'


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
