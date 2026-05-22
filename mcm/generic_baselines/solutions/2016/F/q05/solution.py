from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-F",
  "year": "2016",
  "code": "F",
  "question": "q05",
  "question_title": "Canada、China、United States 区域扩展",
  "statement": "Also consider the inclusion of other refugee destinations such as Canada, China, and the United States. Does your model work for these regions as well?",
  "methods": "把题面要求的 Canada、China、United States 纳入 extension feasibility，保留网络流/容量结构，但重新校准距离、法律准入、资源 readiness 和长期融合能力。对应模型：模型迁移、区域适配、多指标可行性评分。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/F/q05/solution.py",
  "result_path": "question_results/2016/F/q05/result.json",
  "report_path": "question_reports/2016/F/q05/report.md",
  "artifact_path": "question_artifacts/2016/F/q05/route_parameters.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'F' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'F' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'F' / 'q05'


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
