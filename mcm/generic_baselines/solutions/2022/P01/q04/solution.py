from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2022-P01",
  "year": "2022",
  "code": "P01",
  "question": "q04",
  "question_title": "面向港口用户的客户信",
  "statement": "Write a one-page letter to ICM Corporation's customers (the port users) outlining proposed measurement methods and instilling confidence in ICM Corporation's D&A system.",
  "methods": "把成熟度指标、质量检查、访问控制、客户可见仪表盘和卡车伙伴共享标准压缩成 port users 可读客户信。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2022/P01/q04/solution.py",
  "result_path": "question_results/2022/P01/q04/result.json",
  "report_path": "question_reports/2022/P01/q04/report.md",
  "artifact_path": "question_artifacts/2022/P01/q04/maturity_radar.png"
}
RESULT_PATH = BASE / "results" / '2022' / 'P01' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2022' / 'P01' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2022' / 'P01' / 'q04'


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
