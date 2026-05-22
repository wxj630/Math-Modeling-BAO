from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-B",
  "year": "2017",
  "code": "B",
  "question": "q04",
  "question_title": "收费亭类型比例敏感性与 NJTA 信",
  "statement": "How is your solution affected by the proportions of conventional tollbooths, exact-change tollbooths, and electronic toll collection booths?",
  "methods": "比较 mostly conventional、balanced、electronic priority 和 transponder dominant 四种收费服务率组合，判断瓶颈从收费侧转向并道侧的条件，并生成 New Jersey Turnpike Authority 信函。对应模型：服务率模型、情景扫描、非技术政策报告。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/B/q04/solution.py",
  "result_path": "question_results/2017/B/q04/result.json",
  "report_path": "question_reports/2017/B/q04/report.md",
  "artifact_path": "question_artifacts/2017/B/q04/tollbooth_mix_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'B' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'B' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'B' / 'q04'


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
