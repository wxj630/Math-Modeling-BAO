from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('.')
BASE = Path('mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-D",
  "year": "2017",
  "code": "D",
  "question": "q01",
  "question_title": "安检流程排队模型与瓶颈识别",
  "statement": "Develop one or more model(s) that allow(s) you to explore the flow of passengers through a security check point and identify bottlenecks. Clearly identify where problem areas exist in the current process.",
  "methods": "读取官方 2017_ICM_Problem_D_Data.xlsx 的 TSA Pre-Check/Regular 到达时间、ID 检查、毫米波、X-ray 和取物样本，构造确定性 G/G/c 排队模型；基线采用题面 one PreCheck lane for every three regular lanes。对应模型：排队论、离散事件仿真、瓶颈分析。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2017/D/q01/solution.py",
  "result_path": "question_results/2017/D/q01/result.json",
  "report_path": "question_reports/2017/D/q01/report.md",
  "artifact_path": "question_artifacts/2017/D/q01/baseline_queue_metrics.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'D' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'D' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'D' / 'q01'


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
