from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-C",
  "year": "2021",
  "code": "C",
  "question": "q01",
  "question_title": "公众报告数据解释与扩散可预测性",
  "statement": "Address and discuss whether or not the spread of this pest over time can be predicted, and with what level of precision.",
  "methods": "读取官方 4440 条 sightings workbook，按 Positive ID 时间和经纬度构建阳性时间线与空间聚类；用题面 30km 新蜂后范围解释可预测精度边界。对应模型：空间统计、时间序列描述、风险地图。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2021/C/q01/solution.py",
  "result_path": "question_results/2021/C/q01/result.json",
  "report_path": "question_reports/2021/C/q01/report.md",
  "artifact_path": "question_artifacts/2021/C/q01/hornet_spread_map.png"
}
RESULT_PATH = BASE / "results" / '2021' / 'C' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'C' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'C' / 'q01'


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
