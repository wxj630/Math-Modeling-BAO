from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-E",
  "year": "2020",
  "code": "E",
  "question": "q05",
  "question_title": "给 ICM 的两页塑料废弃物备忘录",
  "statement": "Write a two-page memo to ICM describing the target, timeline, and circumstances that accelerate or hinder achievement.",
  "methods": "把 2050 target、减量时间线、公平融资、加速条件和阻碍条件整理为面向 International Council of Plastic Waste Management 的备忘录。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/E/q05/solution.py",
  "result_path": "question_results/2020/E/q05/result.json",
  "report_path": "question_reports/2020/E/q05/report.md",
  "artifact_path": "question_artifacts/2020/E/q05/plastic_policy_package_scores.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'E' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'E' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'E' / 'q05'


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
