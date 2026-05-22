from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-E",
  "year": "2019",
  "code": "E",
  "question": "q04",
  "question_title": "模型有效性评估",
  "statement": "Evaluate the effectiveness of your model based on your analyses and model design.",
  "methods": "统计被生态服务核算标记为 redesign/reject 的项目，并列出强项与局限：透明、跨尺度、可更新但依赖本地服务价值。对应模型：模型评估、敏感性说明。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/E/q04/solution.py",
  "result_path": "question_results/2019/E/q04/result.json",
  "report_path": "question_reports/2019/E/q04/report.md",
  "artifact_path": "question_artifacts/2019/E/q04/project_true_costs.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'E' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'E' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'E' / 'q04'


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
