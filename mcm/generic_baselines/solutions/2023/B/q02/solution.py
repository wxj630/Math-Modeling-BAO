from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-B",
  "year": "2023",
  "code": "B",
  "question": "q02",
  "question_title": "政策结果排名、比较与动物-人类-经济模型",
  "statement": "Develop and describe a methodology to determine which policies and management strategies will result in the best outcomes. Your report should discuss how to rank and compare outcomes from your methodology. Be sure to include descriptions and analyses of the models used to predict the interactions between animals and people, as well as the resulting economic impacts in the area within and around the preserve.",
  "methods": "构建生态、居民、经济、治理可行性和成本惩罚的加权多目标评分；最高政策再进入人兽冲突动态和社区收益投影。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/B/q02/solution.py",
  "result_path": "question_results/2023/B/q02/result.json",
  "report_path": "question_reports/2023/B/q02/report.md",
  "artifact_path": "question_artifacts/2023/B/q02/policy_package_ranking.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'B' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'B' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'B' / 'q02'


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
