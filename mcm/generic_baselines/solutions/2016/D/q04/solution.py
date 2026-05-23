from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-D",
  "year": "2016",
  "code": "D",
  "question": "q04",
  "question_title": "公众兴趣与观点影响模型",
  "statement": "Use the theories and concepts of information influence on networks to model how public interest and opinion can be changed through information networks in today's connected world.",
  "methods": "用 DeGroot 风格一阶观点更新，把 information value、source credibility、initial bias、message form 和 network strength 转成 persuasion index 与 final support share，比较公共卫生警告、低可信党派声明、名人传闻、官方本地灾害信息、科学纠错等情景。对应模型：观点动力学、DeGroot 模型、阈值说服、情景仿真。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/D/q04/solution.py",
  "result_path": "question_results/2016/D/q04/result.json",
  "report_path": "question_reports/2016/D/q04/report.md",
  "artifact_path": "question_artifacts/2016/D/q04/opinion_influence_scenarios.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'D' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'D' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'D' / 'q04'


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
