from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-F",
  "year": "2021",
  "code": "F",
  "question": "q07",
  "question_title": "学生、教师、学校、社区和国家影响",
  "statement": "Discuss the real-world impacts on students, faculty, schools, communities, and the nation during the transition and in the end state, acknowledging that change is hard.",
  "methods": "显式列出 students、faculty、institutions、communities 和 nation 的 transition burden 与 end-state gain，并生成健康前沿图和政策 brief。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/F/q07/solution.py",
  "result_path": "question_results/2021/F/q07/result.json",
  "report_path": "question_reports/2021/F/q07/report.md",
  "artifact_path": "question_artifacts/2021/F/q07/higher_ed_transition_frontier.png"
}
RESULT_PATH = BASE / "results" / '2021' / 'F' / 'q07' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'F' / 'q07' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'F' / 'q07'


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
