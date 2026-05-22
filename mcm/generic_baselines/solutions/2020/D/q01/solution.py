from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-D",
  "year": "2020",
  "code": "D",
  "question": "q01",
  "question_title": "传球网络、二元三元结构与多尺度指标",
  "statement": "Create a network for the ball passing between players, where each player is a node and each pass constitutes a link between players. Use your passing network to identify network patterns, such as dyadic and triadic configurations and team formations. Also consider other structural indicators and network properties across the games.",
  "methods": "读取 COMAP 官方 matches.csv、passingevents.csv、fullevents.csv；以 Huskies 球员为节点、有向传球为加权边，计算二元边、三角 motif、互惠率、PageRank、介数中心性、密度、加权聚类和位置份额。对应模型：图论网络中心性、复杂网络、多尺度团队结构分析。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2020/D/q01/solution.py",
  "result_path": "question_results/2020/D/q01/result.json",
  "report_path": "question_reports/2020/D/q01/report.md",
  "artifact_path": "question_artifacts/2020/D/q01/passing_network_edges.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'D' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'D' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'D' / 'q01'


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
