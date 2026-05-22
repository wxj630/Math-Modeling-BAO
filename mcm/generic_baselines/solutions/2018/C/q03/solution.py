from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2018-C",
  "year": "2018",
  "code": "C",
  "question": "q03",
  "question_title": "2009 最佳能源画像州识别",
  "statement": "Determine which of the four states had the best energy profile in 2009, according to your team's definition of clean renewable energy.",
  "methods": "以 2009 年官方 SEDS 指标为横截面，使用 clean profile score 排序：45% renewable consumption share、25% non-hydro renewable share、20% renewable production per capita、并对高总能耗强度扣分。对应模型：TOPSIS/综合评价思想、加权评分、横截面排序。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2018/C/q03/solution.py",
  "result_path": "question_results/2018/C/q03/result.json",
  "report_path": "question_reports/2018/C/q03/report.md",
  "artifact_path": "question_artifacts/2018/C/q03/state_energy_profiles_2009.csv"
}
RESULT_PATH = BASE / "results" / '2018' / 'C' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2018' / 'C' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2018' / 'C' / 'q03'


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
