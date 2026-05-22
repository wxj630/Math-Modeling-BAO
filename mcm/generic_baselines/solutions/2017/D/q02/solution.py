from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-D",
  "year": "2017",
  "code": "D",
  "question": "q02",
  "question_title": "两类以上流程修改实验",
  "statement": "Develop two or more potential modifications to the current process to improve passenger throughput and reduce variance in wait time. Model these changes to demonstrate how your modifications impact the process.",
  "methods": "比较 2 PreCheck/2 regular 动态车道重平衡、并行取筐/物品准备支持、混合方案三类确定性场景，以 combined mean wait、p90 wait 和 checkpoint clear time 评价。对应模型：方案仿真、多指标比较、服务系统优化。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2017/D/q02/solution.py",
  "result_path": "question_results/2017/D/q02/result.json",
  "report_path": "question_reports/2017/D/q02/report.md",
  "artifact_path": "question_artifacts/2017/D/q02/modification_comparison.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'D' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'D' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'D' / 'q02'


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
