from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-B",
  "year": "2017",
  "code": "B",
  "question": "q02",
  "question_title": "轻交通与重交通吞吐性能",
  "statement": "Determine the performance of your solution in light and heavy traffic.",
  "methods": "用收费亭服务率、下游车道容量和并道冲突惩罚估算 light/heavy demand 下的通过量、瓶颈和平均延误，确保所有容量参数可审计替换。对应模型：通行能力、瓶颈分析、排队延误估计。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/B/q02/solution.py",
  "result_path": "question_results/2017/B/q02/result.json",
  "report_path": "question_reports/2017/B/q02/report.md",
  "artifact_path": "question_artifacts/2017/B/q02/traffic_performance.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'B' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'B' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'B' / 'q02'


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
