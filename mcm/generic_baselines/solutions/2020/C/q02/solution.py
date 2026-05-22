from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-C",
  "year": "2020",
  "code": "C",
  "question": "q02",
  "question_title": "产品声誉随时间增加或下降的模式",
  "statement": "Identify and discuss time-based measures and patterns within each data set that might suggest a product's reputation is increasing or decreasing.",
  "methods": "按 review_date 聚合月度 mean_star、review_count 和 low_rating_share，计算月度评分斜率和低分斜率判断声誉方向。",
  "source_type": "official_comap_tsv_zip",
  "solution_path": "question_solutions/2020/C/q02/solution.py",
  "result_path": "question_results/2020/C/q02/result.json",
  "report_path": "question_reports/2020/C/q02/report.md",
  "artifact_path": "question_artifacts/2020/C/q02/monthly_reputation_trends.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'C' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'C' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'C' / 'q02'


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
