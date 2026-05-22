from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-C",
  "year": "2024",
  "code": "C",
  "question": "q04",
  "question_title": "跨比赛泛化测试与局限",
  "statement": "Test the model on one or more other matches, discuss prediction quality, missing factors, and generalizability to other matches or sports.",
  "methods": "用全体 31 场比赛最后 30 分平均势头预测点数优势方，并把温网决赛作为留出比赛检查。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2024/C/q04/solution.py",
  "result_path": "question_results/2024/C/q04/result.json",
  "report_path": "question_reports/2024/C/q04/report.md",
  "artifact_path": "question_artifacts/2024/C/q04/final_match_momentum_flow.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'C' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'C' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'C' / 'q04'


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
