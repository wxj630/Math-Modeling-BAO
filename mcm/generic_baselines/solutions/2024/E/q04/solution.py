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
  "question": "q04",
  "question_title": "极端天气上升地区的承保模型与两大洲演示",
  "statement": "Develop a model for insurance companies to determine if they should underwrite policies in an area that has a rising number of extreme weather events. Demonstrate your model using two areas on different continents that experience extreme weather events.",
  "methods": "对 North America 飓风洪水走廊和 Asia 气旋洪水走廊做确定性情景演示，明确这些是演示参数而非真实保险组合观测。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/E/q04/solution.py",
  "result_path": "question_results/2024/E/q04/result.json",
  "report_path": "question_reports/2024/E/q04/report.md",
  "artifact_path": "question_artifacts/2024/E/q04/regional_risk_comparison.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'E' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'E' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'E' / 'q04'


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
