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
  "question": "q04",
  "question_title": "政府与 NGO 协同策略",
  "statement": "How does the inclusion of NGO's change your model and strategy?",
  "methods": "比较 government-only 和 with-NGO 两种资源策略的 unmet need；NGO 不改变法律准入，但增加移动医疗、水、食物和临时 shelter 能力，使模型从边境处理转为分布式救援。对应模型：情景对比、资源协同、公共-非政府协作模型。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/F/q04/solution.py",
  "result_path": "question_results/2016/F/q04/result.json",
  "report_path": "question_reports/2016/F/q04/report.md",
  "artifact_path": "question_artifacts/2016/F/q04/ngo_strategy_comparison.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'F' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'F' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'F' / 'q04'


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
