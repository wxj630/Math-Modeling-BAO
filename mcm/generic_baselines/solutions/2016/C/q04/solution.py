from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-C",
  "year": "2016",
  "code": "C",
  "question": "q04",
  "question_title": "给 CFO Alpha Chiang 的两页以内信",
  "statement": "Include a letter to the Chief Financial Officer of the Goodgrant Foundation, Mr. Alpha Chiang, describing the optimal investment strategy, modeling approach, major results, and ROI concept.",
  "methods": "把官方数据来源、ROI 定义、推荐学校组合、年度预算和稳健性检查压缩成 CFO 可读的非技术信。对应模型：非技术政策报告、投资组合说明、ROI 解释。",
  "source_type": "official_comap_xlsx_zip",
  "solution_path": "question_solutions/2016/C/q04/solution.py",
  "result_path": "question_results/2016/C/q04/result.json",
  "report_path": "question_reports/2016/C/q04/report.md",
  "artifact_path": "question_artifacts/2016/C/q04/goodgrant_top_schools.png"
}
RESULT_PATH = BASE / "results" / '2016' / 'C' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'C' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'C' / 'q04'


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
