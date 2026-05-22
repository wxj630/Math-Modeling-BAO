from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-B",
  "year": "2016",
  "code": "B",
  "question": "q01",
  "question_title": "时间相关商业机会模型",
  "statement": "Develop a time-dependent model to determine the best alternative or combination of alternatives that a private firm could adopt as a commercial opportunity to address the space debris problem.",
  "methods": "只使用官方题面中的 500,000+ tracked debris、2009 Kosmos/Iridium collision 和候选技术，构建 10 年 NPV、风险调整得分和碰撞风险降低代理指标。对应模型：项目净现值、风险收益模型、商业可行性评分。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/B/q01/solution.py",
  "result_path": "question_results/2016/B/q01/result.json",
  "report_path": "question_reports/2016/B/q01/report.md",
  "artifact_path": "question_artifacts/2016/B/q01/alternative_scores.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'B' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'B' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'B' / 'q01'


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
