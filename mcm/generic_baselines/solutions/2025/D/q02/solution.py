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
  "question": "q02",
  "question_title": "公交/步行系统改造项目影响",
  "statement": "Select a project that impacts the bus or pedestrian walkway systems and show its effects on stakeholders.",
  "methods": "用官方公交站客流、候车亭字段和最近驾车节点，筛选高客流无候车亭站点，形成公交站安全与可达性升级项目。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2025/D/q02/solution.py",
  "result_path": "question_results/2025/D/q02/result.json",
  "report_path": "question_reports/2025/D/q02/report.md",
  "artifact_path": "question_artifacts/2025/D/q02/priority_bus_stops.png"
}
RESULT_PATH = BASE / "results" / '2025' / 'D' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'D' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'D' / 'q02'


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
