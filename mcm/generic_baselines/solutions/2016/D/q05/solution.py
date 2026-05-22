from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-D",
  "year": "2016",
  "code": "D",
  "question": "q05",
  "question_title": "信息价值、偏见、来源和拓扑强度敏感性",
  "statement": "Determine how information value, people's initial opinion and bias, form of the message or its source, and the topology or strength of the information network in a region, country, or worldwide could be used to spread information and influence public opinion.",
  "methods": "在同一观点影响公式上做 one-at-a-time 敏感性分析，识别 information value、source credibility、initial bias、message form、network strength 中最能改变传播和观点结果的因素。对应模型：敏感性分析、影响因子排序、舆论传播策略设计。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/D/q05/solution.py",
  "result_path": "question_results/2016/D/q05/result.json",
  "report_path": "question_reports/2016/D/q05/report.md",
  "artifact_path": "question_artifacts/2016/D/q05/factor_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'D' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'D' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'D' / 'q05'


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
