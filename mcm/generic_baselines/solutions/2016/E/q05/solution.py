from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-E",
  "year": "2016",
  "code": "E",
  "question": "q05",
  "question_title": "有干预水资源预测与关键问题判断",
  "statement": "Use the intervention from Task 4 and your model to project water availability into the future. Can the region become less susceptible to water scarcity? Will water become a critical issue, and when?",
  "methods": "对比无干预和有干预 15 年 stress index，判断是否降低易受缺水影响以及是否仍为 critical。对应模型：反事实预测、情景对比、政策效果评估。",
  "source_type": "official_pdf_and_world_bank_csv",
  "solution_path": "question_solutions/2016/E/q05/solution.py",
  "result_path": "question_results/2016/E/q05/result.json",
  "report_path": "question_reports/2016/E/q05/report.md",
  "artifact_path": "question_artifacts/2016/E/q05/water_forecast.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'E' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'E' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'E' / 'q05'


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
