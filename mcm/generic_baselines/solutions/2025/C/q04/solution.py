from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-C",
  "year": "2025",
  "code": "C",
  "question": "q04",
  "question_title": "项目数量、运动类型与国家优势运动",
  "statement": "Consider the number and types of events. Explore relationships between events and medal counts, important sports for countries, and host-selected events.",
  "methods": "把每届项目数、运动数量、运动员参赛规模、参赛项目数作为预测特征，并用 2008-2024 奖牌运动员记录统计各国优势运动占比。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2025/C/q04/solution.py",
  "result_path": "question_results/2025/C/q04/result.json",
  "report_path": "question_reports/2025/C/q04/report.md",
  "artifact_path": "question_artifacts/2025/C/q04/sport_importance.json"
}
RESULT_PATH = BASE / "results" / '2025' / 'C' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'C' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'C' / 'q04'


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
