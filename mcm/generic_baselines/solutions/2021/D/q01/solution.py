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
  "question": "q01",
  "question_title": "有向音乐影响网络与影响力参数",
  "statement": "Use the influence_data data set or portions of it to create a directed network of musical influence, where influencers are connected to followers. Develop parameters that capture music influence in this network. Explore a subset of musical influence by creating a subnetwork of your directed influencer network.",
  "methods": "读取 COMAP 官方 influence_data.csv，构建 influencer -> follower 有向图，计算入度、出度、PageRank、综合 influence_score，并给出 Pop/Rock 子网络规模；对应教程模型：图论网络中心性、复杂网络分析。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2021/D/q01/solution.py",
  "result_path": "question_results/2021/D/q01/result.json",
  "report_path": "question_reports/2021/D/q01/report.md",
  "artifact_path": "question_artifacts/2021/D/q01/artist_influence_centrality.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'D' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'D' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'D' / 'q01'


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
