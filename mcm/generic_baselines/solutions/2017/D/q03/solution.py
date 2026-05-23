from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-D",
  "year": "2017",
  "code": "D",
  "question": "q03",
  "question_title": "文化规范与旅客风格敏感性",
  "statement": "Consider how cultural norms may impact the way in which passengers process through checkpoints as a sensitivity analysis. How can the security system accommodate these differences in a manner that expedites passenger throughput and reduces variance?",
  "methods": "在官方流程样本上施加 personal-space cautious、collective-efficiency、individual-fast but variable 三类确定性乘数，说明这些是旅客风格敏感性而非 workbook 中的文化观测。对应模型：敏感性分析、情景参数、服务时间扰动。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2017/D/q03/solution.py",
  "result_path": "question_results/2017/D/q03/result.json",
  "report_path": "question_reports/2017/D/q03/report.md",
  "artifact_path": "question_artifacts/2017/D/q03/cultural_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'D' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'D' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'D' / 'q03'


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
