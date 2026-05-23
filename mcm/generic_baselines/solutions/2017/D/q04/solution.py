from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2017-D",
  "year": "2017",
  "code": "D",
  "question": "q04",
  "question_title": "安全经理政策建议、验证和未来工作",
  "statement": "Propose policy and procedural recommendations for security managers based on your model. Validate the model, assess strengths and weaknesses, and propose ideas for improvement.",
  "methods": "将瓶颈、流程修改和文化敏感性结果整理为 TSA security managers memo，并明确官方样本规模、无随机造数、缺少小时级真实速度/成本数据等验证限制。对应模型：政策决策报告、模型验证、局限性分析。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2017/D/q04/solution.py",
  "result_path": "question_results/2017/D/q04/result.json",
  "report_path": "question_reports/2017/D/q04/report.md",
  "artifact_path": "question_artifacts/2017/D/q04/checkpoint_wait_times.png"
}
RESULT_PATH = BASE / "results" / '2017' / 'D' / 'q04' / "result.json"
REPORT_PATH = BASE / "reports" / '2017' / 'D' / 'q04' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2017' / 'D' / 'q04'


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
