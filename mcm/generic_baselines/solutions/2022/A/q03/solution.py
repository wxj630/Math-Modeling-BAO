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
  "question": "q03",
  "question_title": "天气条件对赛果的敏感性",
  "statement": "Determine the potential impact of weather conditions, including wind directions and wind strengths, to determine how sensitive your results are for small differences in the weather and environment.",
  "methods": "在同一逐段功率计划下枚举顺风、静风和逆风，把风速按赛段暴露系数折算到空气阻力项，输出完赛时间变化。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/A/q03/solution.py",
  "result_path": "question_results/2022/A/q03/result.json",
  "report_path": "question_reports/2022/A/q03/report.md",
  "artifact_path": "question_artifacts/2022/A/q03/weather_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'A' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'A' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'A' / 'q03'


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
