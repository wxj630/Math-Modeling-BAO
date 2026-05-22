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
  "question": "q03",
  "question_title": "长期趋势、确定性与迁移到其他保护区",
  "statement": "Given your proposed plan, provide predictions about the long-term trends that will result from your recommendations. Analyze and provide estimates of the certainties and impacts of the possible long-term outcomes. You should also describe how your approach could be applied to other wildlife management areas.",
  "methods": "对最佳 integrated mosaic plan 做 20 年离散动态投影，输出 conflict index、wildlife index、resident acceptance、community benefit，并给出迁移步骤和风险登记。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/B/q03/solution.py",
  "result_path": "question_results/2023/B/q03/result.json",
  "report_path": "question_reports/2023/B/q03/report.md",
  "artifact_path": "question_artifacts/2023/B/q03/human_wildlife_interaction_projection.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'B' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'B' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'B' / 'q03'


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
