from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-B",
  "year": "2016",
  "code": "B",
  "question": "q02",
  "question_title": "成本、风险、收益与重要因素估计",
  "statement": "Your model should include quantitative and/or qualitative estimates of costs, risks, benefits, as well as other important factors.",
  "methods": "对 water jets、high energy lasers、sweeper satellites、tracking subscription 逐项估计 capex、opex、revenue、10 年移除数量、技术风险、监管风险和 scalability。对应模型：多指标综合评价、成本效益分析、风险矩阵。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/B/q02/solution.py",
  "result_path": "question_results/2016/B/q02/result.json",
  "report_path": "question_reports/2016/B/q02/report.md",
  "artifact_path": "question_artifacts/2016/B/q02/alternative_scores.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'B' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'B' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'B' / 'q02'


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
