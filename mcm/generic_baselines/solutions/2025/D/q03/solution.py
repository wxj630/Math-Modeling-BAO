from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-D",
  "year": "2025",
  "code": "D",
  "question": "q03",
  "question_title": "推荐项目对居民的收益",
  "statement": "Recommend a project for the transportation network that best improves residents' lives. What are the benefits to residents?",
  "methods": "综合桥梁韧性和高客流公交站升级，量化直接连通性恢复和无候车亭高客流覆盖。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2025/D/q03/solution.py",
  "result_path": "question_results/2025/D/q03/result.json",
  "report_path": "question_reports/2025/D/q03/report.md",
  "artifact_path": "question_artifacts/2025/D/q03/priority_bus_stops.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'D' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'D' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'D' / 'q03'


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
