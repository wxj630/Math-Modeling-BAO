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
  "question": "q01",
  "question_title": "Kariba 三方案成本收益简评",
  "statement": "ZRA management requires a brief assessment of repairing, rebuilding, or replacing Kariba Dam with sufficient detail to outline potential costs and benefits.",
  "methods": "只使用官方题面给出的三个选项，构造 normalized cost、implementation years、construction disruption、safety improvement 和 water management flexibility 的可替换评分表。对应模型：多指标综合评价、成本收益分析、决策矩阵。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/A/q01/solution.py",
  "result_path": "question_results/2017/A/q01/result.json",
  "report_path": "question_reports/2017/A/q01/report.md",
  "artifact_path": "question_artifacts/2017/A/q01/option_assessment.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'A' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'A' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'A' / 'q01'


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
