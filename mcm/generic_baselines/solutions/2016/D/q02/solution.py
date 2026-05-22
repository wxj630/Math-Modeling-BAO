from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2016-D",
  "year": "2016",
  "code": "D",
  "question": "q02",
  "question_title": "历史事件到今日传播的结构验证",
  "statement": "Validate your model's reliability by using data from the past and the prediction capability of your model to predict the information communication situation for today and compare that with today's reality.",
  "methods": "对官方题面点名的 Taylor Swift 传闻、今日重要人物遇刺、Lincoln 遇刺做确定性扩散曲线比较；验证模型是否重现从电报/报纸/火车时代到智能手机时代的 24 小时 awareness 数量级跃迁。对应模型：指数扩散、历史结构验证、情景对比。",
  "source_type": "official_statement_parameters",
  "solution_path": "question_solutions/2016/D/q02/solution.py",
  "result_path": "question_results/2016/D/q02/result.json",
  "report_path": "question_reports/2016/D/q02/report.md",
  "artifact_path": "question_artifacts/2016/D/q02/diffusion_comparison.csv"
}
RESULT_PATH = BASE / "results" / '2016' / 'D' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2016' / 'D' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2016' / 'D' / 'q02'


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
