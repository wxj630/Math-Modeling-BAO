from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-F",
  "year": "2016",
  "code": "F",
  "question": "q11",
  "question_title": "规模急剧增加时改变或失效的参数",
  "statement": "What parameters in your model change or become irrelevant when the scope of the crisis increases dramatically?",
  "methods": "分析临时 camp capacity、route popularity、daily transport 等参数在长期/超大规模危机中如何让位于住房吸收、国际负担分担、疾病控制和教育连续性。对应模型：尺度转移、参数有效性审计、长期系统动力学。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/F/q11/solution.py",
  "result_path": "question_results/2016/F/q11/result.json",
  "report_path": "question_reports/2016/F/q11/report.md",
  "artifact_path": "question_artifacts/2016/F/q11/scalability_10x.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'F' / 'q11' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'F' / 'q11' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'F' / 'q11'


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
