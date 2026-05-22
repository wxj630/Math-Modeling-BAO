from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-F",
  "year": "2023",
  "code": "F",
  "question": "q01",
  "question_title": "奥运会举办影响指标框架",
  "statement": "Build metrics for the impacts of hosting the games from economic, land use, human satisfaction, travel, opportunity for future improvements, host city/nation prestige, and other criteria.",
  "methods": "把官方题面列出的经济、土地利用、人类满意度、旅行、未来改进、主办声望和体育团结转成 7 维权重指标，并写入可审计 metric framework。对应模型：多指标评价、权重评分、政策指标体系。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/F/q01/solution.py",
  "result_path": "question_results/2023/F/q01/result.json",
  "report_path": "question_reports/2023/F/q01/report.md",
  "artifact_path": "question_artifacts/2023/F/q01/metric_framework.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'F' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'F' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'F' / 'q01'


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
