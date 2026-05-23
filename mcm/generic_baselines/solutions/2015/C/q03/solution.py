from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-C",
  "year": "2015",
  "code": "C",
  "question": "q03",
  "question_title": "未来两年招聘与培训预算",
  "statement": "Use your model to analyze the organization's budget needs for talent management in sigma for the next two years of hiring and training.",
  "methods": "按官方每层招聘时间、招聘成本、人数、工资和年度培训成本，计算两年内替换预计离职人员并恢复 15% 空缺所需的招聘 sigma、培训 sigma 和总 sigma。对应模型：预算预测、招聘容量模型、培训成本模型。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2015/C/q03/solution.py",
  "result_path": "question_results/2015/C/q03/result.json",
  "report_path": "question_reports/2015/C/q03/report.md",
  "artifact_path": "question_artifacts/2015/C/q03/two_year_budget.csv"
}
RESULT_PATH = BASE / "results" / '2015' / 'C' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'C' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'C' / 'q03'


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
