# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2023-D",
  "title": "2023年 CUMCM D题：圈养湖羊的空间利用率",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2023/D.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "在问题 1 的基础上，对 112 个标准羊栏给出具体的生产计划（包括种公羊与基础 母羊的配种时机和数量、羊栏的使用方案、年化出栏羊只数量等），使得年化出栏羊只数量最 大。",
    "tasks": [
      "在问题 1 的基础上，对 112 个标准羊栏给出具体的生产计划（包括种公羊与基础 母羊的配种时机和数量、羊栏的使用方案、年化出栏羊只数量等），使得年化出栏羊只数量最 大"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "方案"
        ]
      }
    ]
  },
  "attachments": []
}
RESULT_PATH = ROOT / "question_results" / "2023" / "D" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2023" / "D" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2023" / "D" / "q02"


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
