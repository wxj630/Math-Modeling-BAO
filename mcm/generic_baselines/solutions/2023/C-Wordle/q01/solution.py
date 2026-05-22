from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-C-Wordle",
  "year": "2023",
  "code": "C-Wordle",
  "question": "q01",
  "question_title": "报告人数变化、3 月 1 日预测区间与困难模式比例",
  "statement": "The number of reported results vary daily. Develop a model to explain this variation and use your model to create a prediction interval for the number of reported results on March 1, 2023. Do any attributes of the word affect the percentage of scores reported that were played in Hard Mode?",
  "methods": "官方 Wordle Excel 清洗 + 对数报告人数 RidgeCV 时间趋势回归 + 词属性标准化回归解释困难模式比例 + 留出集误差评估。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2023/C-Wordle/q01/solution.py",
  "result_path": "question_results/2023/C-Wordle/q01/result.json",
  "report_path": "question_reports/2023/C-Wordle/q01/report.md",
  "artifact_path": "question_artifacts/2023/C-Wordle/q01/reported_results_forecast.png"
}
RESULT_PATH = BASE / "results" / '2023' / 'C-Wordle' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'C-Wordle' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'C-Wordle' / 'q01'


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
