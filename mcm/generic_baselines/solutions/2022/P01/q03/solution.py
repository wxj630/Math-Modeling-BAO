from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-P01",
  "year": "2022",
  "code": "P01",
  "question": "q03",
  "question_title": "效果衡量协议与大小港口/卡车公司迁移",
  "statement": "Suggest effectiveness protocols, demonstrate larger or smaller seaport use, and analyze whether a trucking company could use the maturity metric.",
  "methods": "保留相同成熟度刻度，将港口规模复杂度、客户可见性需求和卡车调度/遥测/交付证明数据替换为迁移参数。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/P01/q03/solution.py",
  "result_path": "question_results/2022/P01/q03/result.json",
  "report_path": "question_reports/2022/P01/q03/report.md",
  "artifact_path": "question_artifacts/2022/P01/q03/port_scaling_scenarios.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'P01' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'P01' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'P01' / 'q03'


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
