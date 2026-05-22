from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-C-Boats",
  "year": "2023",
  "code": "C-Boats",
  "question": "q04",
  "question_title": "帆船数据的其他推论",
  "statement": "Identify and discuss any other interesting and informative inferences or conclusions drawn from the data.",
  "methods": "统计单体船/双体船中位价、双体船溢价、价格与长度/船龄相关性、区域-船型中位价和高价品牌。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2023/C-Boats/q04/solution.py",
  "result_path": "question_results/2023/C-Boats/q04/result.json",
  "report_path": "question_reports/2023/C-Boats/q04/report.md",
  "artifact_path": "question_artifacts/2023/C-Boats/q04/price_by_region_hull.png"
}
RESULT_PATH = BASE / "results" / '2023' / 'C-Boats' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'C-Boats' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'C-Boats' / 'q04'


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
