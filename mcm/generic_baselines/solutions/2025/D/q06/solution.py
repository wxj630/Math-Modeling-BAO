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
  "question": "q06",
  "question_title": "交通系统服务城市安全",
  "statement": "Safety is a significant issue facing Baltimore. How can the transportation system be used to best address this issue?",
  "methods": "用 AADT/lane 暴露和高客流公交站，形成行人庇护岛、照明、速度管理、公交站硬化和路口安全优先级。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2025/D/q06/solution.py",
  "result_path": "question_results/2025/D/q06/result.json",
  "report_path": "question_reports/2025/D/q06/report.md",
  "artifact_path": "question_artifacts/2025/D/q06/high_exposure_roads.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'D' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'D' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'D' / 'q06'


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
