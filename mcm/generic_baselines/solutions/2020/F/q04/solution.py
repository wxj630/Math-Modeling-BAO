from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-F",
  "year": "2020",
  "code": "F",
  "question": "q04",
  "question_title": "UN 系统化响应建议",
  "statement": "Provide recommendations for how the UN should generate a systemized response for EDPs, especially preserving cultural heritage.",
  "methods": "形成 EDP status protocol、迁移协定、文化基金、portable legal identity 和高排放/高能力国家融资责任的建议框架。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/F/q04/solution.py",
  "result_path": "question_results/2020/F/q04/result.json",
  "report_path": "question_reports/2020/F/q04/report.md",
  "artifact_path": "question_artifacts/2020/F/q04/climate_migration_policy_frontier.png"
}
RESULT_PATH = BASE / "results" / '2020' / 'F' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'F' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'F' / 'q04'


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
