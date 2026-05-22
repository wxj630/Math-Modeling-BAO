from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2019-A",
  "year": "2019",
  "code": "A",
  "question": "q01",
  "question_title": "龙的生态影响与栖息要求",
  "statement": "What is the ecological impact and requirements of the dragons?",
  "methods": "只使用官方题面中三条现存龙、孵化约 10kg、一年 30-40kg、持续生长、飞行、喷火和抗创伤等约束，构造顶级捕食者食物、栖息地、水源、巢址和火风险需求。对应模型：生态承载力、多指标影响评价、情景参数审计。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2019/A/q01/solution.py",
  "result_path": "question_results/2019/A/q01/result.json",
  "report_path": "question_reports/2019/A/q01/report.md",
  "artifact_path": "question_artifacts/2019/A/q01/dragon_area_requirements.csv"
}
RESULT_PATH = BASE / "results" / '2019' / 'A' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2019' / 'A' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2019' / 'A' / 'q01'


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
