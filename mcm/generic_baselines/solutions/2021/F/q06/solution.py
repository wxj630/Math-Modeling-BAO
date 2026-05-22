from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-F",
  "year": "2021",
  "code": "F",
  "question": "q06",
  "question_title": "政策效果评估",
  "statement": "Use your model(s) to shape and/or assess the effectiveness of your policies.",
  "methods": "把每项政策的 start year、full effect year、dimension gain 和 implementation difficulty 映射为逐年健康度提升，检查是否达到健康阈值。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/F/q06/solution.py",
  "result_path": "question_results/2021/F/q06/result.json",
  "report_path": "question_reports/2021/F/q06/report.md",
  "artifact_path": "question_artifacts/2021/F/q06/higher_ed_impact_assessment.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'F' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'F' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'F' / 'q06'


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
