from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-A",
  "year": "2025",
  "code": "A",
  "question": "q03",
  "question_title": "并排或单列使用模式",
  "statement": "How many people used the stairs simultaneously? For example, did pairs of people climb the stairs side-by-side or did they travel single file?",
  "methods": "把横截面磨损剖面拆成中心带和左右侧带，使用侧带/中心磨损比估计 single-file、side-by-side 或 mixed 的同时使用模式。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/A/q03/solution.py",
  "result_path": "question_results/2025/A/q03/result.json",
  "report_path": "question_reports/2025/A/q03/report.md",
  "artifact_path": "question_artifacts/2025/A/q03/wear_cross_section.png"
}
RESULT_PATH = BASE / "results" / '2025' / 'A' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'A' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'A' / 'q03'


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
