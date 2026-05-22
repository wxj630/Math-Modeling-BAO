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
  "question": "q01",
  "question_title": "NFLIS 县域传播、起始位置与 2020 风险预测",
  "statement": "Using the NFLIS data provided, build a mathematical model to describe the spread and characteristics of the reported synthetic opioid and heroin incidents in and between the five states and their counties over time. Identify possible locations where specific opioid use might have started, and forecast future threshold concerns.",
  "methods": "读取官方 MCM_NFLIS_Data.xlsx，按 FIPS/year/state/county 汇总 heroin 与 synthetic_or_other_analgesic 报告，构建县-年面板；用最早阳性县和 2010-2017 每县 OLS 趋势识别起点和 2020 高风险阈值。对应模型：时空面板、趋势回归、阈值预警。",
  "source_type": "official_comap_xlsx_csv",
  "solution_path": "question_solutions/2019/C/q01/solution.py",
  "result_path": "question_results/2019/C/q01/result.json",
  "report_path": "question_reports/2019/C/q01/report.md",
  "artifact_path": "question_artifacts/2019/C/q01/county_year_opioid_panel.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'C' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'C' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'C' / 'q01'


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
