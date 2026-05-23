from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2020-C",
  "year": "2020",
  "code": "C",
  "question": "q01",
  "question_title": "三类 Amazon 评论数据的核心评分与评论指标",
  "statement": "Analyze the three product data sets to identify meaningful quantitative and qualitative patterns, relationships, measures, and parameters within and between star ratings, reviews, and helpfulness ratings.",
  "methods": "直接从官方 ZIP 读取 hair_dryer.tsv、microwave.tsv、pacifier.tsv，按产品计算 review_count、mean_star、low-rating share、helpfulness、review length 和 verified share。",
  "source_type": "official_comap_tsv_zip",
  "solution_path": "question_solutions/2020/C/q01/solution.py",
  "result_path": "question_results/2020/C/q01/result.json",
  "report_path": "question_reports/2020/C/q01/report.md",
  "artifact_path": "question_artifacts/2020/C/q01/product_review_measures.csv"
}
RESULT_PATH = BASE / "results" / '2020' / 'C' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2020' / 'C' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2020' / 'C' / 'q01'


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
