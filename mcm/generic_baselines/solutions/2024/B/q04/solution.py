from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-B",
  "year": "2024",
  "code": "B",
  "question": "q04",
  "question_title": "加勒比海迁移、多潜水器协调与希腊政府备忘录",
  "statement": "Extrapolate - How might your model be expanded to account for other tourist destinations such as the Caribbean Sea? How will your model change to account for multiple submersibles moving in the same general vicinity? Prepare a two-page memo addressed to the Greek government to help win approval.",
  "methods": "对加勒比海增大洋流和地形不确定性倍数；多潜水器用唯一声学编码、Voronoi 后验分区和资源冲突约束；输出给 Greek government 的审批备忘录。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/B/q04/solution.py",
  "result_path": "question_results/2024/B/q04/result.json",
  "report_path": "question_reports/2024/B/q04/report.md",
  "artifact_path": "question_artifacts/2024/B/q04/search_plan.png"
}
RESULT_PATH = BASE / "results" / '2024' / 'B' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'B' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'B' / 'q04'


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
