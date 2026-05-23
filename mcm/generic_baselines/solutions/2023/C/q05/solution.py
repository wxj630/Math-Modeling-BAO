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
  "question": "q05",
  "question_title": "给纽约时报 Puzzle Editor 的摘要信",
  "statement": "Summarize your results in a one- to two-page letter to the Puzzle Editor of the New York Times.",
  "methods": "把报告人数预测、EERIE 分布、难度分类和数据集洞察压缩成编辑可读的决策信。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2023/C-Wordle/q05/solution.py",
  "result_path": "question_results/2023/C-Wordle/q05/result.json",
  "report_path": "question_reports/2023/C-Wordle/q05/report.md",
  "artifact_path": "question_artifacts/2023/C-Wordle/q05/eerie_distribution.png"
}
RESULT_PATH = BASE / "results" / '2023' / 'C' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'C' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'C' / 'q05'


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
