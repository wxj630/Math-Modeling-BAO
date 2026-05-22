from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-E",
  "year": "2023",
  "code": "E",
  "question": "q01",
  "question_title": "通用光污染风险指标",
  "statement": "Develop a broadly applicable metric to identify the light pollution risk level of a location.",
  "methods": "官方 PDF 题面现象 + 0-100 综合评价指标：sky glow、生态暴露、人类健康、安全眩光和夜空损失；对应教程模型：综合评价与权重决策。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/E/q01/solution.py",
  "result_path": "question_results/2023/E/q01/result.json",
  "report_path": "question_reports/2023/E/q01/report.md",
  "artifact_path": "question_artifacts/2023/E/q01/location_risk_scores.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'E' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'E' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'E' / 'q01'


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
