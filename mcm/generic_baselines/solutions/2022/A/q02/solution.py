from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-A",
  "year": "2022",
  "code": "A",
  "question": "q02",
  "question_title": "东京、弗兰德斯和自定义计时赛路线功率策略",
  "statement": "Apply your model to the 2021 Olympic Time Trial course in Tokyo, the 2021 UCI World Championship time trial course in Flanders, and a course of your own design with at least four sharp turns and a nontrivial grade.",
  "methods": "把官方列名路线和自定义技术环线拆成坡度、转弯、风暴露段，按空气阻力、滚阻、坡度和能量预算逐段求目标功率与用时。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/A/q02/solution.py",
  "result_path": "question_results/2022/A/q02/result.json",
  "report_path": "question_reports/2022/A/q02/report.md",
  "artifact_path": "question_artifacts/2022/A/q02/course_strategy_results.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'A' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'A' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'A' / 'q02'


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
