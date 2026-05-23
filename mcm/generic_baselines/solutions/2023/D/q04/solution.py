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
  "question": "q04",
  "question_title": "技术、疫情、气候、战争和难民冲击",
  "statement": "Discuss the impact of technological advances, global pandemics, climate change, regional wars, and refugee movements, or other international crises on your team's network and your team's choice of priorities. What are the significant effects on the progress of the UN from a network perspective?",
  "methods": "把题面列出的五类危机覆盖到 SDG 网络，按被冲击目标的优先级加权计算 network severity index 和响应目标组合。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/D/q04/solution.py",
  "result_path": "question_results/2023/D/q04/result.json",
  "report_path": "question_reports/2023/D/q04/report.md",
  "artifact_path": "question_artifacts/2023/D/q04/crisis_impact_matrix.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'D' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'D' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'D' / 'q04'


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
