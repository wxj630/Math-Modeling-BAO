from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-D",
  "year": "2020",
  "code": "D",
  "question": "q04",
  "question_title": "从足球团队推广到一般跨学科团队",
  "statement": "As our societies increasingly solve problems involving teams, can you generalize your findings to say something about how to design and monitor successful teams in other settings?",
  "methods": "把球员映射为专家，把传球映射为任务交接，提炼互惠信息流、冗余三元组、互动类型多样性和持续监控机制，说明如何迁移到科研、工程、医疗或应急团队。对应模型：复杂网络类比、组织协作指标迁移。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2020/D/q04/solution.py",
  "result_path": "question_results/2020/D/q04/result.json",
  "report_path": "question_reports/2020/D/q04/report.md",
  "artifact_path": "question_artifacts/2020/D/q04/passing_network_top_edges.png"
}
RESULT_PATH = BASE / "results" / '2020' / 'D' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'D' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'D' / 'q04'


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
