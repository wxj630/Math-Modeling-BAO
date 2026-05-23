from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-A",
  "year": "2024",
  "code": "A",
  "question": "q04",
  "question_title": "对寄生虫和其他生态系统成员的优势",
  "statement": "Can an ecosystem with variable sex ratios in the lamprey population offer advantages to others in the ecosystem, such as parasites?",
  "methods": "从宿主鱼、七鳃鳗寄生者、捕食者/人类食物资源三类受益方分析可变性别比稳定七鳃鳗丰度后的间接收益与代价。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/A/q04/solution.py",
  "result_path": "question_results/2024/A/q04/result.json",
  "report_path": "question_reports/2024/A/q04/report.md",
  "artifact_path": "question_artifacts/2024/A/q04/lamprey_tradeoff_frontier.png"
}
RESULT_PATH = BASE / "results" / '2024' / 'A' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'A' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'A' / 'q04'


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
