from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-C",
  "year": "2017",
  "code": "C",
  "question": "q02",
  "question_title": "10%/50%/90% 自动驾驶渗透率情景",
  "statement": "Analyze how the effects change as the percentage of self-driving cars increases from 10% to 50% to 90%.",
  "methods": "把 AV share p 进入确定性容量倍率 `1 + 1.20*p^2 + 0.25*p*(1-p)`，分别计算 10%、50%、90% 下 congested segment share、peak vehicle-hours、节省时间和中位速度。对应模型：情景仿真、混合交通容量模型、敏感性分析。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2017/C/q02/solution.py",
  "result_path": "question_results/2017/C/q02/result.json",
  "report_path": "question_reports/2017/C/q02/report.md",
  "artifact_path": "question_artifacts/2017/C/q02/adoption_scenario_summary.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'C' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'C' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'C' / 'q02'


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
