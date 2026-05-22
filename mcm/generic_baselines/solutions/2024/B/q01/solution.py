from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-B",
  "year": "2024",
  "code": "B",
  "question": "q01",
  "question_title": "失联潜水器位置预测与不确定性",
  "statement": "Locate - Develop a model(s) that predicts the location of the submersible over time. What are the uncertainties associated with these predictions? What information can the submersible periodically send to the host ship to decrease these uncertainties prior to an incident? What kinds of equipment would the submersible need to do so?",
  "methods": "官方 PDF 题面约束 + 失去通信/推进情景 + 洋流漂移-中性浮力/海底双状态位置椭圆 + 遥测信息对不确定性的削减清单。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/B/q01/solution.py",
  "result_path": "question_results/2024/B/q01/result.json",
  "report_path": "question_reports/2024/B/q01/report.md",
  "artifact_path": "question_artifacts/2024/B/q01/position_uncertainty.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'B' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'B' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'B' / 'q01'


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
