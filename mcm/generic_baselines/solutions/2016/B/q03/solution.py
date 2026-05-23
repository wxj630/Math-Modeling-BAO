from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-B",
  "year": "2016",
  "code": "B",
  "question": "q03",
  "question_title": "独立方案、组合方案与 what-if 情景",
  "statement": "Your model should be able to assess independent alternatives as well as combinations of alternatives and be able to explore a variety of important what-if scenarios.",
  "methods": "枚举两项/三项组合并加入集成成本和协同收益；对 debris 翻倍、市场变弱、监管支持激光、主动移除成本下降做情景压力测试。对应模型：组合优化、情景分析、敏感性分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/B/q03/solution.py",
  "result_path": "question_results/2016/B/q03/result.json",
  "report_path": "question_reports/2016/B/q03/report.md",
  "artifact_path": "question_artifacts/2016/B/q03/combination_scores.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'B' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'B' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'B' / 'q03'


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
