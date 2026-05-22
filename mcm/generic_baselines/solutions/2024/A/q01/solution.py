from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2024-A",
  "year": "2024",
  "code": "A",
  "question": "q01",
  "question_title": "七鳃鳗可变性别比对更大生态系统的影响",
  "statement": "What is the impact on the larger ecological system when the population of lampreys can alter its sex ratio?",
  "methods": "官方 PDF 题面参数 0.78/0.56 雄性比例端点 + 资源驱动性别比响应曲线 + 七鳃鳗-宿主鱼-寄生者-食物网差分方程。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2024/A/q01/solution.py",
  "result_path": "question_results/2024/A/q01/result.json",
  "report_path": "question_reports/2024/A/q01/report.md",
  "artifact_path": "question_artifacts/2024/A/q01/sex_ratio_response.csv"
}
RESULT_PATH = BASE / "results" / '2024' / 'A' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2024' / 'A' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2024' / 'A' / 'q01'


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
