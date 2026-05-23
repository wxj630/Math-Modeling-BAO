from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-D",
  "year": "2024",
  "code": "D",
  "question": "q02",
  "question_title": "维持最优水位的控制算法",
  "statement": "Establish algorithms to maintain optimal water levels in the five lakes from inflow and outflow data.",
  "methods": "对 Soo Locks/St. Mary's 与 Moses-Saunders/St. Lawrence 两个可控出流采用目标偏差比例控制，并按历史月度 10%-90% 流量裁剪。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2024/D/q02/solution.py",
  "result_path": "question_results/2024/D/q02/result.json",
  "report_path": "question_reports/2024/D/q02/report.md",
  "artifact_path": "question_artifacts/2024/D/q02/control_policy_releases.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'D' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'D' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'D' / 'q02'


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
