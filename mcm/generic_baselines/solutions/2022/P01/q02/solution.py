from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-P01",
  "year": "2022",
  "code": "P01",
  "question": "q02",
  "question_title": "优化 D&A 能力的系统变更建议",
  "statement": "After ICM Corporation uses your model to determine its current D&A maturity level, demonstrate how it could recommend changes to maximize data asset potential.",
  "methods": "按最大加权缺口生成 0-24 个月路线图，包括数据 owner、catalog/lineage、质量流程、客户仪表盘和模型监控。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/P01/q02/solution.py",
  "result_path": "question_results/2022/P01/q02/result.json",
  "report_path": "question_reports/2022/P01/q02/report.md",
  "artifact_path": "question_artifacts/2022/P01/q02/improvement_roadmap.csv"
}
RESULT_PATH = BASE / "results" / '2022' / 'P01' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'P01' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'P01' / 'q02'


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
