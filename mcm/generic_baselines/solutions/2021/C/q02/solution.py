from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-C",
  "year": "2021",
  "code": "C",
  "question": "q02",
  "question_title": "误判分类概率模型",
  "statement": "Most reported sightings mistake other hornets for the Vespa mandarinia. Use only the data set file provided, and possibly the image files provided, to create, analyze, and discuss a model that predicts the likelihood of a mistaken classification.",
  "methods": "只用官方 Positive ID / Negative ID 标签训练确定性留出分类器；特征包含坐标、月份、提交延迟、图片/视频映射、报告文本 TF-IDF、标本和蜂群损失关键词，以及距训练阳性点距离。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2021/C/q02/solution.py",
  "result_path": "question_results/2021/C/q02/result.json",
  "report_path": "question_reports/2021/C/q02/report.md",
  "artifact_path": "question_artifacts/2021/C/q02/classification_holdout_predictions.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'C' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'C' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'C' / 'q02'


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
