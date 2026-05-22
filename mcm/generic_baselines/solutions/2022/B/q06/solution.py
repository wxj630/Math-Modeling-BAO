from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-B",
  "year": "2022",
  "code": "B",
  "question": "q06",
  "question_title": "解决水资源与水电竞争利益的标准",
  "statement": "Recommend the best means to resolve competing interests of water availability and electricity production. Explicitly state the criteria.",
  "methods": "列出不使用历史协议/政治权力、居民最低服务、Mexico/Gulf 保护、部门公平权重和水电替代触发的数学标准。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/B/q06/solution.py",
  "result_path": "question_results/2022/B/q06/result.json",
  "report_path": "question_reports/2022/B/q06/report.md",
  "artifact_path": "question_artifacts/2022/B/q06/state_sector_allocations.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'B' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'B' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'B' / 'q06'


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
