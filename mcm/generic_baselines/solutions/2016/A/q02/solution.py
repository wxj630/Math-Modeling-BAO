from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-A",
  "year": "2016",
  "code": "A",
  "question": "q02",
  "question_title": "浴缸形状、体积、人体和动作敏感性",
  "statement": "Use your model to determine the extent to which your strategy depends upon the shape and volume of the tub, the shape/volume/temperature of the person in the bathtub, and the motions made by the person in the bathtub.",
  "methods": "固定推荐流量，比较短深、基准、长浅浴缸，以及静止、轻柔动作、主动搅动的温度误差和空间温差；人体体积/温度作为显式假设。对应模型：参数扫描、几何尺度分析、混合强度模型、敏感性分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/A/q02/solution.py",
  "result_path": "question_results/2016/A/q02/result.json",
  "report_path": "question_reports/2016/A/q02/report.md",
  "artifact_path": "question_artifacts/2016/A/q02/tub_shape_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'A' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'A' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'A' / 'q02'


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
