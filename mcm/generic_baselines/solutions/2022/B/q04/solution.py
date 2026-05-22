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
  "question": "q04",
  "question_title": "Mexico 权利与加利福尼亚湾入海流量",
  "statement": "Mexico has claims on residual water. Address Mexico's rights and how much water should flow into the Gulf of California after allocations.",
  "methods": "把 Mexico 最小流和 Gulf 生态流写成显式约束，在州部门分配前保护，除非居民最低服务触发紧急重算。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/B/q04/solution.py",
  "result_path": "question_results/2022/B/q04/result.json",
  "report_path": "question_reports/2022/B/q04/report.md",
  "artifact_path": "question_artifacts/2022/B/q04/state_sector_allocations.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'B' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'B' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'B' / 'q04'


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
