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
  "question": "q04",
  "question_title": "影响者是否真的影响追随者",
  "statement": "Indicate whether the similarity data, as reported in the influence_data data set, suggest that the identified influencers in fact influence the respective artists. Do the influencers actually affect the music created by the followers? Are some music characteristics more contagious than others?",
  "methods": "把官方 influence edges 与 data_by_artist 特征向量连接，计算同/跨流派影响边相似度、influencer-follower 特征相关和平均绝对差，识别更具传播性的音乐特征。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2021/D/q04/solution.py",
  "result_path": "question_results/2021/D/q04/result.json",
  "report_path": "question_reports/2021/D/q04/report.md",
  "artifact_path": "question_artifacts/2021/D/q04/feature_contagion.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'D' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'D' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'D' / 'q04'


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
