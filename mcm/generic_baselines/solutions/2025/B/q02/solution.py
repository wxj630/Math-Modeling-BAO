from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-B",
  "year": "2025",
  "code": "B",
  "question": "q02",
  "question_title": "模型迁移到其他过度旅游目的地",
  "statement": "Demonstrate how the model could be adapted to another tourist destination impacted by overtourism, and how to promote less crowded attractions or locations.",
  "methods": "把朱诺模型的容量、收费、居民接受度和资源健康指标迁移到 Barcelona overtourism district，用文化景点拥挤替代冰川退缩约束。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/B/q02/solution.py",
  "result_path": "question_results/2025/B/q02/result.json",
  "report_path": "question_reports/2025/B/q02/report.md",
  "artifact_path": "question_artifacts/2025/B/q02/frontier_policies.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'B' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'B' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'B' / 'q02'


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
