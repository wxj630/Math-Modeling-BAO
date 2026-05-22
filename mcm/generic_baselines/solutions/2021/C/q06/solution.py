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
  "question": "q06",
  "question_title": "给 WSDA 的两页备忘录",
  "statement": "Include a two-page memorandum that summarizes your results for the Washington State Department of Agriculture.",
  "methods": "将分类性能、优先级规则、30km 范围限制、每周更新流程和根除证据条件整理成面向 Washington State Department of Agriculture 的非技术 memo。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2021/C/q06/solution.py",
  "result_path": "question_results/2021/C/q06/result.json",
  "report_path": "question_reports/2021/C/q06/report.md",
  "artifact_path": "question_artifacts/2021/C/q06/priority_reports.png"
}
RESULT_PATH = BASE / "results" / '2021' / 'C' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'C' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'C' / 'q06'


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
