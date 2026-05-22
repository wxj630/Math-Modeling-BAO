from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2015-D",
  "year": "2015",
  "code": "D",
  "question": "q01",
  "question_title": "国家可持续性评价模型",
  "statement": "Develop a model for the sustainability of a country. This model should provide a measure to distinguish more sustainable countries and policies from less sustainable ones, and clearly define when and how a country is sustainable or unsustainable.",
  "methods": "使用 COMAP 官方 PDF 和题面推荐的 World Bank Data，读取 Nepal 的人口、GDP/人、极端贫困、清洁水、用电、森林、卫生设施等缓存指标，构造 0-1 加权可持续性指数。对应模型：多指标综合评价、可持续发展指标、阈值分类。",
  "source_type": "official_pdf_and_world_bank_csv",
  "solution_path": "question_solutions/2015/D/q01/solution.py",
  "result_path": "question_results/2015/D/q01/result.json",
  "report_path": "question_reports/2015/D/q01/report.md",
  "artifact_path": "question_artifacts/2015/D/q01/sustainability_index_components.csv"
}
RESULT_PATH = BASE / "results" / '2015' / 'D' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2015' / 'D' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2015' / 'D' / 'q01'


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
