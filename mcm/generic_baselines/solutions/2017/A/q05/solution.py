from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-A",
  "year": "2017",
  "code": "A",
  "question": "q05",
  "question_title": "极端条件暴露区域与时长限制",
  "statement": "Include information addressing restrictions regarding locations and lengths of time that different areas of the Zambezi River should be exposed to the most detrimental effects of extreme conditions.",
  "methods": "把河道分成 upstream lake margin、mid-river farmland、urban low banks、hydropower intake reaches、delta wetlands，给出 flood/low-water 最大暴露天数和原因。对应模型：风险分区、暴露约束、韧性规划。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/A/q05/solution.py",
  "result_path": "question_results/2017/A/q05/result.json",
  "report_path": "question_reports/2017/A/q05/report.md",
  "artifact_path": "question_artifacts/2017/A/q05/exposure_restrictions.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'A' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'A' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'A' / 'q05'


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
