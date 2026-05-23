from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-F",
  "year": "2019",
  "code": "F",
  "question": "q01",
  "question_title": "全球去中心化数字金融可行性模型",
  "statement": "Construct a model that represents a global decentralized digital financial system and identifies key factors that limit or facilitate growth, access, security, and stability.",
  "methods": "把题面 growth、access、security、stability 拆成国家原型的 unbanked share、digital access、regulatory trust、currency instability 和 illicit flow risk，计算 adoption viability。对应模型：多指标综合评价、政策可行性评分。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/P06/q01/solution.py",
  "result_path": "question_results/2019/P06/q01/result.json",
  "report_path": "question_reports/2019/P06/q01/report.md",
  "artifact_path": "question_artifacts/2019/P06/q01/currency_adoption_viability.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'F' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'F' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'F' / 'q01'


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
