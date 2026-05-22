from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-E",
  "year": "2019",
  "code": "E",
  "question": "q03",
  "question_title": "环境恶化如何计入项目成本",
  "statement": "How would environmental degradation be accounted for in these project costs?",
  "methods": "对社区道路、郊区住房、总部搬迁、跨国管线和商业水道扩展逐项计算 traditional NPV 与加入生态服务损失后的 true NPV。对应模型：全成本核算、残余生态负债。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/E/q03/solution.py",
  "result_path": "question_results/2019/E/q03/result.json",
  "report_path": "question_reports/2019/E/q03/report.md",
  "artifact_path": "question_artifacts/2019/E/q03/project_true_costs.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'E' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'E' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'E' / 'q03'


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
