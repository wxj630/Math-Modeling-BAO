# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2020-B",
  "title": "2020年 CUMCM B题：穿越沙漠",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2020/B.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "穿越沙漠需水和食物两种资源，它们的最小计量单位均为箱。每天玩家拥有的水和食物质量之和不能超过负重上限。若未到达终点而水或食物已耗尽，视为游戏失败。",
    "tasks": [
      "穿越沙漠需水和食物两种资源，它们的最小计量单位均为箱",
      "每天玩家拥有的水和食物质量之和不能超过负重上限",
      "若未到达终点而水或食物已耗尽，视为游戏失败"
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
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/B/2020B-穿越沙漠.docx",
      "name": "2020B-穿越沙漠.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 44282,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/B/Result.xlsx",
      "name": "Result.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 11164,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/B/附件.docx",
      "name": "附件.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 259622,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2020" / "B" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2020" / "B" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2020" / "B" / "q02"


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
