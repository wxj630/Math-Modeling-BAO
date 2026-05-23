from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-E",
  "year": "2024",
  "code": "E",
  "question": "q01",
  "question_title": "保险公司应在什么条件下承保",
  "statement": "Under what conditions should insurance companies underwrite policies?",
  "methods": "官方 PDF 宏观参数 + 气候压力承保可持续性分数：综合净巨灾损失率、保障缺口导致的可负担性压力、减灾效果和资本缓冲。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/E/q01/solution.py",
  "result_path": "question_results/2024/E/q01/result.json",
  "report_path": "question_reports/2024/E/q01/report.md",
  "artifact_path": "question_artifacts/2024/E/q01/underwriting_policy_grid.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'E' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'E' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'E' / 'q01'


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
