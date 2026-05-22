from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-A",
  "year": "2023",
  "code": "A",
  "question": "q04",
  "question_title": "未来干旱频率和变异范围变化的影响",
  "statement": "What are the impact of a greater frequency and wider variation of the occurrence of droughts in future weather cycles? If droughts are less frequent, does the number of species have the same impact on the overall population?",
  "methods": "固定 6 物种群落，改变干旱间隔与严重度倍数，输出 more frequent / less frequent / wider variation 情景下的可持续得分和生物多样性边际价值。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/A/q04/solution.py",
  "result_path": "question_results/2023/A/q04/result.json",
  "report_path": "question_reports/2023/A/q04/report.md",
  "artifact_path": "question_artifacts/2023/A/q04/drought_frequency_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'A' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'A' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'A' / 'q04'


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
