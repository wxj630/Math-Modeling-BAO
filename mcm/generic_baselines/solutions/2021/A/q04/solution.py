from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-A",
  "year": "2021",
  "code": "A",
  "question": "q04",
  "question_title": "生物多样性对分解效率的作用与教材文章",
  "statement": "Describe how fungal diversity impacts decomposition efficiency and include a two-page article appropriate for an introductory college biology textbook.",
  "methods": "比较 1-5 个 species pool 在高波动 temperate 环境下的 Shannon diversity 与 mass loss，形成面向大学生物教材的非技术文章。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/A/q04/solution.py",
  "result_path": "question_results/2021/A/q04/result.json",
  "report_path": "question_reports/2021/A/q04/report.md",
  "artifact_path": "question_artifacts/2021/A/q04/fungi_decomposition_frontier.png"
}
RESULT_PATH = BASE / "results" / '2021' / 'A' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'A' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'A' / 'q04'


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
