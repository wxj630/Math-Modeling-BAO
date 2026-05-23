from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-C",
  "year": "2017",
  "code": "C",
  "question": "q01",
  "question_title": "官方路网画像与交通流模型",
  "statement": "Build a model of traffic-flow effects using the number of lanes, peak and/or average traffic volume, and the percentage of self-driving cooperating vehicles on I-5, I-90, I-405, and SR-520.",
  "methods": "读取官方 2017_MCM_Problem_C_Data.xlsx 的 parsed mile posts 和 definitions 工作表，按 route/milepost/ADT/lanes 构造路段容量、峰小时流量、V/C ratio 和 BPR 速度函数。对应模型：交通流基本图、容量约束、BPR 延误函数、路网分段画像。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2017/C/q01/solution.py",
  "result_path": "question_results/2017/C/q01/result.json",
  "report_path": "question_reports/2017/C/q01/report.md",
  "artifact_path": "question_artifacts/2017/C/q01/clean_traffic_segments.csv"
}
RESULT_PATH = BASE / "results" / '2017' / 'C' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'C' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'C' / 'q01'


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
