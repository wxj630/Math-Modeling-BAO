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
  "question": "q04",
  "question_title": "巴西国家案例：自然资源、森林和未来世代",
  "statement": "Select a country and provide a more in-depth analysis of how this shift might impact them, explicitly tied to the changes between how GDP and GGDP are calculated.",
  "methods": "选择 Brazil，使用 World Bank 观察到的 natural resource rents、forest area、CO2 damage 和 GGDP gap，解释资源租金再投资、森林资本和碳损害可见性。对应模型：国家案例、多指标解释。",
  "source_type": "official_pdf_and_world_bank_api",
  "solution_path": "question_solutions/2023/F-GreenGDP/q04/solution.py",
  "result_path": "question_results/2023/F-GreenGDP/q04/result.json",
  "report_path": "question_reports/2023/F-GreenGDP/q04/report.md",
  "artifact_path": "question_artifacts/2023/F-GreenGDP/q04/brazil_country_analysis.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'F-GreenGDP' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'F-GreenGDP' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'F-GreenGDP' / 'q04'


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
