from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-B",
  "year": "2022",
  "code": "B",
  "question": "q07",
  "question_title": "不足以满足全部水和电需求时的策略",
  "statement": "Use your model to address what should be done if there is not enough water to meet all water and electricity demands.",
  "methods": "触发短缺协议：居民优先、农业/工业分摊缺口、Mexico flow 保护、水电缺口用可再生替代和需求响应处理。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/B/q07/solution.py",
  "result_path": "question_results/2022/B/q07/result.json",
  "report_path": "question_reports/2022/B/q07/report.md",
  "artifact_path": "question_artifacts/2022/B/q07/shortage_response_scenarios.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'B' / 'q07' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'B' / 'q07' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'B' / 'q07'


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
