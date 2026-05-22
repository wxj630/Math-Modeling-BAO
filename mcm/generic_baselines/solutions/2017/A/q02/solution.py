from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-A",
  "year": "2017",
  "code": "A",
  "question": "q02",
  "question_title": "10-20 座小坝数量与坝址推荐",
  "statement": "Provide a detailed analysis of removing Kariba Dam and replacing it with a series of ten to twenty smaller dams along the Zambezi River; support a recommendation for number and placement.",
  "methods": "在官方 10-20 座小坝范围内扫描 dam_count frontier，用 storage、flood attenuation、low-flow support、redundancy 和 coordination penalty 得到 water management index，并给出 0-100 归一化河道坐标坝址。对应模型：离散优化、设施选址、容量规划、多目标权衡。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2017/A/q02/solution.py",
  "result_path": "question_results/2017/A/q02/result.json",
  "report_path": "question_reports/2017/A/q02/report.md",
  "artifact_path": "question_artifacts/2017/A/q02/dam_placement_plan.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'A' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'A' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'A' / 'q02'


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
