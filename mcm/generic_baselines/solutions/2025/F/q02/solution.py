from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-F",
  "year": "2025",
  "code": "F",
  "question": "q02",
  "question_title": "国家网络安全政策有效性特征",
  "statement": "As you explore the published national security policies of various countries and compare these with the distribution of cybercrimes, what patterns emerge that would help you identify parts of a policy or law that are particularly effective (or particularly ineffective) in addressing cybercrime (through prevention, prosecution, or other mitigation efforts)? Depending on your analytical approach, it may be relevant to consider when each policy was adopted.",
  "methods": "构建透明政策特征矩阵：法律框架、国家战略、强制报告、事件响应、能力建设和国际合作；用 ITU GCI 框架验证而不新造网络安全指数。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/F/q02/solution.py",
  "result_path": "question_results/2025/F/q02/result.json",
  "report_path": "question_reports/2025/F/q02/report.md",
  "artifact_path": "question_artifacts/2025/F/q02/policy_feature_matrix.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'F' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'F' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'F' / 'q02'


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
