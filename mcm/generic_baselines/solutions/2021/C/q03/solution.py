from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-C",
  "year": "2021",
  "code": "C",
  "question": "q03",
  "question_title": "有限资源下的调查优先级",
  "statement": "Use your model to discuss how your classification analyses leads to prioritizing investigation of the reports most likely to be positive sightings.",
  "methods": "对 Unprocessed / Unverified 报告按分类概率、30km queen range、图片/标本证据和提交及时性构建 priority_score，输出前 15 个待调查报告。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2021/C/q03/solution.py",
  "result_path": "question_results/2021/C/q03/result.json",
  "report_path": "question_reports/2021/C/q03/report.md",
  "artifact_path": "question_artifacts/2021/C/q03/priority_reports.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'C' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'C' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'C' / 'q03'


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
