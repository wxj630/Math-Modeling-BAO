from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-A",
  "year": "2016",
  "code": "A",
  "question": "q01",
  "question_title": "浴缸水温空间-时间模型与加热水策略",
  "statement": "Develop a model of the temperature of the bathtub water in space and time to determine the best strategy the person in the bathtub can adopt to keep the temperature even throughout the bathtub and as close as possible to the initial temperature without wasting too much water.",
  "methods": "只使用官方题面物理约束，建立一维有限体积浴缸温度模型：热水从水龙头端进入，溢流端排出，水面/缸壁/人体散热，邻近单元混合。对应模型：热传导方程、对流-扩散模型、有限体积法、多目标优化。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/A/q01/solution.py",
  "result_path": "question_results/2016/A/q01/result.json",
  "report_path": "question_reports/2016/A/q01/report.md",
  "artifact_path": "question_artifacts/2016/A/q01/temperature_strategy_grid.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'A' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'A' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'A' / 'q01'


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
