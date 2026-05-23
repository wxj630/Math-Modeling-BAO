from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-B",
  "year": "2024",
  "code": "B",
  "question": "q03",
  "question_title": "初始部署点、搜索路径与发现概率",
  "statement": "Search - Develop a model that will use information from your location model(s) to recommend initial points of deployment and search patterns for the equipment so as to minimize the time to location of a lost submersible. Determine the probability of finding the submersible as a function of time and accumulated search results.",
  "methods": "把位置椭圆转成部署点，按有效扫测面积累计更新发现概率 `1-exp(-swept_area/uncertainty_area)`，形成 24 小时搜索曲线。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/B/q03/solution.py",
  "result_path": "question_results/2024/B/q03/result.json",
  "report_path": "question_reports/2024/B/q03/report.md",
  "artifact_path": "question_artifacts/2024/B/q03/search_probability.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'B' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'B' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'B' / 'q03'


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
