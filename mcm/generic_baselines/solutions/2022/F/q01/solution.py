from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-F",
  "year": "2022",
  "code": "F",
  "question": "q01",
  "question_title": "外层空间条约承诺与全球公平定义",
  "statement": "What is global equity, and how might we measure it?",
  "methods": "将 Outer Space Treaty 的 benefit of all countries 原则转为 benefit_sharing、participation、technology_transfer、governance_voice、risk burden、peaceful use 六维公平指标。对应模型：多指标评价、政策指标体系。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/F/q01/solution.py",
  "result_path": "question_results/2022/F/q01/result.json",
  "report_path": "question_reports/2022/F/q01/report.md",
  "artifact_path": "question_artifacts/2022/F/q01/equity_metric_components.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'F' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'F' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'F' / 'q01'


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
