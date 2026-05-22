from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-D",
  "year": "2016",
  "code": "D",
  "question": "q01",
  "question_title": "信息流与新闻筛选模型",
  "statement": "Develop one or more model(s) that allow(s) you to explore the flow of information and filter or find what qualifies as news.",
  "methods": "只使用官方题面给出的五个传播时期，构造 media access、transmission speed、network connectivity、gatekeeping filter 和 channel capacity 的显式时代参数；用加权 news score 判断 presidential assassination、war news、celebrity rumor、local storm、viral video 是否达到新闻阈值。对应模型：信息扩散、新闻价值评分、多指标综合评价、阈值分类。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/D/q01/solution.py",
  "result_path": "question_results/2016/D/q01/result.json",
  "report_path": "question_reports/2016/D/q01/report.md",
  "artifact_path": "question_artifacts/2016/D/q01/era_parameters.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'D' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'D' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'D' / 'q01'


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
