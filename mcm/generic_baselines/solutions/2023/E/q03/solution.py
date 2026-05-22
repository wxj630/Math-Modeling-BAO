from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-E",
  "year": "2023",
  "code": "E",
  "question": "q03",
  "question_title": "三种光污染干预策略",
  "statement": "Describe three possible intervention strategies to address light pollution. Discuss specific actions to implement each strategy and the potential impacts of these actions on the effects of light pollution in general.",
  "methods": "比较 shielded warm-spectrum fixtures、adaptive dimming and curfew controls、zoning ordinance and sign-lighting limits，并保留 habitat buffer dark corridor 作为保护地增强策略。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/E/q03/solution.py",
  "result_path": "question_results/2023/E/q03/result.json",
  "report_path": "question_reports/2023/E/q03/report.md",
  "artifact_path": "question_artifacts/2023/E/q03/intervention_strategy_scores.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'E' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'E' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'E' / 'q03'


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
