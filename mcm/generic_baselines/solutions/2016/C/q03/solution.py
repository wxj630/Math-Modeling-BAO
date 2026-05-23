from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-C",
  "year": "2016",
  "code": "C",
  "question": "q03",
  "question_title": "ROI 权重稳健性与未来更新",
  "statement": "Validate the model and discuss how the Goodgrant Foundation should assess 2016 donations and future philanthropic educational investments.",
  "methods": "比较 base、need_priority、outcome_priority、scale_priority 四组权重场景，统计 Top20 overlap 和首选学校变化，说明 ROI 不是因果估计而是年度可更新的慈善投资指标。对应模型：敏感性分析、稳健性检验、模型更新机制。",
  "source_type": "official_comap_xlsx_zip",
  "solution_path": "question_solutions/2016/C/q03/solution.py",
  "result_path": "question_results/2016/C/q03/result.json",
  "report_path": "question_reports/2016/C/q03/report.md",
  "artifact_path": "question_artifacts/2016/C/q03/roi_weight_sensitivity.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'C' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'C' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'C' / 'q03'


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
