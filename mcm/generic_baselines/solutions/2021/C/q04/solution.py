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
  "question": "q04",
  "question_title": "新报告到来后的模型更新机制",
  "statement": "Address how you could update your model given additional new reports over time, and how often the updates should occur.",
  "methods": "把新增标签追加到官方 workbook 派生表，按周或新增高风险聚类触发重训；冻结训练截止日期并重新计算留出 AUC、AP、recall 与优先级稳定性。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2021/C/q04/solution.py",
  "result_path": "question_results/2021/C/q04/result.json",
  "report_path": "question_reports/2021/C/q04/report.md",
  "artifact_path": "question_artifacts/2021/C/q04/clean_sightings.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'C' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'C' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'C' / 'q04'


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
