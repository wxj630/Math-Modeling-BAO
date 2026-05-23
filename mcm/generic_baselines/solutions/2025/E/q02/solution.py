from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-E",
  "year": "2025",
  "code": "E",
  "question": "q02",
  "question_title": "当前农业生态系统食物网",
  "statement": "Model the current ecosystem. Build a basic food web model for this new agricultural ecosystem which recently took the place of a heavily forested region. Include the producers and the consumers as well as the impact of the agriculture cycle and its seasonality which changes the system dynamics over time. Consider the impact of herbicides and pesticides by including the effects of chemical use on plant health, insect populations, bat and bird populations as well as the ecosystem stability.",
  "methods": "构建食物网边表和 120 个月季节性差分方程，比较化学基线下生产者、消费者、害虫压力和生态稳定性。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/E/q02/solution.py",
  "result_path": "question_results/2025/E/q02/result.json",
  "report_path": "question_reports/2025/E/q02/report.md",
  "artifact_path": "question_artifacts/2025/E/q02/state_trajectories.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'E' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'E' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'E' / 'q02'


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
