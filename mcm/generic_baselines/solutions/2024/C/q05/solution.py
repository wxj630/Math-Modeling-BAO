from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-C",
  "year": "2024",
  "code": "C",
  "question": "q05",
  "question_title": "给教练的备忘录与训练建议",
  "statement": "Prepare a memo summarizing findings and advice to coaches about the role of momentum and how to prepare players for flow-changing events.",
  "methods": "把势头定义、随机性证据、换向预警指标和比赛泛化结果转化为教练可执行的临场监控建议。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2024/C/q05/solution.py",
  "result_path": "question_results/2024/C/q05/result.json",
  "report_path": "question_reports/2024/C/q05/report.md",
  "artifact_path": "question_artifacts/2024/C/q05/final_match_momentum_flow.png"
}
RESULT_PATH = BASE / "results" / '2024' / 'C' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'C' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'C' / 'q05'


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
