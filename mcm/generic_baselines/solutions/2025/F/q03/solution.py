from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-F",
  "year": "2025",
  "code": "F",
  "question": "q03",
  "question_title": "人口统计变量、混杂因素与领导人备忘录",
  "statement": "What national demographics (e.g., access to internet, wealth, education levels, etc.) correlate with your cybercrime distribution analysis? And how might these support (or conflate with) your theory? Create a one-page memo to country leaders attending an upcoming ITU Summit on Cybersecurity.",
  "methods": "调用 World Bank 指标补充互联网使用率、GDP/人和教育支出，计算与 VCDB 可见事件数的描述性相关，并把混杂因素和政策建议写成 ITU 峰会非技术备忘录。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/F/q03/solution.py",
  "result_path": "question_results/2025/F/q03/result.json",
  "report_path": "question_reports/2025/F/q03/report.md",
  "artifact_path": "question_artifacts/2025/F/q03/demographic_correlations.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'F' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'F' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'F' / 'q03'


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
