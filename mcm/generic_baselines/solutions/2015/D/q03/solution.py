from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-D",
  "year": "2015",
  "code": "D",
  "question": "q03",
  "question_title": "20 年计划影响评估与最高性价比政策",
  "statement": "Evaluate the effect your 20-year sustainability plan has on your country's sustainability measure. Determine which programs or policies produce the greatest effect on the sustainability measure for your country.",
  "methods": "把项目年度增益作为显式规划假设累积到各组件分数，计算 20 年后总分、状态变化，并用 score gain per billion USD 排序。对应模型：系统动力学、成本效益分析、项目效率排序。",
  "source_type": "official_pdf_and_world_bank_csv",
  "solution_path": "question_solutions/2015/D/q03/solution.py",
  "result_path": "question_results/2015/D/q03/result.json",
  "report_path": "question_reports/2015/D/q03/report.md",
  "artifact_path": "question_artifacts/2015/D/q03/policy_efficiency.csv"
}
RESULT_PATH = BASE / "results" / '2015' / 'D' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'D' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'D' / 'q03'


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
