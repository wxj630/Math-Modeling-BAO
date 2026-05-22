from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-D",
  "year": "2024",
  "code": "D",
  "question": "q04",
  "question_title": "环境条件变化敏感性",
  "statement": "How sensitive is the algorithm to environmental changes such as precipitation, snowpack, and ice jams?",
  "methods": "用偏离分月目标带的高水位/月低水位月数、平均 stakeholder cost 和最大偏离量作为环境冲击敏感性指标。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2024/D/q04/solution.py",
  "result_path": "question_results/2024/D/q04/result.json",
  "report_path": "question_reports/2024/D/q04/report.md",
  "artifact_path": "question_artifacts/2024/D/q04/annual_mean_levels.png"
}
RESULT_PATH = BASE / "results" / '2024' / 'D' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'D' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'D' / 'q04'


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
