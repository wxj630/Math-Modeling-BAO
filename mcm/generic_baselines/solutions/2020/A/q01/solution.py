from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-A",
  "year": "2020",
  "code": "A",
  "question": "q01",
  "question_title": "苏格兰鲱鱼和鲭鱼北迁模型",
  "statement": "Model how Scottish herring and mackerel may move north over the next 50 years as waters warm.",
  "methods": "用 species thermal sensitivity、stock mobility 和 best/most-likely/worst warming 情景计算 50 年 habitat center northward shift 与小渔船距离。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/A/q01/solution.py",
  "result_path": "question_results/2020/A/q01/result.json",
  "report_path": "question_reports/2020/A/q01/report.md",
  "artifact_path": "question_artifacts/2020/A/q01/habitat_shift_projection.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'A' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'A' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'A' / 'q01'


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
