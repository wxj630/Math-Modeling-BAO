from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-F-GreenGDP",
  "year": "2023",
  "code": "F-GreenGDP",
  "question": "q02",
  "question_title": "GGDP 替代 GDP 的全球气候影响模型",
  "statement": "Make a simple model that is easily defendable to estimate the expected global impact on climate mitigation if your selected GGDP is adopted as the primary measure of the economic health of a nation.",
  "methods": "调用 World Bank WDI 最新可用 GDP、CO2 damage、资源耗减、森林耗减、森林面积和资源租金指标，构建全球与国家面板并估计 GGDP penalty。对应模型：公开数据面板、确定性情景模型。",
  "source_type": "official_pdf_and_world_bank_api",
  "solution_path": "question_solutions/2023/F-GreenGDP/q02/solution.py",
  "result_path": "question_results/2023/F-GreenGDP/q02/result.json",
  "report_path": "question_reports/2023/F-GreenGDP/q02/report.md",
  "artifact_path": "question_artifacts/2023/F-GreenGDP/q02/world_bank_green_gdp_panel.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'F-GreenGDP' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'F-GreenGDP' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'F-GreenGDP' / 'q02'


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
