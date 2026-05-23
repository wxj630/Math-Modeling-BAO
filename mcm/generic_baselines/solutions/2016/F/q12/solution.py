from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-F",
  "year": "2016",
  "code": "F",
  "question": "q12",
  "question_title": "新增长期健康安全参数与时间阈值",
  "statement": "Do new parameters need to be added? How does this increase the time required to resolve refugee placement, and what new issues might arise such as disease control, childbirth, and education?",
  "methods": "加入 disease surveillance、birth/maternal care、school-age education、employment/housing absorption、social cohesion 等长期参数，并设置 180 天阈值触发长期政策。对应模型：长期安置系统动力学、公共卫生模型、教育和社会融合约束。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/F/q12/solution.py",
  "result_path": "question_results/2016/F/q12/result.json",
  "report_path": "question_reports/2016/F/q12/report.md",
  "artifact_path": "question_artifacts/2016/F/q12/scalability_10x.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'F' / 'q12' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'F' / 'q12' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'F' / 'q12'


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
