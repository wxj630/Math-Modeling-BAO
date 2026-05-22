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
  "question": "q06",
  "question_title": "支持最优迁移模式的政策包与 UN 信件",
  "statement": "Write a report on your model and propose a set of policies that will support the optimal set of conditions ensuring the optimal migration pattern.",
  "methods": "把安全路线分流、多个入口点、容量触发配额、shelter/healthcare 前置、NGO 物流通道和本地居民健康安全合并为政策包，并写给 UN Secretary General 和 Chief of Migration 的一页政策信。对应模型：政策优化、执行摘要、风险治理、健康安全约束。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/F/q06/solution.py",
  "result_path": "question_results/2016/F/q06/result.json",
  "report_path": "question_reports/2016/F/q06/report.md",
  "artifact_path": "question_artifacts/2016/F/q06/refugee_flow_network.png"
}
RESULT_PATH = BASE / "results" / '2016' / 'F' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'F' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'F' / 'q06'


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
