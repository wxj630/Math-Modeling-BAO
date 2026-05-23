from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-A",
  "year": "2019",
  "code": "A",
  "question": "q02",
  "question_title": "龙的能量消耗与热量摄入",
  "statement": "What are the energy expenditures of the dragons, and what are their caloric intake requirements?",
  "methods": "用异速代谢基线叠加飞行、喷火、生长和创伤储备项，输出三条龙每日 kcal、猎物 kg 和饮水需求；所有质量和能量系数作为显式可替换假设。对应模型：异速生理模型、能量预算。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/A/q02/solution.py",
  "result_path": "question_results/2019/A/q02/result.json",
  "report_path": "question_reports/2019/A/q02/report.md",
  "artifact_path": "question_artifacts/2019/A/q02/dragon_energy_budget.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'A' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'A' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'A' / 'q02'


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
