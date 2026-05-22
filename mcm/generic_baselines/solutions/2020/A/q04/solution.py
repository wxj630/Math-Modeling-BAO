from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-A",
  "year": "2020",
  "code": "A",
  "question": "q04",
  "question_title": "领海和跨境捕捞治理影响",
  "statement": "Assess how movement into different territorial waters could affect fishing rights and policy.",
  "methods": "按 Scottish coastal、UK EEZ、Norwegian/Faroese negotiation 和 Icelandic high-latitude access thresholds 计算边界压力和政策响应。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/A/q04/solution.py",
  "result_path": "question_results/2020/A/q04/result.json",
  "report_path": "question_reports/2020/A/q04/report.md",
  "artifact_path": "question_artifacts/2020/A/q04/territorial_waters_pressure.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'A' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'A' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'A' / 'q04'


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
