from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-F",
  "year": "2016",
  "code": "F",
  "question": "q07",
  "question_title": "外生事件下会改变的模型参数",
  "statement": "What parameters of the model would likely shift or change completely in a major exogenous event?",
  "methods": "以题面 Paris attack/Brussels lockdown 为例，把 approval rate、border processing capacity、route safety、local acceptance、security screening time 设为外生事件敏感参数。对应模型：冲击情景、参数敏感性、鲁棒性分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/F/q07/solution.py",
  "result_path": "question_results/2016/F/q07/result.json",
  "report_path": "question_reports/2016/F/q07/report.md",
  "artifact_path": "question_artifacts/2016/F/q07/exogenous_event_stress.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'F' / 'q07' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'F' / 'q07' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'F' / 'q07'


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
