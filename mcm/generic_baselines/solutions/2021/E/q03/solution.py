from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-E",
  "year": "2021",
  "code": "E",
  "question": "q03",
  "question_title": "发达和发展中国家的模型应用",
  "statement": "Once you have developed your food system model, apply your model to at least one developed and one developing country to support your findings.",
  "methods": "将相同评分模型应用到 United States、Germany、India 和 Kenya，显式标注 developed/developing 分组、当前分、目标分和主要缺口。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/E/q03/solution.py",
  "result_path": "question_results/2021/E/q03/result.json",
  "report_path": "question_reports/2021/E/q03/report.md",
  "artifact_path": "question_artifacts/2021/E/q03/country_food_system_applications.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'E' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'E' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'E' / 'q03'


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
