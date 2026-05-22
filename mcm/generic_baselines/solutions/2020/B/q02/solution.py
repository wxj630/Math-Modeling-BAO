from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-B",
  "year": "2020",
  "code": "B",
  "question": "q02",
  "question_title": "无添加材料的最佳水沙比例",
  "statement": "Using your model, determine an optimal sand-to-water mixture proportion for the castle foundation, assuming you use no other additives or materials.",
  "methods": "扫描 6%-22% water fraction，把 capillary cohesion、drainage 和 slump risk 映射到 lifetime multiplier，选择同一推荐形状下寿命最长的比例。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/B/q02/solution.py",
  "result_path": "question_results/2020/B/q02/result.json",
  "report_path": "question_reports/2020/B/q02/report.md",
  "artifact_path": "question_artifacts/2020/B/q02/sand_water_mixture_scores.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'B' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'B' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'B' / 'q02'


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
