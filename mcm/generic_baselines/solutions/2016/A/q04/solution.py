from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-A",
  "year": "2016",
  "code": "A",
  "question": "q04",
  "question_title": "给浴缸用户的一页非技术说明",
  "statement": "Include a one-page non-technical explanation for users of the bathtub that describes your strategy while explaining why it is so difficult to get an evenly maintained temperature throughout the bath water.",
  "methods": "把推荐流量、动作建议、热水入口/溢流出口导致的冷热不均、泡沫保温作用和浪费水权衡写成用户可读说明。对应模型：非技术解释、策略说明、模型限制说明。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/A/q04/solution.py",
  "result_path": "question_results/2016/A/q04/result.json",
  "report_path": "question_reports/2016/A/q04/report.md",
  "artifact_path": "question_artifacts/2016/A/q04/temperature_profiles.png"
}
RESULT_PATH = BASE / "results" / '2016' / 'A' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'A' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'A' / 'q04'


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
