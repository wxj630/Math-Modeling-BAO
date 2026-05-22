from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-A",
  "year": "2021",
  "code": "A",
  "question": "q03",
  "question_title": "环境快速波动与长期竞争动态",
  "statement": "Examine sensitivity to rapid environmental fluctuations and assess the impact of variation of local weather patterns.",
  "methods": "在 arid、semi-arid、temperate、arboreal、tropical rain forest 五种环境下枚举 moisture variability 倍数，比较最终分解和优势种迁移。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/A/q03/solution.py",
  "result_path": "question_results/2021/A/q03/result.json",
  "report_path": "question_reports/2021/A/q03/report.md",
  "artifact_path": "question_artifacts/2021/A/q03/environmental_variability_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'A' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'A' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'A' / 'q03'


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
