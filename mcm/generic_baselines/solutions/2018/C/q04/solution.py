from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2018-C",
  "year": "2018",
  "code": "C",
  "question": "q04",
  "question_title": "无政策变化下 2025/2050 基线预测",
  "statement": "Predict the energy profiles of the four states in 2025 and 2050 if no policy changes are made.",
  "methods": "使用官方 1990-2009 SEDS renewable share 与 per-capita energy 线性趋势外推 2025、2050，明确这是 no-policy baseline 而不是未来观测数据。对应模型：线性趋势预测、基线情景、外推不确定性说明。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2018/C/q04/solution.py",
  "result_path": "question_results/2018/C/q04/result.json",
  "report_path": "question_reports/2018/C/q04/report.md",
  "artifact_path": "question_artifacts/2018/C/q04/renewable_share_forecast.csv"
}
RESULT_PATH = BASE / "results" / '2018' / 'C' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2018' / 'C' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2018' / 'C' / 'q04'


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
