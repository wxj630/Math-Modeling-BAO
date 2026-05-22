from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-C",
  "year": "2024",
  "code": "C",
  "question": "q01",
  "question_title": "发球校正势头流与比赛流程可视化",
  "statement": "Develop a model that captures the flow of play as points occur, identify which player is performing better at a given time and how much better, and provide a visualization.",
  "methods": "发球胜率基线 + 逐分残差 + 指数加权移动平均势头指数 + 决赛逐分可视化。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2024/C/q01/solution.py",
  "result_path": "question_results/2024/C/q01/result.json",
  "report_path": "question_reports/2024/C/q01/report.md",
  "artifact_path": "question_artifacts/2024/C/q01/final_match_momentum_flow.png"
}
RESULT_PATH = BASE / "results" / '2024' / 'C' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'C' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'C' / 'q01'


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
