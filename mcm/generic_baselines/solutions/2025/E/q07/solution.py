from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2025-E",
  "year": "2025",
  "code": "E",
  "question": "q07",
  "question_title": "方法建议、经济权衡与政策激励",
  "statement": "Advise the farmer on what methods should be employed including discussions on economic trade-offs as well as sustainability. Help the farmer determine strategies that could be implemented to balance costs and sustainability and how advocating for certain policies could incentivize this type of conservation in agriculture.",
  "methods": "推荐分阶段减少化学投入、恢复边缘栖息地、使用蝙蝠/食虫鸟生物控害和争取生态服务补贴，以平衡现金流与长期稳定性。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2025/E/q07/solution.py",
  "result_path": "question_results/2025/E/q07/result.json",
  "report_path": "question_reports/2025/E/q07/report.md",
  "artifact_path": "question_artifacts/2025/E/q07/organic_tradeoff_frontier.csv"
}
RESULT_PATH = BASE / "results" / '2025' / 'E' / 'q07' / "result.json"
REPORT_PATH = BASE / "reports" / '2025' / 'E' / 'q07' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2025' / 'E' / 'q07'


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
