from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-F",
  "year": "2022",
  "code": "F",
  "question": "q08",
  "question_title": "Outer Space Treaty 更新的一页 UN 备忘录",
  "statement": "Use the results of your analyses to make justified policy recommendations so that asteroid mining might truly benefit all humankind.",
  "methods": "把公平指标、推荐愿景、敏感性和政策包压缩成给 UN 条约更新委员会的一页 memo。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/F/q08/solution.py",
  "result_path": "question_results/2022/F/q08/result.json",
  "report_path": "question_reports/2022/F/q08/report.md",
  "artifact_path": "question_artifacts/2022/F/q08/un_policy_package.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'F' / 'q08' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'F' / 'q08' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'F' / 'q08'


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
