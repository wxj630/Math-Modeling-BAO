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
  "question": "q04",
  "question_title": "商业建议与两页执行摘要",
  "statement": "Determine whether an economically attractive opportunity exists. If viable, compare options and recommend how debris should be removed; otherwise provide innovative alternatives for avoiding collisions. Include a two-page executive summary for non-technical decision makers and media analysts.",
  "methods": "把最佳独立/组合候选、what-if 结果和 staged business model 写成给政策制定者与媒体分析师的非技术执行摘要。对应模型：执行摘要、政策建议、模型限制说明。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/B/q04/solution.py",
  "result_path": "question_results/2016/B/q04/result.json",
  "report_path": "question_reports/2016/B/q04/report.md",
  "artifact_path": "question_artifacts/2016/B/q04/debris_strategy_frontier.png"
}
RESULT_PATH = BASE / "results" / '2016' / 'B' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'B' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'B' / 'q04'


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
