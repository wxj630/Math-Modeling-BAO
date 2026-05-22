from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-A",
  "year": "2017",
  "code": "A",
  "question": "q03",
  "question_title": "多坝系统正常水文周期调度策略",
  "statement": "Include a strategy for modulating the water flow through the new multiple dam system that provides a reasonable balance between safety and costs under known or predicted normal water cycles.",
  "methods": "把 normal wet-season 和 normal dry-season 转成 flow_index 区间，制定上游蓄水、中游错峰、下游生态脉冲和低流量补给规则。对应模型：水库群调度、规则曲线、系统动力学、风险-成本权衡。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/A/q03/solution.py",
  "result_path": "question_results/2017/A/q03/result.json",
  "report_path": "question_reports/2017/A/q03/report.md",
  "artifact_path": "question_artifacts/2017/A/q03/flow_modulation_policy.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'A' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'A' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'A' / 'q03'


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
