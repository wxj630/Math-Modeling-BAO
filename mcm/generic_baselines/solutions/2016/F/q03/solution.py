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
  "question": "q03",
  "question_title": "动态容量、资源前置与资源优先级",
  "statement": "What resources can be prepositioned and how should they be allocated in light of these dynamics? What resources need priority and how do you incorporate resource availability and flow in your model?",
  "methods": "把 shelter、healthcare、water、food 作为每千名难民的资源包，比较需求、政府可用量和 NGO 加成后的缺口，按 weighted unmet need 识别优先资源和前置行动。对应模型：系统动力学、资源配置、库存-流量模型、优先级排序。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/F/q03/solution.py",
  "result_path": "question_results/2016/F/q03/result.json",
  "report_path": "question_reports/2016/F/q03/report.md",
  "artifact_path": "question_artifacts/2016/F/q03/resource_prepositioning.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'F' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'F' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'F' / 'q03'


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
