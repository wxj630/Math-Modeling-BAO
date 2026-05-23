from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-C",
  "year": "2024",
  "code": "C",
  "question": "q02",
  "question_title": "教练随机波动假设检验",
  "statement": "A coach is skeptical that momentum plays a role and assumes swings are random. Use the model or metrics to evaluate this claim.",
  "methods": "对发球校正残差做跨比赛 lag-1 相关、最长连续得分串和决赛势头范围分析，评估是否存在时间结构。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2024/C/q02/solution.py",
  "result_path": "question_results/2024/C/q02/result.json",
  "report_path": "question_reports/2024/C/q02/report.md",
  "artifact_path": "question_artifacts/2024/C/q02/largest_momentum_points.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'C' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'C' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'C' / 'q02'


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
