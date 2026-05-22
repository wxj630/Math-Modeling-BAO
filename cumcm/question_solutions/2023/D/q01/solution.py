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
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "不考虑不确定因素和种羊的淘汰更新，假定自然交配期 20 天，母羊都能受孕，孕 期 149 天，每胎产羔 2 只，哺乳期 40 天，羔羊育肥期 210 天，母羊空怀休整期 20 天。该湖羊 养殖场现有 112 个标准羊栏，在实现连续生产的条件下，试确定养殖场种公羊与基础母羊的合 理数量， 并估算年化出栏羊只数量的范围。 若该养殖场希望每年出栏不少于 1500 只羊，试估算 现有标准羊栏数量的缺口。",
    "tasks": [
      "不考虑不确定因素和种羊的淘汰更新，假定自然交配期 20 天，母羊都能受孕，孕 期 149 天，每胎产羔 2 只，哺乳期 40 天，羔羊育肥期 210 天，母羊空怀休整期 20 天",
      "该湖羊 养殖场现有 112 个标准羊栏，在实现连续生产的条件下，试确定养殖场种公羊与基础母羊的合 理数量， 并估算年化出栏羊只数量的范围"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "通用"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "通用"
        ]
      }
    ]
  },
  "attachments": []
}
RESULT_PATH = ROOT / "question_results" / "2023" / "D" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2023" / "D" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2023" / "D" / "q01"


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
