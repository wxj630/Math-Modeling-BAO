from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-E",
  "year": "2024",
  "code": "E",
  "question": "q06",
  "question_title": "识别需要保存保护的重要建筑",
  "statement": "As a community leader, how could you identify buildings in a community that should be preserved and protected due to their cultural, historical, economic, or community significance?",
  "methods": "构造文化、历史、经济和社区意义加权分，并乘以灾害暴露形成保护紧迫度，排除 Cape Hatteras Lighthouse 后选择 St. Augustine Lighthouse 做应用。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/E/q06/solution.py",
  "result_path": "question_results/2024/E/q06/result.json",
  "report_path": "question_reports/2024/E/q06/report.md",
  "artifact_path": "question_artifacts/2024/E/q06/preservation_priority.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'E' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'E' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'E' / 'q06'


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
