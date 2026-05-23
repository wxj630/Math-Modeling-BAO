from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2023-D",
  "year": "2023",
  "code": "D",
  "question": "q01",
  "question_title": "17 个 SDG 的关系网络",
  "statement": "Create a network of the relationships between the 17 SDGs.",
  "methods": "官方 PDF 给出的 17 个 SDG 节点 + 透明确定性有向加权边，构造 SDG 影响网络；对应教程模型：复杂网络与图论模型。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2023/D/q01/solution.py",
  "result_path": "question_results/2023/D/q01/result.json",
  "report_path": "question_reports/2023/D/q01/report.md",
  "artifact_path": "question_artifacts/2023/D/q01/sdg_network_edges.csv"
}
RESULT_PATH = BASE / "results" / '2023' / 'D' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2023' / 'D' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2023' / 'D' / 'q01'


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
