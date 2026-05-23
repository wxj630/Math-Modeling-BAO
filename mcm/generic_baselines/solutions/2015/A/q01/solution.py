from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-A",
  "year": "2015",
  "code": "A",
  "question": "q01",
  "question_title": "Ebola 传播、药物生产与配送优化模型",
  "statement": "Build a realistic, sensible, and useful model that considers Ebola spread, medicine demand, feasible delivery systems, delivery locations, manufacturing speed, and other critical factors to optimize eradication or containment.",
  "methods": "SEIR 传播动力学、药物库存方程、设施选址、配送路径优化、情景敏感性分析。",
  "source_type": "official_html_statement",
  "solution_path": "question_solutions/2015/A/q01/solution.py",
  "result_path": "question_results/2015/A/q01/result.json",
  "report_path": "question_reports/2015/A/q01/report.md",
  "artifact_path": "question_artifacts/2015/A/q01/experiment_table.csv"
}
RESULT_PATH = BASE / "results" / '2015' / 'A' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'A' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'A' / 'q01'


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
