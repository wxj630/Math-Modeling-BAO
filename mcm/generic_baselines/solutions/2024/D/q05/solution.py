from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-D",
  "year": "2024",
  "code": "D",
  "question": "q05",
  "question_title": "Lake Ontario 专项利益相关者分析",
  "statement": "Focus extensive analysis only on stakeholders and factors influencing Lake Ontario, where water level management has drawn concern.",
  "methods": "对 Lake Ontario 分析高低水位月份、目标偏离、与 Niagara/Ottawa/St. Lawrence 流量相关性和最高 stakeholder cost 月份。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2024/D/q05/solution.py",
  "result_path": "question_results/2024/D/q05/result.json",
  "report_path": "question_reports/2024/D/q05/report.md",
  "artifact_path": "question_artifacts/2024/D/q05/lake_ontario_target_band.png"
}
RESULT_PATH = BASE / "results" / '2024' / 'D' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'D' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'D' / 'q05'


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
