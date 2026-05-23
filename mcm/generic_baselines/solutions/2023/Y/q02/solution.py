from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-Y",
  "year": "2023",
  "code": "Y",
  "question": "q02",
  "question_title": "区域对挂牌价的实际与统计影响",
  "statement": "Use your model to explain the effect, if any, of region on listing prices. Discuss whether regional effects are consistent across all sailboat variants and address practical and statistical significance.",
  "methods": "以 Europe 为基准，对 log(price) 做 OLS 区域效应模型，控制长度、船龄、船型和船型-区域交互，报告百分比效应、p 值和船型一致性。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2023/C-Boats/q02/solution.py",
  "result_path": "question_results/2023/C-Boats/q02/result.json",
  "report_path": "question_reports/2023/C-Boats/q02/report.md",
  "artifact_path": "question_artifacts/2023/C-Boats/q02/region_effects.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'Y' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'Y' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'Y' / 'q02'


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
