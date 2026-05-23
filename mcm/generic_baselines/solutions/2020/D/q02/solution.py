from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-D",
  "year": "2020",
  "code": "D",
  "question": "q02",
  "question_title": "团队表现指标与协作成功模型",
  "statement": "Identify performance indicators that reflect successful teamwork such as diversity in the types of plays, coordination among players or distribution of contributions. Use the performance indicators and team level processes that you have identified to create a model that captures structural, configurational, and dynamical aspects of teamwork.",
  "methods": "构建逐场协作特征表：传球总数、相对传球优势、网络密度、互惠率、聚类、传球类型熵、头部传球对占比、贡献 Gini、平均传球距离、前向传球和进攻三区比例、射门/对抗/犯规事件；用前 30 场训练、后 8 场时间留出检验非输球分类模型。对应模型：指标体系、解释型决策树、时间留出验证。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2020/D/q02/solution.py",
  "result_path": "question_results/2020/D/q02/result.json",
  "report_path": "question_reports/2020/D/q02/report.md",
  "artifact_path": "question_artifacts/2020/D/q02/match_teamwork_features.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'D' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'D' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'D' / 'q02'


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
