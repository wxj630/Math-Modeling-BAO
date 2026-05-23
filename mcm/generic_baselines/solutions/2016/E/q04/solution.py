from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-E",
  "year": "2016",
  "code": "E",
  "question": "q04",
  "question_title": "覆盖所有缺水驱动因素的干预计划",
  "statement": "For your chosen region, design an intervention plan taking all the drivers of water scarcity into account. Discuss surrounding-area and ecosystem impacts, strengths and weaknesses.",
  "methods": "设计农业节水、污水回用和卫生、漏损控制、海水淡化+可再生能源、雨水收集和地下水回补五类组合计划，并记录周边生态影响。对应模型：干预组合设计、成本效益分析、生态外部性评估。",
  "source_type": "official_pdf_and_world_bank_csv",
  "solution_path": "question_solutions/2016/E/q04/solution.py",
  "result_path": "question_results/2016/E/q04/result.json",
  "report_path": "question_reports/2016/E/q04/report.md",
  "artifact_path": "question_artifacts/2016/E/q04/intervention_plan.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'E' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'E' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'E' / 'q04'


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
