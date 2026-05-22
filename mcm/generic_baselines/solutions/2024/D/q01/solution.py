from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-D",
  "year": "2024",
  "code": "D",
  "question": "q01",
  "question_title": "五大湖分月最优水位目标",
  "statement": "Determine optimal water levels of the five Great Lakes at any time of year, considering stakeholder desires.",
  "methods": "用官方月度水位历史中位数定义分月目标水位，用 25%-75% 分位数形成兼顾洪涝、航运和生态的运行带。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2024/D/q01/solution.py",
  "result_path": "question_results/2024/D/q01/result.json",
  "report_path": "question_reports/2024/D/q01/report.md",
  "artifact_path": "question_artifacts/2024/D/q01/monthly_level_targets.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'D' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'D' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'D' / 'q01'


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
