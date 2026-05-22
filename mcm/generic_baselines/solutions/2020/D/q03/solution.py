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
  "question": "q03",
  "question_title": "给 Huskies 教练的结构策略建议",
  "statement": "Use the insights gained from your teamwork model to inform the coach about what kinds of structural strategies have been effective for the Huskies. Advise the coach on what changes the network analysis indicates that they should make next season to improve team success.",
  "methods": "比较胜/负场协作指标差异与决策树特征重要性，形成互惠传球、midfield-forward 三角、传球多样性、赛后监测四类建议，并给出面向教练的非技术备忘录。对应模型：对比分析、特征重要性、策略决策表。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2020/D/q03/solution.py",
  "result_path": "question_results/2020/D/q03/result.json",
  "report_path": "question_reports/2020/D/q03/report.md",
  "artifact_path": "question_artifacts/2020/D/q03/teamwork_feature_importance.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'D' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'D' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'D' / 'q03'


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
