from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-E",
  "year": "2016",
  "code": "E",
  "question": "q01",
  "question_title": "清洁水供给能力模型",
  "statement": "Develop a model that provides a measure of the ability of a region to provide clean water to meet the needs of its population. You may need to consider the dynamic nature of the factors that affect both supply and demand.",
  "methods": "读取 World Bank Jordan 缓存指标，用 freshwater withdrawals/internal renewable resources 构造物理水压力，并用基础饮水、卫生服务和 GDP/capita 修正经济稀缺。对应模型：水资源压力指数、系统动力学、多指标评价。",
  "source_type": "official_pdf_and_world_bank_csv",
  "solution_path": "question_solutions/2016/E/q01/solution.py",
  "result_path": "question_results/2016/E/q01/result.json",
  "report_path": "question_reports/2016/E/q01/report.md",
  "artifact_path": "question_artifacts/2016/E/q01/water_scarcity_components.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'E' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'E' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'E' / 'q01'


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
