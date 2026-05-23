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
  "question": "q04",
  "question_title": "不同援助水平下的人类社区规模",
  "statement": "How large a community is necessary to support a dragon for varying levels of assistance that can be provided to the dragons?",
  "methods": "扫描 0%、25%、50%、75% 人类供食份额，把猎物 kg/day 转换为牧养家庭和专业 handler 需求。对应模型：资源供给规划、社区承载能力。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/A/q04/solution.py",
  "result_path": "question_results/2019/A/q04/result.json",
  "report_path": "question_reports/2019/A/q04/report.md",
  "artifact_path": "question_artifacts/2019/A/q04/dragon_community_support.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'A' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'A' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'A' / 'q04'


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
