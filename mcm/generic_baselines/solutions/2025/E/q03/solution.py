from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-E",
  "year": "2025",
  "code": "E",
  "question": "q03",
  "question_title": "边缘栖息地成熟与物种回归",
  "statement": "Incorporate the reemergence of species. Over time, the edge habitats begin to mature which brings back the species native to the area. As species return, the agricultural ecosystem changes due to the interactions of these species with the current environment. Incorporate two different species into the model to determine the impacts.",
  "methods": "显式加入蝙蝠和食虫鸟两类回归物种，量化生物控害、授粉、食物网冗余和稳定性变化。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/E/q03/solution.py",
  "result_path": "question_results/2025/E/q03/result.json",
  "report_path": "question_reports/2025/E/q03/report.md",
  "artifact_path": "question_artifacts/2025/E/q03/scenario_summary.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'E' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'E' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'E' / 'q03'


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
