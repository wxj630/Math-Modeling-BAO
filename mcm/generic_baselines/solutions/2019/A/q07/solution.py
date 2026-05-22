from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-A",
  "year": "2019",
  "code": "A",
  "question": "q07",
  "question_title": "给 George R.R. Martin 的信与现实类比",
  "statement": "Draft a two-page letter to George R.R. Martin and describe a non-fictional situation that the modeling could inform.",
  "methods": "把生态足迹、气候迁移和社区支持结论整理为作者建议信，并迁移到大型顶级捕食者重引入/迁地保护问题。对应模型：非技术政策信、模型迁移。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/A/q07/solution.py",
  "result_path": "question_results/2019/A/q07/result.json",
  "report_path": "question_reports/2019/A/q07/report.md",
  "artifact_path": "question_artifacts/2019/A/q07/dragon_resource_frontier.png"
}
RESULT_PATH = BASE / "results" / '2019' / 'A' / 'q07' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'A' / 'q07' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'A' / 'q07'


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
