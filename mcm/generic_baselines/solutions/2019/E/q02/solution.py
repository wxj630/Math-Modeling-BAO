from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-E",
  "year": "2019",
  "code": "E",
  "question": "q02",
  "question_title": "土地利用开发的环境成本是否可定价",
  "statement": "Is it possible to put a value on the environmental cost of land use development projects?",
  "methods": "用单位面积服务价值、扰动强度和 mitigation share 把环境成本并入项目 cost-benefit ratio，给出可审计但需本地校准的价值化方法。对应模型：成本收益分析、影子价格。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/E/q02/solution.py",
  "result_path": "question_results/2019/E/q02/result.json",
  "report_path": "question_reports/2019/E/q02/report.md",
  "artifact_path": "question_artifacts/2019/E/q02/project_true_costs.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'E' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'E' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'E' / 'q02'


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
