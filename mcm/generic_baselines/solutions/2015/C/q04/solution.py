from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-C",
  "year": "2015",
  "code": "C",
  "question": "q04",
  "question_title": "25% 与 35% 年流失率下的 80% 填补率可持续性",
  "statement": "Can ICM maintain its 80% filled positions if annual turnover for all positions increases to 25%? What about 35%? What are the costs of these higher turnover rates? What indirect effects might high turnover cause?",
  "methods": "把题面 8%-10% 主动招聘范围转成可审计招聘吞吐量，比较 18%、25%、35% 年流失下的离职负荷、第一年填补率和间接成本。对应模型：稳态容量约束、人员库存模型、敏感性分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2015/C/q04/solution.py",
  "result_path": "question_results/2015/C/q04/result.json",
  "report_path": "question_reports/2015/C/q04/report.md",
  "artifact_path": "question_artifacts/2015/C/q04/turnover_scenarios.csv"
}
RESULT_PATH = BASE / "results" / '2015' / 'C' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'C' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'C' / 'q04'


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
