from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-D",
  "year": "2023",
  "code": "D",
  "question": "q03",
  "question_title": "某一 SDG 达成后的网络结构和新增目标",
  "statement": "If one of the SDGs is achieved (for example, there is no poverty or no hunger), what would be the structure of the resulting network? How would this achievement impact your team's priorities? Are there other goals that should be included or proposed to the UN for inclusion?",
  "methods": "以 SDG 1 达成为情景，衰减其紧急依赖边，重算网络优先级，并提出 Digital Public Trust and Resilience 作为技术/危机治理补充目标。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/D/q03/solution.py",
  "result_path": "question_results/2023/D/q03/result.json",
  "report_path": "question_reports/2023/D/q03/report.md",
  "artifact_path": "question_artifacts/2023/D/q03/achieved_goal_network_priorities.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'D' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'D' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'D' / 'q03'


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
