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
  "question": "q03",
  "question_title": "尚未获奖国家的首枚奖牌概率",
  "statement": "Include countries that have yet to earn medals and project how many will earn their first medal in the next Olympics, with odds/confidence.",
  "methods": "将有参赛记录但历史总奖牌为 0 的国家纳入候选，用随机森林树预测分布估计 P(total >= 0.5)，再求期望数量。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2025/C/q03/solution.py",
  "result_path": "question_results/2025/C/q03/result.json",
  "report_path": "question_reports/2025/C/q03/report.md",
  "artifact_path": "question_artifacts/2025/C/q03/prediction_2028.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'C' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'C' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'C' / 'q03'


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
