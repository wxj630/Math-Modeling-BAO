from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-D",
  "year": "2016",
  "code": "D",
  "question": "q03",
  "question_title": "2050 通信网络关系与容量预测",
  "statement": "Use your model to predict the communication networks' relationships and capacities around the year 2050.",
  "methods": "将五个官方时期的 channel capacity 指数做保守 log-linear 外推，并给出 human-to-human、human-to-platform、machine-to-machine、local-to-global 四类关系变化。对应模型：趋势外推、技术扩散、容量预测、网络关系图谱。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/D/q03/solution.py",
  "result_path": "question_results/2016/D/q03/result.json",
  "report_path": "question_reports/2016/D/q03/report.md",
  "artifact_path": "question_artifacts/2016/D/q03/communication_capacity_2050.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'D' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'D' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'D' / 'q03'


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
