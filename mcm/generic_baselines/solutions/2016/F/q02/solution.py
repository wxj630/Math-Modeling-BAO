from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-F",
  "year": "2016",
  "code": "F",
  "question": "q02",
  "question_title": "六条路线容量约束难民流动模型",
  "statement": "Create a model of optimal refugee movement that would incorporate projected flows of refugees across the six travel routes mentioned in the problem, with consideration of transportation routes/accessibility, safety of route and countries' resource capacities.",
  "methods": "对 West/Central/Eastern Mediterranean、West Balkans、Eastern Borders、Albania to Greece 六条官方路线建立安全性、可达性、临时容量和日处理能力参数；按吸引力和容量进行整数分配，容量不足时显式记录 emergency overflow。对应模型：网络流、容量约束分配、整数流量分配、瓶颈分析。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/F/q02/solution.py",
  "result_path": "question_results/2016/F/q02/result.json",
  "report_path": "question_reports/2016/F/q02/report.md",
  "artifact_path": "question_artifacts/2016/F/q02/route_flow_plan.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'F' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'F' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'F' / 'q02'


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
