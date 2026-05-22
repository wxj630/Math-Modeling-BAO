from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-C-Boats",
  "year": "2023",
  "code": "C-Boats",
  "question": "q05",
  "question_title": "给香港帆船经纪人的报告",
  "statement": "Prepare a one- to two-page report for the Hong Kong (SAR) sailboat broker with a few well-chosen graphics.",
  "methods": "把官方价格模型精度、区域效应、香港情景、双体/单体差异和经纪报价建议压缩成可执行摘要。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2023/C-Boats/q05/solution.py",
  "result_path": "question_results/2023/C-Boats/q05/result.json",
  "report_path": "question_reports/2023/C-Boats/q05/report.md",
  "artifact_path": "question_artifacts/2023/C-Boats/q05/model_fit_actual_vs_predicted.png"
}
RESULT_PATH = BASE / "results" / '2023' / 'C-Boats' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'C-Boats' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'C-Boats' / 'q05'


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
