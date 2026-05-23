from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-A",
  "year": "2024",
  "code": "A",
  "question": "q03",
  "question_title": "性别比变化对生态系统稳定性的影响",
  "statement": "What is the impact on the stability of the ecosystem given the changes in the sex ratios of lampreys?",
  "methods": "在资源水平和七鳃鳗控制压力上做确定性网格，比较自适应性别比与固定 1:1 性别比的稳定性指标。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/A/q03/solution.py",
  "result_path": "question_results/2024/A/q03/result.json",
  "report_path": "question_reports/2024/A/q03/report.md",
  "artifact_path": "question_artifacts/2024/A/q03/stability_surface.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'A' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'A' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'A' / 'q03'


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
