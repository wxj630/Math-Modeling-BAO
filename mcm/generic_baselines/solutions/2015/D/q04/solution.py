from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-D",
  "year": "2015",
  "code": "D",
  "question": "q04",
  "question_title": "20 页报告、模型优缺点与 ICM 投资建议",
  "statement": "Write a 20-page report that explains your model, sustainability measure, sustainable development plan, and the effect of your plan based on the model and country's environment. Detail the strengths and weaknesses of the model.",
  "methods": "把官方题面、World Bank 数据、指数定义、20 年计划、项目效率排序和模型限制整理为 ICM 可读报告，强调项目效果不是因果估计。对应模型：实验报告、政策备忘录、模型限制说明。",
  "source_type": "official_pdf_and_world_bank_csv",
  "solution_path": "question_solutions/2015/D/q04/solution.py",
  "result_path": "question_results/2015/D/q04/result.json",
  "report_path": "question_reports/2015/D/q04/report.md",
  "artifact_path": "question_artifacts/2015/D/q04/sustainability_projection.png"
}
RESULT_PATH = BASE / "results" / '2015' / 'D' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'D' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'D' / 'q04'


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
