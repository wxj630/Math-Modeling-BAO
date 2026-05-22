from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-B",
  "year": "2019",
  "code": "B",
  "question": "q02",
  "question_title": "机队、医疗包与 ISO 集装箱装载",
  "statement": "Recommend a drone fleet and medical packages, and design packing configurations for up to three ISO cargo containers.",
  "methods": "用官方 ISO 内部尺寸、drone shipping dimensions、cargo bay type 和 MED1/MED2/MED3 尺寸约束，选择 C/G/B/F/H 组合并分配三地 container cells。对应模型：三维装箱近似、载荷约束筛选。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/B/q02/solution.py",
  "result_path": "question_results/2019/B/q02/result.json",
  "report_path": "question_reports/2019/B/q02/report.md",
  "artifact_path": "question_artifacts/2019/B/q02/container_packing_plan.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'B' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'B' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'B' / 'q02'


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
