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
  "question": "q04",
  "question_title": "Wordle 数据集的其他有趣特征",
  "statement": "List and describe some other interesting features of this data set.",
  "methods": "统计报告人数年度衰减、困难模式平均占比、重复字母与期望尝试次数差异、星期效应和关键相关系数。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2023/C-Wordle/q04/solution.py",
  "result_path": "question_results/2023/C-Wordle/q04/result.json",
  "report_path": "question_reports/2023/C-Wordle/q04/report.md",
  "artifact_path": "question_artifacts/2023/C-Wordle/q04/wordle_clean_data.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'C' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'C' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'C' / 'q04'


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
