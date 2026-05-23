from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-E",
  "year": "2020",
  "code": "E",
  "question": "q01",
  "question_title": "单次使用塑料废弃物安全缓解容量",
  "statement": "Develop a model to estimate maximum levels of single-use or disposable plastic product waste that can safely be mitigated without further environmental damage.",
  "methods": "使用官方 9% recycling、4-12 million tons ocean input 等题面数字，按区域 waste、single-use share、mitigation capacity 和 policy capacity 估算安全处理容量和溢出。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2020/E/q01/solution.py",
  "result_path": "question_results/2020/E/q01/result.json",
  "report_path": "question_reports/2020/E/q01/report.md",
  "artifact_path": "question_artifacts/2020/E/q01/regional_safe_mitigation_capacity.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'E' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'E' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'E' / 'q01'


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
