from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-F",
  "year": "2016",
  "code": "F",
  "question": "q10",
  "question_title": "10 倍危机规模下不可扩展特征",
  "statement": "Using your model, expand the crisis to a larger scale by a factor of 10. Are there features of your model that are not scalable to larger populations?",
  "methods": "把官方 715,000 规模放大 10 倍，比较不扩容时处理天数，识别 manual case processing、single-route bottleneck relief、short-term shelter-only planning、government-only deployment 等不可扩展特征。对应模型：尺度分析、容量扩展、瓶颈分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/F/q10/solution.py",
  "result_path": "question_results/2016/F/q10/result.json",
  "report_path": "question_reports/2016/F/q10/report.md",
  "artifact_path": "question_artifacts/2016/F/q10/scalability_10x.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'F' / 'q10' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'F' / 'q10' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'F' / 'q10'


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
