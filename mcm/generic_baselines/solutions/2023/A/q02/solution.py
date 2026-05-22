from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-A",
  "year": "2023",
  "code": "A",
  "question": "q02",
  "question_title": "群落受益所需的最少物种数与规模效应",
  "statement": "How many different plant species are required for the community to benefit and what happens as the number of species grows?",
  "methods": "以单物种为基线，枚举 1-12 个物种，计算末 20 年生物量、存活比例、干旱代际生物量和稳定性综合得分，识别至少 4 个物种的受益阈值。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/A/q02/solution.py",
  "result_path": "question_results/2023/A/q02/result.json",
  "report_path": "question_reports/2023/A/q02/report.md",
  "artifact_path": "question_artifacts/2023/A/q02/biodiversity_threshold.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'A' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'A' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'A' / 'q02'


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
