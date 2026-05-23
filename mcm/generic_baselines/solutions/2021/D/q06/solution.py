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
  "question": "q06",
  "question_title": "单一流派的动态影响过程",
  "statement": "Analyze the influence processes of musical evolution that occurred over time in one genre. Can your team identify indicators that reveal the dynamic influencers, and explain how the genres or artists changed over time?",
  "methods": "以官方数据中记录最多的 Pop/Rock 流派作为子网络示例，结合活跃年代、网络中心性和 genre/year 特征斜率，解释动态影响者与音频特征变化。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2021/D/q06/solution.py",
  "result_path": "question_results/2021/D/q06/result.json",
  "report_path": "question_reports/2021/D/q06/report.md",
  "artifact_path": "question_artifacts/2021/D/q06/genre_similarity_heatmap.png"
}
RESULT_PATH = BASE / "results" / '2021' / 'D' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'D' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'D' / 'q06'


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
