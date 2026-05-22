from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-A",
  "year": "2025",
  "code": "A",
  "question": "q07",
  "question_title": "材料来源一致性指导",
  "statement": "Can the source of the material be determined? For example, if stone is used is the wear consistent with materials from a quarry the archaeologist believes is the original source or if wood was used is the wear consistent with the age and type of trees that are assumed to be used?",
  "methods": "给出石材/木材的非破坏材料代理测量流程：硬度、密度、纹理、工具痕和反推磨损系数必须与候选采石场或木材参考范围重叠。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/A/q07/solution.py",
  "result_path": "question_results/2025/A/q07/result.json",
  "report_path": "question_reports/2025/A/q07/report.md",
  "artifact_path": "question_artifacts/2025/A/q07/measurement_template.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'A' / 'q07' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'A' / 'q07' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'A' / 'q07'


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
