from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-B",
  "year": "2023",
  "code": "B",
  "question": "q04",
  "question_title": "给 Kenyan Tourism and Wildlife Committee 的非技术报告",
  "statement": "Finally, provide a two-page non-technical report for the Kenyan Tourism and Wildlife Committee discussing your proposed plan and its value for the preserve.",
  "methods": "把分区策略、政策排名、长期趋势、社区收益、风险和迁移价值压缩为 Kenyan Tourism and Wildlife Committee 可读的非技术报告。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/B/q04/solution.py",
  "result_path": "question_results/2023/B/q04/result.json",
  "report_path": "question_reports/2023/B/q04/report.md",
  "artifact_path": "question_artifacts/2023/B/q04/maasai_mara_policy_frontier.png"
}
RESULT_PATH = BASE / "results" / '2023' / 'B' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'B' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'B' / 'q04'


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
