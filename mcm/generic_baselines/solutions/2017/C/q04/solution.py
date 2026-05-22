from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-C",
  "year": "2017",
  "code": "C",
  "question": "q04",
  "question_title": "自动驾驶专用车道条件与政策",
  "statement": "Identify under what conditions, if any, lanes should be dedicated to self-driving cooperating cars and whether other policy changes are suggested.",
  "methods": "对 lanes>=3 且 AV share>=50% 的路段比较混行与一条 AV-only lane 的 peak vehicle-hours，若专用车道不能改善则输出不设专用车道的约束性政策。对应模型：瓶颈容量比较、车道分配优化、政策约束规则。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2017/C/q04/solution.py",
  "result_path": "question_results/2017/C/q04/result.json",
  "report_path": "question_reports/2017/C/q04/report.md",
  "artifact_path": "question_artifacts/2017/C/q04/dedicated_lane_candidates.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'C' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'C' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'C' / 'q04'


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
