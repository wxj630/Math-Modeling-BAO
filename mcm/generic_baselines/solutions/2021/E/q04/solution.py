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
  "question": "q04",
  "question_title": "改变食物系统优先级的收益、成本和发生时间",
  "statement": "What are the benefits and costs of changing the priorities of a food system? When would they occur? How do these benefits and costs differ between developed and developing countries?",
  "methods": "把区域采购、再生生产、营养券、仓储减损和小生产者风险共担列为干预，按收益指数、成本、首次见效年份和发达/发展中国家适配度排序。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/E/q04/solution.py",
  "result_path": "question_results/2021/E/q04/result.json",
  "report_path": "question_reports/2021/E/q04/report.md",
  "artifact_path": "question_artifacts/2021/E/q04/food_system_benefit_cost.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'E' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'E' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'E' / 'q04'


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
