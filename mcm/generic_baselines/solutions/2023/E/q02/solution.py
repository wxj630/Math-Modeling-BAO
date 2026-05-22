from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-E",
  "year": "2023",
  "code": "E",
  "question": "q02",
  "question_title": "四类地点风险评估和解释",
  "statement": "Apply your metric and interpret its results on the following four diverse types of locations: a protected land location, a rural community, a suburban community, and an urban community.",
  "methods": "对 protected_land、rural、suburban、urban 四类题面地点分别设置可替换确定性场景参数，计算风险分、风险等级和主要成分解释。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/E/q02/solution.py",
  "result_path": "question_results/2023/E/q02/result.json",
  "report_path": "question_reports/2023/E/q02/report.md",
  "artifact_path": "question_artifacts/2023/E/q02/location_risk_scores.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'E' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'E' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'E' / 'q02'


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
