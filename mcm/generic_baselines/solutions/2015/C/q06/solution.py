from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-C",
  "year": "2015",
  "code": "C",
  "question": "q06",
  "question_title": "团队科学与多层组织网络扩展",
  "statement": "Summarize the potential use of team science and multilayer networks to realize the HR manager's vision of connecting the human capital network to information flow, trust, influence, and friendship layers.",
  "methods": "把人力资本网络扩展为信息流、信任、影响力、友谊和培训依赖的 multiplex 网络，用跨层中心性识别关键员工和关键岗位。对应模型：团队科学、多层网络、multiplex centrality、组织网络分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2015/C/q06/solution.py",
  "result_path": "question_results/2015/C/q06/result.json",
  "report_path": "question_reports/2015/C/q06/report.md",
  "artifact_path": "question_artifacts/2015/C/q06/workforce_level_table.csv"
}
RESULT_PATH = BASE / "results" / '2015' / 'C' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'C' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'C' / 'q06'


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
