from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-C",
  "year": "2015",
  "code": "C",
  "question": "q07",
  "question_title": "20 页报告与执行摘要",
  "statement": "Write a 20-page report introducing your organizational model, its functions, and the issues the manager asked you to consider. A one-page executive summary does not count toward the page limit.",
  "methods": "把官方题面参数、网络模型、流失动态、两年预算、25%/35% 情景、中层 30% 冲击和团队科学路线图整理为 HR 经理可读报告。对应模型：实验报告、执行摘要、政策备忘录、模型限制说明。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2015/C/q07/solution.py",
  "result_path": "question_results/2015/C/q07/result.json",
  "report_path": "question_reports/2015/C/q07/report.md",
  "artifact_path": "question_artifacts/2015/C/q07/human_capital_health.png"
}
RESULT_PATH = BASE / "results" / '2015' / 'C' / 'q07' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'C' / 'q07' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'C' / 'q07'


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
