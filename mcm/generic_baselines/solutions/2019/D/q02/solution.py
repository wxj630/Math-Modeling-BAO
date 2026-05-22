from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-D",
  "year": "2019",
  "code": "D",
  "question": "q02",
  "question_title": "威胁情景、额外出口与救援进入权衡",
  "statement": "Design an adaptable model for threats that can alter or remove route segments while allowing emergency personnel to enter quickly.",
  "methods": "比较 main exits 全开、Pyramid 不可用、地下烟雾、河岸安全事件等情景，显式保留 responder corridor 并控制 service exits 的安全开启。对应模型：鲁棒路线组合、情景分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/D/q02/solution.py",
  "result_path": "question_results/2019/D/q02/result.json",
  "report_path": "question_reports/2019/D/q02/report.md",
  "artifact_path": "question_artifacts/2019/D/q02/louvre_threat_scenarios.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'D' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'D' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'D' / 'q02'


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
