from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-F",
  "year": "2016",
  "code": "F",
  "question": "q08",
  "question_title": "邻国难民流动级联效应",
  "statement": "What would be the cascading effects on the movement of refugees in neighboring countries?",
  "methods": "对 West Balkans、Eastern Mediterranean 等高流量路线施加安全和处理容量下降，输出各路线 post-event safety/capacity 与 queue spillover 解释。对应模型：网络级联、瓶颈传播、压力测试。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/F/q08/solution.py",
  "result_path": "question_results/2016/F/q08/result.json",
  "report_path": "question_reports/2016/F/q08/report.md",
  "artifact_path": "question_artifacts/2016/F/q08/exogenous_event_stress.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'F' / 'q08' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'F' / 'q08' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'F' / 'q08'


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
