from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-A",
  "year": "2022",
  "code": "A",
  "question": "q04",
  "question_title": "偏离目标功率分布的敏感性与 split 区间",
  "statement": "Determine how sensitive the results are to rider deviations from the target power distribution and provide expected split-time ranges at key parts of a course.",
  "methods": "对指导案例进行 ±4%/±8% 目标功率扰动，比较完赛时间、能量余量和高功率负荷，形成 Directeur Sportif 可用 split 容忍带。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/A/q04/solution.py",
  "result_path": "question_results/2022/A/q04/result.json",
  "report_path": "question_reports/2022/A/q04/report.md",
  "artifact_path": "question_artifacts/2022/A/q04/target_power_deviation.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'A' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'A' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'A' / 'q04'


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
