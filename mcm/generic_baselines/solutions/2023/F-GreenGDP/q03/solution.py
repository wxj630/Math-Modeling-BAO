from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-F-GreenGDP",
  "year": "2023",
  "code": "F-GreenGDP",
  "question": "q03",
  "question_title": "全球尺度替换 GDP 的收益与阻力权衡",
  "statement": "Determine if your model indicates that the switch is worthwhile at a global scale, comparing both the potential upside of climate mitigation impact and the potential downside of the effort required to replace the status quo.",
  "methods": "对 cautious pilot、phased G20/resource exporters、full primary metric switch 三种情景比较 climate/resource benefit index、transition effort index 和 net benefit score。对应模型：成本收益、多情景评价。",
  "source_type": "official_pdf_and_world_bank_api",
  "solution_path": "question_solutions/2023/F-GreenGDP/q03/solution.py",
  "result_path": "question_results/2023/F-GreenGDP/q03/result.json",
  "report_path": "question_reports/2023/F-GreenGDP/q03/report.md",
  "artifact_path": "question_artifacts/2023/F-GreenGDP/q03/global_impact_scenarios.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'F-GreenGDP' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'F-GreenGDP' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'F-GreenGDP' / 'q03'


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
