from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-P06",
  "year": "2019",
  "code": "P06",
  "question": "q02",
  "question_title": "采用策略、准入、安全与稳定",
  "statement": "Discuss adoption strategies and implementation problems without choosing an existing digital currency.",
  "methods": "比较 wallet-first inclusion、regulated stable settlement、remittance corridor、full substitution 和 privacy-preserving compliance 等策略，强调不早期强制放弃本币。对应模型：策略组合评分、实施风险分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/P06/q02/solution.py",
  "result_path": "question_results/2019/P06/q02/result.json",
  "report_path": "question_reports/2019/P06/q02/report.md",
  "artifact_path": "question_artifacts/2019/P06/q02/currency_strategy_scores.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'P06' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'P06' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'P06' / 'q02'


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
