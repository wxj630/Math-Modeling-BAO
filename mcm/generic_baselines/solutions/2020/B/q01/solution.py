from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-B",
  "year": "2020",
  "code": "B",
  "question": "q01",
  "question_title": "同沙量同海滩条件下的最长寿基础形状",
  "statement": "Construct a mathematical model to identify the best 3-dimensional geometric shape to use as a sandcastle foundation that will last the longest period of time under the same beach, sand, volume, distance, and water-to-sand proportion.",
  "methods": "用暴露表面积、角部冲刷、坡度稳定性、足迹扩散和可建造性构造确定性 erosion index，比较 low mound、truncated cone、hemisphere、frustum、ridge 和 tower。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/B/q01/solution.py",
  "result_path": "question_results/2020/B/q01/result.json",
  "report_path": "question_reports/2020/B/q01/report.md",
  "artifact_path": "question_artifacts/2020/B/q01/sandcastle_shape_scores.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'B' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'B' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'B' / 'q01'


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
