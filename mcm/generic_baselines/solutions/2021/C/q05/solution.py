from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-C",
  "year": "2021",
  "code": "C",
  "question": "q05",
  "question_title": "根除证据标准",
  "statement": "Using your model, what would constitute evidence that the pest has been eradicated in Washington State?",
  "methods": "组合无阳性持续时间、30km 范围内高优先级报告处理、主动诱捕/搜巢阴性、公众报告量充足和模型低风险阈值，形成根除证据清单。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2021/C/q05/solution.py",
  "result_path": "question_results/2021/C/q05/result.json",
  "report_path": "question_reports/2021/C/q05/report.md",
  "artifact_path": "question_artifacts/2021/C/q05/spread_timeline.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'C' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'C' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'C' / 'q05'


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
