from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-C",
  "year": "2015",
  "code": "C",
  "question": "q05",
  "question_title": "中层 30% 流失、无外部招聘与内部晋升情景",
  "statement": "Simulate the effect of 30% of both junior managers and experienced supervisors leaving, with no external recruiting and with only qualified employees promoted over the next two years. Explain the effect on organizational HR health.",
  "methods": "对 junior managers 和 experienced supervisors 施加官方要求的 30% 流失冲击，比较无外部招聘与资深主管/初级主管/资深员工内部晋升链；晋升池比例为显式假设。对应模型：晋升链仿真、岗位替补模型、瓶颈分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2015/C/q05/solution.py",
  "result_path": "question_results/2015/C/q05/result.json",
  "report_path": "question_reports/2015/C/q05/report.md",
  "artifact_path": "question_artifacts/2015/C/q05/promotion_shock_projection.csv"
}
RESULT_PATH = BASE / "results" / '2015' / 'C' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'C' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'C' / 'q05'


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
