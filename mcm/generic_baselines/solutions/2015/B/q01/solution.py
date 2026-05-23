from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-B",
  "year": "2015",
  "code": "B",
  "question": "q01",
  "question_title": "失联飞机开放水域搜索规划模型",
  "statement": "Build a generic mathematical model to assist searchers in planning an open-water search for a lost plane flying from Point A to Point B with no signal from the downed plane.",
  "methods": "贝叶斯搜索、概率热区、洋流漂移不确定性、探测概率、搜索路径与资源调度。",
  "source_type": "official_html_statement",
  "solution_path": "question_solutions/2015/B/q01/solution.py",
  "result_path": "question_results/2015/B/q01/result.json",
  "report_path": "question_reports/2015/B/q01/report.md",
  "artifact_path": "question_artifacts/2015/B/q01/experiment_table.csv"
}
RESULT_PATH = BASE / "results" / '2015' / 'B' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'B' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'B' / 'q01'


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
