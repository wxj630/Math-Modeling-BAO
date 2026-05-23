from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-Z",
  "year": "2023",
  "code": "Z",
  "question": "q03",
  "question_title": "可行性、实施时间线和影响评估",
  "statement": "Consider the feasibility, timeline to implement, and impact of potential strategies on your metrics.",
  "methods": "对推荐策略生成 IOC 治理里程碑，显式记录 feasibility、timeline years、governance complexity 和 impact score，避免把策略推荐变成不可审计口号。对应模型：实施路线图、治理复杂度评分。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/F/q03/solution.py",
  "result_path": "question_results/2023/F/q03/result.json",
  "report_path": "question_reports/2023/F/q03/report.md",
  "artifact_path": "question_artifacts/2023/F/q03/implementation_timeline.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'Z' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'Z' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'Z' / 'q03'


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
