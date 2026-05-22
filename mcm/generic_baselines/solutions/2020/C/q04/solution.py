from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-C",
  "year": "2020",
  "code": "C",
  "question": "q04",
  "question_title": "低星级是否激发更多评论",
  "statement": "Do specific star ratings incite more reviews, for example after seeing a series of low star ratings?",
  "methods": "按时间排序计算 previous-20-review mean rating，比较低评分环境和高评分环境之后的评论数量与评论长度。",
  "source_type": "official_comap_tsv_zip",
  "solution_path": "question_solutions/2020/C/q04/solution.py",
  "result_path": "question_results/2020/C/q04/result.json",
  "report_path": "question_reports/2020/C/q04/report.md",
  "artifact_path": "question_artifacts/2020/C/q04/star_rating_incitement.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'C' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'C' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'C' / 'q04'


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
