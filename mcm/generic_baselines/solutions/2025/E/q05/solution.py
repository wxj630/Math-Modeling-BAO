from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-E",
  "year": "2025",
  "code": "E",
  "question": "q05",
  "question_title": "有机农业情景与权衡前沿",
  "statement": "Go green? Analyze the implications of a farmer considering organic farming methods. Consideration should be given to different scenarios with varying components of organic farming. Demonstrate the impact on the ecosystem as a whole and to the individual components. Discuss aspects such as pest control, crop health, plant reproduction, biodiversity, long-term sustainability and cost effectiveness.",
  "methods": "比较化学基线、去除除草剂、蝙蝠边缘栖息地、部分有机和完全有机五个情景，输出生态稳定、害虫压力、产量、净收益和成本有效性排序。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/E/q05/solution.py",
  "result_path": "question_results/2025/E/q05/result.json",
  "report_path": "question_reports/2025/E/q05/report.md",
  "artifact_path": "question_artifacts/2025/E/q05/organic_tradeoff_frontier.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'E' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'E' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'E' / 'q05'


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
