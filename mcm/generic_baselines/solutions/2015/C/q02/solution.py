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
  "question": "q02",
  "question_title": "组织流失动态过程与生产率影响",
  "statement": "Use your model to identify dynamic processes within the human capital network. Describe and incorporate dynamic processes involved in organizational churn and the effect of churn on organizational productivity.",
  "methods": "把官方 18% 年流失率和中层高流失描述转化为确定性层级流失风险，叠加网络影响、职业阻塞和 salary-sigma 加权生产率损失；所有非题面系数写入 assumption_audit。对应模型：Markov 人员流动、网络影响扩散、生产率损失函数。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2015/C/q02/solution.py",
  "result_path": "question_results/2015/C/q02/result.json",
  "report_path": "question_reports/2015/C/q02/report.md",
  "artifact_path": "question_artifacts/2015/C/q02/workforce_level_table.csv"
}
RESULT_PATH = BASE / "results" / '2015' / 'C' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'C' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'C' / 'q02'


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
