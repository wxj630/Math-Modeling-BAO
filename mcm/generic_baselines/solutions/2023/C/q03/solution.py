from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-C",
  "year": "2023",
  "code": "C",
  "question": "q03",
  "question_title": "答案词难度分类与 EERIE 难度",
  "statement": "Develop and summarize a model to classify solution words by difficulty. Identify attributes associated with each classification. Using your model, how difficult is EERIE? Discuss accuracy.",
  "methods": "用 1-6/X 百分比分布计算期望尝试次数，并按训练集三分位划分 easy/medium/hard；再用随机森林分类器从日期和词属性预测难度类别。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2023/C-Wordle/q03/solution.py",
  "result_path": "question_results/2023/C-Wordle/q03/result.json",
  "report_path": "question_reports/2023/C-Wordle/q03/report.md",
  "artifact_path": "question_artifacts/2023/C-Wordle/q03/difficulty_by_word.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'C' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'C' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'C' / 'q03'


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
