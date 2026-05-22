from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-C",
  "year": "2016",
  "code": "C",
  "question": "q01",
  "question_title": "Goodgrant 慈善 ROI 定义与候选学校评分",
  "statement": "Develop a model to determine an optimal investment strategy based on each candidate school's demonstrated potential for effective use of private funding and an estimated philanthropic ROI.",
  "methods": "读取官方 ProblemCDATA.zip 中 Scorecard 主表、候选 IPEDS UID 表和数据字典，筛选 current operating、predominant degree 3/4、UGDS>500 的候选学校；构造 student_success、grant_need、leverage 三类指数和 charitable ROI。对应模型：多指标综合评价、标准化加权评分、教育投资 ROI。",
  "source_type": "official_comap_xlsx_zip",
  "solution_path": "question_solutions/2016/C/q01/solution.py",
  "result_path": "question_results/2016/C/q01/result.json",
  "report_path": "question_reports/2016/C/q01/report.md",
  "artifact_path": "question_artifacts/2016/C/q01/goodgrant_ranked_candidates.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'C' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'C' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'C' / 'q01'


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
