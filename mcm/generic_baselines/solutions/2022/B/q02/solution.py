from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-B",
  "year": "2022",
  "code": "B",
  "question": "q02",
  "question_title": "五州农业、工业、居民用水和电力分配",
  "statement": "Determine a suitable allocation of water and electricity to agriculture, industry, and residences in AZ, CA, WY, NM, and CO.",
  "methods": "建立五州三部门透明需求表；先保留 Mexico/Gulf flow，再按居民、工业、农业优先级和公平权重分配余水。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/B/q02/solution.py",
  "result_path": "question_results/2022/B/q02/result.json",
  "report_path": "question_reports/2022/B/q02/report.md",
  "artifact_path": "question_artifacts/2022/B/q02/state_sector_allocations.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'B' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'B' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'B' / 'q02'


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
