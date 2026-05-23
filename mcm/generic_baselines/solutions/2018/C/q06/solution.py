from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2018-C",
  "year": "2018",
  "code": "C",
  "question": "q06",
  "question_title": "给四州州长的能源政策备忘录",
  "statement": "Write a concise memo to the Governors of Arizona, California, New Mexico, and Texas explaining the model results and recommending compact actions.",
  "methods": "把四州能源画像、2009 最佳 benchmark、2025/2050 gap 和政策行动翻译为州长可读备忘录。对应模型：非技术决策报告、政策建议、模型结果解释。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2018/C/q06/solution.py",
  "result_path": "question_results/2018/C/q06/result.json",
  "report_path": "question_reports/2018/C/q06/report.md",
  "artifact_path": "question_artifacts/2018/C/q06/renewable_share_trends.png"
}
RESULT_PATH = BASE / "results" / '2018' / 'C' / 'q06' / "result.json"
REPORT_PATH = BASE / "reports" / '2018' / 'C' / 'q06' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2018' / 'C' / 'q06'


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
