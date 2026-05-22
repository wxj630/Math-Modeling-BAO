from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-D",
  "year": "2025",
  "code": "D",
  "question": "q04",
  "question_title": "对其他利益相关者的影响",
  "statement": "How does the recommended project impact other stakeholders?",
  "methods": "从居民、港口货运、通勤者、公交运营方、沿街商户和过境车辆角度整理收益和代价。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2025/D/q04/solution.py",
  "result_path": "question_results/2025/D/q04/result.json",
  "report_path": "question_reports/2025/D/q04/report.md",
  "artifact_path": "question_artifacts/2025/D/q04/bridge_od_impacts.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'D' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'D' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'D' / 'q04'


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
