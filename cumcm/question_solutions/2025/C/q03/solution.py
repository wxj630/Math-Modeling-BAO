# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2025-C",
  "title": "2025年 CUMCM C题：NIPT 的时点选择与胎儿的异常判定",
  "problem_path": "cumcm/problems/2025/C.md",
  "question_index": 3,
  "question": {
    "label": "问题3",
    "statement": "男胎Y 染色体浓度达标时间受多种因素(身高、体重、年龄等)的影响，试综合考虑这些因 素、检测误差和胎儿的Y 染色体浓度达标比例（即浓度达到或超过4%的比例），根据男胎孕妇的BMI， 给出合理分组以及每组的最佳NIPT 时点，使得孕妇潜在风险最小，并分析检测误差对结果的影响。",
    "tasks": [
      "男胎Y 染色体浓度达标时间受多种因素(身高、体重、年龄等)的影响，试综合考虑这些因 素、检测误差和胎儿的Y 染色体浓度达标比例（即浓度达到或超过4%的比例），根据男胎孕妇的BMI， 给出合理分组以及每组的最佳NIPT 时点，使得孕妇潜在风险最小，并分析检测误差对结果的影响"
    ],
    "models": [
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "综合"
        ]
      },
      {
        "key": "ml_statistics",
        "name": "机器学习与统计",
        "chapter": "CH9",
        "keywords": [
          "检测"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/C题/C题.pdf",
      "name": "C题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 357653,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/C题/附件.xlsx",
      "name": "附件.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 481734,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2025" / "C" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2025" / "C" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2025" / "C" / "q03"


def main() -> None:
    result = solve_question(PAYLOAD, ARTIFACT_DIR)
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_question_report(result, REPORT_PATH)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
