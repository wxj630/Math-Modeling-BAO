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
  "question": "q02",
  "question_title": "EERIE 在 2023-03-01 的得分分布预测",
  "statement": "For a given future solution word on a future date, develop a model that allows you to predict the associated percentages of (1, 2, 3, 4, 5, 6, X). Give a specific example for EERIE on March 1, 2023 and discuss uncertainty.",
  "methods": "用官方历史分布训练多输出随机森林回归，预测 1/2/3/4/5/6/X 七个百分比桶，非负裁剪并归一化到 100%，用树分布和留出误差给出不确定性。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2023/C-Wordle/q02/solution.py",
  "result_path": "question_results/2023/C-Wordle/q02/result.json",
  "report_path": "question_reports/2023/C-Wordle/q02/report.md",
  "artifact_path": "question_artifacts/2023/C-Wordle/q02/eerie_prediction.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'C-Wordle' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'C-Wordle' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'C-Wordle' / 'q02'


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
