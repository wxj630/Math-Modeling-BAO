from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-C",
  "year": "2019",
  "code": "C",
  "question": "q03",
  "question_title": "反制策略情景、参数边界与 DEA/NFLIS 备忘录",
  "statement": "Using a combination of Part 1 and Part 2 results, identify a possible strategy for countering the opioid crisis. Use your models to test effectiveness and identify parameter bounds. Include a memo to the Chief Administrator, DEA/NFLIS Database.",
  "methods": "基于 2020 预测设置 high/watch 县阈值，测试 lab feedback、treatment/prescriber outreach、combined supply/treatment 三类情景的报告减少幅度，并输出 DEA/NFLIS memo。对应模型：情景仿真、阈值政策、敏感性边界。",
  "source_type": "official_comap_xlsx_csv",
  "solution_path": "question_solutions/2019/C/q03/solution.py",
  "result_path": "question_results/2019/C/q03/result.json",
  "report_path": "question_reports/2019/C/q03/report.md",
  "artifact_path": "question_artifacts/2019/C/q03/opioid_forecast_2020.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'C' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'C' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'C' / 'q03'


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
