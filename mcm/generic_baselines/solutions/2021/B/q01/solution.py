from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-B",
  "year": "2021",
  "code": "B",
  "question": "q01",
  "question_title": "Rapid Bushfire Response 无人机组合采购模型",
  "statement": "Create a model to determine the optimal numbers and mix of SSA drones and Radio Repeater drones to purchase.",
  "methods": "使用官方 AUD 10000 单价、30km 航程、20m/s、2.5h 续航、1.75h 充电、10W/20km repeater 参数，对 SSA/repeater 组合网格搜索。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/B/q01/solution.py",
  "result_path": "question_results/2021/B/q01/result.json",
  "report_path": "question_reports/2021/B/q01/report.md",
  "artifact_path": "question_artifacts/2021/B/q01/drone_mix_optimization.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'B' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'B' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'B' / 'q01'


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
