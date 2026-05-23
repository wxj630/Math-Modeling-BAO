from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-C",
  "year": "2015",
  "code": "C",
  "question": "q01",
  "question_title": "ICM 组织人力资本网络模型",
  "statement": "Build a human capital network model of the personnel situation at ICM using the provided data. You may have to make bold assumptions to build the model; be sure to describe the model and your assumptions.",
  "methods": "只使用官方题面中的 370 个岗位、46 个 7 人部门、12 个 4 人办公室、85% 填补率、8%-10% 主动招聘范围和岗位层级表；构造层级、工作单元、流失影响、培训依赖四层人力资本网络。对应模型：多层网络、组织结构图建模、多指标 HR 健康指数。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2015/C/q01/solution.py",
  "result_path": "question_results/2015/C/q01/result.json",
  "report_path": "question_reports/2015/C/q01/report.md",
  "artifact_path": "question_artifacts/2015/C/q01/workforce_level_table.csv"
}
RESULT_PATH = BASE / "results" / '2015' / 'C' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'C' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'C' / 'q01'


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
