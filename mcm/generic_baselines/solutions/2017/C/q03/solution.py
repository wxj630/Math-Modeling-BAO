from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-C",
  "year": "2017",
  "code": "C",
  "question": "q03",
  "question_title": "均衡与性能突变临界点",
  "statement": "Determine whether equilibria exist and whether there is a tipping point where performance changes markedly.",
  "methods": "把总峰小时 vehicle-hours 作为系统性能指标，在 0%-100% AV share 网格上寻找首次比全人类驾驶基线降低 10% 的临界点，并解释该点附近的容量反馈。对应模型：离散均衡扫描、阈值分析、系统性能曲线。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2017/C/q03/solution.py",
  "result_path": "question_results/2017/C/q03/result.json",
  "report_path": "question_reports/2017/C/q03/report.md",
  "artifact_path": "question_artifacts/2017/C/q03/adoption_segment_profiles.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'C' / 'q03' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'C' / 'q03' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'C' / 'q03'


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
