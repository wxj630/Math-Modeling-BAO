from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-A",
  "year": "2023",
  "code": "A",
  "question": "q06",
  "question_title": "长期可行性和大环境管理建议",
  "statement": "What does your model indicate should be done to ensure the long-term viability of a plant community and what are the impacts on the larger environment?",
  "methods": "把物种数阈值、功能性状、干旱敏感性和污染栖息地压力合成为管理前沿，给出最少功能物种数、恢复缓冲和大环境影响备忘录。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/A/q06/solution.py",
  "result_path": "question_results/2023/A/q06/result.json",
  "report_path": "question_reports/2023/A/q06/report.md",
  "artifact_path": "question_artifacts/2023/A/q06/viability_strategy_frontier.png"
}
RESULT_PATH = BASE / "results" / '2023' / 'A' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'A' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'A' / 'q06'


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
