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
  "question": "q03",
  "question_title": "15 年无干预水资源预测与居民影响",
  "statement": "In your chosen region, use your model to show what the water situation will be in 15 years. How does this situation impact the lives of citizens? Incorporate environmental drivers' effects.",
  "methods": "用最近人口增长率乘以题面用水增长为人口增长两倍的约束，外推无干预 stress index，并给出居民生活影响。对应模型：趋势外推、需求增长模型、风险阈值分析。",
  "source_type": "official_pdf_and_world_bank_csv",
  "solution_path": "question_solutions/2016/E/q03/solution.py",
  "result_path": "question_results/2016/E/q03/result.json",
  "report_path": "question_reports/2016/E/q03/report.md",
  "artifact_path": "question_artifacts/2016/E/q03/water_forecast.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'E' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'E' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'E' / 'q03'


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
