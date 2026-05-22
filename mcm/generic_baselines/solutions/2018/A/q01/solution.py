from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2018-A",
  "year": "2018",
  "code": "A",
  "question": "q01",
  "question_title": "Maximum multi-hop distance over calm oceans",
  "statement": "If additional reflections take place off calm oceans, determine the maximum distance a signal could be detected.",
  "methods": "Apply spherical Earth and ionosphere geometry using official statement parameters and explicit ionosphere-height assumptions.",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2018/A/q01/solution.py",
  "result_path": "question_results/2018/A/q01/result.json",
  "report_path": "question_reports/2018/A/q01/report.md",
  "artifact_path": "question_artifacts/2018/A/q01/hop_distance_table.csv"
}
RESULT_PATH = BASE / "results" / '2018' / 'A' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2018' / 'A' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2018' / 'A' / 'q01'


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
