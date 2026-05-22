from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path('/Users/wuxiaojun/code/Math-Modeling-World')
BASE = Path('/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines')
sys.path.insert(0, str(REPO_ROOT / "mcm" / "lib"))
from generic_baseline import solve_question_generic_baseline, write_generic_report

PAYLOAD = {
  "problem_id": "2018-C",
  "year": "2018",
  "code": "C",
  "question": "q01",
  "question_title": "四州能源画像与清洁可再生定义",
  "statement": "Using the provided spreadsheet, develop a mathematical model to describe the energy profile of Arizona, California, New Mexico, and Texas. Define what your team means by cleaner, renewable energy and use the data to compare the states.",
  "methods": "读取官方 2018_MCM_Problem_C_Data.xlsx 的 seseds 与 msncodes 工作表，抽取 RETCB、REPRB、TETCB、TEPRB、TPOPP、HYTCB、WYTCB、SOTCB、GETCB、BMTCB 等 SEDS MSN 指标，构造 renewable share、renewable production share、non-hydro renewable share、per-capita energy 和 clean profile score。对应模型：多指标综合评价、能源结构画像、标准化评分。",
  "source_type": "official_comap_xlsx",
  "solution_path": "question_solutions/2018/C/q01/solution.py",
  "result_path": "question_results/2018/C/q01/result.json",
  "report_path": "question_reports/2018/C/q01/report.md",
  "artifact_path": "question_artifacts/2018/C/q01/state_energy_profiles_2009.csv"
}
RESULT_PATH = BASE / "results" / '2018' / 'C' / 'q01' / "result.json"
REPORT_PATH = BASE / "reports" / '2018' / 'C' / 'q01' / "report.md"
ARTIFACT_DIR = BASE / "artifacts" / '2018' / 'C' / 'q01'


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
