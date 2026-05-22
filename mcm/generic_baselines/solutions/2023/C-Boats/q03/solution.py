from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-C-Boats",
  "year": "2023",
  "code": "C-Boats",
  "question": "q03",
  "question_title": "香港市场可比挂牌样本与区域效应情景",
  "statement": "Discuss how the regional modeling can be useful in the Hong Kong (SAR) market. Choose an informative subset split between monohulls and catamarans, find comparable Hong Kong listing prices, and model the Hong Kong regional effect.",
  "methods": "明确官方 Excel 没有香港行；用带来源 URL 的香港当前挂牌补充样本做情景校准，并与官方区域模型对同船型/长度/船龄的预测中位价比较。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2023/C-Boats/q03/solution.py",
  "result_path": "question_results/2023/C-Boats/q03/result.json",
  "report_path": "question_reports/2023/C-Boats/q03/report.md",
  "artifact_path": "question_artifacts/2023/C-Boats/q03/hong_kong_comparables.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'C-Boats' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'C-Boats' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'C-Boats' / 'q03'


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
