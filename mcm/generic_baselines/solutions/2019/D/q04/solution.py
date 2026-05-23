from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-D",
  "year": "2019",
  "code": "D",
  "question": "q04",
  "question_title": "验证、模型局限与大型拥挤结构迁移",
  "statement": "Validate the model, discuss strengths and weaknesses, and explain adaptation to other large crowded structures.",
  "methods": "用官方数量级做容量 sanity check，说明没有公开全部出口清单的限制，并给出体育馆、机场、商场等结构的迁移步骤。对应模型：模型验证、迁移应用。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/D/q04/solution.py",
  "result_path": "question_results/2019/D/q04/result.json",
  "report_path": "question_reports/2019/D/q04/report.md",
  "artifact_path": "question_artifacts/2019/D/q04/louvre_evacuation_frontier.png"
}
RESULT_PATH = BASE / "results" / '2019' / 'D' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'D' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'D' / 'q04'


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
