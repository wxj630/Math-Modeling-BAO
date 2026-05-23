from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-Y",
  "year": "2023",
  "code": "Y",
  "question": "q01",
  "question_title": "二手帆船挂牌价解释模型与估计精度",
  "statement": "Develop a mathematical model that explains the listing price of each sailboat in the provided spreadsheet. Include useful predictors, identify data sources, and discuss precision for each sailboat variant's price.",
  "methods": "读取官方单体船/双体船 Excel，清洗长度、船龄、品牌、型号、区域和价格，用随机森林预测 log(price)，并在留出集按型号统计误差精度。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2023/C-Boats/q01/solution.py",
  "result_path": "question_results/2023/C-Boats/q01/result.json",
  "report_path": "question_reports/2023/C-Boats/q01/report.md",
  "artifact_path": "question_artifacts/2023/C-Boats/q01/variant_precision.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'Y' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'Y' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'Y' / 'q01'


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
