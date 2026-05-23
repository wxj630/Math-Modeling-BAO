from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-B",
  "year": "2017",
  "code": "B",
  "question": "q01",
  "question_title": "收费亭后 8 到 3 车道并道几何",
  "statement": "Determine the shape, size, and merging pattern of the area following the toll barrier in which vehicles fan in from B tollbooth egress lanes down to L lanes of traffic.",
  "methods": "只使用官方题面参数 L、B、B > L 和 3 车道/8 收费亭示例，构造 short taper、staged zipper、collector-distributor 和 metered merge 四类可替换几何方案，按冲突指数、吞吐能力和土地/控制成本评分。对应模型：道路几何规划、多目标评分、成本-安全权衡。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/B/q01/solution.py",
  "result_path": "question_results/2017/B/q01/result.json",
  "report_path": "question_reports/2017/B/q01/report.md",
  "artifact_path": "question_artifacts/2017/B/q01/merge_geometry.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'B' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'B' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'B' / 'q01'


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
