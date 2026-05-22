from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2018-C",
  "year": "2018",
  "code": "C",
  "question": "q05",
  "question_title": "四州能源 compact 目标与行动",
  "statement": "Develop a plan for an interstate compact among the four states that moves the region toward cleaner renewable energy. Identify target values and practical actions.",
  "methods": "以 2009 最佳州 benchmark 和 2025/2050 基线中位水平设置 compact target，计算各州 gap，并提出可交易清洁能源信用、跨州输电储能、需求侧效率三类行动。对应模型：目标规划、差距分析、多主体政策组合。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2018/C/q05/solution.py",
  "result_path": "question_results/2018/C/q05/result.json",
  "report_path": "question_reports/2018/C/q05/report.md",
  "artifact_path": "question_artifacts/2018/C/q05/compact_targets.csv"
}
RESULT_PATH = BASE / "results" / '2018' / 'C' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2018' / 'C' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2018' / 'C' / 'q05'


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
