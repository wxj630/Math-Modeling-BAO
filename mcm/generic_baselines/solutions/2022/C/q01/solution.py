from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-C",
  "year": "2022",
  "code": "C",
  "question": "q01",
  "question_title": "仅用历史价格的每日交易策略",
  "statement": "Develop a model that gives the best daily trading strategy based only on price data up to that day. How much is the initial $1000 investment worth on 9/10/2021 using your model and strategy?",
  "methods": "读取 COMAP 官方 LBMA-GOLD.csv 与 BCHAIN-MKPRU.csv，构建 `[cash, gold_oz, bitcoin]` 投资组合模拟器；候选策略只使用截至当日价格，按手续费和交易日约束回测。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2022/C/q01/solution.py",
  "result_path": "question_results/2022/C/q01/result.json",
  "report_path": "question_reports/2022/C/q01/report.md",
  "artifact_path": "question_artifacts/2022/C/q01/portfolio_value_curve.png"
}
RESULT_PATH = BASE / "results" / '2022' / 'C' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'C' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'C' / 'q01'


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
