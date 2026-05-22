from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-A",
  "year": "2019",
  "code": "A",
  "question": "q05",
  "question_title": "气候条件重要性",
  "statement": "How important are the climate conditions to your analysis?",
  "methods": "比较干旱、暖温带、北极三类气候的热调节倍数、猎物密度、水压力和巢址惩罚，量化资源需求差异。对应模型：敏感性分析、生态情景比较。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/A/q05/solution.py",
  "result_path": "question_results/2019/A/q05/result.json",
  "report_path": "question_reports/2019/A/q05/report.md",
  "artifact_path": "question_artifacts/2019/A/q05/dragon_climate_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'A' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'A' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'A' / 'q05'


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
