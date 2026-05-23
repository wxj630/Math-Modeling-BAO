from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-D",
  "year": "2025",
  "code": "D",
  "question": "q01",
  "question_title": "Key Bridge 坍塌/重建的路网影响",
  "statement": "What does the network model show is the impact of the Francis Scott Key Bridge collapse and/or reconstruction on Baltimore transportation stakeholders?",
  "methods": "基于官方驾车路网构建加权有向图，移除 I-695/Baltimore Beltway 港口桥梁走廊边，比较关键 OD 最短路和断连状态。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2025/D/q01/solution.py",
  "result_path": "question_results/2025/D/q01/result.json",
  "report_path": "question_reports/2025/D/q01/report.md",
  "artifact_path": "question_artifacts/2025/D/q01/bridge_od_impacts.png"
}
RESULT_PATH = BASE / "results" / '2025' / 'D' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'D' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'D' / 'q01'


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
