from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-D",
  "year": "2021",
  "code": "D",
  "question": "q03",
  "question_title": "流派关系与随时间演化",
  "statement": "Compare similarities and influences between and within genres. What distinguishes a genre and how do genres change over time? Are some genres related to others?",
  "methods": "将 full_music_data.csv 的 artist_id 合并到 influence_data 的流派标签，按 year 和 genre 聚合音频特征，用线性趋势斜率描述流派演化，并用流派中心相似矩阵识别相关流派。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2021/D/q03/solution.py",
  "result_path": "question_results/2021/D/q03/result.json",
  "report_path": "question_reports/2021/D/q03/report.md",
  "artifact_path": "question_artifacts/2021/D/q03/genre_feature_evolution.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'D' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'D' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'D' / 'q03'


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
