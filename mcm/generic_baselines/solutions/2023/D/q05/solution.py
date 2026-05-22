from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-D",
  "year": "2023",
  "code": "D",
  "question": "q05",
  "question_title": "网络方法迁移到其他公司和组织",
  "statement": "Discuss how your network approach may help other companies and organizations set priorities of their goals.",
  "methods": "把 SDG 网络方法抽象成目标节点、依赖边、中心性、直接需求、风险覆盖和达成后重算，用于 ESG、公共卫生、高校和 NGO 目标组合决策。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/D/q05/solution.py",
  "result_path": "question_results/2023/D/q05/result.json",
  "report_path": "question_reports/2023/D/q05/report.md",
  "artifact_path": "question_artifacts/2023/D/q05/sdg_priority_network.png"
}
RESULT_PATH = BASE / "results" / '2023' / 'D' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'D' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'D' / 'q05'


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
