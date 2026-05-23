from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-A",
  "year": "2019",
  "code": "A",
  "question": "q03",
  "question_title": "支撑三条龙所需面积",
  "statement": "How much area is required to support the three dragons?",
  "methods": "把年度猎物需求除以不同气候猎物密度，得到三条龙在暖温带、干旱和北极情景下的 habitat footprint。对应模型：承载力估计、资源面积换算。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/A/q03/solution.py",
  "result_path": "question_results/2019/A/q03/result.json",
  "report_path": "question_reports/2019/A/q03/report.md",
  "artifact_path": "question_artifacts/2019/A/q03/dragon_area_requirements.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'A' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'A' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'A' / 'q03'


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
