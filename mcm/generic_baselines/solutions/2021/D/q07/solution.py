from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-D",
  "year": "2021",
  "code": "D",
  "question": "q07",
  "question_title": "文化影响解释与 ICM Society 一页文档",
  "statement": "How does your work express information about cultural influence of music in time or circumstances? Write a one-page document to the ICM Society about the value of using your approach, how results would change with richer data, and recommendations for further study.",
  "methods": "用 follower active-start decade 分布描述时间环境下的影响网络，并把网络、相似性、演化和数据局限整理成面向 ICM Society 的一页说明。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2021/D/q07/solution.py",
  "result_path": "question_results/2021/D/q07/result.json",
  "report_path": "question_reports/2021/D/q07/report.md",
  "artifact_path": "question_artifacts/2021/D/q07/influence_network_top_artists.png"
}
RESULT_PATH = BASE / "results" / '2021' / 'D' / 'q07' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'D' / 'q07' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'D' / 'q07'


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
