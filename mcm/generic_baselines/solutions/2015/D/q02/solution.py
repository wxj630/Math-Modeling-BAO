from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-D",
  "year": "2015",
  "code": "D",
  "question": "q02",
  "question_title": "LDC 20 年可持续发展计划",
  "statement": "Select a country from the United Nations list of the 48 Least Developed Countries. Using your model and research from Task 1, create a 20 year sustainable development plan for your selected LDC country.",
  "methods": "选定 Nepal 作为 LDC 示例，基于 World Bank 基线指标设计清洁水和卫生、分布式清洁能源、气候韧性农业、教育与生计、森林和灾害风险管理五类 20 年项目。对应模型：情景规划、多目标规划、项目组合设计。",
  "source_type": "official_pdf_and_world_bank_csv",
  "solution_path": "question_solutions/2015/D/q02/solution.py",
  "result_path": "question_results/2015/D/q02/result.json",
  "report_path": "question_reports/2015/D/q02/report.md",
  "artifact_path": "question_artifacts/2015/D/q02/development_plan.csv"
}
RESULT_PATH = BASE / "results" / '2015' / 'D' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'D' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'D' / 'q02'


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
