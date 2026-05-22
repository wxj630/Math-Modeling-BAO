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
  "question": "q05",
  "question_title": "给巴西领导人的一页非技术报告",
  "statement": "Based on your country-specific analysis, write a one-page non-technical report to the leaders of that country on whether to support a switch to GGDP or to reject a switch and maintain GDP.",
  "methods": "把 adjusted-savings GGDP 公式、Brazil GGDP penalty、森林/资源政策含义、全球 phased switch 建议和实施风险压缩成领导人可读报告。对应模型：政策备忘录、非技术摘要。",
  "source_type": "official_pdf_and_world_bank_api",
  "solution_path": "question_solutions/2023/F-GreenGDP/q05/solution.py",
  "result_path": "question_results/2023/F-GreenGDP/q05/result.json",
  "report_path": "question_reports/2023/F-GreenGDP/q05/report.md",
  "artifact_path": "question_artifacts/2023/F-GreenGDP/q05/green_gdp_policy_frontier.png"
}
RESULT_PATH = BASE / "results" / '2023' / 'F-GreenGDP' / 'q05' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'F-GreenGDP' / 'q05' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'F-GreenGDP' / 'q05'


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
