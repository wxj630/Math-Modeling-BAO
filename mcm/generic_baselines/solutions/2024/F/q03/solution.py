from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-F",
  "year": "2024",
  "code": "F",
  "question": "q03",
  "question_title": "文献和分析如何支持项目选择",
  "statement": "What research, from published literature and from your own analyses, supports the selection of your proposed project?",
  "methods": "用官方 26.5B USD/year 与第四大非法贸易约束，加上复杂系统网络和干预证据说明 targeted corridor disruption 比泛化宣传更适合客户。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/F/q03/solution.py",
  "result_path": "question_results/2024/F/q03/result.json",
  "report_path": "question_reports/2024/F/q03/report.md",
  "artifact_path": "question_artifacts/2024/F/q03/complex_system_edges.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'F' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'F' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'F' / 'q03'


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
