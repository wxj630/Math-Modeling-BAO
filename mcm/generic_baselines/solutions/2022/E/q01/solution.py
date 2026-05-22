from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-E",
  "year": "2022",
  "code": "E",
  "question": "q01",
  "question_title": "森林与林产品 100 年碳封存模型",
  "statement": "Develop a carbon sequestration model to determine how much carbon dioxide a forest and its products can be expected to sequester over time.",
  "methods": "按官方题面 100 年评估要求，建立活树、土壤、长中短寿命林产品和替代信用的逐年确定性碳账户。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/E/q01/solution.py",
  "result_path": "question_results/2022/E/q01/result.json",
  "report_path": "question_reports/2022/E/q01/report.md",
  "artifact_path": "question_artifacts/2022/E/q01/carbon_stock_trajectories.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'E' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'E' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'E' / 'q01'


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
