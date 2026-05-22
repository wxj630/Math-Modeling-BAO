from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-D",
  "year": "2021",
  "code": "D",
  "question": "q05",
  "question_title": "音乐革命性跃迁与革命者艺术家",
  "statement": "Identify if there are characteristics that might signify revolutions or major leaps in musical evolution from these data. What artists represent revolutionaries in your network?",
  "methods": "综合网络影响力、出边规模和影响者到追随者的平均标准化特征距离，构建 revolutionary_score，筛选高影响且带来大特征跃迁的艺术家。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2021/D/q05/solution.py",
  "result_path": "question_results/2021/D/q05/result.json",
  "report_path": "question_reports/2021/D/q05/report.md",
  "artifact_path": "question_artifacts/2021/D/q05/revolutionary_artists.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'D' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'D' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'D' / 'q05'


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
