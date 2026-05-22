from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-E",
  "year": "2016",
  "code": "E",
  "question": "q02",
  "question_title": "选择超载地区并解释缺水驱动因素",
  "statement": "Using the UN water scarcity map pick one country or region where water is heavily or moderately overloaded. Explain why and how water is scarce in that region, addressing physical and/or economic scarcity.",
  "methods": "选择 Jordan 作为 heavily overloaded 地区；用 World Bank 总取水占内部资源比例、农业/生活/工业取水份额、饮水和卫生覆盖解释物理稀缺与经济稀缺。对应模型：指标诊断、社会-环境驱动分析。",
  "source_type": "official_pdf_and_world_bank_csv",
  "solution_path": "question_solutions/2016/E/q02/solution.py",
  "result_path": "question_results/2016/E/q02/result.json",
  "report_path": "question_reports/2016/E/q02/report.md",
  "artifact_path": "question_artifacts/2016/E/q02/world_bank_water_panel.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'E' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'E' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'E' / 'q02'


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
