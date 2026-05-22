from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-C",
  "year": "2025",
  "code": "C",
  "question": "q02",
  "question_title": "2028 洛杉矶奖牌榜预测、进步与退步国家",
  "statement": "Project the 2028 Los Angeles medal table, include prediction intervals, and identify countries likely to improve or do worse than 2024.",
  "methods": "用 2024 国家状态外推到 2028，设置美国东道主变量，比较预测总奖牌与 2024 实际总奖牌。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2025/C/q02/solution.py",
  "result_path": "question_results/2025/C/q02/result.json",
  "report_path": "question_reports/2025/C/q02/report.md",
  "artifact_path": "question_artifacts/2025/C/q02/prediction_2028.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'C' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'C' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'C' / 'q02'


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
