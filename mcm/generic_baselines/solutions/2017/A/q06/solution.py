from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-A",
  "year": "2017",
  "code": "A",
  "question": "q06",
  "question_title": "ZRA 摘要报告与推荐策略",
  "statement": "Submit a standard summary sheet, a 1-2 page brief assessment report, and the main solution for Requirement 2.",
  "methods": "把三方案决策矩阵、推荐小坝数量、坝址、正常/极端调度、暴露限制和模型局限整理为 ZRA 管理层可读报告。对应模型：工程政策报告、执行摘要、模型限制说明。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/A/q06/solution.py",
  "result_path": "question_results/2017/A/q06/result.json",
  "report_path": "question_reports/2017/A/q06/report.md",
  "artifact_path": "question_artifacts/2017/A/q06/dam_system_frontier.png"
}
RESULT_PATH = BASE / "results" / '2017' / 'A' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'A' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'A' / 'q06'


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
