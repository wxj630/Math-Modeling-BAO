from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-C",
  "year": "2019",
  "code": "C",
  "question": "q02",
  "question_title": "ACS 社会经济因素关联与模型修正",
  "statement": "Using the U.S. Census socio-economic data provided, determine whether use or trends-in-use are associated with any of the provided Census data, and modify the model from Part 1 to include important factors.",
  "methods": "读取 2010-2016 官方 ACS DP02 CSV，按 FIPS/year 合并 NFLIS opioid_rate_per_1000_drug_reports，计算教育、退伍军人、残障、外来出生、居住稳定性等特征的描述性相关。对应模型：面板合并、相关分析、社会特征解释。",
  "source_type": "official_comap_xlsx_csv",
  "solution_path": "question_solutions/2019/C/q02/solution.py",
  "result_path": "question_results/2019/C/q02/result.json",
  "report_path": "question_reports/2019/C/q02/report.md",
  "artifact_path": "question_artifacts/2019/C/q02/socioeconomic_correlations.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'C' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'C' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'C' / 'q02'


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
