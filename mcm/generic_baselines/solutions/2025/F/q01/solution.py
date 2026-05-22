from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-F",
  "year": "2025",
  "code": "F",
  "question": "q01",
  "question_title": "全球网络犯罪分布与报告偏差",
  "statement": "How is cybercrime distributed across the globe? Which countries are disproportionately high targets of cybercrimes, where are cybercrimes successful, where are cybercrimes thwarted, where are cybercrimes reported, where are cybercrimes prosecuted? Do you notice any patterns?",
  "methods": "官方 PDF 题面 + 题面引用 VCDB/VERIS 公开事件样本：按受害国统计事件、披露事件和有公开引用的报告事件，并明确起诉/挫败字段在 VCDB 中不可完整观测。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/F/q01/solution.py",
  "result_path": "question_results/2025/F/q01/result.json",
  "report_path": "question_reports/2025/F/q01/report.md",
  "artifact_path": "question_artifacts/2025/F/q01/vcdb_country_distribution.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'F' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'F' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'F' / 'q01'


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
