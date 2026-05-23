from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[6]
BASE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2021-D",
  "year": "2021",
  "code": "D",
  "question": "q02",
  "question_title": "音乐特征相似性与流派内外比较",
  "statement": "Use full_music_data and/or the two summary data sets of music characteristics, to develop measures of music similarity. Using your measure, are artists within genre more similar than artists between genres?",
  "methods": "读取官方 data_by_artist.csv，对 danceability、energy、valence、tempo、loudness 等音频特征标准化；比较同流派艺术家到流派中心的距离相似度，并输出流派中心相似矩阵。",
  "source_type": "official_comap_csv",
  "solution_path": "question_solutions/2021/D/q02/solution.py",
  "result_path": "question_results/2021/D/q02/result.json",
  "report_path": "question_reports/2021/D/q02/report.md",
  "artifact_path": "question_artifacts/2021/D/q02/genre_similarity_matrix.csv"
}
RESULT_PATH = BASE / "results" / '2021' / 'D' / 'q02' / "result.json"
REPORT_PATH = BASE / "reports" / '2021' / 'D' / 'q02' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2021' / 'D' / 'q02'


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
