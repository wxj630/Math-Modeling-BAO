from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-A",
  "year": "2025",
  "code": "A",
  "question": "q01",
  "question_title": "楼梯使用频率反演",
  "statement": "How often were the stairs used?",
  "methods": "官方 PDF 题面参数 + 非破坏测量模板 + Archard 型磨损守恒反演：由中心磨损深度、材料磨损系数和年龄先验估计累计通行量与日均使用人数。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/A/q01/solution.py",
  "result_path": "question_results/2025/A/q01/result.json",
  "report_path": "question_reports/2025/A/q01/report.md",
  "artifact_path": "question_artifacts/2025/A/q01/measurement_template.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'A' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'A' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'A' / 'q01'


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
