from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-B",
  "year": "2023",
  "code": "B",
  "question": "q01",
  "question_title": "保护区内不同区域的政策和管理策略",
  "statement": "Consider and recommend specific policies and management strategies for different areas within the current preserve that will protect wildlife and other natural resources while also balancing the interests of the people who live in the area. These policies and strategies should help mitigate the impacts of lost opportunities experienced by the people who live near the preserve, as well as minimize negative interactions between animals and the people attracted to the preserve.",
  "methods": "官方 PDF 题面 + Maasai Mara 分区多指标评价：wildlife value、habitat fragility、resident pressure、conflict exposure、tourism value；对应教程模型：综合评价与权重决策、空间分区。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/B/q01/solution.py",
  "result_path": "question_results/2023/B/q01/result.json",
  "report_path": "question_reports/2023/B/q01/report.md",
  "artifact_path": "question_artifacts/2023/B/q01/policy_zone_scores.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'B' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'B' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'B' / 'q01'


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
