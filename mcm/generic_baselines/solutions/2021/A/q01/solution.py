from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-A",
  "year": "2021",
  "code": "A",
  "question": "q01",
  "question_title": "多真菌地表凋落物分解模型",
  "statement": "Build a mathematical model that describes the breakdown of ground litter and woody fibers through fungal activity in the presence of multiple species of fungi.",
  "methods": "将题面指定的 growth rate 与 moisture tolerance 两个 trait 转成分解率、竞争权重和环境适配项，模拟固定 patch 的凋落物质量损失。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2021/A/q01/solution.py",
  "result_path": "question_results/2021/A/q01/result.json",
  "report_path": "question_reports/2021/A/q01/report.md",
  "artifact_path": "question_artifacts/2021/A/q01/decomposition_environment_results.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'A' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'A' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'A' / 'q01'


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
