from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-C",
  "year": "2024",
  "code": "C",
  "question": "q03",
  "question_title": "比赛流程换向预测与关键因素",
  "statement": "Develop a model to predict when flow is about to shift from one player to the other and identify relevant factors.",
  "methods": "以未来 8 分内强势头换向为标签，使用逻辑回归解释 `abs_momentum`、破发点、发球、速度、回合数和非受迫失误等因素。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2024/C/q03/solution.py",
  "result_path": "question_results/2024/C/q03/result.json",
  "report_path": "question_reports/2024/C/q03/report.md",
  "artifact_path": "question_artifacts/2024/C/q03/swing_model_coefficients.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'C' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'C' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'C' / 'q03'


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
