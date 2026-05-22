from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-D",
  "year": "2023",
  "code": "D",
  "question": "q02",
  "question_title": "网络结构驱动的 UN 优先级和 10 年计划",
  "statement": "Use the individual SDGs, as well as the structure of your network, to set priorities that can most efficiently move the work of the UN forward. How did you evaluate the effectiveness of each priority? What could be reasonable to achieve in the next 10 years if your priorities are initiated?",
  "methods": "PageRank、介数中心性、出边强度、入边支持和直接需求指数综合评价，生成 17 个目标排序和 10 年 first-wave priority portfolio。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/D/q02/solution.py",
  "result_path": "question_results/2023/D/q02/result.json",
  "report_path": "question_reports/2023/D/q02/report.md",
  "artifact_path": "question_artifacts/2023/D/q02/priority_ranking.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'D' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'D' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'D' / 'q02'


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
