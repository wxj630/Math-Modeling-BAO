from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-C",
  "year": "2020",
  "code": "C",
  "question": "q03",
  "question_title": "文本描述词与评分的组合信号",
  "statement": "Determine combinations of text-based measures and ratings-based measures that best indicate a potentially successful or failing product.",
  "methods": "构造 enthusiastic、disappointed、durable、broken、easy 描述词组的 rating lift 与 helpfulness，和评分、低分占比合成 success_signal_score。",
  "source_type": "official_comap_tsv_zip",
  "solution_path": "question_solutions/2020/C/q03/solution.py",
  "result_path": "question_results/2020/C/q03/result.json",
  "report_path": "question_reports/2020/C/q03/report.md",
  "artifact_path": "question_artifacts/2020/C/q03/text_descriptor_rating_lift.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'C' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'C' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'C' / 'q03'


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
