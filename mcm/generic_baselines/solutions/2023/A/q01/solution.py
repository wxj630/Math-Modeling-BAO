from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-A",
  "year": "2023",
  "code": "A",
  "question": "q01",
  "question_title": "不规则天气与干旱循环下的植物群落动态模型",
  "statement": "Develop a mathematical model to predict how a plant community changes over time as it is exposed to various irregular weather cycles. Include times of drought when precipitation should be abundant. The model should account for interactions between different species during cycles of drought.",
  "methods": "官方 PDF 题面观察 + 多物种生物量差分方程 + 干旱压力时间序列 + 物种互补促进项；对应教程模型：微分/差分方程、敏感性分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/A/q01/solution.py",
  "result_path": "question_results/2023/A/q01/result.json",
  "report_path": "question_reports/2023/A/q01/report.md",
  "artifact_path": "question_artifacts/2023/A/q01/community_trajectories.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'A' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'A' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'A' / 'q01'


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
